import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float
    }
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    
    """
    Template for loading data from API
    """
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    li = []
    for n in months:
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{n}.parquet"
        df = pd.read_parquet(path=url)
        df['lpep_pickup_date'] = pd.to_datetime(df['lpep_pickup_datetime']).dt.date
        df['lpep_dropoff_date'] = pd.to_datetime(df['lpep_dropoff_datetime']).dt.date
        print(f"loading month {n=} with {url=}")
        li.append(df)
    merged_df = pd.concat(li, axis=0, ignore_index=True)

    return merged_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

