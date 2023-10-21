#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Importing modules

import os
import csv
import pandas as pd


# In[ ]:


#Reading the data with Panda

df =pd.read_csv(budget_csv)


# In[ ]:


#Get variables in path

budget_csv=os.path.join('..','PyBank','Resources','budget_data.csv')


# In[12]:


#counting months

number_of_months=len("df")
print("Total months: ",number_of_months)


# In[ ]:


#Total of profit/losses

total_amount=sum(df["Profit/Losses"])
print("Total: ",total_amount)


# In[ ]:


#Calculating mean"avg"change profit/losses

average_change=total_amount/number_of_months
print("Average Change: ",average_change)


# In[ ]:


#Calculating avg "mean"change profit/losses

greatest_increase=max(df["Profit/Losses"])
print("Greatest Increase in Profit: ",greatest_increase)


# In[ ]:


#Calculating avg change profit/losses

greatest_decrease=min(df["Profit/Losses"])
print("Greatest Decrease in Profit: ",greatest_decrease)

