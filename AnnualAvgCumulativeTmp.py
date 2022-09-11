def leap(year):
  if (year % 4) == 0:
    if (year % 100) == 0:
      if (year % 400) == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


nc_1 = nc.Dataset("tavg_data/tavg.1960-2018.monthly.5km-grid-v4_tas_BCSD_TaiESM_ssp126.nc")
nc_2 = nc.Dataset("tavg_data/tavg.1960-2018.monthly.5km-grid-v4_tas_BCSD_TaiESM_ssp585.nc")
arr1 = np.array(nc_1["tas"])
arr2 = np.array(nc_2["tas"])


# 處理空值(-999.99)問題
for k in range(1692):
  for i in range(81):
    for j in range(60):
      if arr1[k][i][j] < -900:
        arr1[k][i][j] = np.nan
      if arr2[k][i][j] < -900:
        arr2[k][i][j] = np.nan

new_arr1 = np.empty([81,60])
new_arr2 = np.empty([81,60])

def gdd_csv(yr_start, yr_end):
  for t in range(yr_start, yr_end+1):
    # if 閏年
    if leap(t):
      start = (t-1960)*12
      for m in range(81):
        for n in range(60):
          new_arr1[m][n] = (31*(arr1[start][m][n])+29*(arr1[start+1][m][n])+31*(arr1[start+2][m][n])
          +30*(arr1[start+3][m][n])+31*(arr1[start+4][m][n])+30*(arr1[start+5][m][n])
          +31*(arr1[start+6][m][n])+31*(arr1[start+7][m][n])+30*(arr1[start+8][m][n])
          +31*(arr1[start+9][m][n])+30*(arr1[start+10][m][n])+31*(arr1[start+11][m][n]))
          new_arr2[m][n] = (31*(arr2[start][m][n])+29*(arr2[start+1][m][n])+31*(arr2[start+2][m][n])
          +30*(arr2[start+3][m][n])+31*(arr2[start+4][m][n])+30*(arr2[start+5][m][n])
          +31*(arr2[start+6][m][n])+31*(arr2[start+7][m][n])+30*(arr2[start+8][m][n])
          +31*(arr2[start+9][m][n])+30*(arr2[start+10][m][n])+31*(arr2[start+11][m][n]))

    else:
      start = (t-1960)*12
      for m in range(81):
        for n in range(60):
          new_arr1[m][n] = (31*(arr1[start][m][n])+28*(arr1[start+1][m][n])+31*(arr1[start+2][m][n])
          +30*(arr1[start+3][m][n])+31*(arr1[start+4][m][n])+30*(arr1[start+5][m][n])
          +31*(arr1[start+6][m][n])+31*(arr1[start+7][m][n])+30*(arr1[start+8][m][n])
          +31*(arr1[start+9][m][n])+30*(arr1[start+10][m][n])+31*(arr1[start+11][m][n]))
          new_arr2[m][n] = (31*(arr2[start][m][n])+28*(arr2[start+1][m][n])+31*(arr2[start+2][m][n])
          +30*(arr2[start+3][m][n])+31*(arr2[start+4][m][n])+30*(arr2[start+5][m][n])
          +31*(arr2[start+6][m][n])+31*(arr2[start+7][m][n])+30*(arr2[start+8][m][n])
          +31*(arr2[start+9][m][n])+30*(arr2[start+10][m][n])+31*(arr2[start+11][m][n]))      
    np.savetxt("tmp126_"+str(t)+".csv", new_arr1, delimiter=",")
    np.savetxt("tmp585_"+str(t)+".csv", new_arr2, delimiter=",")
gdd_csv(1960, 2100)