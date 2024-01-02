#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list to a 3x3 NumPy array
    matrix = np.array(lst).reshape(3, 3)
    
    # Calculate statistics
    mean = [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.flatten().mean()]
    variance = [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.flatten().var()]
    std_dev = [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.flatten().std()]
    max_val = [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.flatten().max()]
    min_val = [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.flatten().min()]
    sum_vals = [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.flatten().sum()]
    
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_vals
    }


# In[4]:


calculate([1,2,3,4,5,6,7,8,9])


# In[ ]:




