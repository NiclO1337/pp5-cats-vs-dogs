import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

from source.data_management import download_dataframe_as_csv
from source.machine_learning.predictive_analysis import (
    resize_input_image,
    load_model_and_predict,
    plot_predictions_and_probabilities,
)


def page_image_classifier_body():

    st.write('---')

    st.header('**Image classifyer**')

    st.info('''
Business Requirement 2: Demonstrate the model's capability to classify images,
enabling clients to test their HIP software.
''')

    st.warning('''
Click [**here**](link),
to download a set of cat and dog images for live prediction.''')

    images_buffer = st.file_uploader('Upload images of cats or dogs here, \
you can select more than one at the time.')

    if images_buffer is not None:

        df_report = pd.DataFrame([])

        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f'Uploaded image name: *{image.name}*')
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f'Image size: {img_array.shape[1]} px \
width x {img_array.shape[0]} px height')

            version = 'v1'

            resized_img = resize_input_image(img=img_pil, version=version)
            predict_proba, predict_class = load_model_and_predict(
                resized_img, version=version)

            plot_predictions_and_probabilities(predict_proba, predict_class)

            df_report = df_report.append({
                'Name': image.name, 'Result': pred_class}, ignore_index=True)

        if not df_report.empty:
            st.warning('Analysis Report')
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report),
                        unsafe_allow_html=True)
