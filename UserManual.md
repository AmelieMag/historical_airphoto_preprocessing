# GAPP User manual 
## 1. Environment 

To use GAPP application you need serval libraries install in your environment: 
- Glob 
- Joblib 
- Matplotlib   
- Numpy 
- OpenCv 
- Pandas 
- Pathlib 
- Pillow 
- Spyder 
- Tkinter (Tk) 

I used an anaconda environment. 

To install libraries, you can use this line: 
>``conda install librairy`` 

To install Glob you can use: 
>``conda install -c conda-forge glob2`` 

## 2. Launch GAPP 

In a anaconda or miniconda terminal, run: 
>``spyder`` 

In spyder open GAPP.py and run it with F5 keyboard command or with the green arrow. 

![Spyder](images\capturedecranspyder.png) 

## 3. Application 

The following window will be open: 

![Main window](images\capturedecranGAPP.png) 

**Every space must be filled** 

### Folder 

In Folder part you have fill 
- The folder where the photos to pre-process locate, 
- The folder where you want to every steps of the program will be save, 
- The folder of the Fiducial template.
- The dataset name (you can check il it corresponds to the fiducial template you gave with the "Check dataset" button) 
- The p-value (% of image width that is a black/white strip)
- The strip location must be: left, top, right, bottom. You can put sevral location.
- The camera used to take the air photos 
- The input resolution (scanning resolution)  
- The output resolution 
- The CLAHE Historical calibration 
- The Sharpening intensity  

you have to push the buttons in the right order :

- first button "Run Canvas sized and Fiducial mark detection"
the process can spend time finding fiducial mark especially if you gave a  lot of images. please wait for "FID MARK DETECTION COMPLETED" in the consol to clic next button.
![Console](images\consoleFinishRunDetection.PNG) 

- second button "Run fid mark correction". fi there are fiducial mark to correct an extention of the main window will be open. You can move and zoom (+/-) on the corner image. double clic on th fiducial center and clic "OK" button, next corner will be open (To find the fiducial centre a target is here to help). When all the corner will be corrected and all modifications in fill finished, the extention will be closed
![Main window extention](images\capturedecranGAPPcorrectfidmarkextention.png)
- clic on "Run Reprojection" and wait for the end message in the console: "PROCESS COMPLETED" (could be long)
- clic on "Run resize" wait for the end messagein th e console: "--- data processing time was [duration of the process] --- (could be long)
- clic on "Run Create mask" (should be quick)

### What is the fiducial template? 
![Fiducial template example](images\capturedecranfiducialtemplate.png) 

"bande10" is the dataset name, followed by the corner and the half width and half-length of each image. 

For each line of the fiducial template a picture like this is in the same folder and is name after the first column. 

For instance, this following image is the top right fiducial mark of the first image of the air photo folder 

![Fiducial mark example](images\capturedecranfiducialMark.png) 

### How to create fiducial template 

Click on "Createfiducial template", 

![](images\capturedecranGAPP2.png) 

This new window will be open: 

![](images\capturedecranfiducialtemplatecreator.PNG) 

You must find the coordinates of every fiducial mark of a least one air photo of the dataset. Choose a photo where the fiducial marks are the most visible as possible.
You may use Photoshop or GIMP to find the coordinates in pixels of the fiducial marks centers.
fill the following spaces :
- the fiducial centers of each corner
- the half width of the image
- the data set name.

Once you have filed the input image and the output folder, please click on "Create fiducial template". The script will create four image files, a txt file and close the fiducial template creator window. 

Check the fiducial template. You must be able of see the entire mark on the picture and it must be centered. You can check it in the output folder that you gave before. 


### What if you don't find the right camera? 
Click on "Add camera system" in menu bar 

![](images\capturedecranGAPP3.png) 

The following window will be open: 

![](images\capturedecranAddCamera.png) 

You must fill every space: 
- Camera name without spaces, 
- Hight and low resolution have recommended default value but it can be change 
- All length must be given in centimetres or inches 
- Choose unity 

Run the script with "Add camera" button, the window will be close. On the main window click "Refresh camera list" button to get the new camera in the list. 