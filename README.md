# Purrfect Paws Predictor

![Project image](docs/woof_meow.jpg)

### Cats vs Dogs Classification

Link to live website: [Purrfect Paws Predictor](https://purrfect-paws-predictor-ab2bd8b45a44.herokuapp.com/)
<br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)



## Dataset Content

The dataset contains 25000 pictures of cats and dogs from [Asirra](http://research.microsoft.com/en-us/um/redmond/projects/asirra/) in partnership with [Petfinder.com](http://www.petfinder.com/) <br>
The images are taken and manually classified by people at thousands of animal shelters. They are used by Asirra for HIP (Human Interactive Proof). HIPs are used for many purposes, such as to reduce email and blog spam and prevent brute-force attacks on web site passwords.

## Business Requirements

As a Data Analyst from Code Institute Consulting, we are tasked with helping Asirra improve on their HIP software. The current literature suggests that machine classifiers can score above 80% accuracy on this task. Therefore, Asirra is no longer considered safe from attack.

- The client requires us to do a study of their dataset and show them our results.
- The client wants us to develop a machine learning model that is able to crack the CAPTCHA.
- The client needs a dashboard where they can test our model with live data.


## Hypothesis and how to validate?

- Cats are more uniform while dogs come in all shapes and sizes.
  - We will use an average image study to investigate this.

- A deep learning model with a convolutional neural network (CNN) should be able to accuratly classify the clients images.
  - We will train a model using CNN and then test the performance.

- Augmenting training set images will greatly improve performance.
  - Test model without augmented images first and then compare results.

- Fine tuning hyperparameters will significantly improve the models accuracy.
  - Test the model with base settings and then attempt to increase the score.

- Training the model with images that has higher resolution will improve accuracy.
  - Create datasets with different image quality, then train and test the model with each dataset.


## The rationale to map the business requirements to the Data Visualizations and ML tasks

### **Business Requirement 1**: Data Visualization
- As a client, we want to be able to access the data analysis and ML tool so that we can learn valuable insights
  - We will design a dashboard for client using Streamlit.

- As clients, we want to understand how the model interprets the images so that we can identify the distinctive features it recognizes and better select images for our HIP software.
  - We will display the "mean" and "standard deviation" from the average image study

- As a client, we want to see how the model can differentiate between cat and dogs so that we know how to improve our software in the future
  - We will show the differences between the average cat and dog images.

- As a client, when looking at the analysis we want to be able to see a examples of images from the dataset so that we are reminded of what the current images looks like.
  - We will show a montage of images from the dataset of both cats and dogs.

### **Business Requirement 2**: Classification

- As a client, we want to have a ML model so that we can use it to test our HIP software.
  - We will design a model, test the performance and display the results on the dashboard.

- As a client, I want to be able to upload images to test the model so that we learn which types of images is easy or not to predict on.
  - We will predict if a given image is of a cat or a dog.


## ML Business Case

### Cats vs Dogs classification

- We want an ML model to predict if an image is of a cat or a dog.

- Our ideal outcome is to improve the state of the art in automatic image classification for distinguishing cats and dogs, potentially rendering Asirra CAPTCHAs obsolete and advancing computer vision techniques.

- The models success metrics are
  - Accuracy above 80% on the test set.

- The model output is defined as a flag indicating if the image is of a cat or a dog, along with the associated probability for each class. This model could be used to automate tasks that involve identifying cats and dogs in images, such as in CAPTCHAs or pet adoption websites.

- Heuristics: Traditional image recognition tasks for distinguishing between cats and dogs have relied on manual classification, which can be slow and inconsistent. The Asirra dataset, used in CAPTCHAs, is a good example where humans outperform machines. By improving machine accuracy in this task, we aim to enhance automated systems' reliability and potentially mitigate security concerns related to CAPTCHAs.

- The dataset is sourced from [Kaggle](https://www.kaggle.com/competitions/dogs-vs-cats) as part of a public competition. This dataset contains 25,000 images of cats and dogs, these labeled images will be split into training, validation, and test sets for model development. This split will ensure that the model has a well-rounded understanding during training and can be accurately evaluated on unseen data during validation and testing phases.


## Dashboard Design

### Page 1: Quick Projet Summary

- General information:  An overview of the project, its goals, and its importance.
- Project Dataset: Detail about the dataset, including its source, size, and the type of data it contains.
- Link to additional information: Provide links to external resources, documentation, or additional project related information.
- Business requirements: Clearly state the business requirements that this project aims to address.


### Page 2: Image study

This page will provide an analysis of the dataset's images to understand their characteristics.

- Image Shape Analysis: Display the "mean" and "standard deviation" from the average image study.
- Difference Between Cat and Dog Images: Show the differences between the average cat and dog images.
- Image Montage: Display a montage of images from the dataset of both cats and dogs to remind users of what the current images look like.

Business requirement 1: Help clients understand how the model interprets images and provide insights into distinctive features.


### Page 3: Cats vs Dogs Classifier

Display the results of the classification model.

- Upload Image Widget: Allow users to upload an image for classification.
- Model Prediction: Display the prediction results, including the predicted class (cat or dog) and the associated probabilities.
- Model Differentiation: Show how the model can differentiate between cats and dogs, providing insights on the effectiveness of the model.

Business Requirement 2: Demonstrate the model's capability to classify images, enabling clients to test their HIP software.


### Page 4: Project Hopothesis and Validation

Show each hypothesis related to the project, describe how they were validated, and the conclusions drawn.

- Hypothesis Statements: Clearly state each hypothesis.
- Validation Process: Methods and steps taken to validate each hypothesis.
- Conclusions: Present the outcomes and implications of each hypothesis.

Business Requirement 1 & 2: Provide a scientific basis for the project’s approach and validate the underlying assumptions.


### Page 5: ML Performance Metrics

Display the performance metrics of the ML model to evaluate its effectiveness.

- Model History: Learning curves (loss/accuracy) for training and validation sets.
- Performance Metrics: Include metrics such as accuracy and confusion matrix for both training and test sets.
- Evaluation Results: Summarize whether the model meets the performance criteria defined in the business case.

Business Requirement 2: Assess the success of the model in achieving the desired accuracy and reliability, ensuring it meets the project goals.


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

On deployed version, the V8 model, which performs much better when tested. Can not accuratly predict on live images at all, much worse than the previously deployed V1 model. Further investigation is needed.


## Deployment

### Heroku

* The App live link is: [Purrfect Paws Predictor](https://purrfect-paws-predictor-ab2bd8b45a44.herokuapp.com/)
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in (or sign up) to Heroku. ( https://www.heroku.com/ )
2. From the dashboard, create a "new app" and follow the instructions.
3. Go to the deployment tab.
    - Select GitHub as deployment method.
    - Connect app to the correct repository.
4. Select the branch you want to deploy.
5. Choose to deploy either manully or enable automatic deploys.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


### Local development

#### Forking the project

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [TODO](TODO).
<br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)

3. Click the Fork button in the top right corner.

#### Cloning the project

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [TODO](TODO) or your forked copy.
<br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)

3. Click on the code button, select whether you would like to clone with HTTPS, SSH, or GitHub CLI, and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
Type 'git clone' into the terminal and then paste the link you copied in step 3.
5. Press enter.

#### Running a development server

1. Create a virtual environment in your workspace.
2. Install all the required dependencies in your workspace with 'pip install -r requirements.txt' command in the terminal
3. Run the server with the command 'streamlit run app.py'

#### Changes to the code
If changes has been made in local development that requires new dependencies, these needs to be added to the requirements.txt file. It is done by entering the following command in the terminal: 'pip3 freeze > requirements.txt'. Updated requirements file must then be added, commited, and pushed to GitHub.



## Main Data Analysis and Machine Learning Libraries

- **Pandas**, used to manage and analyze structured data related to images (e.g., filenames, labels, image dimensions).
- **NumPy**, essential for numerical operations on image data, especially during preprocessing and model input preparation.
- **Matplotlib** and **Seaborn**, used to create visualizations that aid in understanding model performance, such as plots of accuracy and loss.
- **Plotly**, used to create visualizations within the Streamlit app, allowing users to explore the predictions in more detail.
- **TensorFlow** and **Keras**, the core libraries for defining, training, and evaluating your convolutional neural network (CNN) model.
- **Joblib**, used for example to save and load trained machine learning model, making it faster to deploy your app without retraining every time.
- **Kaggle**, source for your initial dataset.
- **Streamlit**, used to create a dashboard for client.


## Credits

### Honorable mentions

- To all lovely people in our #community-sweden slack channel: Thank you for endless support and great laughs!
- Code Institute for providing the premade deployment ready template with a finished README structure to follow.

TODO:Remove
* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

TODO:Remove
- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

TODO:Remove
- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

### Code

- Some of the code from the Code Institutes walkthrough project was used and adapted.


