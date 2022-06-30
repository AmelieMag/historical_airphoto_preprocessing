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
![](images\capturedecranGAPP.png)

**Every space must be filled**

### Folder

In Folder part you have fill
1. The folder where the photos to scan locate,
1. The folder where you want to every steps of the programm will be save,
1. The folder of the Fiducial template.

### What is the fiducial template?

![](images\capturedecranfiducialtemplate.png)

"bande10" is the dataset name, followed by the corner and the half width and half lenth of each images.

For each line of the fiducial template a picture like this is in the same folder and is name after the first column.

For instance this folling image is the top right fiducial mark of the first image of the airphoto folder

![](images\capturedecranfiducialMark.png)

### How to create fiducuial template

Clic on "Createfiducial template",

![](images\capturedecranGAPP2.png)

this new window will be open:
![](images\capturedecranfiducialtemplatecreator.PNG)

You must find the coordinates of every fiducial marks of a least one air photo of the dataset, give the half width of the image you want. you must be able of see the entire mark on the picture.

