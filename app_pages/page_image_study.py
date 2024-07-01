import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.image import imread


def page_image_study_body():

    
    st.write('---')

    st.header('**Image study**')

    st.info('''
Business requirement 1: Help clients understand how the model interprets 
images and provide insights into distinctive features.
''')

    version = 'v1'
    
    if st.checkbox(
        'Display the mean and standard deviation\
        from the average image study'):

        avg_var_cat = plt.imread(f'outputs/{version}/avg_var_cat.png')
        avg_var_dog = plt.imread(f'outputs/{version}/avg_var_dog.png')

        st.success('There is too much variation in how images are taken to be \
able to see any distinctive features in this image study.')

        st.image(avg_var_cat, caption='Cat image - Average and Variablility')
        st.image(avg_var_dog, caption='Dog image - Average and Variablility')

    if st.checkbox(
        'Show the differences between the average cat and dog images.'):

        avg_differences = plt.imread(f'outputs/{version}/avg_diff.png')

        st.warning('Images in the dataset are too different so we are \
not able to see any clear differences in this image study.')

        st.image(avg_differences,
        caption='Average differences between cat and dog images')

    if st.checkbox(
        'Display a montage of images from the dataset of both cats or dogs'):
        st.error('Hello')


    