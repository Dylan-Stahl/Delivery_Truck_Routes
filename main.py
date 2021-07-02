from user_interface import *
from data_loader import *
from packages import *


# Name: Dylan Stahl
# Student ID: 002996740

# For major blocks of code space-time complexity is described in comments

# The main function runs when the program is run. The function provides a console user interface and directs the user
# to type 1, 2, 3, 4, or 5 to access/write data and type quit when exiting the application.
def main():
    # Most of the options within the user interface involve working with the packages' data. The load_packages
    # function which comes from the file, data_loader.py is called on the CSV file packages.csv which holds the
    # package data. The load_packages function creates package objects and stores them in a hash table using the
    # package id as the key.
    # Space and Time Complexity for load_packages() -> O(N)
    load_packages('CSV_files/packages.csv')

    print('Welcome to Western Governors University Parcel Service (WGUPS), this program has found an efficient route '
          'and delivery distribution for Daily Local Deliveries (DLD). \n')

    # Assigns the variable user_input None so that the variable is declared. This variable will be overwritten by the
    # user input when making selections.
    user_input = None
    while user_input != 'quit':
        print('Press 1 to check the status of a package')
        print('Press 2 to view the status and info of all packages at a specified time, and the total mileage driven '
              'by each truck')
        print('Press 3 to view the end of day result')
        print('Press 4 to insert a new package')
        print('Press 5 to reset the packages to the original list')
        print('Type \'quit\' to exit the application \n')
        print()

        user_input = (input(''))

        if user_input == '1':
            # These variables collect the data needed to search for the package in which the user would like to
            # check the status of.
            package_id_input = (input('Enter the ID of the package: '))
            time_input = input('Enter the time in which you would like to check the package status (HHMM) or enter '
                               'EOD to view the package results at the end of the day: ')

            # Try except blocks are used to ensure that the program will not crash when incorrect data is entered,
            # like time input and package id.
            if time_input != 'EOD':
                try:
                    # time_input_datetime collects the correct hour and minute but do not get the current year, month,
                    # or day. To set the current year, month, and day an instance of datetime.today() is made. From that
                    # instance the current year, month, and day can be obtained. time_input_datetime's year, month, and day
                    # can be set to these values using the replace method.
                    time_input_datetime = datetime.datetime.strptime(time_input, "%H%M")

                    current_date = datetime.datetime.today()
                    current_year = current_date.year
                    current_month = current_date.month
                    current_day = current_date.day
                    # time_input_datetime can now be used to compare against the package's current status
                    time_input_datetime = time_input_datetime.replace(year=current_year, month=current_month,
                                                                      day=current_day)
                    try:
                        # If the package id is not a digit, the status can not be obtained as an integer is needed.
                        if package_id_input.isdigit():
                            # Space and Time Complexity of package_status -> O(N^2)
                            package_status(package_hash.search(int(package_id_input)), time_input_datetime)
                        else:
                            print('Enter a valid integer value for the package you are looking for')
                    except Exception as e:
                        print('Enter a valid package ID!')
                except Exception as e2:
                    print("Please enter correct time in HHMM format")

            # If the user wants to view the package status at the end of day this elif block is run.
            # Try and except blocks are used to ensure correct data is entered.
            elif time_input == 'EOD':
                try:
                    # If the package id is not a digit, the status can not be obtained as an integer is needed.
                    if package_id_input.isdigit():
                        # Space and Time Complexity of package_status -> O(N^2)
                        package_status(package_hash.search(int(package_id_input)), time_input)
                    else:
                        print('Enter a valid integer value for the package you are looking for')
                except Exception as e:
                    print('Enter a valid package ID!')

        elif user_input == '2':
            time_input = input(
                'Enter the time in which you would like to check the status of all truck and packages (HHMM): ')

            try:
                # time_input_datetime collects the correct hour and minute but do not get the current year, month,
                # or day. To set the current year, month, and day an instance of datetime.today() is made. From that
                # instance the current year, month, and day can be obtained. time_input_datetime's year, month, and day
                # can be set to these values using the replace method.
                time_input_datetime = datetime.datetime.strptime(time_input, "%H%M")
                current_date = datetime.datetime.today()
                current_year = current_date.year
                current_month = current_date.month
                current_day = current_date.day

                # time_input_datetime can now be used to compare against the package's current status
                time_input_datetime = time_input_datetime.replace(year=current_year, month=current_month,
                                                                  day=current_day)

                # The function results_at_specified_time is located in the user_interface.py file. It is a modified
                # end_of_day_result function that displays the route at a specified time. The package's status and
                # whether or not that package was delivered is correctly set based on the time the user is looking
                # at the route.
                # Space and Time Complexity of results_at_specified_time -> O(N^2)
                results_at_specified_time(time_input_datetime)
            except:
                print("Please enter correct time in HHMM format \n")

        elif user_input == '3':
            # The function end_of_day_result is located in the user_interface.py file. It displays the packages on each
            # truck, the package information, the path for the truck, the distance traveled per truck, and the total
            # distance traveled across all three trucks.
            # Space and Time Complexity of end_of_day_result -> O(N^2)
            end_of_day_result()

        elif user_input == '4':
            # Obtains data needed to create a package object
            print('Please enter the package information carefully, it is case sensitive.')
            package_id = input('Enter the package id (Must be unique, any id after 40 and before 49: \n')
            package_address = input('Enter the package address (must be a location in the spreadsheet): \n')
            package_deadline = input('Enter the package deadline (No guarantee delivery before 10:30) or EOD. HHMM '
                                     'format: ')
            package_city = input('Enter the package\'s delivery city: ')
            package_zip = input('Enter the package\'s delivery zip code: ')
            package_weight = input('Enter the package\'s weight in pounds: ')
            # package_city = 'Salt Lake City'
            package_state = 'Utah'
            package_notes = 'None'

            # Try except block is used to ensure correct time format is entered. Error message printed to user if
            # the wrong format is entered.
            if package_deadline != 'EOD':
                try:
                    # package_deadline collects the correct hour and minute but do not get the current year, month,
                    # or day. To set the current year, month, and day an instance of datetime.today() is made. From
                    # that instance the current year, month, and day can be obtained. time_input_datetime's year,
                    # month, and day can be set to these values using the replace method.
                    package_deadline = datetime.datetime.strptime(package_deadline, "%H%M")
                    current_date = datetime.datetime.today()
                    current_year = current_date.year
                    current_month = current_date.month
                    current_day = current_date.day

                    # package_deadline can now be used to compare against the package's current status
                    package_deadline = package_deadline.replace(year=current_year, month=current_month,
                                                                day=current_day)
                except:
                    print('Incorrect time format!')

            # The package file contains 40 packages. The max number of packages that can be loaded on all the trucks
            # is 48 packages. Also, if two many packages are entered, than the deadlines will be harder to meet. This
            # if statement is not ideal for scalability but more information would be needed as to how new package data
            # will be given to the system each time it is used.
            if 40 < int(package_id) < 49 and package_hash.search(package_id) is None:
                # Creates a new package object given the user input.
                new_package = Package(int(package_id), package_address, package_city, package_state, package_zip,
                                      package_deadline, package_weight, package_notes)
                try:
                    # Inserts package into the hash table so that the load trucks function can access it.
                    package_hash.insert(int(package_id), new_package)
                    # load_trucks is located in the truck.py file and is an algorithm that sorts the packages into
                    # trucks that will make the nearest neighbor algorithm more efficient. For example, it will try
                    # to add packages that have the same address to the same truck so that more than 1 truck are
                    # going to the same location. The new package will now be in a truck object that is stored in a
                    # hash table of it's own, truck_hash.
                    load_trucks()

                except Exception as e:
                    print(e.with_traceback())
            else:
                print('Package id must be after 40 and before 49 and also be unique!')

        elif user_input == '5':
            # The packages hash table will be reset and be loaded with all the data from the packages.csv file
            load_packages('CSV_files/packages.csv')


# __name__ is the current file's name. The program runs the main.py file and this if statement evaluates to True and
# runs the main function.
if __name__ == '__main__':
    main()
