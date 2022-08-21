# Setup
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 對tmp_diff(i.e. GDD Increment)分組
selected_K = #根據Kmeans_clusterNum結果代入
kmeans = KMeans(n_clusters=selected_K)
labels = kmeans.fit_predict(df)

# 將分組資料 (分類標籤) 併入原資料
lb = pd.DataFrame(labels, columns=['labels'])
df = pd.concat((lb, df), axis=1)

df.insert(2,"col",df_col)
df.insert(3,"row",df_row)
df.insert(4,"lon",df_lon)
df.insert(5,"lat", df_lat)
df.insert(6,"year",df_year)
df.insert(7,"temperature", df_tmp)

# 印出labels和tmp_diff、以及其統計結果
print(df[['labels', 'tmp_diff']], '\n')
print('原始資料\n', df['tmp_diff'].describe(), '\n')
# 抽出不同組的tmp_diff並印出統計結果
df_group = []
for i in range(selected_K):
    df_new = df[df['labels']==i]['tmp_diff']
    print(f'分類 {i + 1}\n', df_new.describe(), '\n')
    df_group.append(df_new)
# 用 seaborn 畫出所有組別tmp_diff的箱型圖
sns.boxplot(data=df_group)
plt.show()

#繪製結果
plt.scatter(df["col"],df["row"],c=df["labels"])
plt.xlabel("col")
plt.ylabel("row")
plt.title("tmp_diff Scatter Plot")
x_major_locator=MultipleLocator(100)
y_major_locator=MultipleLocator(100)
ax=plt.gca()
ax.set_aspect(1)
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
plt.xlim(0,900)
plt.ylim(0,900)
plt.show()