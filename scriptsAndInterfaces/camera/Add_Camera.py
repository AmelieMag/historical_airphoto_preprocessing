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

resolution_high = 2400
resolution_low = 900

lenth_u_x =18
FMx = 16.5

lenth_u_y =18
FMy = 16.5

unity = "cm"

# ------------------------------------------------------------------------------
############################## END OF SETUP ###################################
# ------------------------------------------------------------------------------


def add_camera(camera, resh, resl, Lux,Luy,FMux,FMuy,u):

    
    if __name__ != "__main__":

        # getting the variable from interface
        
        print(FMux,FMux.get())
        camera = camera.get()
        resh = resh.get()
        resl = resl.get()
        Lux = Lux.get()
        Luy = Luy.get()
        FMux = FMux.get()
        FMuy = FMuy.get()
        u = u.get()

    # get path and name of the script
    path, filename = os.path.split(os.path.abspath(__file__))

    # Adding the name of the new camera to the camera name file
    L = (';{}'.format(camera))
    with open(r"{}/camera.txt".format(path), "a") as f:
        f.write(L)

    # conversion
    
    # list resolution 
    
    res = []
    for r in range(resl,resh+100,100):
        res.append(r)
    
    # res = np.array(res)
    lpx = []
    lpy = []
    
    FMpx = []
    FMpy = []
    
    # choose unity
    
    if u == "inche":
        for i in range( len(res)):
            lpx.append(round(Lux*res[i]))
            lpy.append(round(Luy*res[i]))
            
            FMpx.append(round(FMux*res[i]))
            FMpy.append(round(FMuy*res[i]))
            
    elif u =="cm":
        for i in range( len(res)):
            lpx.append(round((Lux/2.54)*res[i]))
            lpy.append(round((Luy/2.54)*res[i]))
            
            FMpx.append(round((FMux/2.54)*res[i]))
            FMpy.append(round((FMuy/2.54)*res[i]))
            
            
        
    lpx = np.array(lpx)
    FMpx = np.array(FMpx)
    
    lpy = np.array(lpy)
    FMpy = np.array(FMpy)

    # calculating the coordinate of fiducial marks in pixels
    fm_centerx = (lpx - FMpx)/2
    fm_CENTERx = fm_centerx + FMpx
    
    fm_centery = (lpy - FMpy)/2
    fm_CENTERy = fm_centery + FMpy

    fm_centerx = [int(i) for i in fm_centerx]
    fm_CENTERx = [int(i) for i in fm_CENTERx]
    
    fm_centery = [int(i) for i in fm_centery]
    fm_CENTERy = [int(i) for i in fm_CENTERy]

    # creating csv with pandas
    file = pd.DataFrame({"Resolution": pd.Series(res),
                         "X ximension (pixel)": pd.Series(lpx),
                         "Y dimension (pixel)": pd.Series(lpy),
                         "X distance between FM": pd.Series(FMpx),
                         "Y distance between FM": pd.Series(FMpy),
                         "Xp1": fm_centerx,
                         "Yp1": fm_centery,
                         "Xp2": fm_CENTERx,
                         "Yp2": fm_centery,
                         "Xp3": fm_CENTERx,
                         "Yp3": fm_CENTERy,
                         "Xp4": fm_centerx,
                         "Yp4": fm_CENTERy,
                         })

    # creating csv with ";" as separator
    file.to_csv("{}/{}_Airphoto_Photo_dimensions_vs_dpi.csv".format(path,
                camera), sep=';', index=False)


if __name__ == "__main__":
    add_camera(camera_name, resolution_high,resolution_low, lenth_u_x,lenth_u_y,FMx,FMy,unity)
