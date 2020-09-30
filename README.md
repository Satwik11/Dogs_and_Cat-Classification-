# Dogs_and_Cat-Classification-
## Problem statement : 
In this Section we are implementing Convolution Neural Network(CNN) Classifier for Classifying dog and cat images. The Total number of images available for training is 8000 and final testing is done on seperate 1880 images.

![Test_Image_4](https://user-images.githubusercontent.com/45566835/87918055-242b7180-ca76-11ea-8a26-c346edd710c5.gif)

## Dependencies

numpy,
matplotlib,
keras,
pillow,
opencv-python,
streamlit,
scikit-learn,
tensorflow

Then use the image of web app using streamlit 

### Images of web app : 
### for cat:
![Test Image 1](https://github.com/Satwik11/Dogs_and_Cat-Classification-/blob/master/cat1.png)
### for dog:
![Test Image 2](https://github.com/Satwik11/Dogs_and_Cat-Classification-/blob/master/dog1.png)

## Image Classification :
The very first step in CNN is to classify image,since it very easy to visualize an image with human eye but how can we make the same thing to visualize through our machine …..sad but machines can see :( this can be achieved through the matrix representation of image)

![Test Image 3](https://www.jeremyjordan.me/content/images/2018/01/Screen-Shot-2017-11-07-at-12.32.19-PM.png)

## Augmenting and Compiling the images :
This is something which helps in training our model with best fit. Augmentation is the pre-processing of image where an model is been trained with wide diversity of an image. This diversity of an image can be carried out in following ways like scaling, translation, rotation and flipping etc.


## To execute file:
To see web app execute Making web app and hosting.ipynb as ngrock change url every time

The Making web app and hosting.ipynb link is : https://colab.research.google.com/drive/1tZ4xgZE1XwgFHIo1_R0MqeyZv236gnjF?usp=sharing

from pyngrok import ngrok
url = ngrok.connect(port=8501)
url
http://6e471a60426c.ngrok.io -> After executing you will get this type of url just copy and paste it you can see the webapp
