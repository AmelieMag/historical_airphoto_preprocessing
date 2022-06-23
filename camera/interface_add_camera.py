# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:32:45 2022

@author: Amelie Maginot
         Ecole nationale des sciences geographiques
"""

from Add_Camera import add_camera
import tkinter as tk
from tkinter import ttk
import sys
from functools import partial

sys.path.insert(0, '')


def add_camera_interface():
    root = tk.Tk()

    root.title("Add camera to pre-processing program")
        
    # camera name
    tk.Label(root, text="   Camera name without spaces:   ").grid(
        row=0, column=0)
    cam = tk.StringVar(root,value="azerty")
    camera = tk.Entry(root, textvariable=cam)
    camera.grid(row=0, column=1)
    
    # resolution
    tk.Label(root, text="    high resolution:").grid(row=2, column=0)
    resh=tk.IntVar(root)
    resolution = tk.Entry(root, textvariable=resh)
    resolution.grid(row=2, column=1)
    
    tk.Label(root, text="    low resolution:").grid(row=3, column=0)
    resl=tk.IntVar(root)
    resolution = tk.Entry(root, textvariable=resl)
    resolution.grid(row=3,column=1)
    
    # total lenth in x 
    tk.Label(root, text="    total lenth X:").grid(row=4, column=0)
    Lux=tk.DoubleVar(root,value=18)
    resolution = tk.Entry(root, textvariable=Lux)
    resolution.grid(row=4,column=1)
    
    # total lenth in y 
    tk.Label(root, text="    total lenth Y:").grid(row=5, column=0)
    Luy = tk.DoubleVar(root,value=18)
    resolution = tk.Entry(root, textvariable=Luy)
    resolution.grid(row=5,column=1)
    
    #  beetween fiducial marks in x 
    tk.Label(root, text="    beetween fiducial marks X:").grid(row=6, column=0)
    FMux = tk.DoubleVar(root,value=16.5)
    resolution = tk.Entry(root, textvariable=FMux)
    resolution.grid(row=6,column=1)
    
    # lenth beetween fiducial marksin y 
    tk.Label(root, text="    beetween fiducial marks Y:").grid(row=7, column=0)
    FMuy = tk.DoubleVar(root,value=16.5)
    resolution = tk.Entry(root, textvariable=FMuy)
    resolution.grid(row=7,column=1)
    
    # unity
    tk.Label(root, text="unity")
    u = tk.StringVar(root,"unity")
    tk.OptionMenu(root, u, *["cm","inche"]).grid(row=8,columnspan=2)
    

    main = partial(add_camera, camera, resh, resl, Lux, Luy, FMux, FMuy, u)
    
    # add camera button
    tk.Label(root, text=" ").grid(row=9, column=1)
    ttk.Button(root, text="Add camera", style='Accent.TButton',
               command=main).grid(row=10, columnspan=2)
    tk.Label(root, text=" ").grid(row=11, column=1)
    tk.Label(root, text=" ").grid(row=11, column=2)
    
    root.mainloop()


if __name__ == "__main__":
    add_camera_interface()
