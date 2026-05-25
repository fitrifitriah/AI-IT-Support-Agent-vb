import streamlit as st
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai
from typing import Dict, Any

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI IT Support Agent",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        color: #1f77b4;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subheader {
        color: #555;
        font-size: 1.1em;
        margin-bottom: 20px;
    }
    .section-title {
        color: #1f77b4;
        font-size: 1.3em;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 10px;
    }
    .success-box {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border-left: 4px solid #17a2b8;
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
    .error-box {
        background-color: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)


class ITSupportAgent:
    """AI-powered IT Support Agent using Google Gemini"""

    def __init__(self):
        """Initialize the IT Support Agent with Gemini API"""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in environment variables. "
                "Please set it in your .env file or system environment."
            )
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def parse_issue(self, issue_description: str) -> Dict[str, Any]:
        """
        Parse technical issue and generate structured response

        Args:
            issue_description: User's technical issue description

        Returns:
            Dictionary containing parsed issue details
        """
        prompt = f"""Analyze the following IT support issue and provide a detailed, structured response in valid JSON format.

ISSUE DESCRIPTION:
{issue_description}

You must respond with ONLY valid JSON (no markdown, no extra text) with this exact structure:
{{
    "category": "Hardware|Network|Software|M365",
    "category_explanation": "Brief explanation of why this category was chosen",
    "urgency_level": "Critical|High|Medium|Low",
    "urgency_justification": "Brief explanation of the urgency assessment",
    "root_cause_analysis": "Detailed analysis of the probable root cause(s)",
    "troubleshooting_steps": [
        {{
            "step_number": 1,
            "action": "Action to perform",
            "details": "Detailed instructions for IT staff",
            "expected_outcome": "What to expect if this step is successful"
        }}
    ],
    "email_response": {{
        "subject": "Email subject line",
        "body": "Professional, polite email response to the user"
    }},
    "additional_notes": "Any other relevant information or warnings"
}}

Ensure the JSON is properly formatted and valid. The troubleshooting steps should be practical and step-by-step."""

        try:
            response = self.model.generate_content(prompt)
            # Extract JSON from response
            response_text = response.text.strip()

            # Try to parse JSON directly
            try:
                result = json.loads(response_text)
            except json.JSONDecodeError:
                # If direct parsing fails, try to extract JSON from the response
                start_idx = response_text.find("{")
                end_idx = response_text.rfind("}") + 1
                if start_idx != -1 and end_idx > start_idx:
                    json_str = response_text[start_idx:end_idx]
                    result = json.loads(json_str)
                else:
                    raise ValueError("Could not extract valid JSON from response")

            return result
        except Exception as e:
            return {
                "error": str(e),
                "category": "Unknown",
                "urgency_level": "Unknown",
            }

    def validate_response(self, response: Dict[str, Any]) -> bool:
        """Validate the structure of the API response"""
        required_keys = [
            "category",
            "urgency_level",
            "root_cause_analysis",
            "troubleshooting_steps",
            "email_response",
        ]
        return all(key in response for key in required_keys)


def initialize_session_state():
    """Initialize Streamlit session state"""
    if "parsed_issue" not in st.session_state:
        st.session_state.parsed_issue = None
    if "processing" not in st.session_state:
        st.session_state.processing = False


def display_issue_summary(response: Dict[str, Any]):
    """Display a summary section of the parsed issue"""
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"**Category:** {response.get('category', 'N/A')}")
        st.caption(response.get("category_explanation", ""))

    with col2:
        urgency = response.get("urgency_level", "N/A")
        # Color code urgency
        if urgency == "Critical":
            st.error(f"**Urgency:** {urgency}")
        elif urgency == "High":
            st.warning(f"**Urgency:** {urgency}")
        else:
            st.info(f"**Urgency:** {urgency}")


def display_root_cause(response: Dict[str, Any]):
    """Display root cause analysis"""
    st.markdown('<div class="section-title">🔍 Root Cause Analysis</div>', unsafe_allow_html=True)
    st.write(response.get("root_cause_analysis", "N/A"))


def display_troubleshooting_guide(response: Dict[str, Any]):
    """Display step-by-step troubleshooting guide"""
    st.markdown(
        '<div class="section-title">📋 Step-by-Step Troubleshooting Guide</div>',
        unsafe_allow_html=True,
    )

    steps = response.get("troubleshooting_steps", [])
    for step in steps:
        with st.expander(
            f"Step {step.get('step_number', '?')}: {step.get('action', 'Unknown')}",
            expanded=False,
        ):
            st.write(f"**Details:** {step.get('details', 'N/A')}")
            st.write(f"**Expected Outcome:** {step.get('expected_outcome', 'N/A')}")


