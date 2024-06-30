import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_image_study import page_image_study_body

app = MultiPage(app_name='Purrfect Paws Predictor')

app.app_page('Project Summary', page_summary_body)
app.app_page('Image Study', page_image_study_body)

app.run()