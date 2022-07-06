# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:06:01 2022

@author: Amelie Maginot
         Ecole nationale des sciences geographiques
"""

import tkinter as tk
import sys 

from GAPP_Script_00_Tool_FiducialTemplateCreator_v101 import fiducialTemplateCreator
from tkinter import ttk
from tkinter import filedialog
from time import sleep

sys.path.insert(0, '')

def interface_fiducial_template():
    root = tk.Tk()
    root.title("Fiducial Template creator")
    tk.Label(root, text=" ").grid(rowspan=15, column=0)
    tk.Label(root, text=" ").grid(rowspan=15, column=5)
    tk.Label(root, text=" ").grid(rowspan=15, column=7)
    
    # hight left corner
    tk.Label(root, text="Hight left corner coordinates").grid(row=1, column=0,columnspan=2)
    tk.Label(root, text="X =").grid(row=2, column=0)
    tk.Label(root, text="Y =").grid(row=3, column=0)
    X1 = tk.IntVar(root)
    Y1 = tk.IntVar(root)
    HLx = tk.Entry(root, textvariable=X1)
    HLy = tk.Entry(root, textvariable=Y1)
    HLx.grid(row=2, column=1)
    HLy.grid(row=3, column=1)
    
    # hight right corner
    tk.Label(root, text="Hight right corner coordinates").grid(row=1, column=3,columnspan=2)
    tk.Label(root, text="X =").grid(row=2, column=3)
    tk.Label(root, text="Y =").grid(row=3, column=3)
    X2 = tk.IntVar(root)
    Y2 = tk.IntVar(root)
    HRx = tk.Entry(root, textvariable=X2)
    HRy = tk.Entry(root, textvariable=Y2)
    HRx.grid(row=2, column=4)
    HRy.grid(row=3, column=4)
    
    # low right corner
    tk.Label(root, text="Low right corner coordinates").grid(row=9, column=3,columnspan=2)
    tk.Label(root, text="X =").grid(row=10, column=3)
    tk.Label(root, text="Y =").grid(row=11, column=3)
    X3 = tk.IntVar(root)
    Y3 = tk.IntVar(root)
    LRx = tk.Entry(root, textvariable=X3)
    LRy = tk.Entry(root, textvariable=Y3)
    LRx.grid(row=10, column=4)
    LRy.grid(row=11, column=4)
    
    # low left corner
    tk.Label(root, text="Low left corner coordinates").grid(row=9, column=0,columnspan=2)
    tk.Label(root, text="X =").grid(row=10, column=0)
    tk.Label(root, text="Y =").grid(row=11, column=0)
    X4 = tk.IntVar(root)
    Y4 = tk.IntVar(root)
    LLx = tk.Entry(root, textvariable=X4)
    LLy = tk.Entry(root, textvariable=Y4)
    LLx.grid(row=10, column=1)
    LLy.grid(row=11, column=1)
    
    # settings
    # halfwith
    tk.Label(root, text="half width (int)").grid(row=4, column=2)
    halfwidth = tk.IntVar(root)
    tk.Entry(root, textvariable=halfwidth).grid(row=5, column=2)
    # dataset
    tk.Label(root, text="dataset name without spaces").grid(row=6, column=2)
    dataset = tk.StringVar(root)
    tk.Entry(root, textvariable=dataset).grid(row=7, column=2)
    
    # image
    tk.Label(root, text="  Input image").grid(row=13, column=0)
    entry_input_images = tk.Entry(root, width=80)
    entry_input_images.grid(row=13, column=1, columnspan=4)
    
    tk.Button(root, text="Select image", command=lambda: find_input_image(
        entry_input_images, "Select image ")).grid(row=13, column=6)
    
    # folders
    tk.Label(root, text="  Output data folder").grid(row=14, column=0)
    entry_output_folder = tk.Entry(root, width=80)
    entry_output_folder.grid(row=14, column=1, columnspan=4)
    
    tk.Button(root, text="Select folder", command=lambda: find_output_folder(
        entry_output_folder, "Select output directory")).grid(row=14, column=6)
    
    global path
    path = "./"
    
    
    def find_input_image(e, text):
        global path
        root.filename = filedialog.askopenfilename(initialdir=path, title=text)
        path = root.filename
        e.insert(0, root.filename)
        input_image.append(path)
    
    
    def find_output_folder(e, text):
        global path
        root.filename = filedialog.askdirectory(initialdir=path, title=text)
        path = root.filename
        e.insert(0, root.filename)
        output_folder.append(path)
    
    
    input_image = []
    output_folder = []
    
    
    def main():
        fiducialCenters = {'top_left': [X1.get(), Y1.get()],
                           'top_right': [X2.get(),Y2.get()],
                           'bot_right': [X3.get(),Y3.get()],
                           'bot_left': [X4.get(), Y4.get()]}
        print("interface fidcenter: {}".format(X1.get()))
        w = halfwidth.get()
        d = dataset.get()
    
        fiducialTemplateCreator(input_image[0], output_folder[0], fiducialCenters, w, d)
        sleep(1)
        root.destroy()
    
    
    tk.Label(root, text=" ").grid(row=12)
    tk.Label(root, text=" ").grid(row=15)
    tk.Label(root, text=" ").grid(row=17)
    
    ttk.Button(root, text="Create fiducial template",
               command=main).grid(row=16, column=2)
    
    root.mainloop()

if __name__ == '__main__':
    interface_fiducial_template()