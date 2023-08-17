import streamlit as st


def login_widget(check_username_password_authentication, load_user_by_username):
    login_form = st.sidebar.form("Login")
    login_form.subheader("Login")

    username = login_form.text_input('Username').lower()
    password = login_form.text_input('Password', type='password')

    if login_form.form_submit_button('Login'):
        if check_username_password_authentication(username, password):
            return load_user_by_username(username)
        else:
            return None
