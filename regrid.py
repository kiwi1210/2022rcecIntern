import numpy as np
import netCDF4
import sys

def regrid(year,to_year):
  year = int(year)
  to_year = int(to_year)
  for t in range(year,to_year+1):
    nc_tavg_tas = np.genfromtxt("./new_tmp/tmp126_"+str(t)+".csv",delimiter=",")
    nc_tavg_lat = np.array(netCDF4.Dataset("/lfs/home/ychen/TCCIP/CMIP6_BSCD_monthly/tavg.1960-2018.monthly.5km-grid-v4_tas_BCSD_TaiESM_ssp585.nc")["latitude"])
    nc_tavg_lon = np.array(netCDF4.Dataset("/lfs/home/ychen/TCCIP/CMIP6_BSCD_monthly/tavg.1960-2018.monthly.5km-grid-v4_tas_BCSD_TaiESM_ssp585.nc")["longitude"])
    nc_lulcc_lat = np.array(netCDF4.Dataset("/lfs/home/ychen/LULCC_TW/future/SSP585_nc/LUH2_585_2016.nc")["latitude"])
    nc_lulcc_lon = np.array(netCDF4.Dataset("/lfs/home/ychen/LULCC_TW/future/SSP585_nc/LUH2_585_2016.nc")["longitude"])
    nc_tavg_year = np.empty([81,60])
    new_tavg_year = np.empty([900,747])
    grid_lat = np.empty([81,60])
    grid_lon = np.empty([81,60])
    for i in range(81):
      for j in range(60):
        grid_lat[i][j] = nc_tavg_lat[i]
    for i in range(81):
      for j in range(60):
        grid_lon[i][j] = nc_tavg_lon[j]
    for i in range(900):
      for j in range(747):
        d = ((grid_lat-nc_lulcc_lat[i][j])**2+(grid_lon-nc_lulcc_lon[i][j])**2)**0.5
        new_tavg_year[i][j] = nc_tavg_tas[np.unravel_index(d.argmin(),d.shape)]
    np.savetxt("./tmp_regrid/new_tmp126_"+str(t)+".csv",new_tavg_year,delimiter=",")
    nc_tavg_tas = np.genfromtxt("./new_tmp/tmp585_"+str(t)+".csv",delimiter=",")
    nc_tavg_lat = np.array(netCDF4.Dataset("/lfs/home/ychen/TCCIP/CMIP6_BSCD_monthly/tavg.1960-2018.monthly.5km-grid-v4_tas_BCSD_TaiESM_ssp585.nc")["latitude"])
    nc_tavg_lon = np.array(netCDF4.Dataset("/lfs/home/ychen/TCCIP/CMIP6_BSCD_monthly/tavg.1960-2018.monthly.5km-grid-v4_tas_BCSD_TaiESM_ssp585.nc")["longitude"])
    nc_lulcc_lat = np.array(netCDF4.Dataset("/lfs/home/ychen/LULCC_TW/future/SSP585_nc/LUH2_585_2016.nc")["latitude"])
    nc_lulcc_lon = np.array(netCDF4.Dataset("/lfs/home/ychen/LULCC_TW/future/SSP585_nc/LUH2_585_2016.nc")["longitude"])
    nc_tavg_year = np.empty([81,60])
    new_tavg_year = np.empty([900,747])
    grid_lat = np.empty([81,60])
    grid_lon = np.empty([81,60])
    for i in range(81):
      for j in range(60):
        grid_lat[i][j] = nc_tavg_lat[i]
    for i in range(81):
      for j in range(60):
        grid_lon[i][j] = nc_tavg_lon[j]
    for i in range(900):
      for j in range(747):
        d = ((grid_lat-nc_lulcc_lat[i][j])**2+(grid_lon-nc_lulcc_lon[i][j])**2)**0.5
        new_tavg_year[i][j] = nc_tavg_tas[np.unravel_index(d.argmin(),d.shape)]
    np.savetxt("./tmp_regrid/new_tmp585_"+str(t)+".csv",new_tavg_year,delimiter=",")

regrid(sys.argv[1],sys.argv[2])