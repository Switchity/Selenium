import csv

def read_test_data_from_csv():
    test_data = []

    path = 'C:\\Users\\Switchity Networks\\Desktop\\REST_API\\Test_pytest\\a.csv'

    with open(path, newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        next(data)  # skip header row
        for row in data:
            test_data.append(row)
    return test_data


