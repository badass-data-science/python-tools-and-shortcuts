import pandas as pd
from datetime import datetime, timezone

class Fips():
    def __init__(
        self,
        url_fips_codes = 'https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt',
    ):
        self.url_fips_codes = url_fips_codes
        self.timestamp_download = None

    def set_download_timestamp(self):
        self.timestamp_download = datetime.now(timezone.utc)
        
class FipsCounty(Fips):
    def __init__(
        self,
        url_fips_codes = 'https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt',
    ):
        super().__init__(url_fips_codes)
    
    def download_FIPS_codes(self):
        self.df = (
            pd.read_csv(
                self.url_fips_codes,
                sep = '|',
                dtype = {
                    'STATE' : str,
                    'STATEFP' : str,
                    'COUNTYFP' : str,
                    'COUNTYNS' : str,
                },
            )
            .drop_duplicates()
            .sort_values(by = ['STATE', 'COUNTYFP'])
            .reset_index(drop = True)
        )
        self.set_download_timestamp()

class FipsState(Fips):
    def __init__(
        self,
        url_fips_codes = 'https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt',
    ):
        super().__init__(url_fips_codes)
    
    def download_FIPS_codes(self):
        self.df = (
            pd.read_csv(
                self.url_fips_codes,
                sep = '|',
                dtype = {
                    'STATE' : str,
                    'STATEFP' : str,
                },
            )
            [['STATE', 'STATEFP']]
            .drop_duplicates()
            .sort_values(by = ['STATE'])
            .reset_index(drop = True)
        )
        self.set_download_timestamp()
