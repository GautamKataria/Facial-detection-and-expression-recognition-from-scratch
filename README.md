# Facial-detection-and-emotion-expression-recognition-from-scratch



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

### Deployment

##### Now to see the final product run the model_working.py file which will show you the result and detections in realtime.

