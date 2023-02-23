import utility
import requests
import pytest

file = 'C:\\Users\\Switchity Networks\\Desktop\\REST_API\\Test_self\\Data_DrivenAPI.xlsx'
read_row = utility.countrows(file=file, sheetname='Sheet1')
read_column = utility.countcolumns(file=file, sheetname='Sheet1')

for row in range(1,read_row+1):
    SNo = utility.readData(file=file, sheetname='Sheet1', rows=row, columns=1)
    Country = utility.readData(file=file, sheetname='Sheet1', rows=row, columns=2)
    country_code = utility.readData(file=file, sheetname='Sheet1', rows=row, columns=3)
    zip_code = utility.readData(file=file, sheetname='Sheet1', rows=row, columns=4)
    print(SNo,Country,country_code,zip_code)

    @pytest.mark.parametrize(country_code,zip_code)
    def test_chandan(country_code,zip_code):
        response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
        response_body = response.json()
        if response.status_code ==200:

            utility.writeData(file=file,sheetname='Sheet1',row=row,column=5,value='pass')
            print("pass")
        else:
            utility.writeData(file=file, sheetname='Sheet1', row=row, column=6, value='Fail')
            print('fail')











