# Cats vs Dogs

![Amiresponsive image](TODO)

Link to live website: [Cats vs Dogs](TODO) <br>(*Hold Ctrl (or Cmd) and click to open in a new window.*)



## Dataset Content

TODO: remove
* Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's maximum size and to have a shorter model training time. If you are doing an image recognition project, we suggest you consider using an image shape that is 100px × 100px or 50px × 50px, to ensure the model meets the performance requirement but is smaller than 100Mb for a smoother push to GitHub. A reasonably sized image set is ~5000 images, but you can choose ~10000 lines for numeric or textual data. 

The dataset contains 12500 pictures of cats and dogs from [Asirra](http://research.microsoft.com/en-us/um/redmond/projects/asirra/) in partnership with [Petfinder.com](http://www.petfinder.com/) <br>
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

- The dataset is sourced from [Kaggle](https://www.kaggle.com/competitions/dogs-vs-cats) as part of a public competition. This dataset contains 25,000 images of cats and dogs, out of which only half are labeled and will be used in this project. These 12,500 labeled images will be split into training, validation, and test sets for model development. This split will ensure that the model has a well-rounded understanding during training and can be accurately evaluated on unseen data during validation and testing phases.


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).

TODO


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

TODO


## Deployment
### Heroku

* The App live link is: TODO
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries

- **Pandas**, used in the project and provide an example(s) of how you used these libraries.
- **NumPy**, used in the project and provide an example(s) of how you used these libraries.

TODO


## Credits 

TODO


* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people that provided support through this project.

