# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:34:15 2022

@author: Amelie Maginot ENSG(Ecole national des sciences geographiques)
"""

import os
import pandas as pd
import cv2


def Main_correction_fid_marks(dataset,path):
    i=0
    
    fidFile = pd.read_csv(path+'/_fiducial_marks_coordinates_'+dataset+'.csv',sep=";").copy()
    correctfidFile = pd.read_csv(path+'/_fiducial_marks_coordinates_'+dataset+'_Checked.csv',sep=",")

    newfidFile   = path+'/new_fiducial_marks_coordinates_'+dataset+'.csv'
    
    imgName=os.listdir(path)[0]
    
    header = list(fidFile.columns)
    
    # create a new fid mark folder
    # TODO : make it rewrite the fid marks csv file
    for a in  fidFile.index:
        imgName = fidFile.loc[a]['name']
        fid=fidFile.loc[a]
        for i in range(len(correctfidFile)):
            correction={}
            if (correctfidFile.iloc[i]['image'] in imgName):
                correctionf = correctfidFile.iloc[i].to_dict()
                correction = correct_fid(fid,correctionf,imgName+'.tif',path)
                
        fidFile.loc[a]=  correction
            
    fidFile.to_csv(newfidFile, mode='w', header=header,sep=",", index=True)
    

def correct_fid(fid,correction,imgName,path):
    print(imgName)
    img = cv2.imread(path+'/'+imgName)
    
    cornerW = correction['corner width'] #get corner width
    cornerH = correction['corner height'] # get corner height
    
    w, h = img.shape[0],img.shape[1] # get image size 
    
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
        
    return fid

if __name__ =='__main__':
    dataset = 'Usumbura_1957-58-59'
    path = r'D:\ENSG_internship_2022\Burundi_1981-82\test10\01_CanvasSized'
    
    Main_correction_fid_marks(dataset,path)
    