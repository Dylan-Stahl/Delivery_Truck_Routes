from user_interface import *
from data_loader import *


# Name: Dylan Stahl
# Student ID: 002996740

def main():
    print('Welcome to Western Governors University Parcel Service (WGUPS), this program has found an efficient route '
          'and delivery distribution for Daily Local Deliveries (DLD). \n')
    user_input = '1'
    while user_input != 'quit':

        # 1 is complete
        print('Press 1 to check the status of a package')
        #
        print('Press 2 to view the status and info of all packages at a specified time, and the total mileage driven '
              'by each truck')
        # 3 is complete
        print('Press 3 to view the end of day result')
        print('Press 4 to change the address of package 9, that has in the notes, \'wrong address listed\'')
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
                        load_packages('CSV_files/packages.csv')
                        package_status(package_hash.search(int(package_id_input)), time_input_datetime)
                    else:
                        print('Enter a valid integer value for the package you are looking for')
                except:
                    print('Enter a valid package ID!')

            except:
                print("Please enter correct time in HHMM format")

        elif user_input =='2':
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

        if user_input == '3':
            end_of_day_result()


if __name__ == '__main__':
    main()
