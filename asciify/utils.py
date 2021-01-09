import cv2
import numpy as np

def get_filtered_image(image, action):
    if action == 'NO_FILTER':
        filtered = image
    elif action == 'EDGE DETECTION':
        kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
        filtered = cv2.filter2D(image, -1, kernel)
    elif action == 'SHARPENING':
        kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        filtered = cv2.filter2D(image, -1, kernel)
    elif action == 'EMBOSSING':
        kernel = (1/16) * np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
        filtered = cv2.filter2D(image, -1, kernel)
    elif action == 'BLURRED':
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        width, height = img.shape[:2]
        if width > 500:
            k = (50, 50)
        elif width > 200 and width < 500:
            k = (25, 25)
        else:
            k = (10,10)
        blur = cv2.blur(img, k)
        filtered = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
    
    return filtered