# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:34:15 2022

@author: Amelie Maginot ENSG(Ecole national des sciences geographiques)
"""

import pandas as pd
import cv2

from GAPP_Script_03_AirPhoto_Reprojection_v201 import main_script_03

def Main_correction_fid_marks(dataset,path,p,black_stripe_location):
    
    fidFile = pd.read_csv(path+'/_fiducial_marks_coordinates_'+dataset+'.csv',sep=",", encoding='utf-8').copy()
    print('\n',fidFile)
    correctfidFile = pd.read_csv(path+'/_fiducial_marks_coordinates_'+dataset+'_Checked.csv',sep=",")

    newfidFile   = path+'/new_fiducial_marks_coordinates_'+dataset+'.csv'
    
    columns = list(correctfidFile.columns)
    
    for i in range(len(fidFile['name'])):
    
        imgName = fidFile.iloc[i]['name'] # get image name
        print(imgName)
        fid = fidFile.loc[i]
        
        # find the checked corner
        L = [correctfidFile.iloc[i] for i in range(len(correctfidFile['image'])) if correctfidFile.iloc[i]['image'] in imgName]
        D = pd.DataFrame(columns=columns)
        for l in L:
            D = D.append(l)
            
        # update the image fid marks coordinate
        for d in range(len(D)):
            fid = correct_fid(fid,D.iloc[d].to_dict(),imgName,path,p,black_stripe_location)
            
        # update the current image line
        new_line =pd.DataFrame(dict(fid), index = [i])
        fidFile.update(new_line)
        
    # save new_file
    fidFile.to_csv(newfidFile, mode='w', header=list(fidFile.columns), sep=",", index=False)  # append to file
    print(fidFile)

def correct_fid(fid,correction,imgName,path,p,black_stripe_location):
    
    img = cv2.imread(path+'/'+imgName+'.tif')
    
    cornerW = correction['corner width'] #get corner width
    cornerH = correction['corner height'] # get corner height
    
    x = correction['x']
    y = correction['y']
    
    
    h, w = img.shape[0],img.shape[1] # get image size 
    
    # correct fid coords
    if correction['corner']== 'top_left':
        fid['X1'] = x
        fid['Y1'] = y
    elif correction['corner']== 'top_right':        
        fid['X2'] = w - cornerW + x
        fid['Y2'] = y
        
    elif correction['corner']== 'bot_right':        
        fid['X3'] = w - cornerW + x
        fid['Y3'] = h - cornerH + y
        
    elif correction['corner']== 'bot_left': 
        fid['X4'] = x
        fid['Y4'] = h - cornerH + y
    
    # blac strip correctionpath_out_fold
    if 'top' in black_stripe_location:
        
        if correction['corner']== 'top_left': 
            fid['Y1'] = fid['Y1'] + h*p        
        if correction['corner']== 'top_right':
            fid['Y2'] = fid['Y2'] + h*p
        
    if 'bottom' in black_stripe_location:
        
        if correction['corner']== 'bot_right':
            fid['Y3'] = fid['Y3'] + h*p
        if correction['corner']== 'bot_left':
            fid['Y4'] = fid['Y4'] + h*p
        
    if 'left' in black_stripe_location:

        if correction['corner']== 'top_left': 
            fid['X1'] = fid['X1'] + w*p
        if correction['corner']== 'bot_left':
            fid['X4'] = fid['X4'] + w*p 
        
    if 'right' in black_stripe_location:
        
        if correction['corner']== 'top_right': 
            fid['X2'] = fid['X2'] - w*p
        if correction['corner']== 'bot_right':
            fid['X3'] = fid['X3'] - w*p
        
    return fid

if __name__ =='__main__':
    Path = r'C:\Users\AmelieMaginot\Documents\ING_2\StageMRAC\bot_left_issue\test2\01_CanvasSized'
    dataset = 'Burundi_1981-82'
    p=0.04
    stripes='left'
    Main_correction_fid_marks(dataset,Path,p,stripes)
    