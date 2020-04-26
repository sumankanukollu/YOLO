# Program To Read video 
# and Extract Frames 
import cv2 
import os
# Function to extract frames 
def FrameCapture(path, outputpath): 
    if not os.path.exists(outputpath):
        print("Creating output folder at {}".format(outputpath))
        os.makedirs(outputpath)
    else:
        print("Output folder exists. Delete it")
        exit()

    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        if count % 3 ==0:
            # Saves the frames with frame-count 
            framepath = os.path.join(outputpath, "frame{}.jpg".format(count))
            cv2.imwrite(framepath, image) 
  
        count += 1
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    #FrameCapture("/home/harv/Downloads/TomAndJerry/073   The Missing Mouse [1953].mkv", "/home/harv/Downloads/frames/73") 
    FrameCapture("Tom_Yolov3_TestVedio.mp4", "Tom_Test") 
