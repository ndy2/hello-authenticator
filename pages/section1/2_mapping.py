import streamlit as st
from st_pages import add_page_title

from auth.decorator_login import login_required

add_page_title()


# @login_required
def mapping():
    st.write("do plot")


mapping()
