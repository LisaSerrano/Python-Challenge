#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dependencies 

import os
import csv


# In[7]:


#Upload files

pypoll_csv = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')


# In[8]:


#variable

total_votes = 0

total_candidates=0

candidate_votes=0

candidate_1_votes=0

candidate_2_votes=0

candidate_3_votes=0


# In[9]:


#Making list

candidates=[]

candidates_index=[0,1,2]


# In[ ]:


#Read into the CSV File

open(py_poll_csv, newline='') as csvfile:

csvreader = csv.reader(csvfile, delimiter=',')


# In[ ]:


#Skip header row

next(csvreader)


# In[ ]:


#Loop through file

for row in csvreader:

#Set the number of ballots equal to the row number

ballot=row

#Count number of total votes

total_votes += 1



# In[ ]:


#Capturing names and replace candidates with candidate_name

if row[2] not in candidates:

candidates.append(row[2])

#Count the votes for candidate 1

if row[2]==candidates[0]:

candidate_1_votes+=1

if row[2]==candidates[1]:

candidate_2_votes+=1

if row[2]==candidates[2]:

candidate_3_votes+=1

candidate1rate=round(candidate_1_votes/total_votes*100,3)

print(candidates[0],":", candidate1rate, "% (",candidate_1_votes,")")

print(candidate_2_votes)

print(candidate_3_votes)


# In[ ]:




