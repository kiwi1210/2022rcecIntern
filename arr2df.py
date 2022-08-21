# Setup
import netCDF4 as nc
import zipfile
import numpy as np
import pandas as pd

# unzip data
with zipfile.ZipFile("drive/MyDrive/tavg_data.zip") as zip_ref:
  zip_ref.extractall("")
with zipfile.ZipFile("drive/MyDrive/lulcc_data.zip") as zip_ref:
  zip_ref.extractall("")

# 將array轉換成data frame

tmp = np.genfromtxt("final_data/tmp585_2020_2030.csv", delimiter=",").flatten()
tmp_diff = np.genfromtxt("rcecIntern/final/final_data/tmp585_diff_2020_2030.csv", delimiter=",").flatten()
lat = np.array(nc.Dataset("lulcc_data/SSP585_nc/LUH2_585_2020.nc")["latitude"]).flatten()
lon = np.array(nc.Dataset("lulcc_data/SSP585_nc/LUH2_585_2020.nc")["longitude"]).flatten()

df = pd.DataFrame()
col = []
row = []
yr = []
for i in range(900):
  for j in range(747):
    col.append(j)
    row.append(i)
    yr.append("2020_2030")
df.insert(0,"temperature",tmp)
df.insert(1,"tmp_diff",tmp_diff)
df.insert(2,"lon",lon)
df.insert(3,"lat",lat)
df.insert(4,"col",col)
df.insert(5,"row",row)
df.insert(6,"year",yr)
df = df.dropna()

df.to_csv("df585_2020_2030.csv",index=False)