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
    
    for img in listImage:
        check_corners(dataset,Path,img)

def correct_fid(fid,correction,img):
    
    # trouver  la taille du coin fr
    
    w, h = img.shape[0],img.shape[1]
    if correction['corner']== 'top_left':
        fid['x']=correction['x']
        
        fid['y']=correction['y']
    elif correction['corner']== 'top_right':
        
        fid['x']=w -2500+correction['x']
        fid['y']=correction['y']
        
    elif correction['corner']== 'bot_right':
        
        fid['x']=correction['x']
        fid['y']=correction['y']
        
    elif correction['corner']== 'bot_left': 
        fid['x']=correction['x']  
        fid['y']=correction['y'] 

if __name__ =='__main__':
    dataset = 'Burundi_1981-82'
    path = r'D:\ENSG_internship_2022\Burundi_1981-82\test8\01_CanvasSized'
    
    check(dataset,path)
    