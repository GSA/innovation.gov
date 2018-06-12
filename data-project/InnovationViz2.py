# -*- coding: utf-8 -*-
#First version of visualization of Innovation in Government
#June 12, 2018

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show, output_notebook, output_file
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.palettes import Spectral11

innovation=pd.read_excel('WhereisInnovationFixed.xlsx')

depts=innovation.Department.value_counts()

#Generate a list of departments, with each agency taking up one row, so that a
#department with 5 agencies appears 5 times

deptList=[]

for y in range(len(depts)):
    for x in range(depts[y]):
        deptList.append(depts.index[y])

#Newer Form will have the data in a form we can use, sorted by department
newerForm=pd.DataFrame(index=deptList,columns=['dept','firstTime','deptNum','agencyNum','Agency','Initiative','Type','Color','WhatMakes'])

#agencyNums is the number of agencies in a given department. It starts blank,
#but the code fills it in
agencyNums={}

for rowNum in range(len(innovation.index)):
    thisDept=innovation.iloc[rowNum, 4]

#This codes fills in agencyNums and identifies the first time a Department appears
    if thisDept in agencyNums.keys():
        agencyNums[thisDept]+=1
        firstTime=0
    else:
        agencyNums[thisDept]=1
        firstTime=1
        
#If the department is filled in, assign it a number, so that all agencies
#in a given department will appear in the same row (Y location).
#And give every initiative a unique number for its X location.
    if type(thisDept)==str:
        deptNum=list(depts.index).index(thisDept)
        #NFrow is the row an initiatve will be in the newerForm
        NFrow=list(newerForm.index).index(thisDept)+agencyNums[thisDept]-1
        initType=innovation.iloc[rowNum,-3]
 
       #Group filled iniative types by the first four letters, or None
        if type(initType)==str:
            initTypeFF=initType[:4]
        else:
            initTypeFF='None'
            
        #Fill in the values for NewerForm
        newerForm.iloc[NFrow]=[thisDept,firstTime,-deptNum,agencyNums[thisDept],innovation.iloc[rowNum,5],innovation.iloc[rowNum,0],initType,initTypeFF,innovation.iloc[rowNum,-1]]

#Replace the initiative type with the color code
newerForm.Color=newerForm.Color.map(lambda initTypeFF: Spectral11[min(10,list(newerForm.Color.value_counts().index).index(initTypeFF))])
 
p = figure(plot_width = 700, plot_height = 780, 
           title = 'Innovation in Government')
p.x_range.end=55

#Only build a legend for the first time a Department appears
p.circle(x='agencyNum',y='deptNum',color='Color', legend='dept', source=ColumnDataSource(newerForm.loc[lambda df:df.firstTime==1]))

p.circle(x='agencyNum',y='deptNum',color='Color', source=ColumnDataSource(newerForm.loc[lambda df:df.firstTime==0]))

p.legend.label_text_font_size='8pt'

#Add a hover tool
hover = HoverTool(tooltips=[("Department","@dept"),("Agency","@Agency"),("Initiative","@Initiative"),("Type","@Type"),("What makes this innovative?","@WhatMakes")])
p.add_tools(hover)

output_file('innovation_data.html')
show(p)