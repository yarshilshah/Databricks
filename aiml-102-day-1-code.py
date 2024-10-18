#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#######################################################
#######################################################
############    COPYRIGHT - DATA SOCIETY   ############
#######################################################
#######################################################

## AIML 102 DAY 1/AIML 102 PART 1 ##

## NOTE: To run individual pieces of code, select the line of code and
##       press ctrl + enter for PCs or command + enter for Macs




# In[ ]:


#=================================================-
#### Slide 33: Exercise 1  ####






# In[ ]:


#=================================================-
#### Slide 50: Exercise 2  ####





# In[ ]:


#######################################################
#######################################################
############    COPYRIGHT - DATA SOCIETY   ############
#######################################################
#######################################################

## AIML 102 DAY 1/AIML 102 PART 2 ##

## NOTE: To run individual pieces of code, select the line of code and
##       press ctrl + enter for PCs or command + enter for Macs




# In[2]:


#=================================================-
#### Slide 2: Loading packages  ####

import pandas as pd
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt




# In[3]:


#=================================================-
#### Slide 3: Directory settings  ####

data_dir = "/home/jovyan/iqvia-aiml-102/data"




# In[4]:


#=================================================-
#### Slide 9: Load the dataset  ####

costa_rica_poverty = pd.read_csv(data_dir + '/costa_rica_poverty.csv')
print(costa_rica_poverty.head())




# In[5]:


#=================================================-
#### Slide 11: Subsetting data - cont'd  ####

costa_viz = costa_rica_poverty[['ppl_total', 'dependency_rate',
                               'num_adults', 'rooms', 'age', 'monthly_rent',
                               'Target']]
print(costa_viz.head())




# In[6]:


#=================================================-
#### Slide 12: Data prep: clean NAs  ####

print(costa_viz.isnull().sum())




# In[7]:


#=================================================-
#### Slide 13: Data cleaning: NAs  ####

# Set the dataframe equal to the imputed dataset.
costa_viz = costa_viz.fillna(costa_viz.mean())
# Check how many values are null in monthly_rent.
print(costa_viz.isnull().sum())




# In[8]:


#=================================================-
#### Slide 14: Converting the target variable  ####

costa_viz['Target'] = np.where(costa_viz['Target'] <= 3, 'vulnerable', 'non_vulnerable')
print(costa_viz['Target'].head())




# In[9]:


#=================================================-
#### Slide 15: Data prep: target  ####

print(costa_viz.Target.dtypes)
costa_viz["Target"] = np.where(costa_viz["Target"] == "non_vulnerable", True, False)

# Check class again.
print(costa_viz.Target.dtypes)




# In[10]:


#=================================================-
#### Slide 19: Prepare data: group and summarize - cont'd  ####

# Group data by `Target` variable.
grouped = costa_viz.groupby('Target')

# Compute mean on the listed variables using the grouped data.
costa_grouped_mean = grouped.mean()[['ppl_total','dependency_rate','num_adults','rooms','age']]
print(costa_grouped_mean)




# In[13]:


#=================================================-
#### Slide 20: Prepare data: group and summarize - cont'd  ####

# Reset index of the dataset.
costa_grouped_mean = costa_grouped_mean.reset_index()
print(costa_grouped_mean)




# In[14]:


#=================================================-
#### Slide 23: Wide to long format: melt - cont'd  ####

# Melt the wide data into long.
costa_grouped_mean_long = pd.melt(costa_grouped_mean,       #<- wide dataset
                                  id_vars = ['Target'],     #<- identifying variable
                                  var_name = 'metric',      #<- contains col names of wide data
                                  value_name = 'mean')      #<- contains values from above columns
print(costa_grouped_mean_long)





# In[15]:


#=================================================-
#### Slide 25: Long to wide format: pivot - cont'd  ####

# Melt the long data into wide.
costa_grouped_mean_wide = costa_grouped_mean_long.pivot(
                                                    index = 'Target',   #<- identifying variable
                                                    columns = 'metric', #<- col names of wide data
                                                    values = 'mean')    #<- values from above columns
print(costa_grouped_mean_wide)




# In[ ]:


#=================================================-
#### Slide 27: Pickle cleaned dataset  ####

pickle.dump(costa_viz, open(data_dir + "/costa_viz.sav","wb"))
pickle.dump(costa_grouped_mean_long, open(data_dir + "/costa_grouped_mean_long.sav","wb"))
pickle.dump(costa_grouped_mean_wide, open(data_dir + "/costa_grouped_mean_wide.sav","wb"))




# In[ ]:


#=================================================-
#### Slide 29: Exercise 3  ####






# In[ ]:


#=================================================-
#### Slide 32: Importing matplotlib  ####

import matplotlib.pyplot as plt




# In[ ]:


#=================================================-
#### Slide 34: Univariate plots: histogram  ####

plt.rcParams.update({'font.size': 15})
plt.hist(costa_viz['rooms'])
plt.show()




# In[ ]:


#=================================================-
#### Slide 35: Univariate plots: histogram - cont'd  ####

plt.hist(costa_viz['rooms'], bins = 20)
plt.xlabel('rooms')       #<- label x-axis
plt.ylabel('Frequency')   #<- label y-axis
plt.title('Rooms Distribution')  #<- add plot title
plt.show()




