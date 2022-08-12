# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:34:15 2022

@author: Amelie Maginot ENSG(Ecole national des sciences geographiques)
"""

import os, sys

absFilePath = os.path.abspath(__file__)
filepath, filename = os.path.split(absFilePath)

sys.path.insert(0, '{}/scriptsAndInterfaces'.format(filepath))  # Local imports

from zoom_and_move_app import check_corners

def check(dataset,path):
    Path =path+'/cornerToCheck'
    listImage = os.listdir(Path)
    i=0
    
    for img in listImage:
        i+=1
        txt = 'checking {} fiducial mark [{} out of {}]'.format(img,i,len(listImage))
        check_corners(dataset,Path,img,txt)

def correct_fid(fid,correction,img):
    
    imgW, imgH = img.shape[0],img.shape[1] #get image size
    
    cornerW = correction['corner width'] # get corner width
    cornerH = correction['corner height'] # get corner height
    
    # correct the fid file
    if correction['corner']== 'top_left':
        fid['x']=correction['x']
        fid['y']=correction['y']
        
    elif correction['corner']== 'top_right':
        fid['x']=imgW-cornerW+correction['x']
        fid['y']=correction['y']
        
    elif correction['corner']== 'bot_right':
        fid['x']=imgW-cornerW+correction['x']
        fid['y']=imgH-cornerH+correction['y']
        
    elif correction['corner']== 'bot_left': 
        fid['x']=correction['x']
        fid['y']=imgH-cornerH+correction['y'] 

if __name__ =='__main__':
    dataset = 'Usumbura_1957-58-59'
    # path = r'D:\ENSG_internship_2022\Burundi_1981-82\test8\01_CanvasSized'
    path = r'C:\Users\AmelieMaginot\Documents\ING_2\StageMRAC\testzoom1\01_CanvasSized'
    
    check(dataset,path)
    