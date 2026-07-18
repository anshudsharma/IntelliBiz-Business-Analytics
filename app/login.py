import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))



import streamlit as st
from auth.auth_service import AuthService



st.set_page_config(
    page_title="IntelliBiz Login",
    page_icon="🔐",
    layout="centered"
)

# # Hide the page navigation when not logged in.
st.markdown("""
<style>

/* Hide Streamlit multipage navigation */
[data-testid="stSidebarNav"] {
    display: none;
}

/* Hide collapse button */
[data-testid="collapsedControl"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)


st.title("🔐 IntelliBiz Login")



st.write(
    "Sign in to access IntelliBiz."
)

email = st.text_input(
    "Email"
)

password = st.text_input(
    "Password",
    type="password"
)

auth = AuthService()

if st.button(
    "Login",
    use_container_width=True
):

    user = auth.login(
        email,
        password
    )

    if user is None:

        st.error(
            "Invalid email or password."
        )

    else:

        st.session_state.user_id = (
            user["user_id"]
        )

        st.session_state.company_id = (
            user["company_id"]
        )
        st.session_state.full_name = (
            user["full_name"]
        )

        st.session_state.role = (
            user["role"]
        )

        st.success(
            f"Welcome {user['full_name']}"
        )

        st.switch_page(
            "pages/0_Dashboard.py"
        )