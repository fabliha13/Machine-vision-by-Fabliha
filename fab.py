import cv2  
  
# Load the cascade  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
  
# To capture video from webcam.   
cap = cv2.VideoCapture("face video.mp4")  
  
while True:  
    # Read the frame  
    _, img = cap.read()  
  
    # Convert to grayscale  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  
    # Detect the faces  
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  
  
    # Draw the rectangle around each face  
    for (x, y, w, h) in faces:  
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
    

    font = cv2.FONT_HERSHEY_SIMPLEX
    moment = cv2.moments(gray)
    imgx= int(moment ["m10"] / moment["m00"])
    imgy= int(moment ["m01"] / moment["m00"])
    cv2.circle(img, (imgx,imgy), 15, (255, 0, 0), 7)
    distance =((((x + w//2)-imgx)**2)-(((y + h//2)-imgy)**2))**(0.5)
  
    # Use putText() method for
    # inserting text on video
    cv2.putText(img, 
                'Face Position', 
                (20, 20), 
                font, 1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
    cv2.putText(img, 
                str(center), 
                (50, 50), 
                font, 1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
    cv2.putText(img, 
                'Distance', 
                (268, 268), 
                font, 1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
    cv2.putText(img, 
                str(distance), 
                (300, 300), 
                font, 1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
    # Display  
    cv2.imshow('Video', img)  
  
    # Stop if escape key is pressed  
    k = cv2.waitKey(30) & 0xff  
    if k==27:  
        break 
