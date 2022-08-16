# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:34:15 2022

@author: Amelie Maginot ENSG(Ecole national des sciences geographiques)
"""

import os, sys
import pandas as pd
import numpy as np
import cv2

from PIL import Image

absFilePath = os.path.abspath(__file__)
filepath, filename = os.path.split(absFilePath)

sys.path.insert(0, '{}/scriptsAndInterfaces'.format(filepath))  # Local imports

from zoom_and_move_app import check_corners

def check(dataset,path):
    Path =path+'/cornerToCheck'
    listImage = os.listdir(Path)
    
    # i=0
    # for img in listImage:
    #     i+=1
    #     text = '[{} out of {}] Correcting {} fiducial marks coordinate'.format(i,len(listImage),img)
    #     check_corners(dataset,Path,img,text)
    
    fidFile = pd.read_csv(path+'/_fiducial_marks_coordinates_'+dataset+'.csv',sep=";").copy()
    correctfidFile = pd.read_csv(path+'/_fiducial_marks_coordinates_'+dataset+'_Checked.csv',sep=",")

    newfidFile   = path+'/new_fiducial_marks_coordinates_'+dataset+'.csv'
    
    imgName=os.listdir(path)[0]
    
    F=fidFile.set_index('name')
    header = list(fidFile.columns)
    
    for a in  fidFile.index:
        imgName = fidFile.loc[a]['name']
        fid=fidFile.loc[a]
        for i in range(len(correctfidFile)):
            correction={}
            if (correctfidFile.iloc[i]['image'] in imgName):
                correctionf = correctfidFile.iloc[i].to_dict()
                correction = correct_fid(fid,correctionf,imgName+'.tif')
            
               
        fidFile.loc[a]=  correction
            
    fidFile.to_csv(newfidFile, mode='w', header=header,sep=",", index=True)
    
            
    

def correct_fid(fid,correction,imgName):
    print(imgName)
    img = cv2.imread(path+'/'+imgName)
    
    cornerW = correction['corner width'] #get corner width
    cornerH = correction['corner height'] # get corner height
    
    w, h = img.shape[0],img.shape[1] # get image size
    print(fid)
    # correct fid coords
    if correction['corner']== 'top_left':
        fid['X1'] = correction['x']
        fid['Y1'] = correction['y']
        
    elif correction['corner']== 'top_right':        
        fid['X2'] = w - cornerW + correction['x']
        fid['Y2'] = correction['y']
        
    elif correction['corner']== 'bot_right':        
        fid['X3'] = w - cornerW + correction['x']
        fid['Y3'] = h - cornerH + correction['y']
        
    elif correction['corner']== 'bot_left': 
        fid['X4']=correction['x']
        fid['Y4']= h - cornerH + correction['y']
    print(fid)
    return fid

if __name__ =='__main__':
    dataset = 'Usumbura_1957-58-59'
    path = r'J:\2_SfM_READY_photo_collection\Usumbura_1957-58-59\GAPP\testzoom1\01_CanvasSized'
    
    check(dataset,path)
    