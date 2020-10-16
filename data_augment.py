import cv2
import os
import sys

DATA_PATH = sys.argv[1]

for direc in os.listdir(DATA_PATH):
    if direc not in ['rock','paper','scissor']:
        continue
    
    print(direc)

    count = direc.count

    for picture in os.listdir(os.path.join(DATA_PATH,direc)):
        pict_path = os.path.join(DATA_PATH,direc+'/'+picture)
        print(pict_path)
        img = cv2.imread(pict_path)
        aug_img1 = cv2.flip(img,1)
        aug_img2 = cv2.resize(img[50:250,50:250],(300,300))
        cv2.imwrite(pict_path[:-4]+"_aug1.jpg",aug_img1)
        cv2.imwrite(pict_path[:-4]+"_aug2.jpg",aug_img2)