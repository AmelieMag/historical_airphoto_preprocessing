# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:07:23 2022

@author: Amelie Maginot
        (Ecole Nationale des Sciences Geograpgiques)
"""

import os,sys
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image,ImageTk

absFilePath = os.path.abspath(__file__)
filepath, filename = os.path.split(absFilePath)
sys.path.insert(0, '{}/scriptsAndInterfaces'.format(filepath))  # Local imports

from zoom_and_move_app import Zoom_Advanced


def toCheckList(input_folder,dataset):

    list_folder=os.listdir(r'{}/01_CanvasSized/_To_Be_Checked'.format(input_folder))
    # list_folder = os.listdir(r'{}/_To_Be_Checked'.format(input_folder))
    
    # print(list_folder)
    corners = ['top_left','top_right','bot_right','bot_left']
    listToCheck = []
    for name in list_folder:
        for corner  in corners:
            if corner in name:
                l = len('_CanvasSized.tif_')+len(corner)+len('.png')
                listToCheck.append([name[9:-l],corner])
    
    return listToCheck


def fe(ImagePath):
    root = tk.Tk()
    tk.Label(root,text=str(ImagePath)).pack()
    ImagePath = r'F:\2_SfM_READY_photo_collection\Burundi_1981-82\GAPP\test4\01_CanvasSized\_To_Be_Checked/_ToCheck_Bande_31_001_CanvasSized.tif_bot_left.png'
    
    image = Image.open(ImagePath)#,encoding='utf-8')
    photo = tk.PhotoImage(file=image)
    tk.Label(root,image=photo)
    image.close()
    # print('image =',image)
    
    ttk.Button(root,text = 'destroy',command = root.destroy).pack()
    
def fe2(Path):
    
    i=0
    listImage = os.listdir(Path)
    imageName = listImage[i]
    ImagePath = r'{}/{}'.format(Path,imageName)
    
    root = tk.Tk()
    root.title("Title")
    
    img = Image.open(ImagePath)
    bg = ImageTk.PhotoImage(img)
    img.close()
    
    lbl = tk.Label(root, image=bg)
    lbl.place(x=0, y=0)
    
    #Set the geometry of tkinter frame
    root.geometry("750x250")

    root.bind('<Motion>',callback)
    root.bind('<MouseWheel>',test)

    tk.mainloop()
        
        

def callback(e):
   x= e.x
   y= e.y
   print("Pointer is currently at %d, %d" %(x,y),e)


def test(e):
    print(e,' est ce qui est retourner par bind mousewheel')
    
    
def interface_image_to_check(image):
    
    # listToCheck = toCheckList(input_folder,dataset)
    # list_folder = os.listdir(r'{}/01_CanvasSized/_To_Be_Checked'.format(input_folder))
    # # print(list_folder)
    # print(len(listToCheck))
    
    global path
    path = "./"
    
    #initialazing the windows
    root = tk.Tk()
    root.title("Image to check")
    # root.geometry("1000x450")
    
    
    frameImage=tk.Frame(root, width=1000, height=1000)
    frameText=tk.Frame(root)
    frameFid=tk.Frame(root)
    
    
    # for i in range(len(listToCheck)):
    #     Path = r'{}\01_CanvasSized\_To_Be_Checked/{}'.format(input_folder,list_folder[i])
    #     print(Path)
    #     fe(Path)
    
    app = Zoom_Advanced(frameImage,image)
    
    
    frameImage.bind('<Motion>',callback)
    root.bind('<MouseWheel>',test)
    
        
    # airPhoto = tk.PhotoImage('{}/01_CanvasSized/{}'.format(input_folder))
    
    frameText.pack()
    frameImage.pack()
    frameFid.pack()
    
    
    # frameImage.loop()
    
    
    
    # Close Button
    ttk.Button(frameText, text = 'Ok',command=root.destroy).grid(column=0)
    
    # Mainloop
    root.mainloop()

# def choose_fid_marque():
    

if __name__=='__main__':
    # outFold = r'F:\2_SfM_READY_photo_collection\Burundi_1981-82\GAPP\test4'
    # data = ''
    # interface_image_to_check(outFold,data)
    
    Path = r'F:\2_SfM_READY_photo_collection\Burundi_1981-82\GAPP\test6\01_CanvasSized\cornerToCheck'
    img = os.listdir(Path)[0]
    
    imgPath = r'{}\{}'.format(Path,img) # place path to your image here
    # fe2(Path)

    interface_image_to_check(imgPath)
