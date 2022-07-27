# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:07:23 2022

@author: Amelie Maginot
        (Ecole Nationale des Sciences Geograpgiques)
"""

from tkinter import ttk
from tkinter import filedialog
from functools import partial
from joblib import Parallel,delayed
import tkinter as tk
import sys, os
import multiprocessing

def toCheckList(output_folder,dataset):

    # list_folder=os.listdir('{}/01_CanvasSized/_To_Be_Checked'.format(output_folder))
    list_folder = os.listdir('{}/test3/_To_Be_Checked'.format(output_folder))
    
    # print(list_folder)
    corners = ['top_left','top_right','bot_right','bot_left']
    listToCheck = []
    for name in list_folder:
        for corner  in corners:
            if corner in name:
                l = len('_CanvasSized.tif_')+len(corner)+len('.png')
                listToCheck.append([name[9:-l],corner])
    
    return listToCheck

def interface_image_to_check(output_folder,dataset):
    
    listToCheck = toCheckList(output_folder,dataset)
    print(len(listToCheck))
    
    #initialazing the windows
    root = tk.Tk()
    root.title("Image to check")
    i=0
    tk.Label(root, text='The algorithme could not find any good solution for the following corner.').grid(row=i)
    for image in listToCheck:
        i+=1
        l=tk.Label(root,text=image).grid(column=0,row=i)
        # ttk.Button(root,text='Modify').grid(column=1,row=i)
        # ttk.Button(root,text='Ignore').grid(column=2,row=i)
        ttk.Button(root,text='Ok',command=lambda : l.grid_remove()).grid(column=2,row=2)
    
    tk.Label(root,text='Please find the fiducial mark by yourself using softwear like Photoshop, Gimp or Krita.').grid()
    
    # Close nutton
    ttk.Button(root, text = 'Ok',command=root.destroy).grid()
    
    # Mainloop
    root.mainloop()


if __name__=='__main__':
    outFold = r'F:\2_SfM_READY_photo_collection\Burundi_1981-82\GAPP'
    data = ''
    interface_image_to_check(outFold,data)