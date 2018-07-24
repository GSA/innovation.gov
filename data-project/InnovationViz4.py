# -*- coding: utf-8 -*-
#Second version of visualization of Innovation in Government
#June 25, 2018

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import show, output_file, reset_output
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.palettes import Spectral11


innovation=pd.read_excel('WhereisInnovationFixed2.xlsx')
innovation.fillna(value='Not Specified')

def make_dataset(raw_data):
    depts=raw_data.Department.value_counts()

#Newer Form will have the data in a form we can use, sorted by department
    newerForm=pd.DataFrame(index=raw_data.index,columns=['dept','firstTime','deptNum','agencyNum','initNum','Agency','Initiative','Type','Color','Transformation','WhatMakes'])

#agencyNums is the number of agencies in a given department. It starts blank,
#but the code fills it in
    agencyNames={}
    initNums={}

    for rowNum in range(len(raw_data.index)):
        thisDept=raw_data.iloc[rowNum, 4]
        thisAgency=raw_data.iloc[rowNum, 5]

#This codes fills in agencyNums and identifies the first time a Department appears
        if thisDept in agencyNames.keys():
            if thisAgency in agencyNames[thisDept]:
                initNums[(thisDept,thisAgency)]+=1
            else:
                agencyNames[thisDept].append(thisAgency)
                initNums[(thisDept,thisAgency)]=1
            firstTime=0
        else:
            agencyNames[thisDept]=[thisAgency]
            initNums[(thisDept,thisAgency)]=1
            firstTime=1
        
#If the department is filled in, assign it a number, so that all agencies
#in a given department will appear in the same row (Y location).
#And give every initiative a unique number for its X location.
        if type(thisDept)==str:
            deptNum=5*list(depts.index).index(thisDept)
            #oddDept is used to stagger the first agency in each row
            oddDept=deptNum%2
            agencyNum=agencyNames[thisDept].index(thisAgency)
        #NFrow is the row an initiatve will be in the newerForm
            initType=raw_data.iloc[rowNum,-3]
 
       #Group filled iniative types by the first four letters, or None
            if type(initType)==str:
                initTypeFF=initType[:4]
            else:
                initTypeFF='None'
            
        #Fill in the values for NewerForm
        initNum=initNums[(thisDept,thisAgency)]
        newerForm.iloc[rowNum]=[thisDept,firstTime,-deptNum,2.5*(agencyNum+oddDept),0.15*initNum,raw_data.iloc[rowNum,5],raw_data.iloc[rowNum,0],initType,initTypeFF,raw_data.iloc[rowNum,-2],raw_data.iloc[rowNum,-1]]

    #Replace the initiative type with the color code
    newerForm.Color=newerForm.Color.map(lambda initTypeFF: Spectral11[min(10,list(newerForm.Color.value_counts().index).index(initTypeFF))])

    return newerForm
     
def make_plot(data_source):
    newForm=make_dataset(data_source)
    p = figure(plot_width = 1250, plot_height = 710, title = 'Innovation in Government')
    p.x_range.end=55

    #Only build a legend for the first time a Department appears
    p.circle(x='agencyNum',y='deptNum',radius='initNum',color='Color', source=ColumnDataSource(newForm.loc[lambda df:df.firstTime==0].iloc[::-1]))
    p.circle(x='agencyNum',y='deptNum',radius='initNum', color='Color', legend='dept', source=ColumnDataSource(newForm.loc[lambda df:df.firstTime==1].sort_values(by='deptNum',axis=0,ascending=False)))

    p.legend.label_text_font_size='15pt'

    #Add a hover tool
    hover = HoverTool(tooltips=[("Department","@dept"),("Agency","@Agency"),("Initiative","@Initiative"),("Type","@Type"),("Transformation Element","@Transformation"),("What makes this innovative?","@WhatMakes")])
    p.add_tools(hover)

    return(p)

#creates the graphic
def init_graph():
    reset_output()
    p=make_plot(innovation)
    output_file('innovation_data2.html')
    show(p)

init_graph()

#saves the Dataset for Tableau to use
newForm=make_dataset(innovation)
newForm.to_csv('newInnovation.csv')