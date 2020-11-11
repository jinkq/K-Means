import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import sys
import os


def read_file(path):
    with open(path) as f:
        data = f.readlines();
    df = pd.DataFrame()
    for row in data:
        x = int(row.split(',')[0])
        y = int(row.split(',')[1].split('\t')[0])
        label = row.split('\t')[1].strip()
        instance = pd.DataFrame({'x':x, 'y':y, 'label':label}, index=[0])
        df = pd.concat([df, instance])
    return df

df = read_file('../../../output/clusteredInstances/part-m-00000')

sns.scatterplot(x="x", y="y", data=df, hue='label', style='label', sizes=100, palette=sns.color_palette("Set2", df.label.nunique()));

plt.legend(bbox_to_anchor=(1, 1), title='Label', frameon=False).texts[0].set_text("")
plt.title('k: '+sys.argv[1]+', iternum: '+sys.argv[2])

outputDir = '../../../result/k=' + sys.argv[1]
if not os.path.exists(outputDir):
    os.makedirs(outputDir)
plt.savefig(outputDir+'/k='+sys.argv[1]+'_iternum='+sys.argv[2]+'.png')

