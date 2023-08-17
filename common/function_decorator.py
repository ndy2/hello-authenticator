from functools import wraps

import streamlit as st
import inspect

from auth.domain import User
from config.auth_config import hello_authenticate


def login_required(func):
    @wraps(func)
    def wrapper():

        try:
            name, authenticated, username = hello_authenticate.login("Login", "sidebar")
            print(name, authenticated, username)
            if authenticated is not "ANONYMOUS":
                st.sidebar.markdown(f"welcome *{name}*")
                hello_authenticate.logout('Logout', 'sidebar', key='unique_key')
                user = User(name=username)

                func(user)
                print(inspect.signature(func))


            else:
                st.error('Username/password is incorrect')
        except KeyError:
            st.warning('Please enter your username and password')

    return wrapper
