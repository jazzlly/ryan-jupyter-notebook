#%% 
import os

os.makedirs(os.path.join('..', 'data'), exist_ok=True)
data_file = os.path.join('..', 'data', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n')  # 列名
    f.write('NA,Pave,127500\n')  # 每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')
    
#%%
import pandas as pd

data = pd.read_csv(data_file)
print(data)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean())
print(inputs)

inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)
# inputs['Alley_Pave'] = (inputs['Alley'] == 'Pave')
# inputs['Alley_nan'] = (inputs['Alley'] != 'Pave')
# del inputs['Alley']
# inputs

#%%
import torch

X, Y = torch.tensor(inputs.values), torch.tensor(outputs.values)
X, Y