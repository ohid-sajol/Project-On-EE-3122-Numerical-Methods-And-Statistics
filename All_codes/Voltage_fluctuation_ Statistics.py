import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

all_data_1 = pd.read_excel("Day_1.xlsx")
all_data_2 = pd.read_excel("Day_2.xlsx")
all_data_3 = pd.read_excel("Day_3.xlsx")


## Mean deviation

data_num = len(all_data_1.index)

data_day_1 = np.array(all_data_1["Line voltage(RMS)"].tolist())
data_day_2 = np.array(all_data_2["Line voltage(RMS)"].tolist())
data_day_3 = np.array(all_data_3["Line voltage(RMS)"].tolist())



mean_1 = np.sum(data_day_1)/data_num
mean_2 = np.sum(data_day_2)/data_num
mean_3 = np.sum(data_day_3)/data_num

diff_day_1 = abs(data_day_1-mean_1)
diff_day_2 = abs(data_day_2-mean_2)
diff_day_3 = abs(data_day_3-mean_3)


mean_deviation_1 = np.sum(diff_day_1)/data_num
mean_deviation_2 = np.sum(diff_day_2)/data_num
mean_deviation_3 = np.sum(diff_day_3)/data_num

print("Mean deviation \n")

print(mean_deviation_1,"\n")
print(mean_deviation_2,"\n")
print(mean_deviation_3,"\n")


## Standard deviation

sum_1 =  0
sum_2 = 0
sum_3 = 0

i = 0

while i <= data_num-1:
    sum_1 = abs((data_day_1[i] - mean_1)*(data_day_1[i] - mean_1))
    sum_2 = abs((data_day_2[i] - mean_2)*(data_day_2[i] - mean_2))
    sum_3 = abs((data_day_3[i] - mean_3)*(data_day_3[i] - mean_3))
    i = i+1

sd_1 = math.sqrt(sum_1/data_num)
sd_2 = math.sqrt(sum_2/data_num)
sd_3 = math.sqrt(sum_3/data_num)

print("Standard Deviation \n")

print(sd_1,"\n",sd_2,"\n",sd_3,"\n")

## Skewness



sum_1 =  0
sum_2 = 0
sum_3 = 0

i = 0

while i <= data_num-1:
    sum_1 = abs((data_day_1[i] - mean_1)*(data_day_1[i] - mean_1)*(data_day_1[i] - mean_1))
    sum_2 = abs((data_day_2[i] - mean_2)*(data_day_2[i] - mean_2)*(data_day_2[i] - mean_2))
    sum_3 = abs((data_day_3[i] - mean_3)*(data_day_3[i] - mean_3)*(data_day_3[i] - mean_3))
    i = i+1

skewness_1 = sum_1/(data_num*sd_1**3)
skewness_2 = sum_2/(data_num*sd_2**3)
skewness_3 = sum_3/(data_num*sd_3**3)

print("Skewness are: \n")
print(skewness_1,"\n",skewness_2,"\n",skewness_3,"\n")

## Kurtosis calculation

sum_1 =  0
sum_2 = 0
sum_3 = 0

i = 0

while i <= data_num-1:
    sum_1 = abs((data_day_1[i] - mean_1)*(data_day_1[i] - mean_1)*(data_day_1[i] - mean_1)*(data_day_1[i] - mean_1))
    sum_2 = abs((data_day_2[i] - mean_2)*(data_day_2[i] - mean_2)*(data_day_2[i] - mean_2)*(data_day_2[i] - mean_2))
    sum_3 = abs((data_day_3[i] - mean_3)*(data_day_3[i] - mean_3)*(data_day_3[i] - mean_3)*(data_day_3[i] - mean_3))
    i = i+1

kurtosis_1 = sum_1/(data_num*sd_1**4)
kurtosis_2 = sum_2/(data_num*sd_2**4)
kurtosis_3 = sum_3/(data_num*(sd_3**4))

print("Kurtosis are: \n")

print(kurtosis_1,"\n",kurtosis_2,"\n",kurtosis_3,"\n")