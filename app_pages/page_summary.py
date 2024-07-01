import streamlit as st


def page_summary_body():

    st.write('---')

    st.header('**Project summary**')

    st.info('''
**General information**
* information.  
hello

hello
''')

    st.success('''
**Project dataset**

''')

    st.warning('''
**Additional information**

''')

    st.error('''
**Business requirements**

''')