import pandas as pd
import numpy as np
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import seaborn as sns

def ab_test(group_a:list, group_b:list, count:int):
    # Create a numpy array for mean differances
    mean_diffs = np.empty([count,1])

    group_a = np.array(group_a)
    group_b = np.array(group_b)

    mean_a = group_a.mean()
    mean_b = group_b.mean()
    observed_diff = mean_a - mean_b

    len_a = len(group_a)
    len_b = len(group_b)

    combined_group = np.append(group_a,group_b)

    label_a = np.ones(len_a)
    label_b = np.zeros(len_b)

    # Set 1 for group a and 0 for group b
    combined_label = np.append(label_a, label_b)
    combined_data = np.column_stack((combined_label, combined_group))

    # Shuffel to make our data white
    np.random.shuffle(combined_data)

    len_combined_data = len(combined_data)

    for i in range(count):
        # Generate random labels
        experiment_label = np.random.randint(0, 2, len_combined_data)
        # Create new data from new labels and values from combined data
        experiment_data = np.column_stack((experiment_label, combined_data[:, 1]))
        # Calculate mean of data values with label equal to 1
        group_a_mean = experiment_data[experiment_data[:,0] == 1][:,1].mean()
        # Calculate mean of data values with label equal to 0
        group_b_mean = experiment_data[experiment_data[:,0] == 0][:,1].mean()
        mean_diffs[i] = group_a_mean - group_b_mean
    
    extreme_count = np.sum(np.abs(mean_diffs) >= np.abs(observed_diff))
    p_value = extreme_count / count
    return p_value