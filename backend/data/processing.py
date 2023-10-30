import pandas as pd
from ..backend.time_series import time_series_example
from ..utils.parameters import PARAMETERS_TS, STARTDATE_TS

def process_data():        
    data_in = time_series_example()
    df = pd.DataFrame(data=data_in, columns=['start_date', 'end_date', PARAMETERS_TS[0], PARAMETERS_TS[1] ])
    print(data_in)
    print(df)
    df.to_csv(path=f"/output_csv_files/{STARTDATE_TS}.csv", header=True)

    return df

process_data()




