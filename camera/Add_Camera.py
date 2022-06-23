# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:54:32 2022

@author: Amelie Maginot
        Ecole nationale des sciences geographique
"""
import os
import pandas as pd
import numpy as np

# ------------------------------------------------------------------------------
################################## SETUP ######################################
# ------------------------------------------------------------------------------

camera_name = 'wild_test'
resolution = [1500, 1400]
total_lenth = [10630, 9921]
lenth_FM = [9744, 9094]

# ------------------------------------------------------------------------------
############################## END OF SETUP ###################################
# ------------------------------------------------------------------------------


def add_camera(camera, res, tot_l, l_FM):

    if __name__ != "__main__":

        # getting the variable from interface
        camera = camera.get()
        resolution = []
        lenth_tot = []
        FMs = []
        for r in res:
            resolution.append(r.get())
        for t in tot_l:
            lenth_tot.append(t.get())
        for f in l_FM:
            FMs.append(f.get())

        res = resolution
        tot_l = lenth_tot
        l_FM = FMs

    # get path and name of the script
    path, filename = os.path.split(os.path.abspath(__file__))

    # Adding the name of the new camera to the camera name file
    L = (';{}'.format(camera))
    with open(r"{}/camera.txt".format(path), "a") as f:
        f.write(L)

    # creating csv with pandas

    tot_l = np.array(tot_l)
    l_FM = np.array(l_FM)

    # calculating the coordinate of fiducial marks
    fm_center = (tot_l - l_FM)/2
    fm_CENTER = fm_center + l_FM

    fm_center = [int(i) for i in fm_center]
    fm_CENTER = [int(i) for i in fm_CENTER]

    file = pd.DataFrame({"Resolution": pd.Series(res),
                         "X ximension (pixel)": pd.Series(tot_l),
                         "Y dimension (pixel)": pd.Series(tot_l),
                         "X distance between FM": pd.Series(l_FM),
                         "Y distance between FM": pd.Series(l_FM),
                         "Xp1": fm_center,
                         "Yp1": fm_center,
                         "Xp2": fm_CENTER,
                         "Yp2": fm_center,
                         "Xp3": fm_CENTER,
                         "Yp3": fm_CENTER,
                         "Xp4": fm_center,
                         "Yp4": fm_CENTER,
                         })

    # creating csv with ";" as separator
    file.to_csv("{}/{}_Airphoto_Photo_dimensions_vs_dpi.csv".format(path,
                camera), sep=';', index=False)


if __name__ == "__main__":
    add_camera(camera_name, resolution, total_lenth, lenth_FM)
