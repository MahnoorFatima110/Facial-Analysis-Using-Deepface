
from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2 as cv
import os

prefix="dataset/"
length=len(os.listdir("dataset"))
image_name=input("Enter an image number ")
image_type=input("Enter extension ")
image_type.upper()
image_path=prefix+image_name+"."+image_type
img=cv.imread(image_path)
print(image_path)
plt.imshow(img[:,:,::-1])
result=DeepFace.analyze(img)
if(str(result["gender"])=="Man"):
    plt.title("Hello Sir!")
else:
    plt.title("Hello Miss!")
plt.xticks(())
plt.yticks(())
#print(result)
print("This is a "+str(result["gender"])+" from the race "+str(result["race"]))
if(str(result["gender"])=="Man"):
    print("He ",end=" ")
else:
    print("She ",end=" ")
print("is of age "+str(result["age"])+" and is feeling "+ str(result["emotion"]) )

