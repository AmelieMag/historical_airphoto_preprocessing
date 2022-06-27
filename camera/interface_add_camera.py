# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:32:45 2022

@author: Amelie Maginot
         Ecole nationale des sciences geographiques
"""

from Add_Camera import add_camera
import tkinter as tk
from tkinter import ttk
import sys,os
from functools import partial
import time as t

sys.path.insert(0, '')

absFilePath = os.path.abspath(__file__)
filepath, filename = os.path.split(absFilePath)

sys.path.insert(0, '{}/camera'.format(filepath))


def add_camera_interface():
    root = tk.Tk()

    root.title("Add camera to pre-processing program")
        
    # camera name
    tk.Label(root, text="   Camera name without spaces:   ").grid(
        row=1, column=0)
    cam = tk.StringVar(root)
    camera = tk.Entry(root, textvariable=cam)
    camera.grid(row=1, column=1)
    
    # resolution
    tk.Label(root, text="    High resolution:").grid(row=3, column=0)
    resh=tk.IntVar(root,value=2000)
    resolution = tk.Entry(root, textvariable=resh)
    resolution.grid(row=3, column=1)
    
    tk.Label(root, text="    Low resolution:").grid(row=4, column=0)
    resl=tk.IntVar(root, value=600)
    resolution = tk.Entry(root, textvariable=resl)
    resolution.grid(row=4,column=1)
    
    # total lenth in x 
    tk.Label(root, text="    Total lenth X:").grid(row=5, column=0)
    Lux=tk.DoubleVar(root,value=18)
    resolution = tk.Entry(root, textvariable=Lux)
    resolution.grid(row=5,column=1)
    
    # total lenth in y 
    tk.Label(root, text="    Total lenth Y:").grid(row=6, column=0)
    Luy = tk.DoubleVar(root,value=18)
    resolution = tk.Entry(root, textvariable=Luy)
    resolution.grid(row=6,column=1)
    
    #  beetween fiducial marks in x 
    tk.Label(root, text="    Beetween fiducial marks X:").grid(row=8, column=0)
    FMux = tk.DoubleVar(root,value=16.5)
    resolution = tk.Entry(root, textvariable=FMux)
    resolution.grid(row=7,column=1)
    
    # lenth beetween fiducial marksin y 
    tk.Label(root, text="    Beetween fiducial marks Y:").grid(row=8, column=0)
    FMuy = tk.DoubleVar(root,value=16.5)
    resolution = tk.Entry(root, textvariable=FMuy)
    resolution.grid(row=8,column=1)
    
    # unity
    u = tk.StringVar(root,"Unity")
    tk.OptionMenu(root, u, *["cm","inche"]).grid(row=10,columnspan=2)
    

    def main():
        add_camera(camera, resh, resl, Lux, Luy, FMux, FMuy, u)
        
        t.sleep(0.3)
        root.destroy()
    
    # add camera button
    ttk.Button(root, text="Add camera", style='Accent.TButton',
               command=main).grid(row=12, columnspan=2)
    
    tk.Label(root, text=" ").grid(row=11, column=1)
    tk.Label(root, text=" ").grid(row=13, column=1)
    tk.Label(root, text=" ").grid(row=13, column=2)
    tk.Label(root, text="   ").grid(row=0, column=2)
    tk.Label(root, text=" ").grid(row=9, column=2)
    
    root.mainloop()
    
    
    camera_file = open(r"{}/camera.txt".format(filepath), "r")
    update_list = camera_file.readlines()[0].split(";")
    camera_file.close()
    
    return update_list

if __name__ == "__main__":
    add_camera_interface()
