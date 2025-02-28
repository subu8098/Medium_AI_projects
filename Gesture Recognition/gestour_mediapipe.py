import mediapipe as mp
import cv2
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mphand = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

cam = cv2.VideoCapture(0)
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
def Hands(frame):
    farmeRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = mphand.process(farmeRGB)

    if results.multi_hand_landmarks:
        TotalHands=[]
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks=[]
            for landmark in hand_landmarks.landmark:
                landmarks.append((int(landmark.x*frame_width),int(landmark.y*frame_height)))
            TotalHands.append(landmarks)
        return TotalHands
           
def location(datapoints):
    detectionArray=np.zeros([len(datapoints),len(datapoints)],dtype='float')
    for row in range(0,len(datapoints)):
        for column in range(0,len(datapoints)):
            detectionArray[row][column]=((datapoints[row][0]-datapoints[column][0])**2+(datapoints[row][1]-datapoints[column][1])**2)**(1./2.)
    return detectionArray

def findError(knownmatrix,unknownmatrix,keypoints):
    error=0
    for row in keypoints:
        for column in keypoints:
            error=error+abs(knownmatrix[row][column]-unknownmatrix[row][column])
    return error

keypoints=[0,4,5,9,13,17,8,12,16,20]
train=True
while True:
    ret, frame = cam.read()
    MyHands=Hands(frame)
    
    if train==True:
        if MyHands!=[]:
            print('Show your Gesture, press t when Ready')
            if cv2.waitKey(1) & 0xff==ord('t') and MyHands!=None:
                knownGesture=location(MyHands[0])
                train=False
                print(knownGesture)
    if train == False:
        if MyHands!=None:
            unknownGesture=location(MyHands[0])
            error=findError(knownGesture,unknownGesture,keypoints)
            cv2.putText(frame,str(int(error,)),(100,175),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),8)
            if cv2.waitKey(1)==ord('r'):
                train=True
    if MyHands!=None:
        for h in MyHands:
            for i in keypoints:
                frame=cv2.circle(frame,(h[i][0],h[i][1]),5,(0,0,255),3)


    cv2.imshow('MediaPipe hand', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
