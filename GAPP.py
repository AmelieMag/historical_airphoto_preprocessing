#!C:\\Users\\adille\\anaconda3\\envs\\GEO-Env\\python

"""
------------------------------------------------------------------------------
GeoRiskA Aerial Photo Preprocessing Chain
PYTHON INTERFACE FOR THE STANDARDIZING OF AERIAL PHOTO ARCHIVE
------------------------------------------------------------------------------

Version: 1.0.1
Author: Antoine Dille
        (Royal Museum for Central Africa  )

Citation:
    Smets, B., 2021
    Historical Aerial Photo Pre-Processing
    [Script_1_AirPhoto_CanvasSizing_v101.py].
    Version 1.0
    https://github.com/GeoRiskA/historical_airphoto_preprocessing
    DOI: N/A

Associated article (to be cited too):
    Smets, B., Dewitte, O., Michellier, C., Muganga, G., Dille, A., Kervyn, F.,
    SUBMITTED
    Insights into the SfM photogrammetric processing of historical
    panchromatic aerial photographs without camera calibration
    information.
    ISPRS International Journal of Geo-Information.
    DOI: N/A

Notes:

    - For the required Python libraries, we recommend the use of Anaconda
      or Miniconda.

    - Specific Python modules needed for this script:
        > tKinter

    - To use this script, simply adapt the directory paths and required values
      in the setup section of the script.


"""

from tkinter import ttk
from tkinter import filedialog
from functools import partial
import tkinter as tk
import sys, os
import pandas as pd


absFilePath = os.path.abspath(__file__)
filepath, filename = os.path.split(absFilePath)

sys.path.insert(0, '{}/scriptsAndInterfaces'.format(filepath))  # Local imports

from GAPP_AirPhotoPreprocessing_main_v101 import main_script
from interface_FiducialTemplateCreator_v101 import interface_fiducial_template

sys.path.insert(0, '{}/scriptsAndInterfaces/camera'.format(filepath))

from interface_add_camera import add_camera_interface


