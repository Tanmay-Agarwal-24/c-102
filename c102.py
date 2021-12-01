import cv2
import dropbox
import random
import time
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)  
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite("NewPicture1.jpg",frame)
        result=False
    
    return img_name
    print("snapshort taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
 
def upload_file(img_name):
    access_token=''
    file="NewPicture1.jpg"
    file_from = file
    file_to = "/nnewFolder1"+("NewPicture1.jpg")
    dbx=dropbox.Dropbox(acress_token)

    with open (file_from,'rb') as f:
        print("file uploaded")
  
take_snapshot()