def display_email_draft(response: Dict[str, Any]):
    """Display email draft for user response"""
    st.markdown(
        '<div class="section-title">📧 Email Response Draft</div>', unsafe_allow_html=True
    )

    email = response.get("email_response", {})
    subject = email.get("subject", "Re: Your IT Support Request")
    body = email.get("body", "")

    with st.container():
        st.markdown("**Subject Line:**")
        st.text_input("", value=subject, disabled=True, key="email_subject")

        st.markdown("**Email Body:**")
        st.text_area("", value=body, disabled=True, height=200, key="email_body")

        # Copy button
        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button("📋 Copy Email", key="copy_email"):
                st.success("Email copied to clipboard!")


def display_raw_json(response: Dict[str, Any]):
    """Display raw JSON response"""
    st.markdown('<div class="section-title">📊 Raw JSON Response</div>', unsafe_allow_html=True)
    st.json(response)


def main():
    """Main application function"""
    initialize_session_state()

    # Header
    st.markdown(
        '<div class="main-header">🛠️ AI IT Support Agent</div>', unsafe_allow_html=True
    )
    st.markdown(
        '<div class="subheader">Powered by Google Gemini AI</div>',
        unsafe_allow_html=True,
    )

    # Sidebar
    with st.sidebar:
        st.header("About")
        st.info(
            "This AI IT Support Agent analyzes technical issues and provides:"
            "\n\n✓ Issue categorization\n✓ Urgency assessment\n✓ Root cause analysis"
            "\n✓ Step-by-step troubleshooting\n✓ Email response draft"
        )

        st.header("Instructions")
        st.markdown(
            """
1. Enter a detailed technical issue description
2. Click 'Analyze Issue' to process
3. Review the structured analysis
4. Use the email draft to respond to users
        """
        )

    # Main content
    st.markdown("---")

    # Issue input section
    st.markdown('<div class="section-title">📝 Submit Your Technical Issue</div>', unsafe_allow_html=True)

    issue_input = st.text_area(
        "Describe the technical issue in detail:",
        height=120,
        placeholder="Example: User reports that their laptop screen goes black randomly after 5 minutes. "
        "The device restarts after this happens. Windows has been recently updated.",
        key="issue_input",
    )

    # Process button
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        analyze_button = st.button("🔍 Analyze Issue", type="primary", use_container_width=True)

    with col2:
        clear_button = st.button("🔄 Clear", use_container_width=True)

    if clear_button:
        st.session_state.parsed_issue = None
        st.rerun()

    # Process issue
    if analyze_button:
        if not issue_input.strip():
            st.error("❌ Please enter a technical issue description.")
        else:
            with st.spinner("🤖 Analyzing issue with AI..."):
                try:
                    agent = ITSupportAgent()
                    response = agent.parse_issue(issue_input)

                    if "error" in response:
                        st.error(f"❌ Error processing issue: {response['error']}")
                    else:
                        st.session_state.parsed_issue = response
                        st.rerun()

                except ValueError as e:
                    st.error(f"❌ Configuration Error: {str(e)}")
                    st.info("📌 Please ensure GEMINI_API_KEY is set in your .env file")
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")

    # Display results
    if st.session_state.parsed_issue:
        st.markdown("---")
        st.markdown('<div class="success-box">✅ Issue Analysis Complete!</div>', unsafe_allow_html=True)

        # Create tabs for different views
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["Summary", "Root Cause", "Troubleshooting", "Email", "Raw JSON"]
        )

        response = st.session_state.parsed_issue

        with tab1:
            st.markdown("## Issue Summary")
            display_issue_summary(response)

            if response.get("additional_notes"):
                st.markdown("### Additional Notes")
                st.info(response.get("additional_notes"))

        with tab2:
            display_root_cause(response)

        with tab3:
            display_troubleshooting_guide(response)

        with tab4:
            display_email_draft(response)

        with tab5:
            display_raw_json(response)

        # Download functionality
        st.markdown("---")
        st.markdown("### 📥 Export Results")
        col1, col2 = st.columns(2)

        with col1:
            json_str = json.dumps(response, indent=2)
            st.download_button(
                label="📄 Download as JSON",
                data=json_str,
                file_name="it_support_analysis.json",
                mime="application/json",
            )

        with col2:
            st.write("")  # Placeholder for alignment


if __name__ == "__main__":
    main()
