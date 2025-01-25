from keras.models import load_model
import cv2
import numpy as np
from keras.preprocessing import image
import db 

model = load_model('model.h5')
img = image.load_img(path= 'image/5.jpg',target_size=(100,100,3))
img = image.img_to_array(img)
test_img = img.reshape((1,100,100,3))
img_class = model.predict_classes(test_img)
prediction = img_class
#print(img_class)
print(model.predict(test_img))
# classes = train_generator.class_indices
# inv_dict = {v: k for k, v in classes.items()} 
# print(inv_dict)
dic={0: 'Apple', 1: 'Banana', 2: 'Orange', 3: 'Strawberry', 4: 'znone'}
print(dic.get(img_class[0]))
if img_class[0]!=len(dic)-1:
    db.dbcall(dic[img_class[0]])
