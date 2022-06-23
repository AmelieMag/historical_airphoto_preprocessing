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

    res = []
    tot = []
    FMs = []

    def add_column(n):

        num.set(num.get()+1)
        
        # new resolution entry
        res.append(tk.Text(root))
        resolution = tk.Entry(root, textvariable=res)
        resolution.grid(row=2, column=num.get())
        
        # new total lenth entry
        tot.append(tk.StringVar(root))
        lenth_tot = tk.Entry(root, textvariable=tot)
        lenth_tot.grid(row=3, column=num.get())
        
        # new lenth between camera entry
        FMs.append(tk.Text(root))
        lenth_FMs = tk.Entry(root, textvariable=FMs)
        lenth_FMs.grid(row=4, column=num.get())
    
    # count column
    num = tk.IntVar()
    num.set(1)
    
    # camera name
    tk.Label(root, text="   Camera name without spaces:   ").grid(
        row=0, column=0)
    cam = tk.StringVar(root)
    camera = tk.Entry(root, textvariable=cam)
    camera.grid(row=0, column=1)
    
    # add resolution
    column = partial(add_column, num.get())
    ttk.Button(root, text="Add resolution",
               style='Accent.TButton', command=column).grid(row=1, sticky="E")
    
    # resolution
    tk.Label(root, text="    scan resolution:").grid(row=2, column=0)
    res.append(tk.IntVar(root,))
    resolution = tk.Entry(root, textvariable=res[0])
    resolution.grid(row=2, column=num.get())
    
    # total lenth in px
    tk.Label(root, text="    Total lenth (pixels):").grid(row=3, column=0)
    tot.append(tk.IntVar(root,))
    lenth_tot = tk.Entry(root, textvariable=tot[0])
    lenth_tot.grid(row=3, column=num.get())
    
    # lenth between fiducial marks in px
    tk.Label(root, text="    Lenth between fuducial marks (pixels):    ").grid(
        row=4, column=0)
    FMs.append(tk.IntVar(root))
    lenth_FMs = tk.Entry(root, textvariable=FMs[0])
    lenth_FMs.grid(row=4, column=num.get())

    main = partial(add_camera, cam, res, tot, FMs)
    
    # add camera button
    tk.Label(root, text=" ").grid(row=9, column=1)
    ttk.Button(root, text="Add camera", style='Accent.TButton',
               command=main).grid(row=10, column=1)
    tk.Label(root, text=" ").grid(row=11, column=1)
    
    root.mainloop()


if __name__ == "__main__":
    add_camera_interface()
