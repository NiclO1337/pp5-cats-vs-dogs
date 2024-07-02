import streamlit as st
import pandas as pd
import plotly.express as px

from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_and_probabilities(predicted_probability, predicted_class):
    """
    Plot the prediction and probability result
    """

    probability_per_class = pd.DataFrame(
        data = [0, 0],
        index = {'Cat': 0, 'Dog': 1}.keys(),
        columns = ['Probability'],
    )

    probability_per_class.loc[predicted_class] = predicted_probability

    for x in probability_per_class.index.to_list():
        if x not in predicted_class:
            probability_per_class.loc[x] = 1 - predicted_probability

    probability_per_class = probability_per_class.round(3)
    probability_per_class['Diagnostic'] = probability_per_class.index

    fig = px.bar(
        probability_per_class, x = 'Diagnostic',
        y = probability_per_class['Probability'], range_y = [0, 1],
        width = 600, height = 300, template = 'seaborn',
    )
    st.plotly_chart(fig)


def resize_input_image(img, version):
    """
    Reshape image to image determined in the data visualization notebook
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    resized_image = np.expand_dims(img_resized, axis=0)/255

    return resized_image