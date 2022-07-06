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

It is recommended to use an anaconda or miniconda environment. 

To install libraries, you can use this line: 
>``conda install librairy`` 

To install Glob you can use: 
>``conda install -c conda-forge glob2`` 

## 2. Launch GAPP 

In a terminal, run: 
>``spyder`` 

In spyder open GAPP.py and run it with F5 keyboard command or with the green arrow. 

![Spyder](images\capturedecranspyder.png) 

## 3. Application 

The following window will be open: 
![Main window](images\capturedecranGAPP.png) 

**Every space must be filled** 

### Folder 

In Folder part you have fill 
- The folder where the photos to scan locate, 
- The folder where you want to every step of the program will be save, 
- The folder of the Fiducial template. 
Your back to the main window. Ypu now have to fill 
- The dataset name (you can check il it corresponds to the fiducial template you gave with the "Check dataset" button) 
- The p-value 
- Don't change the stripes location it wouldn't work 
- The camera used to take the air photos 
- The input resolution (scanning resolution)  
- The output resolution 
- The CLAHE Historical calibration 
- The Sharpening intensity  
- Check all the steps you want to launch (it is recommended to check all the steps) 

Run the program with the "Run" button. 
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

You must find the coordinates of every fiducial mark of a least one air photo of the dataset, you may use Photoshop or Krita (Krita is a free drawing software), give the half width of the image you want and the data set name. You must be able of see the entire mark on the picture. You can check it in the output folder that you gave. 

Once you have filed the input image and the output folder, please click on "Create fiducial template". The script will create four folder and close the fiducial template creator window. 

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