import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os
import itertools
import random


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
able to see any distinctive features of cats or dogs in this image study.')

        st.image(avg_var_cat, caption='Cat image - Average and Variablility')
        st.image(avg_var_dog, caption='Dog image - Average and Variablility')

    if st.checkbox(
            'Show the differences between the average cat and dog images'):

        avg_differences = plt.imread(f'outputs/{version}/avg_diff.png')

        st.warning('Images in the dataset are too different from eachother so \
we are not able to see any clear average differences in this image study.')

        st.image(avg_differences,
                 caption='Average differences between cat and dog images')

    if st.checkbox(
            'Display a montage of images from the \
                dataset of both cats or dogs'):
        st.error('To see the montage, select label (cat or dog) and click \
on the "Create Montage" button, then wait for it to load.')

        sample_image_dir = 'outputs/sample_images'
        labels = os.listdir(sample_image_dir)

        labels_to_display = st.selectbox(label='Select label', options=labels,
                                         index=0)

        if st.button('Create Montage'):
            image_montage(sample_image_dir, labels_to_display,
                          nrows=2, ncols=3, figsize=(15,10))


def image_montage(image_dir, labels, nrows, ncols, figsize):

    images_list = os.listdir(image_dir + '/' + labels)
    img_idx = random.sample(images_list, nrows * ncols)

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))

    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
        img = imread(image_dir + '/' + labels + '/' + img_idx[x])
        img_shape = img.shape
        axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
        axes[plot_idx[x][0], plot_idx[x][1]].set_title(
            f"Width {img_shape[1]}px x Height {img_shape[0]}px")
        axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
        axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

    st.pyplot(fig=fig)
