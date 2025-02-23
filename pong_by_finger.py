import cv2
import mediapipe as mp
cam = cv2.VideoCapture(0)
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


mp_hand = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
drawing = mp.solutions.drawing_utils

x=int(frame_width/2)
y=int(frame_height/2)
mx=3
my=3
points=0
def MYhands(framee):
    myHands = []
    frameRGB = cv2.cvtColor(framee, cv2.COLOR_BGR2RGB)
    results = mp_hand.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for one_hand in results.multi_hand_landmarks:
             for hand_landmarks in one_hand.landmark:
                 myHands.append((int(hand_landmarks.x * frame_width), int(hand_landmarks.y * frame_height)))
    return myHands
while True:
    ret, frame = cam.read()
    if not ret:
        break
    handArr = MYhands(frame)
    if len(handArr) > 20:
        frame=cv2.rectangle(frame,(handArr[8][0],0),(handArr[8][0]+65,14),(0,0,255),-1)
    frame=cv2.putText(frame,f"Score:{points}",(20,25),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    frame=cv2.circle(frame,(x,y),10,(0,0,255),-1)
    x+=mx
    y+=my
    if x>=frame_width-4 or x<=0+4:
        mx*=-1
    if y>=frame_height-4 :
        my*=-1
    if y<=0+4:
        points-=1
        my*=-1
    if len(handArr) > 20:
        if handArr[8][0]<=x<=handArr[8][0]+65 and 0<=y<=14:
            points+=1
            my*=-1
    if points < 0:
        frame = cv2.putText(frame, "Game Over", 
                            (int(frame_width / 2) - 130, int(frame_height / 2) - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
        
        cv2.imshow('MediaPipe hand', frame)  # Show the final "Game Over" frame
        cv2.waitKey(2000)  # Wait for 4 seconds
        break  # Exit the loop

    cv2.imshow('MediaPipe hand', frame)
    # if points<0:
    #     time.sleep(4)
    #     break
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()           
