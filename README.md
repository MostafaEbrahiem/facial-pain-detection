# facial-pain-detection

⦁	Dataset: The data used in this project is UNBC-McMaster shoulder pain expression which consists of nearly 48000 thousand frames extracted from videos of patient’s facial expression during treatment, it’s labeled from 0 to 10 as a pain scale.

⦁	Data preparation process: The dataset consists of
         - 400029 images of label 0 (No pain).
         -3128 images of label 1.
         -2351 images of label 2. 
         -1412 images of label 3.
         -802 images of label 4.
         -242 images of label 5.
         -270 images of label 6.
         -53 images of label 7.
         -78 images of label 8.
         -32 images of label 9.
         -10 images of label 10.
         so clearly, it is not balanced data and to balanced it we grouped all the pain                          images (above 0 label) into one label as1 (8369 images) and cut the no pain
         images to 8471 images so it can be balanced and trainable, All images
         resized to 250*250to reduce ram usage during training on colab.   

⦁	Model used: Regular CNN structural used with auto tuning on vgg16 neural network to boost model accuracy which reached 83% classifying 2classes (Pain or no Pain).


⦁	Training and testing time: Training Tooks about 30 minute to train on 13 epochs and testing took about 2 seconds.



⦁	Deploying part: The model deployed on desktop application made using Tkinter library with python.


⦁	Colab notebook link: -  https://colab.research.google.com/drive/1YGtCxL9L3EWq9bNehQv-hek71CGnkrWg?usp=share_link.


⦁	Screen shoots: -


⦁	Model structural 


              

⦁	Training
 



⦁	Model loss and accuracy 
           

⦁	How to run it:-
-open your visual code, open the project folder and inside your terminal write (pip install -r requirements.txt) to install the required library to run the project.

-run the UI.py file.

⦁	NOTES: to obtain good accuracy the uploaded images and the captured images must be in excellent quality, otherwise the results will be inaccurate and to capture an image press the ‘’q’’ button.



