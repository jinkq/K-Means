import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def read_file(path):
    with open(path) as f:
        data = f.readlines();
    df = pd.DataFrame()
    for row in data:
        x = row.split(',')[0]
        y = row.split(',')[1].split('\t')[0]
        label = int(row.split('\t')[1].strip())
        instance = pd.DataFrame({'x':x, 'y':y, 'label':label}, index=[0])
        df = pd.concat([df, instance])
    return df
df = read_file('../../../output/clusteredInstances/part-m-00000')

fig = sns.scatterplot(x="x", y="y", data=df, hue='label', style='label');
plt.savefig('../../../result/result.png')
