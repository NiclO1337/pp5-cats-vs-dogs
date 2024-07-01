import streamlit as st


def page_summary_body():

    st.write('---')

    st.header('**Project summary**')

    st.info('''
**General information**

Web services are often protected with a challenge that's supposed to be easy 
for people to solve, but difficult for computers. Such a challenge is often 
called a CAPTCHA (Completely Automated Public Turing test to tell Computers 
and Humans Apart) or HIP (Human Interactive Proof). HIPs are used for many 
purposes, such as to reduce email and blog spam and prevent brute-force 
attacks on web site passwords.

Asirra (Animal Species Image Recognition for Restricting Access) is a HIP that 
works by asking users to identify photographs of cats and dogs.

As a Data Analyst from Code Institute Consulting, we are tasked with helping 
Asirra improve on their HIP software. The current literature suggests that 
machine classifiers can score above 80% accuracy on this task. Therefore, 
Asirra is no longer considered safe from attack.
''')

    st.success('''
**Project dataset**

The dataset contains 25000 pictures of cats and dogs from Asirra in partnership
with Petfinder.com. The images are taken and manually classified by people at 
thousands of animal shelters. 
''')

    st.warning('''
**Additional information**

The projects [**README**](https://github.com/NiclO1337/pp5-cats-vs-dogs) file 
contains more information.
''')

    st.error('''
**Business requirements**


1. The client requires us to do a study of their dataset and show them our 
results.

2. The client wants to have a ML model so that they can use it to test their 
HIP software.
''')