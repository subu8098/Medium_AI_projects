import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


mp_hand = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
drawing = mp.solutions.drawing_utils

x=int(frame_width/2)
y=int(frame_height/2)
mx=3
my=3
lpoints=0
rpoints=0
def MYhands(framee):
    myHands = []
    labelArr=[]
    frameRGB = cv2.cvtColor(framee, cv2.COLOR_BGR2RGB)
    results = mp_hand.process(frameRGB)
    if results.multi_hand_landmarks and results.multi_handedness :
        for hand_label in results.multi_handedness:
            labelArr.append(hand_label.classification[0].label)

        for one_hand in results.multi_hand_landmarks:
            landmark=[]
            for hand_landmarks in one_hand.landmark:
                landmark.append((int(hand_landmarks.x * frame_width), int(hand_landmarks.y * frame_height)))
            myHands.append(landmark)
    return myHands,labelArr




while True:
    ret, frame = cam.read()
    if not ret:
        break
    handArray,lableArray = MYhands(frame)
    cv2.putText(frame,f"Left_Score:{lpoints}",(20,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
    cv2.putText(frame,f"Right_Score:{rpoints}",(20,frame_height-25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
    frame=cv2.circle(frame,(x,y),10,(105,0,255),-1)
    x+=mx
    y+=my
    if y>=frame_height-4 or y<=0+4:
        my*=-1
    if x>=frame_width-4:
        rpoints-=1
        mx*=-1
    if x<=0+4:
        lpoints-=1
        mx*=-1
    
    if len(handArray) >=1:
        for hand,lable in zip(handArray,lableArray):
            if lable == "Left":
                frame=cv2.rectangle(frame,(frame_width-14,hand[8][1]),(frame_width,hand[8][1]+65),(0,0,255),-1)
                if hand[8][1]<=y<=hand[8][1]+65 and frame_width-14<=x<=frame_width:
                    rpoints+=1
                    mx*=-1

            if lable == "Right":
                frame=cv2.rectangle(frame,(0,hand[8][1]),(14,hand[8][1]+65),(0,0,255),-1)
                if hand[8][1]<=y<=hand[8][1]+65 and 0<=x<=14: 
                    lpoints+=1
                    mx*=-1
            
            
    cv2.imshow('MediaPipe hand', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
print(handArray)
print("......................")
print(lableArray)
cam.release()
cv2.destroyAllWindows()           
