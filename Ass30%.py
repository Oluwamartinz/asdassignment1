#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:30:45 2023

@author: macbookpro
"""
#importing dictionaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_excel(r'https://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=excel', sheet_name = 'Data')

#droping some columns not needed
df = df.drop(df.loc[:, 'Unnamed: 2':'Unnamed: 53'].columns,axis = 1)

#renaming the headers
df.rename({'Data Source':'Country Name','World Development Indicators':'Country Code', 'Unnamed: 54':'2010', 'Unnamed: 55':'2011', 'Unnamed: 56':'2012', 'Unnamed: 57':'2013', 'Unnamed: 58':'2014', 'Unnamed: 59':'2015', 'Unnamed: 60':'2016', 'Unnamed: 61':'2017', 'Unnamed: 62':'2018', 'Unnamed: 63':'2019', 'Unnamed: 64':'2020'}, axis=1, inplace=True)

df.drop(['Unnamed: 65'], axis=1,inplace=True)

df.drop([0,1,2], axis=0,inplace=True)

df = df.reset_index()

df.drop(['index'], axis=1,inplace=True)

Data = df.loc[[3,13,29,35,45,119,154,195,207,263,265], :]

Data = Data.reset_index()
Data.drop(['index'], axis=1,inplace=True)

Data.drop(['Country Code'], axis=1,inplace=True)

#renaming and replacing the serial number with country names
Data.rename({"Country Name":'Serial Number'}, axis=1, inplace=True)

R = Data.T

headers = R.iloc[0]
R = pd.DataFrame(R.values[1:], columns=headers)

#Inserting the year column with the years needed
R.insert(0, "Year", ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'], True)


#Defining function for line plot
def plt_plot(x, y, title, label, color, xaxes, yaxes):
    
    '''

    Here i defined the function for the line plot with the following parameters:
    
    x : The years we are plotting on the x-axis
    y: The list of countries trimmed for the line plot to be displayed on the y-axis
    title : This is the title of the line plot
    label : These are the different labels
    color : Shows the different colour codes of the line plot
    xaxes : shows the x-axis
    yaxes : shows the y-axis

    '''
    
    plt.figure(figsize=(10,6))
    plt.title(title, fontweight="bold")
    
    for i in range(len(y)):
        plt.plot(x, y[i], label=label[i], color=color[i])
    
    plt.xlabel(xaxes)
    plt.ylabel(yaxes)
    plt.legend(loc='best')
    plt.show()
    
    return
x = R["Year"]
y = [R["Africa Western and Central"],R["Australia"],R["Brazil"],R["Canada"],R["Colombia"],R["Japan"],R["Mexico"],R["Paraguay"],R["Senegal"],R["South Africa"],R["Zimbabwe"]] 
title = ('Line plot of Access to electricity rate among selected countries ')
label = ["AFW", "AUS", "BRA", "CAN", "COL", "JPN", "MEX", "PRY", "SEN", "ZAF", "ZIM"]
color = ['red','blue','green','yellow', 'black', 'purple', 'brown', 'pink', 'indigo', 'orange', 'violet']
x_label = "Years"
y_label = "Access to electricity rate"

plt_plot(x, y, title, label, color, x_label, y_label)


#Defining function for bar chat
def plt_bar(x, y, title, label, color, xaxes, yaxes):
    
    '''

    Here i defined the function for the bar plot with the following parameters:
    
    x : The years we are plotting on the x-axis
    y : The list of countries trimmed for the bar plot to be displayed on the y-axis
    title : This is the title of the bar plot
    label : These are the different labels
    color : Shows the different colour codes of the line plot
    xaxes : shows the x-axis
    yaxes : shows the y-axis

    '''
    
    plt.figure(figsize=(10,6))
    index = np.arange(len(x))
    
    
    for i in range(len(y)):
        plt.bar(x, y[i], label=label[i], color=color[i])
    
    plt.xlabel(xaxes)
    plt.ylabel(yaxes)
    plt.legend(loc='best')
    plt.show()
    
    return
    
x = R["Year"]
y = [R["Africa Western and Central"],R["Australia"],R["Brazil"],R["Canada"],R["Colombia"],R["Japan"],R["Mexico"],R["Paraguay"],R["Senegal"],R["South Africa"],R["Zimbabwe"]] 
title = ('Access to electricity rate among selected countries')
label = ["AFW", "AUS", "BRA", "CAN", "COL", "JPN", "MEX", "PRY", "SEN", "ZAF", "ZIM"]
color = ['red','blue','green','yellow', 'black', 'purple', 'brown', 'pink', 'indigo', 'orange', 'violet']
x_label = "Years"
y_label = "Access to electricity rate"

plt_bar(x, y, title, label, color, x_label, y_label)

x = R["Year"]
y = R["Africa Western and Central"] 
x_label = "Years"
y_label = "Access to electricity rate"
plt.scatter(x,y)
plt.xlabel('Years')
plt.ylabel('Rate of access to Electricity')
plt.title('Access to electricity rate in West Central Africa')
plt.plot()
plt.show()
