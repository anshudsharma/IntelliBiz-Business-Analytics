import streamlit as st


def get_role():

    return st.session_state.get(
        "role"
    )


def is_super_admin():

    return get_role() == "SUPER_ADMIN"


def is_company_admin():

    return get_role() == "COMPANY_ADMIN"


def is_employee():

    return get_role() == "EMPLOYEE"