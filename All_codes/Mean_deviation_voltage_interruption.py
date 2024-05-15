import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
all_data_1 = pd.read_excel("Day_1.xlsx")
all_data_2 = pd.read_excel("Day_2.xlsx")
all_data_3 = pd.read_excel("Day_3.xlsx")

row_num = len(all_data_1.index)
samples = np.array(all_data_1["Sample no."].tolist())


data_day_1 = np.array(all_data_1["Voltage(RMS)"].tolist())
data_day_2 = np.array(all_data_2["Voltage(RMS)"].tolist())
data_day_3 = np.array(all_data_3["Voltage(RMS)"].tolist())

## For regular plot

"""plt.plot(samples,data_day_1,label = 'day 1')
plt.plot(samples,data_day_2,label = 'day 2')
plt.plot(samples,data_day_3,label = 'day 3')
plt.xlabel('Sample no.')
plt.ylabel('Voltage level')
plt.title('Voltage interruption scenario')
plt.legend()
plt.show()"""

## end of regular plot

## Code of bar plot

"""plt.bar(samples,data_day_1,width = 0.2,label = 'day 1')
plt.bar(samples+0.2,data_day_2,width = 0.2,label = 'day 2')
plt.bar(samples+0.4,data_day_3,width = 0.2,label = 'day 3')

plt.xlabel('Sample no.')
plt.ylabel('Voltage level')
plt.title('Voltage interruption scenario')
plt.legend()
plt.show()"""

### end of bar plot code

# Mean deviation code

Actual_voltage = 220

diff_day_1 = -1*(data_day_1-Actual_voltage)
diff_day_2 = -1*(data_day_2-Actual_voltage)
diff_day_3 = -1*(data_day_3-Actual_voltage)

mean_deviation_1 = np.sum(diff_day_1)/row_num
mean_deviation_2 = np.sum(diff_day_2)/row_num
mean_deviation_3 = np.sum(diff_day_3)/row_num

mean_deviations = np.array([mean_deviation_1,mean_deviation_2,mean_deviation_3])

plt.bar([1,2,3],mean_deviations)

plt.xlabel('Days')
plt.ylabel('Mean_deviation')
plt.title('Mean deviation scenario')
plt.show()
