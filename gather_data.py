import cv2
import os
import sys
import shutil

path = os.getcwd()+'\\'

label=sys.argv[1]
number_of_samples = int(sys.argv[2])

print(label)

save_path = os.path.join(path,label)

shutil.rmtree(save_path,ignore_errors=True)
try:
    os.makedirs(save_path)
except Exception as e:
    print(f'  {e}  dikkt')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1000)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1000)



count=0
start=False

while True:
    ret , frame = cap.read()

    if not ret:
        continue

    if count==number_of_samples:
        break

    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)

    if start:
        cv2.imwrite(save_path+'\\'+label+'{}.jpg'.format(count),frame[100:500, 100:500])
        count+=1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Collecting {}".format(count),
            (5, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Collecting images", frame)

    k = cv2.waitKey(10)
    if k == ord(' '):
        start = not start

    if k == ord('e'):
        break
    




cap.release()
cv2.destroyAllWindows()









