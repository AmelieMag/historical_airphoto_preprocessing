# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 09:28:09 2022

@author: AmelieMaginot
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys, os

"""
l'objectif de se script est de valider l'utilisation de l'application GAPP à la 
place d'un traitement manuel long et fastidieu 
"""
print('\n')
## import files 

maison = "J"
musee = "F"

serie = 2

# lieu = maison
lieu = musee

# dataset = 'Burundi_1981-82'
# dataset = 'Usumbura1955'
dataset = 'Usumbura_1957-58-59'

# file = r'{}:\2_SfM_READY_photo_collection\Usumbura_1955' #.format(lieu,dataset)
file = r'{}:\2_SfM_READY_photo_collection\{}/GAPP'.format(lieu,dataset)

refFile = r'{}/{}_FidMarks_CSV.csv'.format(file,dataset)
# refFile =  r'{}/GAPP/Burundi_1981-82_FidMarks_Excel2_complete.csv'.format(file)


testFile =  r'{}/test{}/01_CanvasSized/_fiducial_marks_coordinates_{}.csv'.format(file,serie,dataset)
tobeCheck =  r'{}/test{}/01_CanvasSized/_fiducial_marks_coordinates_{}_ToBeChecked.csv'.format(file,serie,dataset)


if serie == 1:
    testFile =  r'{}/GAPP/test1/01_CanvasSized/_fiducial_marks_coordinates_{}.csv'.format(file,dataset)
    tobeCheck =  r'{}/GAPP/test1/01_CanvasSized/_fiducial_marks_coordinates_{}_ToBeChecked.csv'.format(file,dataset)
    
if serie == 3:
    testFile =  r'{}/GAPP/test3/_fiducial_marks_coordinates_{}.csv'.format(file,dataset)
    tobeCheck =  r'{}/GAPP/test3/_fiducial_marks_coordinates_{}_ToBeChecked.csv'.format(file,dataset)

if serie == 4:
    testFile =  r'{}/GAPP\test4\01_CanvasSized/_fiducial_marks_coordinates_{}.csv'.format(file,dataset)
    tobeCheck =  r'{}/GAPP\test4\01_CanvasSized/_fiducial_marks_coordinates_{}_ToBeChecked.csv'.format(file,dataset)




print('refFile = ',refFile)
print('testFile = ', testFile)
print('tobeCheck = ', tobeCheck,"\n")

# print('\n',os.listdir(file+'/GAPP/01_CanvasSized/_fiducial_marks_coordinates_Burundi_1981-82.csv'))

# read csv avec pandas

with open(refFile) as f:
    ref = pd.read_csv(f)
    
with open(testFile) as f:
    test = pd.read_csv(f, sep=';')
  
with open(tobeCheck) as f:
    toCheck = pd.read_csv(f, sep=',')
    
# print(ref)
# print(test)
# print(toCheck)


## functions


def distance(A,B):
    x = (A[0]-B[0])**2
    y = (A[1]-B[1])**2
    return round( np.sqrt(x+y))

# test

listdist = []
count = {}
listcoin = [] 



for i in range(len(ref.index)):
    # print("i=",ref.loc[i])
    # print(ref.loc[i])
    # print(test.loc[i])
    # print(ref.loc[i]['PHOTO_ID'] in toCheck.loc[i]['name'])
    
    top_left_ref = [ref.loc[i]['Xp1'],ref.loc[i]['Yp1']] 
    top_right_ref = [ref.loc[i]['Xp2'],ref.loc[i]['Yp2']] 
    bot_right_ref = [ref.loc[i]['Xp3'],ref.loc[i]['Yp3']] 
    bot_left_ref = [ref.loc[i]['Xp4'],ref.loc[i]['Yp4']] 
    
    top_left_test = [test.loc[i]['X1'],test.loc[i]['Y1']] 
    top_right_test = [test.loc[i]['X2'],test.loc[i]['Y2']] 
    bot_right_test = [test.loc[i]['X3'],test.loc[i]['Y3']] 
    bot_left_test = [test.loc[i]['X4'],test.loc[i]['Y4']] 
    
    top_left_dist = distance(top_left_ref,top_left_test),'top_left'
    top_right_dist = distance(top_right_ref, top_right_test),'top_right'
    bot_right_dist = distance(bot_right_ref, bot_right_test),'bot_right'
    bot_left_dist = distance(bot_left_ref, bot_left_test),'bot_left'
    
    corners_dist = [list(top_left_dist),list(top_right_dist),list(bot_right_dist),list(bot_left_dist)]
    for c in corners_dist:
        listcoin.append ([ref.loc[i]['PHOTO_ID']]+c)
    listdist += corners_dist
 
# on cherche les coins tres problematique
n=0
l1=200
cointresproblematique = []
for i in range(len(listcoin)):
    # print(listcoin[i][1])
    if listcoin[i][1]>=l1:
        n+=1
        cointresproblematique.append(listcoin[i])
        
print("nbr de coins dont la distance est superieur à ",l1 ," : ",n)

# On verifi si les coins problematiques sont dans la liste des coins a verifier
# print('len problem = ',len(cointresproblematique))
print("\ncoins tres problematiqus")
for i in cointresproblematique:
    b = False
    for j in range(len(toCheck)):
        if i[0] in toCheck.loc[j]['image']:
            b = True
    # print(i,b)
    

listdist = sorted(listdist)
c = 0
m=[]
lgraphmax=100
lgraphmin=0
for d in listdist:
    d= d[0]
    
    if d < lgraphmax and lgraphmin<d:
        m.append(d)
        if d in count:
            count[d]=count[d]+1    
        else:
            count[d]=1
    else:
        c+=1

print("nbr de coin compte : ",len(listdist)-c, 'soit ',(len(listdist)-c)*100/len(listdist),'%' )
print('   ',c," coin non compte ", ' sur ',len(listdist) ,'soit',round( c*100/len(listdist),1),'%\n')   # nbr de coin non compte

print ("Sur la selection :")
print("sum = ", sum(list(count.values())))
print("moy =", np.mean(m))
print("ecarttype = ",np.std(m))
print('nbr image = ',int(len(listdist)/4))
print('\n')

plt.title('nbr de coin par distance {}<d<{} \necart type: {}'.format(lgraphmin,lgraphmax,np.std(m)))
plt.scatter(list(count.keys()),list(count.values()))
plt.show()

n=0
l2=30
listCoin=[]
for coin in listcoin:
    b=False
    d=coin[1]
    if d>l2 :#and d<50:
        n+=1
        listCoin.append(coin)
print('il y a __',n,'__ coins dont la distance est superieur à ',l2 )


inToCheck=0
for coin in listCoin:
    b=False
    for j in range(len(toCheck)):
        if coin[0] in toCheck.loc[j]['image'] and coin[2] in toCheck.loc[j]['corner']:
            inToCheck+=1
            b = True
    if not b:
        print(coin, b)

print("nbr de coin dans toCheck",inToCheck,"sur",len(listCoin),"coins\n")
# print(toCheck)