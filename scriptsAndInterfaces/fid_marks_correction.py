# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:34:15 2022

@author: Amelie Maginot ENSG(Ecole national des sciences geographiques)
"""

import pandas as pd
import cv2

def Main_correction_fid_marks(dataset,path):
    
    fidFile = pd.read_csv(path+'/_fiducial_marks_coordinates_'+dataset+'.csv',sep=",").copy()
    print('\n',fidFile)
    correctfidFile = pd.read_csv(path+'/_fiducial_marks_coordinates_'+dataset+'_Checked.csv',sep=",")

    newfidFile   = path+'/new_fiducial_marks_coordinates_'+dataset+'.csv'
    
    columns = list(correctfidFile.columns)
    
    for i in range(len(fidFile['name'])):
    
        imgName = fidFile.iloc[i]['name'] # get image name
        print('\n------------------------------------------\n',imgName)
        fid = fidFile.loc[i]
        
        # find the checked corner
        L = [correctfidFile.iloc[i] for i in range(len(correctfidFile['image'])) if correctfidFile.iloc[i]['image'] in imgName]
        D = pd.DataFrame(columns=columns)
        for l in L:
            D = D.append(l)
        print(D)
        # update the image fid marks coordinate
        for d in range(len(D)):
            fid = correct_fid(fid,D.iloc[d].to_dict(),imgName,path)
            
        # update the current image line
        new_line =pd.DataFrame(dict(fid), index = [i])
        fidFile.update(new_line)
        
    # save new_file
    fidFile.to_csv(newfidFile, mode='w', header=list(fidFile.columns), sep=",", index=False)  # append to file
    

def correct_fid(fid,correction,imgName,path):
    # print(correction['corner'])
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
        
        print("h, w",h,w)
        print("corner H, w :",cornerH,cornerW)
        print("top left avant : ",fid['X1'],fid['Y1'])
        print("bot left avant : ",fid['X4'],fid['Y4'])
        fid['X4'] = x
        fid['Y4'] = h - cornerH + y
        
        print("bot left avant : ",fid['X4'],fid['Y4'])
        # print(fid)    
    return fid

if __name__ =='__main__':
    Path = r'D:\ENSG_internship_2022\Burundi_1981-82\New folder\01_CanvasSized'
    dataset = 'Burundi_1981-82'
    
    Main_correction_fid_marks(dataset,Path)
    