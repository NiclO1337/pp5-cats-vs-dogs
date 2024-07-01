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

    st.write("# This is a major section")  # use markdown to create headers and sub headers
    st.write("## This is subsection 1")
    st.write("* Here is content for subsection 1")
    st.write("## This is subsection 2")
    st.write("* Here is content for subsection 2")
    st.write("### This is sub-subsection 2") # you can play around by adding more sub-sections
    st.write("Here other content")
    st.info("* This is made with st.info()") # Display a text with informational style.
    st.success("* This is made with st.success()") # Display a text with success style.
    st.warning("* This is made with st.warning()") # Display a text with warning style.
    st.error("* This is made with st.error()") # Display a text with error style.
    st.write("---")  # creates a horizontal line, useful to separate the content in the page

    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''If you end a line with two spaces,  
    a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)