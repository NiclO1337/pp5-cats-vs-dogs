import streamlit as st
import pandas as pd


def page_image_classifier_body():
    
    st.write('---')

    st.header('**Image classifyer**')

    st.info('''
Business Requirement 2: Demonstrate the model's capability to classify images, 
enabling clients to test their HIP software.
''')

    st.success('''
Click [**here**](link), 
to download a set of cat and dog images for live prediction.''')

    images_buffer = st.file_uploader('Upload images of cats or dogs here, \
you can select more than one at the time.')

    if images_buffer is not None:
        df_report = pd.DataFrame([])