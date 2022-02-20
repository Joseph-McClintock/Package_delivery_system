# Joseph McClintock #004154968

import datetime
import Distance
import ReadCSV


class Main:

    # Determines what addresses a truck needs to go to, to deliver it's loaded packages
    Distance.organize_truck(ReadCSV.get_first_deliveries(), Distance.get_package_distance(), Distance.get_first_truck())
    Distance.organize_truck(ReadCSV.get_second_deliveries(), Distance.get_package_distance(), Distance.get_second_truck())
    Distance.organize_truck(ReadCSV.get_third_deliveries(), Distance.get_package_distance(), Distance.get_last_delivers())

    # Runs and displays the user interface - Big O(n)
    while True:
        print('Welcome to the WGUPS Routing System\n')
        user_input = input('What would you like to do?\n\n' +
                           '1. Begin simulation\n' +
                           '2. To quit the program\n')

        # If the user selects 1 the simulation will begin - Big O(n)
        if user_input == '1':
            print('Starting simulation...')

            first_deliveries_start_time = datetime.timedelta(hours=8)
            second_deliveries_start_time = datetime.timedelta(hours=9.1)
            third_deliveries_start_time = datetime.timedelta(hours=10.5)

            print('-----------------------------------------------')
            print('Truck one delivering packages...')
            print('-----------------------------------------------')
            # Figures out the best route for truck one and executes that and saves the total miles of the trip
            truck_one_miles = Distance.organize_truck_route(Distance.get_first_truck(), first_deliveries_start_time, ReadCSV.get_first_deliveries())

            print('-----------------------------------------------')
            print('Truck two delivering packages...')
            print('-----------------------------------------------')
            # Figures out the best route for truck two and executes that and saves the total miles of the trip
            truck_two_miles = Distance.organize_truck_route(Distance.get_second_truck(), second_deliveries_start_time, ReadCSV.get_second_deliveries())

            ReadCSV.get_hash_map().get(str(9))[7] = 'Address corrected'
            ReadCSV.get_hash_map().get(str(9))[1] = '410 S State St'
            ReadCSV.get_hash_map().get(str(9))[10] = 'AT HUB'
            ReadCSV.get_hash_map().get(str(9))[9] = ''
            ReadCSV.get_third_deliveries().append(ReadCSV.get_hash_map().get(str(9)))
            print('-----------------------------------------------')
            print('Truck one, second trip, delivering packages...')
            print('-----------------------------------------------')
            # Figures out the best route for truck one trip two and executes that and saves the total miles of the trip
            truck_one_second_run_miles = Distance.organize_truck_route(Distance.get_last_delivers(), third_deliveries_start_time, ReadCSV.get_third_deliveries())
            print('Incorrect address for package 9 was corrected and put on the last trip and delivered successfully!\n')

            all_truck_miles = truck_one_miles + truck_two_miles + truck_one_second_run_miles
            print('All trucks drove a total of', all_truck_miles)
            break

        # Quits the program if the user inputs 2 at the beginning of the program
        elif user_input == '2':
            quit()

        # If the user input is neither 1 nor 2 then it will tell the user invalid input
        else:
            print('Invalid input please try again\n')

    # Asks the user what they would like to do after the simulation O(n)
    while True:

        user_input = input('\nWhat would you like to do next?\n\n' +
                           '4. Look up packages between two times\n' +
                           '5. Look up packages by one time\n' +
                           '6. To quit the program\n')

        # If the user inputs 4 it will prompt the user to select two times. And then checks the status of ALL packages between said times
        if user_input == '4':
            try:
                pick_a_time = input('Please pick the first time: example format 08:13:00 in military time\n')
                picked_time = datetime.datetime.strptime(pick_a_time, "%H:%M:%S")
                search_picked_time = datetime.timedelta(hours=picked_time.hour, minutes=picked_time.minute, seconds=picked_time.second)
                pick_a_time_2 = input('Please pick the second time: example format 10:45:00 in military time\n')
                picked_time_2 = datetime.datetime.strptime(pick_a_time_2, "%H:%M:%S")
                search_picked_time_2 = datetime.timedelta(hours=picked_time_2.hour, minutes=picked_time_2.minute, seconds=picked_time_2.second)

                # Displays all packages from the hashmap and their statuses at the given times - O(n)
                for x in range(1, 41):
                    print(ReadCSV.get_hash_map().get(str(x))[0], ' ', end='')
                    print(ReadCSV.get_hash_map().get(str(x))[1], ' ', end='')
                    print(ReadCSV.get_hash_map().get(str(x))[2], ' ', end='')
                    print(ReadCSV.get_hash_map().get(str(x))[3], ' ', end='')
                    print(ReadCSV.get_hash_map().get(str(x))[4], ' ', end='')
                    print(ReadCSV.get_hash_map().get(str(x))[5], ' ', end='')
                    print(ReadCSV.get_hash_map().get(str(x))[6], ' ', end='')
                    if search_picked_time <= ReadCSV.get_hash_map().get(str(x))[9] <= search_picked_time_2 or ReadCSV.get_hash_map().get(str(x))[9] < search_picked_time:
                        print(ReadCSV.get_hash_map().get(str(x))[9], 'DELIVERED')
                    elif ReadCSV.get_hash_map().get(str(x))[8] > search_picked_time_2:
                        print('AT HUB')
                    else:
                        print('EN ROUTE')
            except ValueError:
                print('Invalid input')

        # If the user inputs 5 it will prompt the user to select one time
        elif user_input == '5':
            try:
                pick_a_time = input('Please pick the first time: example format 08:13:00 in military time\n')
                picked_time = datetime.datetime.strptime(pick_a_time, "%H:%M:%S")
                search_picked_time = datetime.timedelta(hours=picked_time.hour, minutes=picked_time.minute, seconds=picked_time.second)
                search_by = input('\nWhat would you like to search by?\n\n' +
                                  'a - Search all packages\n' +
                                  'i - Lookup packages by ID\n')

                # If the user selects a, the program will output the status of all packages at the inputted time
                if search_by == 'a':
                    print('\nChecking the status for all packages at', search_picked_time, '\n')

                    # Displays all packages from the hashmap and their statuses at the given time - O(n)
                    for x in range(1, 41):
                        print(ReadCSV.get_hash_map().get(str(x))[0], ' ', end='')
                        print(ReadCSV.get_hash_map().get(str(x))[1], ' ', end='')
                        print(ReadCSV.get_hash_map().get(str(x))[2], ' ', end='')
                        print(ReadCSV.get_hash_map().get(str(x))[3], ' ', end='')
                        print(ReadCSV.get_hash_map().get(str(x))[4], ' ', end='')
                        print(ReadCSV.get_hash_map().get(str(x))[5], ' ', end='')
                        print(ReadCSV.get_hash_map().get(str(x))[6], ' ', end='')
                        if ReadCSV.get_hash_map().get(str(x))[9] < search_picked_time:
                            print(ReadCSV.get_hash_map().get(str(x))[9], 'DELIVERED')
                        elif ReadCSV.get_hash_map().get(str(x))[8] <= search_picked_time:
                            print('EN ROUTE')
                        if ReadCSV.get_hash_map().get(str(x))[8] > search_picked_time:
                            print('AT HUB')

                # If the user selects i, the program will output the status of all packages at the inputted time and with the matching ID
                elif search_by == 'i':
                    try:
                        search_by_id = int(input('Enter package ID:'))
                        print('\nChecking the status for all packages by', search_by_id, 'at', search_picked_time, '\n')

                        # Validates the packages' id, if valid it will then display the matching package and its status O(n)
                        if search_by_id > 41 or search_by_id < 1:
                            print('No package with the', search_by_id, 'found!')
                        else:
                            print(ReadCSV.get_hash_map().get(str(search_by_id))[0], ' ', end='')
                            print(ReadCSV.get_hash_map().get(str(search_by_id))[1], ' ', end='')
                            print(ReadCSV.get_hash_map().get(str(search_by_id))[2], ' ', end='')
                            print(ReadCSV.get_hash_map().get(str(search_by_id))[3], ' ', end='')
                            print(ReadCSV.get_hash_map().get(str(search_by_id))[4], ' ', end='')
                            print(ReadCSV.get_hash_map().get(str(search_by_id))[5], ' ', end='')
                            print(ReadCSV.get_hash_map().get(str(search_by_id))[6], ' ', end='')
                            if ReadCSV.get_hash_map().get(str(search_by_id))[9] < search_picked_time:
                                print(ReadCSV.get_hash_map().get(str(search_by_id))[9], 'DELIVERED')
                            elif ReadCSV.get_hash_map().get(str(search_by_id))[8] <= search_picked_time:
                                print('EN ROUTE')
                            if ReadCSV.get_hash_map().get(str(search_by_id))[8] > search_picked_time:
                                print('AT HUB')
                    except ValueError:
                        print('Invalid input')

            # Makes user what the user is inputting is valid
            except ValueError:
                print('Invalid input')

        # Exits the program
        elif user_input == '6':
            break


exit()
