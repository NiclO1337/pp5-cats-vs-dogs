import streamlit as st


def page_project_hypothesis_body():

    st.write('---')

    st.header('**Project hypotheses**')

    st.write('---')

    st.info('''
**Hypohesis 1:** Cats are more uniform while dogs come in all shapes and sizes.
''')

    st.warning('''
**How to validate:** We will use an average image study to investigate this.
''')

    st.error('''
**Conclusion:** Unable to show any distinct features of cats or dogs due to
the dataset having too much variability in the images. Further study is needed
with manually looking over the images in the dataset.
''')

    st.write('---')

    st.info('''
**Hypohesis 2:** A deep learning model with a convolutional neural network
(CNN) should be able to accuratly classify the clients images.''')

    st.warning('''
**How to validate:**
We will train a model using CNN and then test the performance.''')

    st.success('''
**Conclusion:** The CNN did a great job with predicting images even before
augmenting or fine tuning hyperparameters.
''')

    st.write('---')

    st.info('''
**Hypohesis 3:**
Augmenting training set images will greatly improve performance.''')

    st.warning('''
**How to validate:**
Test model without augmented images first and then compare results.''')

    st.success('''
**Conclusion:** Confirmed, augmenting images improved model accuracy by approximately 10%. However it also increased time to train the model by 42%.
''')

    st.write('---')

    st.info('''
**Hypohesis 4:**
Fine tuning hyperparameters will significantly improve the models accuracy.''')

    st.warning('''
**How to validate:**
Test the model with base settings and then attempt to increase the score.''')

    st.success('''
**Conclusion:**
''')

    st.write('---')

    st.info('''
**Hypohesis 5:** Training the model with images that has higher
resolution will improve accuracy.''')

    st.warning('''
**How to validate:** Create datasets with different image quality,
then train and test the model with each dataset.''')

    st.error('''
**Conclusion:** Hypothesis is incorrect. Higher resolution images does
not always equal better model performance.

Training the model on images 25% of the average size
resulted in 20% less accuracy but incredibly fast training time.
Training the model on images 50% of the average size resulted in
better similar accuracy and 80% faster to train the model.
This shape will be used going forward.
''')

    st.write('---')