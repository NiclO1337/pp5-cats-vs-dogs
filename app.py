import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_image_study import page_image_study_body
from app_pages.page_image_classifier import page_image_classifier_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_body

app = MultiPage(app_name='Purrfect Paws Predictor')

app.app_page('Project Summary', page_summary_body)
app.app_page('Image Study', page_image_study_body)
app.app_page('Cats vs dogs classifier', page_image_classifier_body)
app.app_page("Project Hypothesis", page_project_hypothesis_body)
app.app_page("ML Performance Metrics", page_ml_performance_body)

app.run()