

from datetime import datetime as dt
from datetime import timedelta as td
import isodate
import pandas as pd
'''PARAMS:
Arguments:

    publisher -- all, pro (professional submitters), etc
    obs_type -- Filters to only specific observation types. Can be an individual value or a comma-separated string of multiple values. Only snow depth values are processed, but accepted obs_type values are: snowpack_test, snow_conditions, weather, camera, dangerous_wildlife, other_hazard, point_of_interest, water_hazard, trail_conditions, trip_report, incident, avalanche
    limit -- Maximum number of records to return (default 1000)
    start -- Start datetime to return results from, as datetime object
    end -- End datetime to return results from, as datetime object
    bbox -- Bounding box to restrict results, specified as dictionary with items latmax, lonmax, latmin, lonmin
    filter -- Flag indicating whether entries with no snow depth data should be filtered out.




'''

''' Time series specific parameters

#Parameters
#https://www.meteomatics.com/en/api/available-parameters/





'''
COORDINATES_TS = [(47.25,9.34), (30,-4)]
NOW = dt(2023,1,1)
STARTDATE_TS = NOW
ENDDATE_TS = STARTDATE_TS+td(days=180)
interval = ENDDATE_TS - STARTDATE_TS
print(f"interval: {interval}, Start: {STARTDATE_TS}, End: {ENDDATE_TS}")
INTERVAL_TS = td(hours=1)

    
PARAMETERS_TS = ['t_2m:C', 'precip_24h:mm']
MODEL = 'mix'
ENS_SELECT = None  # e.g. 'median'
CLUSTER_SELECT = None  # e.g. "cluster:1", see http://api.meteomatics.com/API-Request.html#cluster-selection

'''df_time = pd.DataFrame({"date": pd.date_range(STARTDATE_TS, ENDDATE_TS, freq=INTERVAL_TS)}, index=df_time.date)
x = 0
for x in range(65):
    if x == 0:
        print(f"run {x} on: {STARTDATE_TS}")
        df_time["date"][x] = STARTDATE_TS
    else:
        print(f"run {x} on: {STARTDATE_TS + td(days=1)}")
        df_time["date"][x] = STARTDATE_TS + td(days=1)
        STARTDATE_TS = STARTDATE_TS + td(days=1)
    print(f"Run: {x} times")

'''

params = {
"coordinates_ts": [(47.25,9.34), (30,-4)],
"now": dt.utcnow().replace(hour=0, minute=0, second=0, microsecond=0),
"startdate_ts": STARTDATE_TS,
"enddate_ts": STARTDATE_TS + td(days=180),
"interval_ts": td(hours=1),
"parameters_ts": ['t_2m:C', 'precip_1h:mm']
}

