import numpy as np
import sys

def regrid_diff(year,to_year):
  year = int(year)
  to_year = int(to_year)
  ssp126_cycle = np.empty([16,900,747])
  ssp585_cycle = np.empty([16,900,747])
  for t in range(1979,1995):
    tmp = np.genfromtxt("./tmp_regrid/new_tmp126_"+str(t)+".csv",delimiter=",")
    for i in range(900):
      for j in range(747):
        ssp126_cycle[t-1979][i][j] = tmp[i][j]
    tmp = np.genfromtxt("./tmp_regrid/new_tmp585_"+str(t)+".csv",delimiter=",")
    for i in range(900):
      for j in range(747):
        ssp585_cycle[t-1979][i][j] = tmp[i][j]
  ssp126_mean = np.empty([900,747])
  ssp585_mean = np.empty([900,747])
  for i in range(900):
    for j in range(747):
      tmp = 0
      for t in range(1979,1995):
        tmp += ssp126_cycle[t-1979][i][j]
      ssp126_mean[i][j] = tmp/16
      tmp = 0
      for t in range(1979,1995):
        tmp += ssp585_cycle[t-1979][i][j]
      ssp585_mean[i][j] = tmp/16
  for t in range(year,to_year+1):
    ssp126_arr = np.genfromtxt("./tmp_regrid/new_tmp126_"+str(t)+".csv",delimiter=",")
    ssp126_arr = ssp126_arr-ssp126_mean
    np.savetxt("./tmp_regrid_diff/tmp126_diff_"+str(t)+".csv",ssp126_arr,delimiter=",")
    ssp585_arr = np.genfromtxt("./tmp_regrid/new_tmp585_"+str(t)+".csv",delimiter=",")
    ssp585_arr = ssp585_arr-ssp585_mean
    np.savetxt("./tmp_regrid_diff/tmp585_diff_"+str(t)+".csv",ssp585_arr,delimiter=",")

regrid_diff(sys.argv[1],sys.argv[2])
