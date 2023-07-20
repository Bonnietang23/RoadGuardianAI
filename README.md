# RoadGuardianAI
## Introduction
This project is about a system that detects humans, bears, cars, animals, and stop signs. 
When the system detects these objects, it will automatically send an email to my Gmail inbox. This project leverages the built-in `detectnet.py` function on jetson-inference library. And your demo is done on jetson nano.The core of this project involves using deep learning techniques, particularly Convolutional Neural Networks (CNN), to recognize and classify different objects. Through this approach, we can achieve efficient and accurate object detection and promptly notify the user when specific objects are detected.
### Paradigm
![Imgur](https://i.imgur.com/9wkQyR2.jpg)
![Imgur](https://i.imgur.com/EFBemRN.jpg)
![Imgur](https://i.imgur.com/UDcLm7k.png)

### The Impactful Places and the Integration of Future Technology
This project has broad application potential. For example, it can be applied to intelligent surveillance systems, where suspicious objects detected by surveillance cameras can be promptly reported to security personnel. Additionally, it can be utilized in traffic monitoring, automatically notifying the traffic management center or drivers when hazardous situations are detected, such as animals or stop signs, to enhance road safety. Moreover, the system contributes to wildlife conservation, aiding in monitoring the activities of bears or other wildlife and providing real-time information to relevant authorities.



## Get started
1.Get jetson infereance

```{bash}
git clone https://github.com/dusty-nv/jetson-inference.git
```
2.Find photos on the web
![Imgur](https://i.imgur.com/9wkQyR2.jpg)
3.Put the photos into the jetson-inference-images file.
4.enter the code

```{bash}
$ ~/project/ssd$ python3 detectnet.py ~/jetson-inference/data/images/<Your_image>.jpg  ~/project/data/images/test/<Output_image>.jpg
```

example code:
```{bash}
$ ~/project/ssd$ python3 detectnet.py ~/jetson-inference/data/images/bear_123123.jpg  ~/project/data/images/test/bear_123123.jpg
```
5.Find the detected pictures in project -data-test
![Imgur](https://i.imgur.com/EFBemRN.jpg)
6.And receive the message that the bear has been detected in the email.
![Imgur](https://i.imgur.com/UDcLm7k.png)


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









