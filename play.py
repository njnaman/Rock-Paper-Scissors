from keras.models import load_model
from random import choice
import cv2
import numpy as np
import ctypes

CLASS_MAP = {
    0: "rock",
    1: "paper",
    2: "scissor",
    3: "none"
}

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def mapper(val):
    return CLASS_MAP[val]

def checkWinner(user1_move , user2_move):
    if(user1_move==user2_move):
        return "TIE"
    
    if(user1_move=="rock"):
        if(user2_move=="scissor"):
            return "User1"
        if(user2_move=="paper"):
            return "User2"

    
    if(user1_move=="paper"):
        if(user2_move=="rock"):
            return "User1"
        if(user2_move=="scissor"):
            return "User2"

    
    if(user1_move=="scissor"):
        if(user2_move=="paper"):
            return "User1"
        if(user2_move=="rock"):
            return "User2"


model = load_model("RPS_MODEL1.h5")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1500)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1500)


prev_move = None

while True:
    ret , frame = cap.read()
    if not ret:
        continue

    cv2.rectangle(frame , (100,100), (500,500 ), (255,255,255),2)

    cv2.rectangle(frame , (800,100) , (1200,500) , (255,255,255),2)

    # User1 move prediction
    roi1 = frame[100:500,100:500]
    img1= cv2.cvtColor(roi1,cv2.COLOR_BGR2RGB)
    img1 = cv2.resize(img1 , (300,300))
    pred1 = model.predict(np.array([img1]))
    move_code = np.argmax(pred1[0])
    user1_move_name = mapper(move_code)

    # User2 move prediction
    roi2 = frame[100:500,800:1200]
    img2= cv2.cvtColor(roi2,cv2.COLOR_BGR2RGB)
    img2 = cv2.resize(img2 , (300,300))
    pred2 = model.predict(np.array([img2]))
    move_code = np.argmax(pred2[0])
    user2_move_name = mapper(move_code)


    #deciding the winner
    winner = checkWinner(user1_move_name , user2_move_name)
    
     # display the information
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "User1 Move: " + user1_move_name, (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "User2 Move: " + user2_move_name, (750, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Winner: " + winner, (400, 600), font, 2, (0, 0, 255), 4, cv2.LINE_AA)


    cv2.imshow("Rock Paper Scissors", frame)

    k = cv2.waitKey(10)
    if k == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
    
    


