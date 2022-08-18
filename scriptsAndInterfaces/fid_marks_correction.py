# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:34:15 2022

@author: Amelie Maginot ENSG(Ecole national des sciences geographiques)
"""

import pandas as pd
import cv2

def Main_correction_fid_marks(dataset,path):
    
    fidFile = pd.read_csv(path+'/_fiducial_marks_coordinates_'+dataset+'.csv',sep=",")
    print(fidFile)
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
            fid = correct_fid(fid,D.iloc[d].to_dict(),imgName,path)
            
        # update the current image line
        new_line =pd.DataFrame(dict(fid), index = [i])
        fidFile.update(new_line)
        
    # save new_file
    fidFile.to_csv(newfidFile, mode='w', header=list(fidFile.columns), sep=",", index=False)  # append to file
    

def correct_fid(fid,correction,imgName,path):
    print( correction['corner'])
    img = cv2.imread(path+'/'+imgName+'.tif')
    
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
    Path = r'F:\2_SfM_READY_photo_collection\Usumbura_1957-58-59\GAPP\test13\traitement\01_CanvasSized'
    dataset = 'Usumbura_1957-58-59'
    
    Main_correction_fid_marks(dataset,Path)
    