from user_interface import *
from data_loader import *
from packages import *


# Name: Dylan Stahl
# Student ID: 002996740

def main():
    load_packages('CSV_files/packages.csv')
    print('Welcome to Western Governors University Parcel Service (WGUPS), this program has found an efficient route '
          'and delivery distribution for Daily Local Deliveries (DLD). \n')
    user_input = '1'
    while user_input != 'quit':

        # 1 is complete
        print('Press 1 to check the status of a package')
        # 2 is complete
        print('Press 2 to view the status and info of all packages at a specified time, and the total mileage driven '
              'by each truck')
        # 3 is complete
        print('Press 3 to view the end of day result')
        # Working on
        print('Press 4 to insert a new package')
        print('Press 5 to reset the packages to the original list')
        print('Type \'quit\' to exit the application \n')
        print()

        user_input = (input(''))

        if user_input == '1':
            package_id_input = (input('Enter the ID of the package: '))
            time_input = input('Enter the time in which you would like to check the package status (HHMM): ')

            try:
                time_input_datetime = datetime.datetime.strptime(time_input, "%H%M")
                current_date = datetime.datetime.today()
                current_year = current_date.year
                current_month = current_date.month
                current_day = current_date.day
                time_input_datetime = time_input_datetime.replace(year=current_year, month=current_month,
                                                                  day=current_day)
                try:
                    if package_id_input.isdigit():
                        # load_packages('CSV_files/packages.csv')
                        package_status(package_hash.search(int(package_id_input)), time_input_datetime)
                    else:
                        print('Enter a valid integer value for the package you are looking for')
                except Exception as e:
                    print('Enter a valid package ID!')
                    #print(e.with_traceback())

            except Exception as e2:

                print("Please enter correct time in HHMM format")
                #print(e2.with_traceback())

        elif user_input == '2':
            time_input = input(
                'Enter the time in which you would like to check the status of all truck and packages (HHMM): ')

            try:
                time_input_datetime = datetime.datetime.strptime(time_input, "%H%M")
                current_date = datetime.datetime.today()
                current_year = current_date.year
                current_month = current_date.month
                current_day = current_date.day
                time_input_datetime = time_input_datetime.replace(year=current_year, month=current_month,
                                                                  day=current_day)

                results_at_specified_time(time_input_datetime)
            except:
                print("Please enter correct time in HHMM format \n")

        elif user_input == '3':
            end_of_day_result()

        elif user_input == '4':
            print('Please enter the package information carefully, it is case sensitive.')
            package_id = input('Enter the package id (Must be unique, any id after 40 and before 47: \n')
            package_address = input('Enter the package address (must be a location in the spreadsheet): \n')
            package_deadline = input('Enter the package deadline (No guarantee delivery before 10:30). HHMM format: ')
            package_city = input('Enter the package\'s delivery city: ')
            package_zip = input('Enter the package\'s delivery zip code: ')
            package_weight = input('Enter the package\'s weight in pounds: ')
            # package_city = 'Salt Lake City'
            package_state = 'Utah'
            package_notes = 'None'
            try:
                package_deadline = datetime.datetime.strptime(package_deadline, "%H%M")
                current_date = datetime.datetime.today()
                current_year = current_date.year
                current_month = current_date.month
                current_day = current_date.day
                package_deadline = package_deadline.replace(year=current_year, month=current_month,
                                                                  day=current_day)
            except:
                print('Incorrect time format!')

            if 40 < int(package_id) < 47 and package_hash.search(package_id) == None:
                # need a function that inserts a package into the hash table, will need to create package object first
                new_package = Package(int(package_id), package_address, package_city, package_state, package_zip,
                                      package_deadline, package_weight, package_notes)
                try:
                    # load_packages('CSV_files/packages.csv')
                    package_hash.insert(int(package_id), new_package)
                    load_trucks()

                except Exception as e:
                    print(e.with_traceback())
            else:
                print('Package id must be after 40 and before 47 and also be unique!')

        elif user_input == '5':
            load_packages('CSV_files/packages.csv')


if __name__ == '__main__':
    main()
