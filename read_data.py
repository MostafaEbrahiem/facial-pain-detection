import os
from tqdm import tqdm
import cv2
from random import shuffle
from pickle import dump
from pickle import load
import numpy as np
from UI import main
from tkinter import *
import pickle as pk
import tensorflow as tf



def create_train_data(TRAIN_DIR,Label_Dir,IMG_SIZE):
   training_data = []
   label_data=[]

   c0=0
   c1=0
   res=0
   #reading label only 
   for folder in os.listdir(Label_Dir):
       c0=0
       for inner_folder in os.listdir((Label_Dir+'/'+folder)):
           path = os.path.join(Label_Dir,folder+'/'+ inner_folder)
           for file in os.listdir(path):                          
                file=os.path.join(path+'/'+file)
                with open(file) as f:
                    lines = f.readlines()
                    if (lines[0][3]=='0' and c0<340):
                      label_data.append('0')
                      res+=1
                      c0+=1
                    if(lines[0][3]!='0'):
                      label_data.append('1')
                      c1+=1
                    f.close()
    
   label_data.append('-1')
   print(str(res) + ' ' + str(c1))
   #reading images and it's labels
   c=0
   c0=0
   c1=0
   res=0
   print(len(label_data))
   for folder in os.listdir(TRAIN_DIR):
        c0=0
        for inner_folder in os.listdir((TRAIN_DIR+'/'+folder)):
            path = os.path.join(TRAIN_DIR,folder+'/'+ inner_folder)
            for img in tqdm(os.listdir(path)):
                img=os.path.join(path+'/'+img)
                img_data = cv2.imread(img,cv2.IMREAD_COLOR)#cv2.IMREAD_COLOR
                img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
                img_data = cv2.cvtColor(img_data,cv2.COLOR_RGB2BGR)
                if (label_data[c]=='-1'):break
                if (label_data[c]=='0' and c0<340):
                  training_data.append([np.array(img_data), label_data[c]])
                  c0+=1
                  res+=1
                  c+=1
                if (label_data[c]!='0'):
                  training_data.append([np.array(img_data), label_data[c]])
                  c+=1
                  c1+=1
            #print(str(res) + ' ' + str(c1))      

   print(str(res) + ' ' + str(c1))           

   shuffle(training_data) 
   dump(training_data, open('/content/drive/MyDrive/saves/training_data.pkl', 'wb'))
   return training_data


def test(IMG_SIZE):
    model=tf.keras.models.load_model("res_model.h5")
    img=cv2.imread("test/5.jpg", cv2.IMREAD_COLOR)
    img=cv2.resize(img,(IMG_SIZE,IMG_SIZE))
    img = np.array(img).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
    prediction=model.predict(img)
    print(prediction)
    print(np.argmax(prediction[0]))
    


if __name__=='__main__':
    TRAIN_DIR='images/Images'
    Label_Dir='Frame_Labels/Frame_Labels/PSPI'
    #create_train_data(TRAIN_DIR,Label_Dir,150)
    test(250)
    


     