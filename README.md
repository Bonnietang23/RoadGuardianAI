# RoadGuardianAI

## Get started


## Basic setting
Go into jetson-inference create data & images

## Dataset
A website that hosts a lot of different datasets. 
https://www.kaggle.com/datasets

The datasets I chose
https://www.kaggle.com/datasets/sharansmenon/animals141

## Detect net
Code : / jetson-inference/project/ssd$ 
## Dataset literal table
https://github.com/dusty-nv/jetson-inference/blob/master/data/networks/ssd_coco_labels.txt

This means because I use the detect net provided by NVIDIA.
So when testing, I have to use the provided items to test.

If you are having trouble with the training project on your nano, you can use this process as an alternative to training a custom network
https://colab.research.google.com/gist/Charlotteec/d625a314ed1ea177e632c210e06c8b28/train_model_backup.ipynb

You can adjust the code in time according to your own situation,
The required data can be found using the Kaggle I mentioned above.

## Find photos on the web
PIC 
ask

## Create a new folder
Create a new folder, rename to <project>
Add data,test and images folders in it.
## The function of this folder
Images : 
images is the place where you store the pictures you selected from the internet (the photos you want to test).

Test :
 test is the place where the pictures are tested (detected).

 ## Sent Email 
Write the code for sending email in project -ssd -send_alert.py

 ## Email Sending Conditions
 Write email conditions and recipient messages in project-ssd-detectnet.py

 During this setup, he will ask you to open your google API, so some operations will be required. If you want to know the complete code, you can refer to this link.
 https://www.learncodewithmike.com/2020/02/python-email.html
 (Chinese)
https://reurl.cc/K0LXWn
(English)








