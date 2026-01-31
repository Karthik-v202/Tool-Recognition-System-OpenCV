import cv2
import numpy as np

#Capture video from default camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # 1. Pre-processing
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (7, 7), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    kernel = np.ones((5,5), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            bbox_area = w * h
            aspect_ratio = w / float(h)
            
            label = None 

            #TOOL CLASSIFICATION BASED ON BOUNDING BOX PROPERTIES
            
            if 3000 < bbox_area < 50000 and aspect_ratio < 0.25:
                label = 'Screwdriver'
            
            elif 100000 < bbox_area < 150000 and aspect_ratio > 2:
                label = 'Cutter'
            
            elif 110000 < bbox_area < 150000 and 4 < aspect_ratio < 5:
                label = 'Desoldering Pump'
            
            elif 200000 < bbox_area < 300000 and 0.8 < aspect_ratio < 1:
                label = 'Small Pliers'
            
            elif 150000 < bbox_area < 250000 and 0.7 < aspect_ratio < 1.3:
                label = 'Wire Stripper'

            elif 150000 < bbox_area < 200000 and 0.5 < aspect_ratio < 0.7:
                label = 'Micro Pliers'

            # --- 3. DRAWING ---
            if label:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            
    #DISPLAY
    cv2.imshow('Tool Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()