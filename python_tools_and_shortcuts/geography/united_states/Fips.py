# Federal Information Processing Standard (FIPS) uniquely identify
# U.S. states, territories, and counties. These are standardized
# across the United States government and managed by NIST.

#
# Load useful libraries
#
import pandas as pd
from datetime import datetime, timezone

#
# Define a parent class for containing FIPS data
#
class Fips():

    # constructor
    def __init__(
        self,
        url_fips_codes = 'https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt',
    ):
        self.url_fips_codes = url_fips_codes
        self.timestamp_download = None

    # save the timestamp when FIPS content download occured
    def set_download_timestamp(self):
        self.timestamp_download = datetime.now(timezone.utc)

#
# Define a child class for working with county-level FIPS codes
#
class FipsCounty(Fips):

    # constructor
    def __init__(
        self,
        url_fips_codes = 'https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt',
    ):
        super().__init__(url_fips_codes)

    # download the FIPS codes and store them per county
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

#
# Define a child class for working with state-level FIPS codes
#
class FipsState(Fips):

    # constructor
    def __init__(
        self,
        url_fips_codes = 'https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt',
    ):
        super().__init__(url_fips_codes)

    # download the FIPS codes and store them per state
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
