import pandas as pd
import numpy as np
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import seaborn as sns

def ab_test(group_a:list, group_b:list, count:int):
    # Create a numpy array for mean differences
    mean_diffs = np.empty(count)

    group_a = np.array(group_a)
    group_b = np.array(group_b)

    mean_a = group_a.mean()
    mean_b = group_b.mean()
    observed_diff = mean_a - mean_b 

    len_a = len(group_a)
    len_b = len(group_b)

    combined_values = np.append(group_a, group_b)
    

    for i in range(count):
        shuffled_values = np.random.permutation(combined_values)
    
        new_group_a = shuffled_values[:len_a]  
        new_group_b = shuffled_values[len_a:] 
        
        group_a_mean = new_group_a.mean()
        group_b_mean = new_group_b.mean()
        
        mean_diffs[i] = group_a_mean - group_b_mean
    
    extreme_count = np.sum(np.abs(mean_diffs) >= np.abs(observed_diff))
    p_value = extreme_count / count
    
    return p_value