
# Importing the libraries
from PIL import Image
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import random
import cv2
import numpy as np
model = load_model('best_model_gautzz.h5')

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image

    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)

    if faces is ():
        return None

    # Crop all faces found
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cropped_face = img[y:y + h, x:x + w]
        # cv2.imshow("winname",cropped_face)
        # cv2.waitKey(0)

    return cropped_face,img


def model_predict(face, model):
    # Preprocessing the image
    x = image.img_to_array(face)
    # x = np.true_divide(x, 255)
    ## Scaling
    x = x / 255
    cv2.imshow("preprocessed img", x)
    cv2.waitKey(1)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    # x = preprocess_input(x)
    # print(x)
    preds = model.predict(x)
    print(preds)
    preds = np.argmax(preds)
    if preds == 0:
        preds = "Angry"
    elif preds == 1:
        preds = "Happy"
    elif preds == 2:
        preds = "Neutral"
    elif preds == 3:
        preds = "Sad"
    elif preds == 4:
        preds = "surprise"

    return preds

while True:
    _, frame = cap.read()

    try:
        face,img = face_extractor(frame)

        face = cv2.resize(face, (224,224))

        pred = model_predict(face, model)

        cv2.putText(img,pred,(10,25),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(255,0,0),thickness=2,lineType=cv2.LINE_AA)
        cv2.imshow("Result", img)
        cv2.waitKey(1)

        print(pred)
    except Exception as e:
        pass