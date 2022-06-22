# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:32:45 2022

@author: Amelie Maginot
         Ecole nationale des sciences geographiques
"""

import tkinter as tk
from tkinter import ttk
import sys
from functools import partial

sys.path.insert(0,'')

from Add_Camera import add_camera

root = tk.Tk()

root.title("Add camera to pre-processing program")

tk.Label(root, text="   Camera name without spaces:   ").grid(row = 0, column= 1)
cam = tk.StringVar(root)
camera = tk.Entry(root,cam)
camera.grid(row = 1, column= 1)

tk.Label(root, text="    scan resolution:").grid(row = 2, column= 1)
res = tk.StringVar(root)
resolution = tk.Entry(root,res)
resolution.grid(row = 3, column= 1)

tk.Label(root, text="    Total lenth (pixeles):").grid(row = 4, column= 1)
tot = tk.StringVar(root)
lenth_tot = tk.Entry(root,tot)
lenth_tot.grid(row = 5, column= 1)

tk.Label(root, text="    Lenth between fuducial marks (pixels):    ").grid(row = 6, column= 1)
FMs = tk.StringVar(root)
lenth_FMs = tk.Entry(root,FMs)
lenth_FMs.grid(row = 7, column= 1)

main = partial(add_camera,cam,res,tot,FMs)

tk.Label(root,text = " ").grid(row = 9, column= 1)
ttk.Button(root, text="Add camera", style='Accent.TButton', command = main).grid(row = 10, column= 1)
tk.Label(root,text = " ").grid(row = 11, column= 1)

root.mainloop()