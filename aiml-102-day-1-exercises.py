#!/usr/bin/env python
# coding: utf-8

# ## AIML 102 DAY 1 EXERCISES  ##
# #### Exercise 3 ####
# #### Task 1
# ##### Import the required packages.
# ##### Set `data_dir` to the path of the data directory.
# ##### Print data_dir.
# #### Result:
# 

# In[ ]:




# #### Task 2
# ##### Load the `chicago_census.csv` dataset. 
# ##### Save it as `chicago_census`.
# ##### View the first few rows of `chicago_census`.
# #### Result:
# 

# In[ ]:




# #### Task 3
# ###### Rename the column names as the following (and double check they are renamed by looking at `.columns`:
# 

# In[ ]:


chicago_census.rename(columns={'Community Area Number': 'community_number',
                               'COMMUNITY AREA NAME': 'community_area' , 
                               'PERCENT OF HOUSING CROWDED': 'percent_house_crowded', 
                               'PERCENT HOUSEHOLDS BELOW POVERTY': 'percent_house_below_poverty', 
                               'PERCENT AGED 16+ UNEMPLOYED': 'percent_16_unemployed' , 
                               'PERCENT AGED 25+ WITHOUT HIGH SCHOOL DIPLOMA': 'percent_25_without_diploma', 
                               'PERCENT AGED UNDER 18 OR OVER 64': 'percent_dependent', 
                               'PER CAPITA INCOME ' : 'per_capita_income',
                               'HARDSHIP INDEX': 'hardship_index'}, inplace = True)


# #### Result:
# 

# In[ ]:




# #### Task 4
# ##### Drop columns `community_number` and `community_area` from the dataframe.
# ##### Look for NAs in `chicago_census` and impute with the mean of the column.
# ##### Check for NAs again to make sure the data looks good.
# #### Result:
# 

# In[ ]:




# #### Task 5
# ##### Create a variable `mean_per_capita_income` which contains the mean of `per_capita_income` from `chicago_census`.
# ##### Convert `per_capita_income` variable to a binary variable where `per_capita_income` is set to 0 if per_capita_income of the row is less than `mean per_capita_income`, otherwise set `per_capita_income` to 1.
# ##### Make a new duplicate dataframe called `ex_viz`.
# #### Result:
# 

# In[ ]:




# #### Task 6
# ##### Group `ex_viz` data by the `per_capita_income` variable. Save as `ex_grouped`.
# ##### Then group and summarize the numeric variables `community_number`, `percent_house_crowded`, 
# ##### `percent_house_below_poverty`,`percent_16_unemployed`, `percent_25_without_diploma`, `percent_dependent`, 
# ###### `hardship_index` by `per_capita_income` using their means. Save as `ex_grouped_mean` and print.
# ##### Reset its index and print the result.
# #### Result:
# 

# In[ ]:




# #### Task 7
# ##### Notice the format of `ex_grouped_mean`. We wish to convert it from wide to long format.
# ##### Use the `pd.melt()` function and convert it to long format. Save as `ex_grouped_mean_long` and print the result.
# #### Result:
# 

# In[ ]:




# #### Task 8
# ##### Now use the `pd.pivot()` function to convert `ex_grouped_mean_long` to wide format.
# ##### Save as `ex_grouped_mean_wide` and print.
# #### Result:
# 

# In[ ]:




# #### Task 9
# ##### Pickle the data frame `ex_viz, ex_grouped_mean_long and ex_grouped_mean_wide` for later use.
# #### Result:
# 

# In[ ]:




# #### Exercise 4 ####
# #### Task 1
# ##### Use the `plt.hist()` function to create a simple histogram of `percent_house_below_poverty`.
# #### Result:
# 

# In[ ]:




# #### Task 2
# ##### Now run the same code as above and set the number of bins as 25. 
# ##### Name the x-axis and the y-axis as `percent_house_below_poverty` and `Frequency` respectively. 
# ##### Also include the title `Percent House below Poverty Distribution`.
# #### Result:
# 

# In[ ]:




# #### Task 3
# ##### Create a simple boxplot of `percent_dependent` and show the results.
# ##### What can you infer from looking at the plot?
# #### Result:
# 

# In[ ]:




# ##### We can see that the median is closer to the 25th percentile than the 75th percentile (slightly skewed). We can also see a few  outliers.
# #### Task 4
# ##### Now try to create the same boxplot by changing its orientation to horizontal.
# ##### Also label the x-axis and title accordingly.
# #### Result:
# 

# In[ ]:




# #### Task 5
# ##### Now let's create a barplot using the long data `ex_grouped_mean_long`.
# ##### To do that, first filter `per_capita_income` as 1 and then create two columns in the dataframe: `metrics` and `means`.
# ##### Save as `ex_true_means` and print.
# #### Result:
# 

# In[ ]:




# #### Task 6
# ##### Create the following variables needed to construct a bar plot:
# - `ex_bar_labels` with the `metric`
# - `ex_bar_heights` with the `mean`
# - `num_bars` having the length of `ex_bar_heights`
# - `ex_bar_positions` having the range of `ex_num_bars`
# #### Result:
# 

# In[ ]:




# #### Task 7
# ##### Create a basic bar chart with the variables above. 
# ##### Label the title and y-axis accordingly. 
# ##### Add the title "Chicago Exercise Means".
# #####  Rotate the labels to a vertical position ( set `rotation`= 90 ) to make them easier to read.
# #### Result:
# 

# In[ ]:




# #### Task 8
# ##### Plot the above bar chart, this time by adjusting the size of the figure.
# ##### Use the `plt.figsize()` to set the width as `20` and the height as `15`.
# #### Result:
# 

# In[ ]:




# #### Task 9
# ##### Create a simple scatterplot with `percent_16_unemployed` on the x-axis and `hardship_index` on the y-axis.
# #### Result:
# 

# In[ ]:




# #### Task 10
# ##### Plot the above scatterplot and name the axes and title accordingly.
# ##### Set the marker to `X` and view the plot.
# #### Result:
# 

# In[ ]:




# #### Exercise 5 ####
# #### Task 1
# ##### Customize the following graphs and view the plots as mentioned below:
# - Histogram of variable `percent_house_below_poverty` and color `lightcoral` 
# - Above bar chart  using color `thistle` using the `plt.figsize()` to set the width as `20` and the height as `15`.
# - Above scatterplot of `percent_16_unemployed` on the x-axis and `hardship_index` on the y-axis using color `firebrick`
# #### Result:
# 

# In[ ]:




# #### Task 2
# ##### Create a color dictionary called `ex_color_dict` corresponding with `per_capita_income`:
# ##### - 0 corresponding to color `darkorange`
# ##### - 1 corresponding to color `skyblue`
# ##### Set the color as `ex_color_dict` and create a scatterplot with the same parameters `percent_16_unemployed` and `hardship_index`.
# ##### Then, change the opacity using `alpha` to 0.6.
# #### Result:
# 

# In[ ]:




# #### Task 3
# ##### Print the available pre-defined styles provided by `matplotlib`.
# ##### Set the style to ` seaborn-darkgrid` .
# ##### Construct the scatterplot above.
# ##### Run the scatterplot again, this time setting the labels using `.rcParams` as:
# ##### - label size as 20
# ##### - label color as red
# ##### - figure title size as 15
# ##### Reset the `rcParams` to default.
# #### Result:
# 

# In[ ]:



