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
import shutil


absFilePath = os.path.abspath(__file__)
filepath, filename = os.path.split(absFilePath)

sys.path.insert(0, '{}/scriptsAndInterfaces'.format(filepath))  # Local imports

# from GAPP_AirPhotoPreprocessing_main_v101 import main_script
from interface_FiducialTemplateCreator_v101 import interface_fiducial_template
from zoom_and_move_app import Zoom_Advanced

from GAPP_Script_01_AirPhoto_CanvasSizing_v201 import main_script_01
from GAPP_Script_02_AutomaticFiducialDetection_v201 import main_script_02
from GAPP_Script_03_AirPhoto_Reprojection_v201 import main_script_03
from GAPP_Script_04_AirPhotos_Resize_v201 import main_script_04
from GAPP_Script_05_AirPhoto_CreateSingleMask_v101 import main_script_05


sys.path.insert(0, '{}/scriptsAndInterfaces/camera'.format(filepath))

from interface_add_camera import add_camera_interface

class GAPP(ttk.Frame):
    
    def __init__(self,root):
        """
        print(' ')
        print('=====================================================================')
        print('=              GeoRiskA Aerial Photos Preprocessing Chain           =')
        print('=         Version 1.0.1 (December 2021) |  Antoine Dille (RMCA)     =')
        print('=====================================================================')
        print(' ')
        """
    
        # Initialize Main Window
        ttk.Frame.__init__(self,master=root)
    
        # Set the Interface Icon and Name
        
        # root.iconphoto(True, tk.PhotoImage(file='logo.png'))
        self.master.title('GeoRiskA Aerial Photos Preprocessing Chain')
    
        # # Set appearence theme
        # master.tk.call("source", "ttk_Theme/sun-valley.tcl")  # https://github.com/rdbende/Sun-Valley-ttk-theme
        # master.tk.call("set_theme", "light")  # light or dark theme
        self.master.option_add('*Font', 'TkMenuFont')  # define font
        
        
        self.path=r'J:\2_SfM_READY_photo_collection\Usumbura_1957-58-59'
        
        # add epmty label for better spacing
        tk.Label(self.master, text="  ").grid(row=12, column=0, columnspan=9, sticky="nsew")
        tk.Label(self.master, text="  ").grid( row=3, column=7, sticky="nsew")
        tk.Label(self.master, text="  ").grid(row=24, column=0, sticky="nsew")
        tk.Label(self.master, text="  ").grid(row=24, column=10, sticky="nsew")
        tk.Label(self.master, text="              ").grid(row=25, column=1, columnspan=9, sticky="nsew")
        tk.Label(self.master, text="  ").grid( row=20, column=1, columnspan=4, sticky="nsew")
        tk.Label(self.master, text=" ").grid( row=34, column=0)
        tk.Label(self.master, text=" ").grid( row=36, column=0)
        
        
        # Menu  
        menubar = tk.Menu(self.master)
        menubar.add_command(label = "Create fiducial template",command = lambda:[interface_fiducial_template()])
        menubar.add_command(label = "Add camera system",command = lambda:[add_camera_interface(),self.refresh()])
        
        self.master.config(menu=menubar) # adds the menu to master
        
        # Labels
        labeltext_input_folder = tk.StringVar()
        labeltext_input_folder.set('   Aerial images folder:')
        
        labeltext_output_folder = tk.StringVar()
        labeltext_output_folder.set('   Output folder:')
        
        labeltext_template_folder = tk.StringVar()
        labeltext_template_folder.set('   Fiducial template folder:')
        
        label1 = tk.Label(self.master, text="\n   Folders", font=('calibre', 11, 'bold'))
        label_input_folder = tk.Label(self.master, textvariable=labeltext_input_folder)
        label_output_folder = tk.Label(self.master, textvariable=labeltext_output_folder)
        label_template_folder = tk.Label(self.master, textvariable=labeltext_template_folder)
        label_template_folder_info = tk.Label(self.master, text='   templates images for 4 typical fiducial marks + associated .txt file. See Script_00_Tool_FiducialTemplateCreator', font=('calibre', 7, 'italic'))
        label5 = tk.Label(self.master, text="   Input parameters",font=('calibre', 11, 'bold'))
        label6 = tk.Label(self.master, text="\n   Steps to launch",font=('calibre', 11, 'bold'))
    
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
    
        # P value
        p_value_list = [0.0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.15, 0.20]
        tk.Label(self.master, text=" p-value:").grid(row=15, column=1, sticky="w")
        label_p_info = tk.Label(self.master, text='   % of image width that is a black/white strip. See Script_02_AutomaticFiducialDetection', font=('calibre', 7, 'italic'))
        label_p_info.grid(row=16, columnspan=6, sticky="w")
        chosen_p = tk.StringVar(self.master)
        chosen_p.set(p_value_list[3])  # by default
        entry_p = tk.OptionMenu(self.master, chosen_p, *p_value_list)
        entry_p.grid(row=15, column=2, sticky="nsew")
        
        self.chosen_p = chosen_p.get()
    
        # blackStripe location
        tk.Label(self.master, text="    Stripes location:").grid(row=17, columnspan=2, sticky="w")
        self.stripes = tk.StringVar(self.master, value='right, bottom')
        entry_stripes = tk.Entry(self.master, textvariable=self.stripes)
        entry_stripes.grid(row=19, column=1, columnspan=2, sticky="nsew")
                        
        # resolution
        tk.Label(self.master, text=" Input scan resolution:").grid(row=23, column=1, sticky="w")
        self.chosen_input_res = tk.StringVar(self.master)
        self.chosen_input_res.set("Choose input resolution")  # by default
        self.entry_input_res = tk.OptionMenu(self.master, self.chosen_input_res, *["choose a camera"])
        self.entry_input_res.grid(row=24, column=1, sticky="nsew")
    
        tk.Label(self.master, text=" Output scan resolution:").grid(row=23, column=2, sticky="w")
        self.chosen_output_res = tk.StringVar(self.master)
        self.chosen_output_res.set("Choose input resolution")  # by default
        self.entry_ouput_res = tk.OptionMenu(self.master, self.chosen_output_res, *["choose a camera"])
        self.entry_ouput_res.grid(row=24, column=2, sticky="nsew")
        
        # camera
        camera_file = open(r"{}/scriptsAndInterfaces/camera/camera.txt".format(filepath), "r")
        camera_value_list = camera_file.readlines()[0].split(";")
        camera_file.close()
        
        tk.Label(self.master, text=" Camera system:").grid(row=21, column=1, sticky="w")
        self.chosen_camera = tk.StringVar(self.master, value= "Wild RC5")
        self.chosen_camera.set("Choose a camera")  # by default
        
        self.resol_list = partial(self.resolution_list)
        entry_camera = tk.OptionMenu(self.master, self.chosen_camera, *camera_value_list, command=self.resol_list)
        entry_camera.grid(row=22, column=1, sticky="nsew")
        
        
        refreshbutton= ttk.Button(self.master, text="refresh camera list", command=self.refresh(self.chosen_camera))
        refreshbutton.grid(row=22, column=2, sticky="nsew")
        
    
        # Histogram calibration
        HistoCal_value_list = ['True', 'False']
        tk.Label(self.master, text=" CLAHE Histogram calibration:").grid(row=25, column=1, sticky="w")
        self.chosen_HistoCal = tk.StringVar(self.master)
        self.chosen_HistoCal.set(HistoCal_value_list[0])  # by default
        entry_HistoCal = tk.OptionMenu(self.master, self.chosen_HistoCal, *HistoCal_value_list)
        entry_HistoCal.grid(row=26, column=1, sticky="nsew")
    
        # Sharpening Intensity
        SharpIntensity_value_list = [0, 1, 2]
        tk.Label(self.master, text=" Sharpening intensity:").grid(row=25, column=2, sticky="w")
        chosen_SharpIntensity = tk.StringVar(self.master)
        chosen_SharpIntensity.set(SharpIntensity_value_list[2])  # by default
        entry_SharpIntensity = tk.OptionMenu(self.master, chosen_SharpIntensity, *SharpIntensity_value_list)
        entry_SharpIntensity.grid(row=26, column=2, sticky="nsew")
        
        self.chosen_SharpIntensity = chosen_SharpIntensity.get()
    
        #scale
        self.scale_percent=60
    
    
        # input folders
        entry_input_images = tk.Entry(self.master, width=80)
        entry_input_images.grid(row=3, column=1, columnspan=4, sticky="nsew")
        self.path_in_fold=tk.StringVar()
        tk.Button(self.master, text="Select folder", 
                  command=lambda: self.find_folder(entry_input_images,
                                                   "Select aerial image folder",
                                                   self.path_in_fold)).grid(row=3, column=8, sticky="w")
        
        self.path_input_folder=self.path_in_fold.get()
        
        
        # output folder
        entry_output_images = tk.Entry(self.master, width=80)
        entry_output_images.grid(row=6, column=1, columnspan=4, sticky="nsew")
        self.path_out_fold=tk.StringVar()
        tk.Button(self.master, text="Select folder", 
                  command=lambda: self.find_folder(entry_output_images, 
                                                   "Select output directory",
                                                   self.path_out_fold)).grid(row=6, column=8, sticky="w")
        
        self.path_output_folder=self.path_out_fold.get()
        
        # fiducial template folder
        entry_fidu = tk.Entry(self.master, width=80)
        entry_fidu.grid(row=10, column=1, columnspan=4, sticky="nsew")
        self.path_temp_fold=tk.StringVar()        
        tk.Button(self.master, text="Select folder",
                  command=lambda: self.find_folder(entry_fidu, 
                                                   "Select template directory",
                                                   self.path_temp_fold)).grid(row=10, column=8, sticky="w")
    
        self.path_temp_folder=self.path_temp_fold.get()      
        
        # Dataset
        
        self.labeltext_dataset = tk.StringVar()
        self.labeltext_dataset.set("   Dataset name:")
        label_dataset = tk.Label(self.master, textvariable=self.labeltext_dataset)
        label_dataset.grid(row=13, columnspan=2, sticky="w")
        
        self.dataset = tk.StringVar(self.master, value="Usumbura_1957-58-59")
        entry_dataset = tk.Entry(self.master, textvariable=self.dataset)
        entry_dataset.grid(row=14, column=1, columnspan=2, sticky="nsew")
        
        self.checkfidButton = ttk.Button(self.master, text="Check Dataset", command=self.check_dataset)
        self.checkfidButton.grid(row =14 , column=3,sticky="nsew")
                
        
        script1button = ttk.Button(self.master, text='Run Canvas sized and Fiducial mark detection',command=self.run_script_01)
        # script2button = ttk.Button(self.master, text='Run fid mark detection',command=self.run_script_02)
        scriptCheckbutton = ttk.Button(self.master, text='Run fid mark correction',command=self.run_script_check_fid)
        script3button = ttk.Button(self.master, text='Run Reprojection',command=self.run_script_03)
        script4button = ttk.Button(self.master, text='Run Resize',command=self.run_script_04)
        script5button = ttk.Button(self.master, text='Run Create mask',command=self.run_script_05)
        
        script1button.grid(row=31, column=1, columnspan=2, sticky="news")
        # script2button.grid(row=31, column=2, sticky="news")
        scriptCheckbutton.grid(row=31, column=3, sticky="news")
        script3button.grid(row=32, column=1, sticky="news")
        script4button.grid(row=32, column=2, sticky="news")
        script5button.grid(row=32, column=3, sticky="news")
        
        
        self.checkFrame = ttk.Frame(self.master)
        self.checkFrame.grid (column=12 ,row=1, rowspan=36)
        
    
    def check_dataset(self):
        FM = pd.read_csv('{}/{}'.format(self.path_temp_fold,
                                        'Center_Fiduciales.txt'), sep=' ',header=None) 
        fid = [n for n in FM[:][0] if n[:len('Template_%s_top' % (self.dataset))]
               in 'Template_%s_top' % (self.dataset) or  n[:len('Template_%s_bot' % (self.dataset))]
               in 'Template_%s_bot' % (self.dataset)]
        if len(fid )==0:
            self.labeltext_dataset.set("  there is not coresponding datase name in fiducial template")
            return False
        else:
            self.labeltext_dataset.set("   Dataset name:")
            return True
    
        
            
        
    def refresh(self,chosen_camera):
            
        # this function recovers the camera chose button with a new button

        # select file
        camera_file = open(r"{}/scriptsAndInterfaces/camera/camera.txt".format(filepath), "r")
        camera_value_list = camera_file.readlines()[0].split(";")
        camera_file.close()
        chosen_camera.set("Choose a camera")
        
        entry_camera = tk.OptionMenu(self.master, chosen_camera, *camera_value_list, command=self.resol_list)
        entry_camera.grid(row=22, column=1, sticky="nsew")
            
        
    def resolution_list(self,camera):
        # this function changes the list of resolution depending on the choosen camera
        # remove current list
        self.entry_input_res['menu'].delete(0, 'end')
        self.entry_ouput_res['menu'].delete(0, 'end')

        # select file
        resolution_file = r"{}/scriptsAndInterfaces/camera/{}_Airphoto_Photo_dimensions_vs_dpi.csv".format(filepath, camera)
        
        res_file = pd.read_csv(resolution_file, sep=',', header=[0])

        res_col = res_file['Resolution']
        res_list = res_col.tolist()

        # Insert list of new options in the input and output resolution lists
        for choice in res_list:
            self.entry_input_res['menu'].add_command(label=choice, command=tk._setit(self.chosen_input_res, choice))
            self.entry_ouput_res['menu'].add_command(label=choice, command=tk._setit(self.chosen_output_res, choice))

            
    
    def find_folder(self,e, text, folder):
        e.delete(first=0, last= len(folder.get()))
        folder.set(filedialog.askdirectory(initialdir=self.path, title=text))
        e.insert(0, folder.get())
        folder = folder.get()
        
        self.path=folder
        self.create_intermediate_folder()
        
    def create_intermediate_folder(self):
        
        #intermediate folders
        
        path=self.path_out_fold.get()
        self.output_canvas_sized = r'{}/{}'.format(path, '01_CanvasSized')
        self.output_reprojected =r'{}/{}'.format( path ,'02_Reprojected')
        self.output_resized =r'{}/{}'.format(path , '03_Resized')
        self.output_mask = r'{}/{}'.format( path , '04_Masks')
        if os.path.isfile(r'{}/_fiducial_marks_coordinates_{}.csv'.format(self.output_canvas_sized,self.dataset.get())):
            self.fiducialmarks_file = r'{}/new_fiducial_marks_coordinates_{}.csv'.format(self.output_canvas_sized,self.dataset.get())
        else:
            self.fiducialmarks_file = r'{}/_fiducial_marks_coordinates_{}.csv'.format(self.output_canvas_sized,self.dataset.get())
        self.resolution_file = r"{}/scriptsAndInterfaces/camera/{}_Airphoto_Photo_dimensions_vs_dpi.csv".format(os.path.split(os.path.abspath(__file__))[0],self.chosen_camera.get())
        
        
        
    def run_script_01(self):
        if '01_CanvasSized' in os.listdir(self.path_out_fold.get()):
            shutil.rmtree('{}/01_CanvasSized'.format(self.path_out_fold.get()))
            print('01_CanvasSized cleared')
            
        main_script_01(self.path_in_fold.get(),  self.output_canvas_sized)
        
    # def run_script_02(self):
        main_script_02(self.output_canvas_sized, self.path_temp_fold.get(),self.dataset.get(), float(self.chosen_p), self.stripes.get())
        
    def run_script_03(self):
        if '02_Reprojected' in os.listdir(self.path_out_fold.get()):
            shutil.rmtree('{}/02_Reprojected'.format(self.path_out_fold.get()))
            print('clear 02_Reprojected')
        self.create_intermediate_folder()
        print( self.chosen_camera.get(), self.resolution_file, self.chosen_input_res.get())
        main_script_03(self.output_canvas_sized, self.output_reprojected, 
                        self.fiducialmarks_file, self.chosen_camera.get(), self.resolution_file, self.chosen_input_res.get())
    
    def run_script_04(self):
        if '03_Resized' in os.listdir(self.path_out_fold.get()):
            shutil.rmtree('{}/03_Resized'.format(self.path_out_fold.get()))
            print('clear 03_Resized')
        self.create_intermediate_folder()
        main_script_04(self.output_reprojected, self.output_resized, self.scale_percent, 
                       self.chosen_HistoCal.get(), int(self.chosen_SharpIntensity), 
                       self.resolution_file, int(self.chosen_output_res.get()))
    
    def run_script_05(self):
        main_script_05(self.output_resized, self.output_mask,self.dataset.get())
    
    def run_script_check_fid(self):
        
        print(self.dataset.get())
        print(self.output_canvas_sized)
        
        Zoom_Advanced(self.checkFrame,self.dataset.get(),self.output_canvas_sized)
        
        # check_corners(self.dataset.get(),self.output_canvas_sized)

    


if __name__ == "__main__":
    root = tk.Tk()
    GAPP(root)
    root.mainloop()