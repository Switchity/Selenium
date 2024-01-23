import utility
import requests
import pytest

file = 'C:\\Users\\Switchity Networks\\Desktop\\REST_API\\Test_self\\Data_DrivenAPI.xlsx'
read_row = utility.countrows(file=file, sheetname='Sheet1')
read_column = utility.countcolumns(file=file, sheetname='Sheet1')

for row in range(1, read_row + 1):
    SNo = utility.readData(file=file, sheetname='Sheet1', rows=row, columns=1)
    country_name = utility.readData(file=file, sheetname='Sheet1', rows=row, columns=2)
    country_code = utility.readData(file=file, sheetname='Sheet1', rows=row, columns=3)
    zip_code = utility.readData(file=file, sheetname='Sheet1', rows=row, columns=4)
    places_name = utility.readData(file=file, sheetname='Sheet1', rows=row, columns=5)


    @pytest.mark.parametrize(country_code, zip_code, country_name)
    def chandan(country_code, zip_code, country_name):
        response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
        response_body = response.json()
        k = response_body.get('post code')
        print(response_body)
        if k == zip_code:
            print('pass')
            utility.writeData(file=file, sheetname='Sheet1', row=row, column=7, value='Pass')
        else:
            print('Fail')
            utility.writeData(file=file, sheetname='Sheet1', row=row, column=7, value='fail')


    chandan(country_code, zip_code, country_name)
