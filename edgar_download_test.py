

# references: check out the below
#https://github.com/edouardswiac/python-edgar

import os
import io
import shutil
import sys
import urllib.request 
import urllib.error 



# download index files from EDGAR
def download_index(start_year, end_year, URLstem):
    for year in range(start_year, end_year+1):
        for qtr in range(1, 5):
            currURL = URLstem + str(year) + '/QTR' + str(qtr) + '/master.idx'
            copy_file = str(year) + 'QTR' + str(qtr) + '.idx'
            local_file = 'master.idx'
            print('Downloading ' + str(year) + ' Q' + str(qtr) + ' master index.')

            try:
                response = urllib.request.urlopen(currURL)
                out_file = open(local_file, 'wb')
                shutil.copyfileobj(response, out_file)
                out_file.close()
                os.rename(local_file, copy_file)

            except HTTPError:
                print('URL not found.')



# extract 10Q and 10K from master idx





if __name__ == '__main__':

	start_year = 2018
	end_year = 2018
	URLstem = 'https://www.sec.gov/Archives/edgar/full-index/'

	download_index(start_year, end_year, URLstem)
