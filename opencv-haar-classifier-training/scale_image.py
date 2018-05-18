import cv2
import numpy as np
import os

def find_resize():
    for file_type in ['positive_images']:
        for img in os.listdir(file_type):
            try:
                current_image_path = str(file_type)+'/'+str(img)
#                print(current_image_path)
                img1 = cv2.imread(current_image_path)
                print(str(img))
                resized_image = cv2.resize(img1, (150, 100))
                cv2.imwrite("postivie_image_new/"+str(img),resized_image)
                #cv2.imwrite("negative_image_new/"+current_image_path,resized_image)
                #print("Resized image", resized_image)
            except Exception as e:
                    print(str(e))

find_resize()


