import streamlit as st
from st_pages import add_page_title

from auth.domain import User
from common.function_decorator import login_required

add_page_title(layout="wide")


@login_required
def plotting(user: User):
    st.write("do plot")
    st.write(f"hello ${user.name}")


plotting()
