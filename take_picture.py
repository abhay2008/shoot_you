import cv2

def take_snapshot():
  #initializing cv2
  videoCaptureObject = cv2.VideoCapture(0)
  result = True
  while(result):
    ret, frame = videoCaptureObject.read()
    cv2.imwrite("Shooted.jpg", frame)
    result = False
    
  videoCaptureObject.release()
  cv2.destroyAllWindows()
  
take_snapshot()