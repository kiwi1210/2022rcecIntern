import numpy as np
import sys

def final_mean(year,to_year):
  year = int(year)
  to_year = int(to_year)
  arr = np.empty([11,900,747])
  arr_mean = np.empty([900,747])
  for t in range(year,to_year+1):
    arr[t-year] = np.genfromtxt("./tmp_regrid_diff/tmp585_diff_"+str(t)+".csv",delimiter=",")
  for i in range(900):
    for j in range(747):
      tmp = 0
      for t in range(11):
        tmp += arr[t][i][j]
      arr_mean[i][j] = tmp/11
  np.savetxt("./final_mean/tmp585_diff_"+str(year)+"_"+str(to_year)+".csv",arr_mean,delimiter=",")

final_mean(sys.argv[1],sys.argv[2])
