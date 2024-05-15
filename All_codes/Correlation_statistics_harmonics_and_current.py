import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

all_data = pd.read_excel("Harmonic_percentage_and_distortion_profile.xlsx")

new = pd.read_excel("New.xlsx")

new_data_x = np.array(new["X"].tolist())
new_data_y = np.array(new["Y"].tolist())


## Mean deviation
data_num = len(all_data.index)

Ua = np.array(all_data["Phase-1 (%)"].tolist())
Ub = np.array(all_data["Phase-2 (%)"].tolist())
Uc = np.array(all_data["Phase-3 (%)"].tolist())

def covariance(x,y) :
    number = len(x)
    mean_x = np.sum(x)/number
    mean_y = np.sum(y)/number

    sum = 0
    i = 0
    while i <= number-1:
       sum = sum + (x[i] - mean_x)*(y[i] - mean_y)
       i = i + 1
    
    cov = sum/number
    return cov
 

def standard_deviation(x) :
    number = len(x)
    mean = np.sum(x)/number
    sum =  0
    i = 0

    while i <= number-1:
      sum = sum + (x[i] - mean)*(x[i] - mean)
      i = i+1

    sd = (math.sqrt(sum/number))
    return sd


coefficient_of_correlation_Ua_Ub = covariance(Ua,Ub)/(standard_deviation(Ua)*standard_deviation(Ub))

coefficient_of_correlation_Ua_Uc = covariance(Ua,Uc)/(standard_deviation(Ua)*standard_deviation(Uc))

coefficient_of_correlation_Ub_Uc = covariance(Ub,Uc)/(standard_deviation(Ub)*standard_deviation(Uc))

Rz_xy = math.sqrt((coefficient_of_correlation_Ua_Uc**2 + coefficient_of_correlation_Ub_Uc**2 - 2*coefficient_of_correlation_Ua_Ub*coefficient_of_correlation_Ub_Uc*coefficient_of_correlation_Ua_Uc)/(1-coefficient_of_correlation_Ua_Ub**2))


print(Rz_xy)