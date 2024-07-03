import streamlit as st


def page_project_hypothesis_body():

    st.write('---')

    st.header('**Project hypotheses**')

    st.write('---')

    st.info('''
**Hypohesis 1:** Cats are more uniform in appearance, while dogs exhibit
greater variability in shape and size.
''')

    st.warning('''
**Validation Method:** Average image study.
''')

    st.error('''
**Conclusion:** The dataset's high image variability prevented identification
of distinct cat or dog features. **Further manual review of the dataset is
recommended.**
''')

    st.write('---')

    st.info('''
**Hypohesis 2:** A deep learning model with a convolutional neural network
(CNN) can accurately classify client images.''')

    st.warning('''
**Validation Method:** Train and test a CNN model.''')

    st.success('''
**Conclusion:** The CNN performed well even without augmentation or
hyperparameter tuning.
''')

    st.write('---')

    st.info('''
**Hypohesis 3:**
Augmenting the training set will substantially improve model performance.''')

    st.warning('''
**Validation Method:**
Compare model performance with and without augmented images.''')

    st.success('''
**Conclusion:** Augmentation increased accuracy by approximately 10% but
extended training time by 42%. **Hypothesis confirmed**.
''')

    st.write('---')

    st.info('''
**Hypohesis 4:**
Fine-tuning hyperparameters will significantly enhance model accuracy.''')

    st.warning('''
**Validation Method:**
Compare model performance with default and tuned hyperparameters.''')

    st.success('''
**Conclusion:** Hyperparameter tuning significantly impacts model performance.
**Hypothesis confirmed**.''')

    st.write('---')

    st.info('''
**Hypohesis 5:**
Training on higher-resolution images will improve accuracy.''')

    st.warning('''
**Validation Method:**
Train and test the model on datasets with varying image resolutions.''')

    st.error('''
**Conclusion:** Initially incorrect, but more nuanced.''')

    st.success('''
**Explanation**: Higher resolution doesn't always equate to better performance.
25% of average size resolution images resulted in lower accuracy but much
faster training. 50% of average size resolution images yielded similar
accuracy with significantly reduced training time. Further testing revealed
that due to dataset complexity, larger image size might be more crucial than
initially thought.''')

    st.write('---')