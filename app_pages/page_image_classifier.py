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
Click [**here**](https://github.com/NiclO1337/pp5-cats-vs-dogs/tree/\
384dbd8385aa5271160c397f9865e7d188dfc462/outputs/sample_images.zip),
to download a set of cat and dog images for live prediction.''')

    images_buffer = st.file_uploader('Upload images of cats or dogs here, \
you can select more than one at the time.', type = 'png',
                                    accept_multiple_files = True)

    if images_buffer is not None:

        df_report = pd.DataFrame([])

        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f'Uploaded image: *{image.name}*')
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f'Image size: {img_array.shape[1]} px \
width x {img_array.shape[0]} px height')

            version = 'v8'

            resized_img = resize_input_image(img=img_pil, version=version)
            predict_probability, predict_class = load_model_and_predict(
                resized_img, version=version)

            plot_predictions_and_probabilities(
                predict_probability, predict_class)

            df_report = pd.concat([df_report, pd.DataFrame(
                {'Name': [image.name], 'Result': [predict_class]}
                )], ignore_index=True)


        if not df_report.empty:
            st.warning('Analysis Report')
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report),
                        unsafe_allow_html=True)
