import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

all_data_1 = pd.read_excel("Day_1.xlsx")
all_data_2 = pd.read_excel("Day_2.xlsx")
all_data_3 = pd.read_excel("Day_3.xlsx")

data_num = len(all_data_1.index)

demand_1 = np.array(all_data_1["Demand(KW)"].tolist())
demand_2 = np.array(all_data_2["Demand(KW)"].tolist())
demand_3 = np.array(all_data_3["Demand(KW)"].tolist())

data_day_1 = np.array(all_data_1["Line voltage(RMS)"].tolist())
data_day_2 = np.array(all_data_2["Line voltage(RMS)"].tolist())
data_day_3 = np.array(all_data_3["Line voltage(RMS)"].tolist())


samples = np.array(all_data_1["Sample no."].tolist())

plt.plot(samples,data_day_1,label = 'day 1')
plt.plot(samples,data_day_2,label = 'day_2')
plt.plot(samples,data_day_3,label = 'day_3')

plt.xlabel('Sample no.')
plt.ylabel('Voltage level (RMS)')
plt.title('Voltage fluctuation scenario (132 kv line voltage)')
plt.legend()
plt.show()