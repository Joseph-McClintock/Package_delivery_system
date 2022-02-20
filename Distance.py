import csv
import datetime
import ReadCSV

# Reads csv data
with open('./csvdata/WGUPS Distance Data.csv') as fp1:
    reader_d = csv.reader(fp1)
    package_distance = list(reader_d)

# List of addresses for a truck to visit
first_truck = []
second_truck = []
last_delivers = []


# Organizes the trucks and determines what addresses each truck need to visit - O(n^2)
def organize_truck(truck, package, organized_truck):
    organized_truck.append(package[0])
    for i in range(0, len(package)):
        for j in range(0, len(truck)):
            if truck[j][1] in package[i][2]:
                if package[i] not in organized_truck:
                    organized_truck.append(package[i])


# Converts miles to a time delta - O(1)
def miles_to_time(distance, start_time):
    time_delivered = distance / 18
    delivered_time = datetime.timedelta(hours=time_delivered)
    final_time = delivered_time + start_time
    return final_time


# Sets the packages status and depart time - O(n)
def set_packages_en_route_and_depart_time(packages, depart_time):
    for index, package_depart_time in enumerate(packages):
        ReadCSV.get_hash_map().get(str(package_depart_time[0]))[10] = 'EN ROUTE'
        ReadCSV.get_hash_map().get((package_depart_time[0]))[8] = depart_time


# Marks the as delivered once the packages address has been visited - O(n)
def set_delivered(delivered_time, address):
    for index in range(1, 41):
        if ReadCSV.get_hash_map().get(str(index))[1] in address:
            if ReadCSV.get_hash_map().get(str(index))[8] != '':
                if ReadCSV.get_hash_map().get(str(index))[9] == '':
                    ReadCSV.get_hash_map().get(str(index))[9] = delivered_time
                    ReadCSV.get_hash_map().get(str(index))[10] = 'DELIVERED'


# travels from address to address in a nearest neighbor fashion
def organize_truck_route(truck, depart_time, packages):
    set_packages_en_route_and_depart_time(packages, depart_time)
    smallest = 50.0
    total_miles = 0.0
    truck_indexes = []
    address_delivered_to = ''
    if len(truck) == 0:
        print('Truck has no packages to deliver')
        return

    for index in range(0, len(truck)):
        truck_indexes.append(int(truck[index][0]))

    for address, element in enumerate(truck):
        current_index = int(truck[address][0])
        for index, distance in enumerate(element[3:]):
            if smallest > float(distance) > 0.0:
                if index in truck_indexes and index != 0:
                    smallest = float(distance)
                    current_index = index

        if len(truck_indexes) > 1:
            truck_indexes.remove(current_index)
            total_miles += smallest

            for remove in range(0, len(truck)):
                if int(truck[remove][0]) == current_index:
                    truck.insert(address + 1, truck.pop(remove))

            print(miles_to_time(total_miles, depart_time), 'Packages delivered to', truck[address + 1][1])
            address_delivered_to = truck[address + 1][1]

        elif len(truck_indexes) == 1:
            smallest = float(element[3])
            total_miles += smallest
            print('Heading back to the HUB')

        set_delivered(miles_to_time(total_miles, depart_time), address_delivered_to)

        smallest = 50.0

    print('Total miles for truck', "{:.2f}".format(total_miles), '\n')
    return total_miles


# O(1)
def get_first_truck():
    return first_truck


# O(1)
def get_second_truck():
    return second_truck


# O(1)
def get_last_delivers():
    return last_delivers


# O(1)
def get_package_distance():
    return package_distance
