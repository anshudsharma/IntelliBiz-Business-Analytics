import streamlit as st


def is_logged_in():

    return (
        "user_id"
        in st.session_state
    )


def logout():

    for key in list(
        st.session_state.keys()
    ):

        del st.session_state[key]


def get_company_id():

    return st.session_state.get(
        "company_id"
    )


def get_role():

    return st.session_state.get(
        "role"
    )