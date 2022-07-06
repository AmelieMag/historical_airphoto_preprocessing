# GAPP User manual
## 1. Environment
To use GAPP application you need sevral librairies install in your environament:
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

It is recommanded to use anaconda or miniconda enviromment.

To install librairies you can use this line:
>``conda install librairy``

To install Glob you can use:
>``conda install -c conda-forge glob2``

## 2. Launch GAPP

in a terminal, run:
>``spyder``

in spyder open GAPP.py and run it with F5 keybord command or with the gree arrow.

![Spyder](images\capturedecranspyder.png)

## 3. Application

The following window will be open:
![Main window](images\capturedecranGAPP.png)

**Every space must be filled**

### Folder

In Folder part you have fill
- The folder where the photos to scan locate,
- The folder where you want to every steps of the programm will be save,
- The folder of the Fiducial template.
Your back to the main window. Ypu now have to fill
- The dataset name (you can check il it corresponds to the fiducial template you gave with the "Check dataset" button)
- The p-value
- Don't change the stripes location it wouldn't work
- The camera used to takes the airphotos
- The input resolution (scanning resolution) 
- The output resolution
- The CLAHE Historical calibration
- The Sharpening intensity 
- Ckeck all the steps you want to launch (it is recommanded to check all the steps)

Run the program with the "Run" button.


### What is the fiducial template?

![Fiducial template exemple](images\capturedecranfiducialtemplate.png)

"bande10" is the dataset name, followed by the corner and the half width and half lenth of each images.

For each line of the fiducial template a picture like this is in the same folder and is name after the first column.

For instance this folling image is the top right fiducial mark of the first image of the airphoto folder

![Fiducial mark exemple](images\capturedecranfiducialMark.png)

### How to create fiducuial template

Clic on "Createfiducial template",

![](images\capturedecranGAPP2.png)

This new window will be open:
![](images\capturedecranfiducialtemplatecreator.PNG)

You must find the coordinates of every fiducial marks of a least one air photo of the dataset, you may use Photoshop or Krita (Krita is a free drawing softwer), give the half width of the image you want and the data set name. You must be able of see the entire mark on the picture. You can check it in the output folder that you gave.
Once you have filed the input image and the output folder, please clic on "Create fiducial template". The script will create four folder and close the fiducial template creator window.

### What if you d'ont find the right camera ?
clic on "Add camera system" in menu bar
![](images\capturedecranGAPP3.png)
The following window will be open:

![](images\capturedecranAddCamera.png)

You must fill every space:
- camera name without spaces,
- hight and low resoluion have recommanded default value but it can be change
- all lenth must be given in centimeters or inches
- choose unity

Run the script with "Add camera" button, the window will be close. On the main window clic "Refresh camera list" button to get the new camera in the list