# In[ ]:


#=================================================-
#### Slide 36: Univariate plots: boxplot  ####

plt.boxplot(costa_viz['ppl_total'])
plt.show()




# In[ ]:


#=================================================-
#### Slide 37: Univariate plots: boxplot - cont'd  ####

plt.boxplot(costa_viz['ppl_total'], vert = False)
plt.xlabel('ppl_total')     #<- label x-axis
# Add plot title
plt.title('Number of people distribution')  
plt.show()




# In[ ]:


#=================================================-
#### Slide 39: Univariate plots: bar chart - cont'd  ####

print(costa_grouped_mean_long.head())
costa_true_means = costa_grouped_mean_long.query('Target == True')[['metric','mean']]
print(costa_true_means)




# In[ ]:


#=================================================-
#### Slide 40: Univariate plots: bar chart - cont'd  ####

bar_labels = costa_true_means['metric']     #<- 1
bar_heights = costa_true_means['mean']      #<- 2
num_bars = len(bar_heights)
bar_positions = np.arange(num_bars)         #<- 3




# In[ ]:


#=================================================-
#### Slide 41: Univariate plots: bar chart - cont'd  ####

# Adjust figure size before plotting.
plt.figure(figsize = (15, 12)) 
plt.bar(bar_positions, bar_heights)
plt.xticks(bar_positions, 
           bar_labels, 
           rotation = 18)
plt.ylabel('Mean values')
plt.title('Costa Means')  #<- add plot title
plt.show()




# In[ ]:


#=================================================-
#### Slide 44: Bivariate plots: scatterplot  ####

plt.scatter(costa_viz['age'],
            costa_viz['monthly_rent'])
plt.show()




# In[ ]:


#=================================================-
#### Slide 45: Bivariate plots: scatterplot - cont'd  ####

plt.scatter(costa_viz['age'],
            costa_viz['monthly_rent'],
            marker = "D") #<- set marker type to diamond
plt.xlabel('Age')
plt.ylabel('Monthly rent')
plt.title('Distribution')
plt.show()




# In[ ]:


#=================================================-
#### Slide 47: Exercise 4  ####






# In[ ]:


#=================================================-
#### Slide 50: Customize colors - cont'd  ####

plt.hist(costa_viz['rooms'],
            facecolor = 'goldenrod') #<- set color
plt.xlabel('Rooms')
plt.ylabel('Frequency')
plt.title('Rooms distribution')
plt.show()
plt.bar(bar_positions, 
        bar_heights, 
        color = "orchid")
plt.xticks(bar_positions, bar_labels)
plt.ylabel('Mean values')
plt.title('Costa Means')  
plt.show()




# In[ ]:


#=================================================-
#### Slide 51: Customize color: scatterplot  ####

plt.scatter(costa_viz['age'],
            costa_viz['monthly_rent'],
            c = 'darkorange') #<- set marker type to diamond
plt.xlabel('Age')
plt.ylabel('Monthly rent')
plt.title('Distribution')
plt.show()




# In[ ]:


#=================================================-
#### Slide 53: Customize color: map colors - cont'd  ####

color_dict = {True: 'darkseagreen', 
              False: 'palevioletred'}
color = costa_viz['Target'].map(color_dict)
print(color.head())
plt.scatter(costa_viz['age'],
            costa_viz['monthly_rent'],
            c = color)
plt.xlabel('Age')
plt.ylabel('Monthly rent')
plt.title('Distribution')
plt.show()




# In[ ]:


#=================================================-
#### Slide 54: Customize color: opacity  ####

plt.scatter(costa_viz['age'],
            costa_viz['monthly_rent'],
            c = color,
            alpha = 0.3)
plt.xlabel('Age')
plt.ylabel('Monthly rent')
plt.title('Distribution')
plt.show()




# In[ ]:


#=================================================-
#### Slide 55: Customize plot settings: available styles  ####

print(plt.style.available)
plt.style.use('ggplot')




# In[ ]:


#=================================================-
#### Slide 56: Customize plot settings: test ggplot style  ####

plt.scatter(costa_viz['age'],
            costa_viz['monthly_rent'],
            c = color,
           alpha = 0.3)
plt.xlabel('Age')
plt.ylabel('Monthly rent')
plt.title('Distribution')
plt.show()




# In[ ]:


#=================================================  -
#### Slide 58: Customize plot settings: labels  ####

plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.labelcolor'] = 'red'
plt.rcParams['axes.titlesize'] = 35
plt.scatter(costa_viz['age'],
            costa_viz['monthly_rent'],
            c = color,
            alpha = 0.3)
plt.xlabel('Age')
plt.ylabel('Monthly rent')
plt.title('Distribution')
plt.show()




# In[ ]:


#================================================= -
#### Slide 59: Customize plot settings: reset defaults  ####

plt.rcdefaults()
plt.scatter(costa_viz['age'],
            costa_viz['monthly_rent'],
            c = color,
           alpha = 0.3)
plt.xlabel('Age')
plt.ylabel('Monthly rent')
plt.title('Distribution')
plt.show()



