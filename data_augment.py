import cv2
import os
import sys


# data path for storing of data
DATA_PATH = sys.argv[1]

for direc in os.listdir(DATA_PATH):
    if direc not in ['rock','paper','scissor']:
        continue
    
    print(direc)

    count = direc.count

    for picture in os.listdir(os.path.join(DATA_PATH,direc)):
        pict_path = os.path.join(DATA_PATH,direc+'/'+picture)

        #reading the already stored image
        img = cv2.imread(pict_path)


        # Image flipping for manipulating data set
        aug_img1 = cv2.flip(img,1)


        # Image resizing for manipulating data set
        aug_img2 = cv2.resize(img[50:250,50:250],(300,300))

        # Stoering the augmented images
        cv2.imwrite(pict_path[:-4]+"_aug1.jpg",aug_img1)
        cv2.imwrite(pict_path[:-4]+"_aug2.jpg",aug_img2)