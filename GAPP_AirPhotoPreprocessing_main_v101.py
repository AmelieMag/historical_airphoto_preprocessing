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

import os, sys
import shutil


sys.path.insert(0, '') # Local imports

from GAPP_Script_01_AirPhoto_CanvasSizing_v201 import main_script_01
from GAPP_Script_02_AutomaticFiducialDetection_v201 import main_script_02
from GAPP_Script_03_AirPhoto_Reprojection_v201 import main_script_03
from GAPP_Script_04_AirPhotos_Resize_v201 import main_script_04


def main_script(input_folder,output_folder, template_folder, dataset, chosen_p, stripes, chosen_camera,chosen_input_res,chosen_output_res,chosen_HistoCal, chosen_SharpIntensity, Steps ):
    input_0=input_folder
    output_canvas_sized=output_folder + '/' + '01_CanvasSized'
    output_reprojected=output_folder + '/' + '02_Reprojected'
    output_resized=output_folder + '/' + '03_Resized'

    template_0= template_folder
    dataset_0=dataset
    chosen_p_0=float(chosen_p)
    stripes_0=stripes
    camera=str(chosen_camera)
    fiducialmarks_file= output_canvas_sized + '/' + '_fiducial_marks_coordinates_' + dataset_0 + '.csv'

    scale_percent_0 = 60
    print( scale_percent_0)
    chosen_HistoCal_0=str(chosen_HistoCal)
    chosen_SharpIntensity_0=float(chosen_SharpIntensity)

    print('-> will run the following steps:')
    print(Steps)


    # scripts
    # 01_CanvasSizing
    if Steps['Script_01'] == 1:
        main_script_01(input_0,output_canvas_sized)
    # 02_AutomaticFiducialDetection
    if Steps['Script_02'] == 1:
        main_script_02(output_canvas_sized, template_0, dataset_0, chosen_p_0, stripes_0)
    # 03_Reprojection
    if Steps['Script_03'] == 1:
        main_script_03(output_canvas_sized, output_reprojected, fiducialmarks_file, camera)
    # 04_Resize
    if Steps['Script_04'] == 1:
        main_script_04(output_reprojected, output_resized, scale_percent_0, chosen_HistoCal_0, chosen_SharpIntensity_0)

#############################################################################################

if __name__== '__main__':
    print(' ')
    print('----------------------------------------------------------------------')
    print('-------------------- Air Photo Processing ----------------------------')
    print('----------------------------------------------------------------------')

    ######################### Dossiers de travail #################################
    """ test wsl """
    """
    input_folder =  '/home/risnatlinux/ENSG_internship_2022/script_Amelie/GAPP-Antoine/test/5858_001-005'
    # e.g. 'D:/ENSG_internship_2022/script_Amelie/GAPP-Antoine/test/5858_001-005'
    output_folder = '' # useless for the moment
    # e.g ''
    fiducial_folder = '/home/risnatlinux/ENSG_internship_2022/script_Amelie/GAPP-Antoine/test/fiducial_marks'
    # e.g. 'D:/ENSG_internship_2022/script_Amelie/GAPP-Antoine/test/fiducial_marks'
    dataset = 'Virunga_1958'     
    # e.g. 'Virunga_1958'
    """

    """test windows"""

    input_folder =  'D:/ENSG_internship_2022/git/test/5858_001-005/'
    output_folder = 'D:/ENSG_internship_2022/git/test/'
    fiducial_folder = 'D:/ENSG_internship_2022/git/test/fiducial_marks'
    dataset = 'Virunga_1958'


    ###############################################################################

    ############################# Parameters ######################################
    p = 0.04  # percentage of black stripe width compare to the total width of the picture (e.g., 0.05). To be associated with parameter >> black_stripe_location

    # don't change the two following parameters scriptisn't ready
    stripes = 'right, bottom'
    camera = 'Wild RC5a'

    input_resolution = 1600
    output_resolution = 900
    choosen_HistoCal = True
    SharpIntensity = 2.0
    Steps = {'Script_01': 0,  # GAPP_Script_01_AirPhoto_CanvasSizing_v201
             'Script_02': 0,  # GAPP_Script_02_AutomaticFiducialDetection_v201
             'Script_03': 0,  # GAPP_Script_03_AirPhoto_Reprojection_v201
             'Script_04': 1}  # GAPP_Script_04_AirPhotos_Resize_v201

    ###############################################################################

    # cleaning the folder / be carefull if you want to use the script several times

    if '01_CanvasSized' in os.listdir(output_folder) and Steps['Script_01']==1:
        shutil.rmtree(output_folder + '/01_CanvasSized')
        print('01_CanvasSized cleared')
    if '02_Reprojected' in os.listdir(output_folder)  and Steps['Script_03']==1:
        shutil.rmtree(output_folder + '/02_Reprojected')
        print('clear 02_Reprojected')
    if '03_Resized' in os.listdir(output_folder)  and Steps['Script_04']==1:
        shutil.rmtree(output_folder + '/03_Resized')
        print('clear 03_Resized')
    print(' ')    

    # Runing main application

    main_script(input_folder, output_folder, fiducial_folder, dataset, p,
      stripes, camera, input_resolution, output_resolution, choosen_HistoCal, SharpIntensity,Steps)



