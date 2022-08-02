# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:07:23 2022

@author: Amelie Maginot
        (Ecole Nationale des Sciences Geograpgiques)
"""

from tkinter import ttk
# from tkinter import filedialog
# from functools import partial
# from joblib import Parallel,delayed
import tkinter as tk
import os

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


def fe(r,ImagePath):
    frame = tk.Frame(r)
    
    tk.Label(frame,text=str(ImagePath)).pack()
    
    photo = tk.PhotoImage(file=ImagePath)
    tk.Label(frame,image = photo).pack()
    
    ttk.Button(frame,text = 'destroy',command = frame.destroy).pack()
    
    frame.grid(column=2,row=1)
    
    
def interface_image_to_check(input_folder,dataset):
    
    listToCheck = toCheckList(input_folder,dataset)
    list_folder = os.listdir(r'{}/01_CanvasSized/_To_Be_Checked'.format(input_folder))
    print(list_folder)
    print(len(listToCheck))
    
    #initialazing the windows
    root = tk.Tk()
    root.title("Image to check")
    
    frameImage=tk.Frame(root)
    frameText=tk.Frame(root)
    
    for i in range(len(listToCheck)):
        Path = '{}\01_CanvasSized\_To_Be_Checked/{}'.format(input_folder,list_folder[i])
        print(Path)
        fe(root,Path)
        
    # airPhoto = tk.PhotoImage('{}/01_CanvasSized/{}'.format(input_folder))
    
    frameText.grid (column=1)
    frameImage.grid(column=2)
    
    # Close Button
    ttk.Button(frameText, text = 'Ok',command=root.destroy).grid()
    
    # Mainloop
    root.mainloop()

if __name__=='__main__':
    outFold = r'F:\2_SfM_READY_photo_collection\Burundi_1981-82\GAPP\test4'
    data = ''
    interface_image_to_check(outFold,data)