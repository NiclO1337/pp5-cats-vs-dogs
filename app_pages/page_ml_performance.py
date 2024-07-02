import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.image import imread


def page_ml_performance_body():

    st.write('---')

    st.header('**ML Performance Metrics**')

    version = 'v1'

    st.info("Labels Frequencies in the dataset")

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation and Test Sets')

    st.write("---")

    st.success("Model training history")
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")