def main():
    """
    print(' ')
    print('=====================================================================')
    print('=              GeoRiskA Aerial Photos Preprocessing Chain           =')
    print('=         Version 1.0.1 (December 2021) |  Antoine Dille (RMCA)     =')
    print('=====================================================================')
    print(' ')
    """

    # Initialize Main Window
    root = tk.Tk()

    # Set the Interface Icon and Name
    
    # root.iconphoto(True, tk.PhotoImage(file='logo.png'))
    root.title('GeoRiskA Aerial Photos Preprocessing Chain')

    # # Set appearence theme
    # root.tk.call("source", "ttk_Theme/sun-valley.tcl")  # https://github.com/rdbende/Sun-Valley-ttk-theme
    # root.tk.call("set_theme", "light")  # light or dark theme
    root.option_add('*Font', 'TkMenuFont')  # define font
    
    
    # add epmty label for better spacing
    tk.Label(root, text="  ").grid(row=12, column=0, columnspan=9, sticky="nsew")
    tk.Label(root, text="  ").grid( row=3, column=7, sticky="nsew")
    tk.Label(root, text="  ").grid(row=24, column=0, sticky="nsew")
    tk.Label(root, text="  ").grid(row=24, column=10, sticky="nsew")
    tk.Label(root, text="              ").grid(row=25, column=1, columnspan=9, sticky="nsew")
    tk.Label(root, text="  ").grid( row=20, column=1, columnspan=4, sticky="nsew")
    tk.Label(root, text=" ").grid( row=34, column=0)
    tk.Label(root, text=" ").grid( row=36, column=0)
    
    
    # Menu    
    menubar = tk.Menu(root)
    menubar.add_command(label = "Create fiducial template",command = lambda:[interface_fiducial_template()])
    menubar.add_command(label = "Add camera system",command = lambda:[add_camera_interface(),refresh()])
    
    root.config(menu=menubar) # adds the menu to root
    
    # Labels

    label1 = tk.Label(root, text="\n   Folders", font=('calibre', 11, 'bold'))
    label_input_folder = tk.Label(root, text='   Aerial images folder:')
    label_output_folder = tk.Label(root, text='   Output folder:')
    label_template_folder = tk.Label(root, text='   Fiducial template folder:')
    label_template_folder_info = tk.Label(root, text='   templates images for 4 typical fiducial marks + associated .txt file. See Script_00_Tool_FiducialTemplateCreator', font=('calibre', 7, 'italic'))
    label5 = tk.Label(root, text="   Input parameters",font=('calibre', 11, 'bold'))
    label6 = tk.Label(root, text="\n   Steps to launch",font=('calibre', 11, 'bold'))

    label1.grid(row=1, columnspan=4, sticky="w")
    label_input_folder.grid(row=2, columnspan=4, sticky="w")
    label_output_folder.grid(row=5, columnspan=4, sticky="w")
    label_template_folder.grid(row=8, columnspan=4, sticky="w")
    label_template_folder_info.grid(row=9, columnspan=6, sticky="w")
    label5.grid(row=12, columnspan=3, sticky="w")
    label6.grid(row=30, columnspan=3, sticky="w")

    global path
    path = "./"

    ######### Initialize Entries #########
    
    # folders
    entry_input_images = tk.Entry(root, width=80)
    entry_input_images.grid(row=3, column=1, columnspan=4, sticky="nsew")
    entry_output_images = tk.Entry(root, width=80)
    entry_output_images.grid(row=6, column=1, columnspan=4, sticky="nsew")

    # fiducial template folder
    entry_fidu = tk.Entry(root, width=80)
    entry_fidu.grid(row=10, column=1, columnspan=4, sticky="nsew")

    # Dataset
    tk.Label(root, text="   Dataset name:").grid(row=13, columnspan=2, sticky="w")
    dataset = tk.StringVar(root, value='WRC10')
    entry_dataset = tk.Entry(root, textvariable=dataset)
    entry_dataset.grid(row=14, column=1, columnspan=2, sticky="nsew")

    # P value
    p_value_list = [0.0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.15, 0.20]
    tk.Label(root, text=" p-value:").grid(row=15, column=1, sticky="w")
    label_p_info = tk.Label(root, text='   % of image width that is a black/white strip. See Script_02_AutomaticFiducialDetection', font=('calibre', 7, 'italic'))
    label_p_info.grid(row=16, columnspan=6, sticky="w")
    chosen_p = tk.StringVar(root)
    chosen_p.set(p_value_list[3])  # by default
    entry_p = tk.OptionMenu(root, chosen_p, *p_value_list)
    entry_p.grid(row=15, column=2, sticky="nsew")

    # blackStripe location
    tk.Label(root, text="    Stripes location:").grid(row=17, columnspan=2, sticky="w")
    stripes = tk.StringVar(root, value='right, bottom')
    entry_stripes = tk.Entry(root, textvariable=stripes)
    entry_stripes.grid(row=19, column=1, columnspan=2, sticky="nsew")

    # camera
    
    def refresh():
            
        # this function recovers the camera chose button with a new button

        # select file
        camera_file = open(r"{}/scriptsAndInterfaces/camera/camera.txt".format(filepath), "r")
        camera_value_list = camera_file.readlines()[0].split(";")
        camera_file.close()
        chosen_camera.set("Choose a camera")
        
        entry_camera = tk.OptionMenu(root, chosen_camera, *camera_value_list, command=resol_list)
        entry_camera.grid(row=22, column=1, sticky="nsew")
        
    
    def resolution_list(camera):
        print("camera = {}".format(camera))
        # this function changes the list of resolution depending on the choosen camera
        # remove current list
        entry_input_res['menu'].delete(0, 'end')
        entry_ouput_res['menu'].delete(0, 'end')

        # select file
        resolution_file = r"{}/scriptsAndInterfaces/camera/{}_Airphoto_Photo_dimensions_vs_dpi.csv".format(filepath, camera)
        res_file = pd.read_csv(resolution_file, sep=';', header=[0])

        res_col = res_file['Resolution']
        res_list = res_col.tolist()

        # Insert list of new options in the input and output resolution lists
        for choice in res_list:
            entry_input_res['menu'].add_command(label=choice, command=tk._setit(chosen_input_res, choice))
            entry_ouput_res['menu'].add_command(label=choice, command=tk._setit(chosen_output_res, choice))

        
    camera_file = open(r"{}/scriptsAndInterfaces/camera/camera.txt".format(filepath), "r")
    camera_value_list = camera_file.readlines()[0].split(";")
    camera_file.close()
    
    refreshbutton= ttk.Button(root, text="refresh camera list", command=refresh)
    refreshbutton.grid(row=22, column=2, sticky="nsew")
    
    # camera_value_list = ["Wild RC5", "Wild RC10"] # other camera could be added here. Values should then be adapted in Script_03_AirPhoto_Reprojection_v102_GAPP.py
    tk.Label(root, text=" Camera system:").grid(row=21, column=1, sticky="w")
    chosen_camera = tk.StringVar(root)
    chosen_camera.set("Choose a camera")  # by default
    resol_list = partial(resolution_list)
    entry_camera = tk.OptionMenu(root, chosen_camera, *camera_value_list, command=resol_list)
    entry_camera.grid(row=22, column=1, sticky="nsew")
    
    # resolution
    # resolution_value_list = ["300","400","600","800","900","1200","1500","1600","1800"]
    tk.Label(root, text=" Input scan resolution:").grid(row=23, column=1, sticky="w")
    chosen_input_res = tk.StringVar(root)
    chosen_input_res.set("Choose input resolution")  # by default
    entry_input_res = tk.OptionMenu(root, chosen_input_res, *["choose a camera"])
    entry_input_res.grid(row=24, column=1, sticky="nsew")

    tk.Label(root, text=" Output scan resolution:").grid(row=23, column=2, sticky="w")
    chosen_output_res = tk.StringVar(root)
    chosen_output_res.set("Choose input resolution")  # by default
    entry_ouput_res = tk.OptionMenu(root, chosen_output_res, *["choose a camera"])
    entry_ouput_res.grid(row=24, column=2, sticky="nsew")

    # Histogram calibration
    HistoCal_value_list = ['True', 'False']
    tk.Label(root, text=" CLAHE Histogram calibration:").grid(row=25, column=1, sticky="w")
    chosen_HistoCal = tk.StringVar(root)
    chosen_HistoCal.set(HistoCal_value_list[0])  # by default
    entry_HistoCal = tk.OptionMenu(root, chosen_HistoCal, *HistoCal_value_list)
    entry_HistoCal.grid(row=26, column=1, sticky="nsew")

    # Sharpening Intensity
    SharpIntensity_value_list = [0, 1, 2]
    tk.Label(root, text=" Sharpening intensity:").grid(row=25, column=2, sticky="w")
    chosen_SharpIntensity = tk.StringVar(root)
    chosen_SharpIntensity.set(SharpIntensity_value_list[2])  # by default
    entry_SharpIntensity = tk.OptionMenu(root, chosen_SharpIntensity, *SharpIntensity_value_list)
    entry_SharpIntensity.grid(row=26, column=2, sticky="nsew")

    def find_input_folder(e, text):
        global path
        root.filename = filedialog.askdirectory(initialdir=path, title=text)
        path = root.filename
        e.insert(0, root.filename)
        input_folder.append(path)

    def find_output_folder(e, text):
        global path
        root.filename = filedialog.askdirectory(initialdir=path, title=text)
        path = root.filename
        e.insert(0, root.filename)
        output_folder.append(path)

    def find_template_folder(e, text):
        global path
        root.filename = filedialog.askdirectory(initialdir=path, title=text)
        path = root.filename
        e.insert(0, root.filename)
        template_folder.append(path)

    # Initialize Buttons:
    input_folder = []
    output_folder = []
    template_folder = []
    check_01 = tk.IntVar()
    check_02 = tk.IntVar()
    check_03 = tk.IntVar()
    check_04 = tk.IntVar()
    check_05 = tk.IntVar()

    ttk.Checkbutton(root, text="Script_01: Canvas Sizing",variable=check_01).grid(row=31, column=1, sticky="w")
    ttk.Checkbutton(root, text="Script_02: Fiducial Detection",variable=check_02).grid(row=31, column=2, sticky="w")
    ttk.Checkbutton(root, text="Script_03: Reproject",variable=check_03).grid(row=32, column=1, sticky="w")
    ttk.Checkbutton(root, text="Script_04: Downsampling",variable=check_04).grid(row=32, column=2, sticky="w")
    ttk.Checkbutton(root, text="Script_05: Create Mask",variable=check_05).grid(row=31, column=3, sticky="w")

    tk.Button(root, text="Select folder", command=lambda: find_input_folder(entry_input_images, "Select aerial image folder")).grid(row=3, column=8, sticky="w")
    tk.Button(root, text="Select folder", command=lambda: find_output_folder(entry_output_images, "Select output directory")).grid(row=6, column=8, sticky="w")
    tk.Button(root, text="Select folder", command=lambda: find_template_folder(entry_fidu, "Select template directory")).grid(row=10, column=8, sticky="w")

    chosen_p = chosen_p.get()
    chosen_SharpIntensity = chosen_SharpIntensity.get()

    # Partial library is used to preset partial functions with the chosen parameters before run it
    main_script_launch = partial(main_script, input_folder, output_folder, template_folder,
                          dataset, chosen_p, stripes, chosen_camera, chosen_input_res,
                          chosen_output_res, chosen_HistoCal, chosen_SharpIntensity,
                          check_01, check_02, check_03, check_04, check_05)

    ttk.Button(root, text="Run", style='Accent.TButton', command=main_script_launch).grid(row=35, column=1, columnspan=9, sticky="nsew")

    # buttonUpdate = ttk.Button(root, text=" update ", style='Accent.TButton', command=click_me).grid(row=31,column=3,columnspan = 2, sticky="w")

    # b = Button(root, text=" update ", command=click_me).grid(row=31,column=3,columnspan = 2, sticky="w")

    # defined a window size to be sure it doesn't change over time
    root.geometry()
    root.resizable(width=tk.TRUE, height=tk.TRUE)
    
    
    # End of interface

    # Mainloop
    root.mainloop()


if __name__ == "__main__":

    main()