import streamlit as st


def page_image_study_body():

    
    st.write('---')

    st.header('**Image study**')

    st.error('''
**Business requirement**


The client requires us to do a study of their dataset and show them our 
results.
''')

    version = 'v1'
    
    if st.checkbox('Hello'):
        st.warning('Hello')

    if st.checkbox('Hello'):
        st.warning('Hello')

    if st.checkbox('Hello'):
        st.warning('Hello')


    