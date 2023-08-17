import streamlit as st
from st_pages import show_pages, Page, Section

from auth.domain import User
from common.function_decorator import login_required


@login_required
def show_nav(user: User):
    show_pages(
        [
            Page("playground.py", "Playground", "🏠"),
            Section(name="Streamlit Hello2", icon=":pig:"),
            Page("pages/section1/1_plotting.py", "Playground1", "🏠"),
            Page("pages/section1/2_mapping.py", "Playground2", "🏠"),
            Page("pages/section1/3_dataframe.py", "Playground3", "🏠"),
        ]
    )


st.session_state['authentication_status'] = "ANONYMOUS"
show_nav()


def main():
    st.write("Welcome to Ai-Portal")
    # st.write(f'Welcome *{name}*')


main()
