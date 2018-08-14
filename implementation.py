import numpy as np
import csv
import pandas as pd

dataset = pd.read_csv('dataset.csv')
a=np.array(dataset)

# firstname = dataset.iloc[:,1].values
# lastname = dataset.iloc[:,3].values
# company =  dataset.iloc[:,5].values

dataset['Email'] = dataset['First_Name'].map(str) + dataset['Middle_Name'] + "." + dataset['Last_Name'] + '@' +dataset['Company'] + '.com'
dataset.to_csv('dataset.csv', index=False)

print(dataset['Email'])



