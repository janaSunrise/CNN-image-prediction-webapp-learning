# CNN Image Detection

## Contents
---
  #### Image Deresolution Script
  - This script creates a deresolution face dataset for you!
  
  #### Django Image Classifier
  
  - The Django folder contains all the files needed for our netlify site implmentation
  
  - Model used: Convolutional Neural Network (CNN)
  - Libraries used: Tensorflow, and Keras
    
##### Steps to start the Django Server in localhost:8000
    
  1. Open up Anaconda3 command prompt or regular command prompt
  
  2. change directory to where django folder is located
  ```
  cd [file location]
  ```
  
  3. Create virtual environment using python 3.6.x:
  **conda**
  NOTE: environment name does not matter
  ```
  conda create -n [environment name] python=3.6
  ```
      
  4. Activate your virtual environment by:
  **conda**
  ```
  conda activate [environment name]
  ```
      
  5. Install dependencies from requirements.txt file:
  ```
  pip install -r requirements.txt
  
                  or
  
  pip3 install -r requirements.txt
  ```
      
  6. Activate the server in localhost:8000:
  ```
  python manage.py runserver
  ```
      
  7. Go to the browser and access local host:
  <p>In url bar, search "localhost:8000" or any similar local hosts.</p>
      

## Resources
- [CNN Slides](https://docs.google.com/presentation/d/1a0WRuEHIr7HNCJbs-l3ocstHtAtfSL8GbBNvRIgH0lU/edit#slide=id.g96c15fa444_1_3)
- [Youtube Video](https://www.youtube.com/watch?v=N7V_5FmjOug&feature=youtu.be&t=438)

## Credits

All the credits for making this project goes to [Hermes Bonilla](https://github.com/HermesBonilla) for making this, and I have just modified the project structure for better conventions, and also modifying the frontend looks, the predictions, and the resources too.
