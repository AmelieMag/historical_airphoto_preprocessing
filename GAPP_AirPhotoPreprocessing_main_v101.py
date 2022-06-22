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

from GAPP_Script_04_AirPhotos_Resize_v201 import main_script_04
from GAPP_Script_03_AirPhoto_Reprojection_v201 import main_script_03
from GAPP_Script_02_AutomaticFiducialDetection_v201 import main_script_02
from GAPP_Script_01_AirPhoto_CanvasSizing_v201 import main_script_01

import os
import sys
import shutil


sys.path.insert(0, '')  # Local imports


def main_script(input_folder, output_folder, template_folder, dataset, chosen_p,
                stripes, chosen_camera, chosen_input_res, chosen_output_res,
                chosen_HistoCal, chosen_SharpIntensity, S1=0, S2=0, S3=0, S4=0, Steps=''):
    """
    

    Parameters
    ----------
    input_folder : TYPE
        folder where the photo are located.
    output_folder : TYPE
        folder where all folder from every scrips will be create.
    template_folder : TYPE
        DESCRIPTION.
    dataset : string
        name of the dataset.
    chosen_p : TYPE
        DESCRIPTION.
    stripes : TYPE
        DESCRIPTION.
    chosen_camera : string
        DESCRIPTION.
    chosen_input_res : int
        resolution of photo.
    chosen_output_res : int
        resolution expected for the output photos.
    chosen_HistoCal : TYPE
        DESCRIPTION.
    chosen_SharpIntensity : TYPE
        DESCRIPTION.
    S1 : TYPE, optional
        do we run script_01 yes = 1 no = 0. The default is 0.
    S2 : TYPE, optional
        do we run script_01 yes = 1 no = 0. The default is 0.
    S3 : TYPE, optional
        do we run script_01 yes = 1 no = 0. The default is 0.
    S4 : TYPE, optional
        do we run script_01 yes = 1 no = 0. The default is 0.
    Steps : dictionnaire, optional
        what scripts are launche if main. The default is ''.

    Returns
    -------
    None.

    """
        
    input_0 = input_folder
    
    template_0 = template_folder
    dataset_0 = dataset
    chosen_p_0 = float(chosen_p)
    stripes_0 = stripes
    camera = str(chosen_camera)

    scale_percent_0 = 60
    chosen_HistoCal_0 = str(chosen_HistoCal)
    chosen_SharpIntensity_0 = float(chosen_SharpIntensity)
    
    if __name__ != '__main__':        
        input_0 = input_folder[0]
        output_folder = output_folder[0]
        print('output folder = {}'.format(output_folder))
        Steps = {'Script_01': S1.get(), 'Script_02': S2.get(), 
                 'Script_03': S3.get(), 'Script_04':S4.get()}
        template_0 = template_folder[0]
        dataset_0 = dataset.get()
        chosen_p_0 = float(chosen_p)
        stripes_0 = stripes.get()
        camera = str(chosen_camera.get())
        chosen_input_res = int(chosen_input_res.get())
        chosen_output_res = int(chosen_output_res.get())
        
    
    output_canvas_sized = '{}/{}'.format(output_folder, '01_CanvasSized')
    output_reprojected ='{}/{}'.format( output_folder ,'02_Reprojected')
    output_resized ='{}/{}'.format( output_folder , '03_Resized_test')
    
    fiducialmarks_file = '{}/_fiducial_marks_coordinates_{}.csv'.format(output_canvas_sized,dataset_0)
       
    
    
    # Get the path of the file where the script is located
    absFilePath = os.path.abspath(__file__)
    path, filename = os.path.split(absFilePath)
    print("Script file path is {}, filename is {}".format(path, filename))
    
    # select the resolution file corresponding to the good camera
    if camera =="Wild RC5a":
        resolution_file = r"{}/Wild_RC5_Airphoto_Photo_dimensions_vs_dpi.csv".format(path)
    if camera == "Wild RC10":
        resolution_file = r"{}/Wild_RC10_Airphoto_Photo_dimensions_vs_dpi.csv".format(path)
        
    print('01_CanvasSized' in os.listdir(output_folder))
    print(Steps['Script_01'] == 1)
    if '01_CanvasSized' in os.listdir(output_folder) and Steps['Script_01'] == 1:
        shutil.rmtree('{}/01_CanvasSized'.format(output_folder))
        print('01_CanvasSized cleared')
    if '02_Reprojected' in os.listdir(output_folder) and Steps['Script_03'] == 1:
        shutil.rmtree('{}/02_Reprojected'.format(output_folder))
        print('clear 02_Reprojected')
    if '03_Resized' in os.listdir(output_folder)  and Steps['Script_04']==1:
        shutil.rmtree('{}/03_Resized'.format(output_folder))
        print('clear 03_Resized')
    print(' ')

    print('-> will run the following steps:')
    print(Steps)

    # scripts
    # 01_CanvasSizing
    if Steps['Script_01'] == 1:
        main_script_01(input_0, output_canvas_sized)
    # 02_AutomaticFiducialDetection
    if Steps['Script_02'] == 1:
        main_script_02(output_canvas_sized, template_0,
                       dataset_0, chosen_p_0, stripes_0)
    # 03_Reprojection
    if Steps['Script_03'] == 1:
        main_script_03(output_canvas_sized, output_reprojected,
                       fiducialmarks_file, camera, resolution_file, chosen_input_res)
    # 04_Resize
    if Steps['Script_04'] == 1:
        main_script_04(output_reprojected, output_resized, scale_percent_0,
                       chosen_HistoCal_0, chosen_SharpIntensity_0, resolution_file, chosen_output_res)
    print('fini')

#############################################################################################


if __name__ == '__main__':
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
    """
    input_folder =  'D:/ENSG_internship_2022/git/test/5858_001-005/'
    output_folder = 'D:/ENSG_internship_2022/git/test/'
    fiducial_folder = 'D:/ENSG_internship_2022/git/test/fiducial_marks'
    dataset = 'Virunga_1958'
    """

    """test teletravail"""
    input_folder = r"C:\Users\AmelieMaginot\Documents\ING_2\StageMRAC\test\5858_001-005"
    output_folder = r"C:\Users\AmelieMaginot\Documents\ING_2\StageMRAC/test/resultat/"
    fiducial_folder = r"C:\Users\AmelieMaginot\Documents\ING_2\StageMRAC\test\fiducial_marks"
    resolution_file = r"C:\Users\AmelieMaginot\Documents\ING_2\StageMRAC\git\historical_airphoto_preprocessing\Airphoto_Photo_dimensions_vs_dpi.csv"
    dataset = 'Virunga_1958'

    ###############################################################################

    ############################# Parameters ######################################
    # percentage of black stripe width compare to the total width of the picture (e.g., 0.05). To be associated with parameter >> black_stripe_location
    p = 0.04

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

    if '01_CanvasSized' in os.listdir(output_folder) and Steps['Script_01'] == 1:
        shutil.rmtree(output_folder + '/01_CanvasSized')
        print('01_CanvasSized cleared')
    if '02_Reprojected' in os.listdir(output_folder) and Steps['Script_03'] == 1:
        shutil.rmtree(output_folder + '/02_Reprojected')
        print('clear 02_Reprojected')
    if '03_Resized' in os.listdir(output_folder)  and Steps['Script_04']==1:
        shutil.rmtree(output_folder + '/03_Resized')
        print('clear 03_Resized')
    print(' ')

    # Runing main application

    main_script(input_folder, output_folder, fiducial_folder, dataset, p,
                stripes, camera, input_resolution, output_resolution,
                choosen_HistoCal, SharpIntensity, Steps = Steps)
