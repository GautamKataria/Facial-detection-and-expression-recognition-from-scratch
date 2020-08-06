# Facial-detection-and-emotion-expression-recognition-from-scratch-using-custom-dataset



### SETUP:
##### First download the following files 
##### Then make the following folders :- 
##### 'Images123' 
##### images -> Train, Test -> all folders of emotions eg- (happy,neutral,angry,sad,surprise)
#####        
### Collecting Data:
##### First run the face_recog_data file which is gonna create image dataset for you by detecting and localizing your face.
##### you can adjust the number of pictures you want by changing count values.
##### It stores the pictures it takes to the "Images123" folder.

##### Move the pictures to images -> Train, Test -> all folders of emotions eg- (happy,neutral,angry,sad,surprise)
##### Do this process for all the emotions/ expressions for train and test folders

### Model building
##### Now follow along the jupytrer notebook to make a tranfer learning Resnet model to classify our images into emotions/expresssions.
##### i have configured it so that only the best model will be chosen through model checkpointing based on val_loss so you dont have to worry about overfitting the model. 

### Results

##### Now to see the final product run the model_working.py file which will show you the result and detections in realtime.
{% figure caption:"Neutral" %}
![neutral](https://res.cloudinary.com/gautzz/image/upload/v1596703695/Emotion%20recognition/neutral_v1_lep0s6.png)
{% endfigure %}
{% figure caption:"Happy" %}
![happy](https://res.cloudinary.com/gautzz/image/upload/v1596703692/Emotion%20recognition/happy_mthl1t.png)
{% endfigure %}
{% figure caption:"Surprised" %}
![surprised](https://res.cloudinary.com/gautzz/image/upload/v1596703701/Emotion%20recognition/surprise_v_idk_weet9e.png)
{% endfigure %}
{% figure caption:"Angry" %}
![angry](https://res.cloudinary.com/gautzz/image/upload/v1596703678/Emotion%20recognition/angry_v1_omfxdr.png)
{% endfigure %}
{% figure caption:"Sad" %}
![Sad](https://res.cloudinary.com/gautzz/image/upload/v1596703698/Emotion%20recognition/sad_wa6b8r.png)
{% endfigure %}

