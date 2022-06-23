#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------
PYTHON SCRIPT FOR CREATING FIDUCIAL TEMPLATES
------------------------------------------------------------------------------

Version: 1.0.1 (22/12/2021)
Author: Antoine Dille
        (Royal Museum for Central Africa )



This script aims at creating templates for the four fiducial (corners) of an aerial image for later automatic
detection of the fiducials on a large set of aerial images (see SCRIPT 02 - Automatic Fiducials Detection).
Simply provide the path of one image of the set with representative fiducial marks. Note that
SCRIPT 02 allows to test multiple templates.


AD December 2021

"""

import cv2
import os
import csv
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------------
################################    SETUP     ################################
# ----------------------------------------------------------------------------
# input parameters
image4template_path = r"D:\ENSG_internship_2022\git\testWRC10\Bande_9_8-778_8-799\Bande_9_8-778.tif"
fiducialCenters = {'top_left': [815, 924], 'top_right': [13509, 931],
                   'bot_right': [13473, 13433], 'bot_left': [855, 13420]}  # manual coordinates


# half width (in pixels) required to cover the entirety of the fiducial mark
halfwidth = 120
# folder where the fiducial template will be saved
output_template_folder = r'D:\ENSG_internship_2022\git\testWRC10\fiducial_marks'
dataset = 'WRC10'  # image dataset name (e.g., 'Virunga_1958')
# Fiducial_type='target'

# ----------------------------------------------------------------------------
################################ END OF SETUP ###############################
# ----------------------------------------------------------------------------


def fiducialTemplateCreator(image4template_path,output_template_folder, fiducialCenters, halfwidth=120, dataset='WRC10'):

    img4template = cv2.imread(image4template_path, cv2.IMREAD_UNCHANGED)
    corner_list = ['top_left', 'top_right', 'bot_right', 'bot_left']

    fiducialCenters_images = {}

    fiducialCenters_images['top_left'] = [img4template[fiducialCenters['top_left'][1] -
                                                       halfwidth:fiducialCenters['top_left'][1] +
                                                       halfwidth,
                                                       fiducialCenters['top_left'][0] -
                                                       halfwidth:fiducialCenters['top_left'][0] +
                                                       halfwidth]][0]

    fiducialCenters_images['top_right'] = [img4template[fiducialCenters['top_right'][1]-halfwidth:fiducialCenters['top_right'][1]+halfwidth,
                                                        fiducialCenters['top_right'][0]-halfwidth:fiducialCenters['top_right'][0]+halfwidth]][0]
    fiducialCenters_images['bot_right'] = [img4template[fiducialCenters['bot_right'][1]-halfwidth:fiducialCenters['bot_right'][1]+halfwidth,
                                                        fiducialCenters['bot_right'][0]-halfwidth:fiducialCenters['bot_right'][0]+halfwidth]][0]
    fiducialCenters_images['bot_left'] = [img4template[fiducialCenters['bot_left'][1]-halfwidth:fiducialCenters['bot_left'][1]+halfwidth,
                                          fiducialCenters['bot_left'][0]-halfwidth:fiducialCenters['bot_left'][0]+halfwidth]][0]

    # Create a figure with the 4 fiducials
    x = 0
    y = 0
    fig, axs = plt.subplots(2, 2, figsize=(6, 6))
    for corner_image in corner_list:
        axs[x, y].imshow(fiducialCenters_images[corner_image],
                         cmap=plt.cm.gray)
        axs[x, y].set_title(corner_image)
        x = x + 1
        if x == 2:
            x = 0
            y = 1

    # save templates as images
    i = 1
    for corner_image in corner_list:
        template_name = 'Template_' + dataset + \
            "_" + corner_image + '_' + str(i) + '.tif'
        while os.path.exists(output_template_folder + "/" + template_name):
            i = i+1
            template_name = 'Template_' + dataset + \
                "_" + corner_image + '_' + str(i) + '.tif'

        corner_image_name = output_template_folder + "/" + template_name
        cv2.imwrite(corner_image_name, fiducialCenters_images[corner_image])

    # create an associated     txt file
    f = open(output_template_folder + '/' +
             "Center_Fiduciales.txt", "a", newline='')
    w = csv.writer(f, delimiter=" ")
    for corner_image in corner_list:
        template_name = 'Template_' + dataset + "_" + \
            corner_image + '_' + str(i)  # + '.tif'
        line = [[template_name, str(halfwidth), str(halfwidth)]]
        w.writerows(line)
    f.close()


if __name__ == '__main__':
    fiducialTemplateCreator(image4template_path,output_template_folder,
                            fiducialCenters, halfwidth, dataset)
