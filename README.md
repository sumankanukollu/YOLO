# EVA4 Assignment 13 - Suman Kanukollu

**Team Members**

- Tusharkant Biswal (Tusharkanta_biswal@stragure.com) 
- V N G Suman Kanukollu (sumankanukollu@gmail.com)
- Harsha Vardhan (harshavardhan.ma@gmail.com)
- Praveen Raghuvanshi (praveenraghuvanshi@gmail.com)[

[Github Directory - Assignment -13](https://github.com/sumankanukollu/YOLO)

### Assignment 13-1

OpenCV Yolo: [SOURCE (https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/)

1. Run this above code on your laptop or Colab. 
2. Take an image of yourself, holding another object which is there in COCO data set (search for COCO classes to learn). 
3. Run this image through the code above. 
4. Upload the link to GitHub implementation of this
5. Upload the annotated image by YOLO. 

#### Solution

- [Github Directory - Assignment-13-1](https://github.com/sumankanukollu/YOLO/tree/master/S13_YOLOv3_Object_detection)

- [Python Script](https://github.com/sumankanukollu/YOLO/blob/master/S13_YOLOv3_Object_detection/YOLO_object_detection_COCO_suman.py)

- [Readme File](https://github.com/sumankanukollu/YOLO/blob/master/S13_YOLOv3_Object_detection/Readme.md)

# Original Image:
![Input Image](https://github.com/sumankanukollu/YOLO/blob/master/S13_YOLOv3_Object_detection/suman_1_input.jpg)

# Output Image: 
##### Detected 6-Objects (Person,chair,clock,refrigerator,cell phone and cup)
![Objects Detected Image](https://github.com/sumankanukollu/YOLO/blob/master/S13_YOLOv3_Object_detection/suman_1_obj_detection.jpg)


- **Submission**

  - Upload the link to GitHub implementation of this : https://github.com/sumankanukollu/YOLO/blob/master/S13_YOLOv3_Object_detection/YOLO_object_detection_COCO_suman.py

  - Upload the annotated image by YOLO : https://github.com/sumankanukollu/YOLO/blob/master/S13_YOLOv3_Object_detection/suman_1_obj_detection.jpg



### Assignment-13-2

Training Custom Dataset on Colab for YoloV3

1. Refer to this Colab File: [LINK ](https://colab.research.google.com/drive/1LbKkQf4hbIuiUHunLlvY-cc0d_sNcAgS)
2. Refer to this GitHub [Repo](https://github.com/theschoolofai/YoloV3)
3. Collect a dataset of 500 images and annotate them. **Please select a class for which you can find a YouTube video as well.** Steps are explained in the readme.md file on GitHub.
4. Once done:
   1. [Download ](https://www.y2mate.com/en19) a very small (~10-30sec) video from youtube which shows your class. 
   2. Use [ffmpeg](https://en.wikibooks.org/wiki/FFMPEG_An_Intermediate_Guide/image_sequence) to extract frames from the video. 
   3. Upload on your drive (alternatively you could be doing all of this on your drive to save upload time)
   4. Inter on these images using detect.py file. **Modify** detect.py file if your file names do not match the ones mentioned on GitHub. 
      `python detect.py --conf-thres 0.3 --output output_folder_name`
   5. Use [ffmpeg](https://en.wikibooks.org/wiki/FFMPEG_An_Intermediate_Guide/image_sequence) to convert the files in your output folder to video
   6. Upload the video to YouTube. 
5. Share the link to your GitHub project with the steps as mentioned above
6. Share the link of your YouTube video
7. Share the link of your YouTube video on LinkedIn, Instagram, etc! You have no idea how much you'd love people complimenting you! 

#### Solution

- This assignment is done as a GROUP and has same submission by all team members. 
- Team members are mentioned at the top
- Assignment has been executed on a local machine and colab is not used.
- We took object detection of cartoon character '**Tom**' from Tom and Jerry tales
- Extracted frames from video for dataset
- Manually annotated 1465 images covering whole body of character 'Tom' (from all team members)
- Ran for 300 epochs
- Classes : 1 - tom
- Resources
  - Custom Dataset Link
  - Custom YoloV3 code repository
  - Weights link
  - Classnames file
  - Sample True Bounding Box
  - Sample Predicted Bounding Box
  - Youtube Video (Duration: --)
  - Logs
- Credits:
  - [The School of AI (YoloV3)](https://github.com/theschoolofai/YoloV3)
- Submission
  - Share the link to your GitHub project with the steps as mentioned above (for YoloV3 training on Colab) 
[Github link](https://github.com/sumankanukollu/YOLO/tree/master/YoloV3)
  - Share the link of your YouTube video (your object annotated by your YoloV3 trained model):
    * [Original Vedio](https://www.youtube.com/watch?v=GfkQTW9LlCg)
    * [TOM-Object Annotated and trained by my YOLOv3-model is in Youtube](https://youtu.be/DFOJu0F4eBs)
