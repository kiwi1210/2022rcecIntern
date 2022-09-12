# Setup
import numpy as np
import seaborn as sns
import pandas as pd
import math
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# read dataframe
df = pd.read_csv("rcecIntern/final/final_df/df126_2020_2030.csv")

#leave only tmp_diff(i.e. GDD Increment) data
df_lat = df.lat
df_lon = df.lon
df_row = df.row
df_col = df.col
df_year = df.year
df_tmp = df.temperature

# Test 1: elbow method
new_arr = np.array(df["tmp_diff"])
new_arr = np.reshape(new_arr,(-1,1))
wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters=i).fit(new_arr)
  wcss.append(kmeans.inertia_)
chg = []
for i in range(1,9):
  chg.append(math.atan(wcss[i+1]-wcss[i])-math.atan(wcss[i]-wcss[i-1]))
max_item = max(chg)
max_index = chg.index(max_item)+1
print(max_index)

# Test 2: silhouette score
df = df.drop(columns=["temperature","lon","lat","col","row","year"])
df1 = df.sample(frac=0.10)
# 最大 K 值
K_max = 10
# 計算側影係數
scores = []
for i in range(2, K_max + 1):
    scores.append(silhouette_score(df1, KMeans(n_clusters=i).fit_predict(df1)))
# 得出最佳 K 值
selected_K = scores.index(max(scores)) + 2
print('K =', selected_K, '\n')

## 從上述兩個檢定方式，尋找合適的分群數量
