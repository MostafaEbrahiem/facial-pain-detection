from PIL import Image
import os
from tkinter import *
import tkinter.messagebox
import numpy as np
from PIL import ImageTk,Image
from tkinter import filedialog
from pickle import dump
import os
import gc
import cv2
import tensorflow as tf

def open_img() :
    global path
    global model
    Imagesize=250

    # canvas.delete("all")

    img_path = filedialog.askopenfilename()
    img_display = Image.open(img_path)

    ########### prediction part ##################
    img=cv2.imread(img_path, cv2.IMREAD_COLOR)
    img=cv2.resize(img,(Imagesize,Imagesize))
    img = np.array(img).reshape(-1, Imagesize, Imagesize, 3)
    prediction=model.predict(img)
    ########### /prediction part #################
    pain_text="this person is in pain ("+str(int(prediction[0][0]*100))+"%)"
    No_pain_text="No Pain"
    print(int(prediction[0][0]*100))
    
    if not np.argmax(prediction[0]):res = Label(text=pain_text,bg='#fff', fg='#f00', pady=10, padx=10, font=10) 
    else: res = Label(text=No_pain_text,bg='#fff', fg='#0f0', pady=10, padx=10, font=10) 
    res.place(x=550, y=450) 
    res.after(4000, res.destroy)
    # img_display = img_display.resize((1200, 650), Image.ANTIALIAS)
    # img_display = ImageTk.PhotoImage(img_display)
    # canvas.create_image(0, 0, anchor=NW, image=img_display)
    ch=1
    gc.collect()
    form.mainloop()


def capture_image():
    Imagesize=250
    img = cv2.VideoCapture()
    # The device number might be 0 or 1 depending on the device and the webcam
    img.open(0, cv2.CAP_DSHOW)
    while (True):
        ret, frame = img.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    img.release()
    cv2.destroyAllWindows()
    
    ########### prediction part ##################
    img=cv2.resize(frame,(Imagesize,Imagesize))
    img = np.array(img).reshape(-1, Imagesize, Imagesize, 3)
    prediction=model.predict(img)
    pain_text="this person is in pain ("+str(int(prediction[0][0]*100))+"%)"
    No_pain_text="No Pain"
    if not np.argmax(prediction[0]):res = Label(text=pain_text,bg='#fff', fg='#f00', pady=10, padx=10, font=10) 
    else: res = Label(text=No_pain_text,bg='#fff', fg='#0f0', pady=10, padx=10, font=10) 
    res.place(x=550, y=450) 
    res.after(4000, res.destroy)
    print(int(prediction[0][0]*100))
    ########### /prediction part #################
    # img_display = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # img_display = Image.fromarray(img_display)
    # img_display = img_display.resize((1200, 650), Image.ANTIALIAS)
    # img_display = ImageTk.PhotoImage(img_display)
    # canvas.create_image(0, 0, anchor=NW, image=img_display)
    form.mainloop()

def main():

    ################GUI##################
    img = Image.open("images\pain-scale-chart-3.gif")
    img = ImageTk.PhotoImage(img)
    canvas.create_image(100, 50, anchor=NW, image=img)

    Upload_butt = Button(text="   Upload   ", command=open_img)
    Upload_butt.place(x=670, y=600)

    capture = Button(text="   Capture   ", command=capture_image)
    capture.place(x=470, y=600)


    form.mainloop()


if __name__ == '__main__':
    model=tf.keras.models.load_model("res_model.h5")
    form = Tk()
    canvas = Canvas(form, width=1200, height=650)
    canvas.pack()
    main()