import cv2 as cv
import numpy as np

x1,x2,y1,y2,xr1 ,xr2 ,yr1, yr2 = 0,0,0,0,0,0,0,0
img = cv.imread("E:\Python\OpenCV\Photos\orman.jpg")
matrix, matrix2 = None, None
img_copy = img.copy()

def ciz(event,x,y,flags,param):
    global x1 ,x2 ,y1 ,y2 ,matrix ,xr1 ,xr2 ,yr1, yr2, matrix2
    
    if event == cv.EVENT_LBUTTONDOWN:
        x1, y1 = x, y

    if event == cv.EVENT_RBUTTONDOWN:
        xr1, yr1 = x, y

    if event == cv.EVENT_LBUTTONUP:
        x2, y2 = x, y
        matrix = img_copy[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
        draw_rectangle()
    
    if event == cv.EVENT_RBUTTONUP:
        xr2, yr2 = x, y
        matrix2 = img_copy[min(yr1, yr2):max(yr1, yr2), min(xr1, xr2):max(xr1, xr2)]
        img[min(yr1, yr2):max(yr1, yr2), min(xr1, xr2):max(xr1, xr2)] = matrix2

def draw_rectangle():
    global x1,x2,y1,y2

    color = (255,151,64)

    for i in range(min(x1, x2), max(x1, x2) ):

        for j in range(min(y1, y2), max(y1, y2) ):

            img[j, i] = color

    cv.imshow("afef", img)    
        
cv.imshow("afef", img)

cv.setMouseCallback("afef",ciz)

while 1 :
    key = cv.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("z"):   
        img[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)] = matrix 
        matrix = None
        
    cv.imshow("afef",img)
    
cv.destroyAllWindows()


