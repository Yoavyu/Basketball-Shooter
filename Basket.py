import cvzone
import cv2
import os
from cvzone.ColorModule import ColorFinder

def get_latest_image(dirpath, valid_extensions=('jpg','jpeg','png','bmp')):
    """
    Get the latest image file in the given directory
    """

    # get filepaths of all files and dirs in the given dir
    valid_files = [os.path.join(dirpath, filename) for filename in os.listdir(dirpath)]
    # filter out directories, no-extension, and wrong extension files
    valid_files = [f for f in valid_files if '.' in f and \
        f.rsplit('.',1)[-1] in valid_extensions and os.path.isfile(f)]

    if not valid_files:
        raise ValueError("No valid images in %s" % dirpath)

    return max(valid_files, key=os.path.getmtime)




# MAIN CODE

while True:
    last_image = get_latest_image(r"C:\out",valid_extensions=('jpg','jpeg','png','bmp')) #getting last image from folder named "out" and contains the photos taken by camera
    #proccesing last image
    img = cv2.imread(last_image)
    img = cv2.rotate(img,cv2.ROTATE_180)
    img = cv2.resize(img,(0,0), None, 2,2)

    myColor = ColorFinder(False)
    Vals = {'hmin': 0, 'smin': 0, 'vmin': 0, 'hmax': 255, 'smax': 255, 'vmax': 15} # recognizing the basket hoop from the image
    imgColor, mask = myColor.update(img, Vals) # mask the rest
    imgConturs, conturs = cvzone.findContours(img, mask, minArea=400) # finding the conturs of the basket loop
    x0,x1,x2,y0,y1,y2 = 0,0,0,0,0,0
    lenghth = len(conturs)
    # proccesing the conturs to one mid point of the hoop
    if lenghth>=1:
        x0,y0 = conturs[0]['center']
    if lenghth >= 2:
        x1, y1 = conturs[1]['center']
    if lenghth >= 3:
        x2, y2 = conturs[2]['center']
    if lenghth!=0:
        x = int((x0 + x1 + x2) /min(3,lenghth) )
        y = int((y0 + y1 + y2) / min(3,lenghth))
        cv2.circle(imgConturs, (x,y), 5,(0,255,0),cv2.FILLED)
        print(x,y) # here is the mid point
        if(x>165 and x <320): #if the mid point is centerd compered with the basket itself
             print(True)
             img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS) #image is turining on green
        else:
            print(False)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # image is turning on red
        #x,y = conturs[0]['center']+ conturs[1]['center']+conturs[2]['center']
        imgColor = cv2.resize(mask,(0,0), None, 1,1)
        #cv2.imshow('imageColored', imgColor)
        cv2.imshow('imageConturs', imgConturs)
        cv2.imshow('image', img)
    cv2.waitKey(2000)



