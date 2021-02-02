import numpy as np
import cv2

cap = cv2.VideoCapture(1)

OFFSET = 25

RECT_LG = {
    "x1":100,
    "y1":40,
    "x2":540,
    "y2":440
    }
RECT_1 = {
    "x1":100+OFFSET,
    "y1":40+OFFSET,
    "x2":247-OFFSET,
    "y2":173-OFFSET
    }
RECT_2 = {
    "x1":247+OFFSET,
    "y1":40+OFFSET,
    "x2":393-OFFSET,
    "y2":173-OFFSET
    }
RECT_3 = {
    "x1":393+OFFSET,
    "y1":40+OFFSET,
    "x2":540-OFFSET,
    "y2":173-OFFSET
    }
RECT_4 = {
    "x1":100+OFFSET,
    "y1":173+OFFSET,
    "x2":247-OFFSET,
    "y2":307-OFFSET
    }
RECT_5 = {
    "x1":247+OFFSET,
    "y1":173+OFFSET,
    "x2":393-OFFSET,
    "y2":307-OFFSET
    }
RECT_6 = {
    "x1":393+OFFSET,
    "y1":173+OFFSET,
    "x2":540-OFFSET,
    "y2":307-OFFSET
    }
RECT_7 = {
    "x1":100+OFFSET,
    "y1":307+OFFSET,
    "x2":247-OFFSET,
    "y2":440-OFFSET
    }
RECT_8 = {
    "x1":247+OFFSET,
    "y1":307+OFFSET,
    "x2":393-OFFSET,
    "y2":440-OFFSET
    }
RECT_9 = {
    "x1":393+OFFSET,
    "y1":307+OFFSET,
    "x2":540-OFFSET,
    "y2":440-OFFSET    }

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Draw rectangle grid
    cv2.rectangle(gray, (RECT_LG["x1"], RECT_LG["y1"]), (RECT_LG["x2"], RECT_LG["y2"]), (255,255,0), 2)
    cv2.rectangle(gray, (RECT_1["x1"], RECT_1["y1"]), (RECT_1["x2"], RECT_1["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_2["x1"], RECT_2["y1"]), (RECT_2["x2"], RECT_2["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_3["x1"], RECT_3["y1"]), (RECT_3["x2"], RECT_3["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_4["x1"], RECT_4["y1"]), (RECT_4["x2"], RECT_4["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_5["x1"], RECT_5["y1"]), (RECT_5["x2"], RECT_5["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_6["x1"], RECT_6["y1"]), (RECT_6["x2"], RECT_6["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_7["x1"], RECT_7["y1"]), (RECT_7["x2"], RECT_7["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_8["x1"], RECT_8["y1"]), (RECT_8["x2"], RECT_8["y2"]), (0,255,0), 2)
    cv2.rectangle(gray, (RECT_9["x1"], RECT_9["y1"]), (RECT_9["x2"], RECT_9["y2"]), (0,255,0), 2)
    
    # Display the result+++++++++++++++++++++++++++++++++++ing frame
    cv2.imshow('Camera Feed',gray)

    k = cv2.waitKey(1)
    
    if (k%256 == 27):
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        print("Images taken.")
        RECT_1_img = "RECT_1.png"
        cv2.imwrite(RECT_1_img, gray[RECT_1["y1"]:RECT_1["y2"], RECT_1["x1"]:RECT_1["x2"]])
        RECT_2_img = "RECT_2.png"
        cv2.imwrite(RECT_2_img, gray[RECT_2["y1"]:RECT_2["y2"], RECT_2["x1"]:RECT_2["x2"]])
        RECT_3_img = "RECT_3.png"
        cv2.imwrite(RECT_3_img, gray[RECT_3["y1"]:RECT_3["y2"], RECT_3["x1"]:RECT_3["x2"]])
        RECT_4_img = "RECT_4.png"
        cv2.imwrite(RECT_4_img, gray[RECT_4["y1"]:RECT_4["y2"], RECT_4["x1"]:RECT_4["x2"]])
        RECT_5_img = "RECT_5.png"
        cv2.imwrite(RECT_5_img, gray[RECT_5["y1"]:RECT_5["y2"], RECT_5["x1"]:RECT_5["x2"]])
        RECT_6_img = "RECT_6.png"
        cv2.imwrite(RECT_6_img, gray[RECT_6["y1"]:RECT_6["y2"], RECT_6["x1"]:RECT_6["x2"]])
        RECT_7_img = "RECT_7.png"
        cv2.imwrite(RECT_7_img, gray[RECT_7["y1"]:RECT_7["y2"], RECT_7["x1"]:RECT_7["x2"]])
        RECT_8_img = "RECT_8.png"
        cv2.imwrite(RECT_8_img, gray[RECT_8["y1"]:RECT_8["y2"], RECT_8["x1"]:RECT_8["x2"]])
        RECT_9_img = "RECT_9.png"
        cv2.imwrite(RECT_9_img, gray[RECT_9["y1"]:RECT_9["y2"], RECT_9["x1"]:RECT_9["x2"]])
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
