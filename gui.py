import streamlit as st

from describe_project import do_describe_folder

folder_path = st.text_input('Input the path of the folder you want to describe')
description_set = do_describe_folder(folder_path)
st.write(description_set)
