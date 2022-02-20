import csv
from HashTable import HashMap

# Reads csv data
with open("./csvdata/WGUPS Package File.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')

    # Hashmap of all the packages
    hashmap = HashMap()

    # List of packages that need to be delivered
    first_deliveries = []
    second_deliveries = []
    third_deliveries = []

    # Parses each row in the csv file and assigns them to certain values - O(n)
    for row in reader:
        id_column = row[0]
        address_column = row[1]
        city_column = row[2]
        state_column = row[3]
        postal_code_column = row[4]
        deliver_by_column = row[5]
        weight_column = row[6]
        special_instructions_column = row[7]
        depart_time = ''
        arrival_time = ''
        delivery_status = 'AT HUB'

        data = [id_column, address_column, city_column, state_column, postal_code_column, deliver_by_column,
                weight_column, special_instructions_column, depart_time, arrival_time, delivery_status]

        # Determines what packages to add each package list
        if 'Can only' in data[7] or 'Delayed' in data[7] or '84106' in data[4] and '29' not in data[0]:
            second_deliveries.append(data)
        elif 'Delayed' not in data[7] and 'EOD' not in data[5] or 'Wrong' in data[7] and 'Must be' in data[7] \
                or '84115' in data[4]:
            first_deliveries.append(data)
        elif 'Wrong' in data[7]:
            first_deliveries.append(data)
        else:
            third_deliveries.append(data)

        hashmap.insert(id_column, data)


# O(1)
def get_hash_map():
    return hashmap


# O(1)
def get_first_deliveries():
    return first_deliveries


# O(1)
def get_second_deliveries():
    return second_deliveries


# O(1)
def get_third_deliveries():
    return third_deliveries
