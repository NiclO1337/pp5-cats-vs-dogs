import streamlit as st


def page_image_study_body():

    
    st.write('---')

    st.header('**Image study**')

    st.error('''
Business requirement 1: Help clients understand how the model interprets 
images and provide insights into distinctive features.
''')

    version = 'v1'
    
    if st.checkbox(
        'Display the mean and standard deviation\
        from the average image study'
        ):
        st.warning('Hello')

    if st.checkbox(
        'Show the differences between the average cat and dog images.'):
        st.warning('Hello')

    if st.checkbox(
        'Display a montage of images from the dataset of both cats or dogs'):
        st.warning('Hello')


    