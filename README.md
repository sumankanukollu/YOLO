# EVA4 Assignment 13 - Suman Kanukollu

**Team Members**

- Tusharkant Biswal (Tusharkanta_biswal@stragure.com) 
- V N G Suman Kanukollu (sumankanukollu@gmail.com)
- Harsha Vardhan (harshavardhan.ma@gmail.com)
- Praveen Raghuvanshi (praveenraghuvanshi@gmail.com)[

[Github Directory - Assignment -13](https://github.com/sumankanukollu/YOLO)

### Assignment 13-1:
[OpenCV source](https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/)

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

#### Resources
  * [Trained weights are placed in google drive](https://drive.google.com/drive/u/1/folders/1306WHjGv0O4Il9GDvjMArGc37pLMOM-C)
  * [Custom Train dataset (images and labels) is placed in google drive](https://drive.google.com/drive/u/1/folders/1dMEiGlPPTg6N_Xz9vch8_gBcrF4IA1DB)
  * Command to run : 
  `!python detect.py --conf-thres 0.1 --output Tom_Test_BB_1500 --source test_yolov3_tomNdJerry_Diwali.mp4`
  * detect.py Modifications:
    ```
        parser.add_argument('--cfg', type=str, default='cfg/yolov3-custom.cfg', help='*.cfg path')
        parser.add_argument('--names', type=str, default='data/customdata/custom.names', help='*.names path')
        parser.add_argument('--weights', type=str, default='weights/best.pt', help='weights path')
        parser.add_argument('--source', type=str, default='data/customdata/Tom_Test/', help='source')  # input file/folder, 0 for webcam
        parser.add_argument('--output', type=str, default='output', help='output folder')  # output folder
        parser.add_argument('--img-size', type=int, default=512, help='inference size (pixels)')
        parser.add_argument('--conf-thres', type=float, default=0.3, help='object confidence threshold')
        parser.add_argument('--iou-thres', type=float, default=0.6, help='IOU threshold for NMS')
        parser.add_argument('--fourcc', type=str, default='mp4v', help='output video codec (verify ffmpeg support)')
        parser.add_argument('--half', action='store_true', help='half precision FP16 inference')
        parser.add_argument('--device', default='', help='device id (i.e. 0 or 0,1) or cpu')
        parser.add_argument('--view-img', action='store_true', help='display results')
        parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
        parser.add_argument('--classes', nargs='+', type=int, help='filter by class')
        parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
        parser.add_argument('--augment', action='store_true', help='augmented inference')
    ```

#### Solution

- This assignment is done as a GROUP and has same submission by all team members. 
- Team members are mentioned at the top
- Assignment has been executed on a local GPU machine and colab is not used.
- We took object detection of cartoon character '**Tom**' from Tom and Jerry tales
- Extracted frames from video for dataset
- Manually annotated 1465 images covering whole body of character 'Tom' (from all team members)
- Ran for 300 epochs
- Classes : 1 - **tom**
- Training Time: 07.541 hours

- Steps
  - Made changes to the cfg file
    - Search for 'filters=255' (you should get entries). Change 255 to 18 = (4+1+1)*3
    - Search for 'classes=80' and change all three entries to 'classes=1'
    - burn_in to 100
    - max_batches to 5000
    - steps to 4000,4500
  - custom.names had only 'tom' as class.
  - custom.txt has path to all images
  - Trained model for 300 epochs 
  - Ran detect.py to generate frames for predicted bounding boxes
  - Tested model with best.pt file generated on new video and uploaded it to Youtube.
  
- Resources
  - Custom Dataset (TOM):
    - [Images](https://github.com/sumankanukollu/YOLO/tree/master/YoloV3/data/customdata/images)
    - [Labels](https://github.com/sumankanukollu/YOLO/tree/master/YoloV3/data/customdata/labels)
    
  - Custom YoloV3 code [repository](https://github.com/sumankanukollu/YOLO/tree/master/YoloV3)
  
  - [Youtube Video (Duration: 02:34 mins)](https://www.youtube.com/watch?v=7_lH-jFB0Cg)
  
    [![RIP Gene Deitch | Yolov3 Object Detection | Tom Detector](http://img.youtube.com/vi/7_lH-jFB0Cg/0.jpg)](https://www.youtube.com/watch?v=7_lH-jFB0Cg)
  
  - [Logs](https://github.com/sumankanukollu/YOLO/blob/master/YoloV3/customDataset_TOM_train_log_on_YOLOv3.log)

- Submission
  - Share the link to your GitHub project with the steps as mentioned above (for YoloV3 training on Colab) 
[Github link](https://github.com/sumankanukollu/YOLO/tree/master/YoloV3)
[Training Logs link](https://github.com/sumankanukollu/YOLO/blob/master/YoloV3/customDataset_TOM_train_log_on_YOLOv3.log)

  - Share the link of your YouTube video (your object annotated by your YoloV3 trained model):
    * [colab Notebook file](https://github.com/sumankanukollu/YOLO/blob/master/YoloV3/EVA4_S13_YoloV3_tomNjerry_video_model_suman.ipynb)
    * [Original Vedio](https://www.youtube.com/watch?v=GfkQTW9LlCg)
    * [Youtube Video (Duration: 00:30 sec)](https://youtu.be/DFOJu0F4eBs)
    * [Youtube Video (Duration: 02:34 mins)](https://www.youtube.com/watch?v=7_lH-jFB0Cg)
    [![RIP Gene Deitch | Yolov3 Object Detection | Tom Detector](http://img.youtube.com/vi/7_lH-jFB0Cg/0.jpg)](https://www.youtube.com/watch?v=7_lH-jFB0Cg)
    
- Credits:

  - [The School of AI (YoloV3)](https://github.com/theschoolofai/YoloV3)
