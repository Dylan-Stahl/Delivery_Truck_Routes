import datetime
from hash_table_chaining import ChainingHashTable

date = datetime.date.today()
# Creates a hash table that sets the capacity to 49. This hash table is used to store all the packages.
package_hash = ChainingHashTable(49)


# Holds data regarding each package
class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, package_notes, visited = False, status='At the '
                                                                                                             'hub',
                 time_delivered = datetime.datetime(date.year, date.month, date.day, 23, 59, 0),
                 number_on_truck=-1):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.package_notes = package_notes
        self.status = status
        self.number_on_truck = number_on_truck
        self.time_delivered = time_delivered
        self.visited = visited

    # Returns package id -> O(1)
    def get_id(self):
        return self.id

    # Returns proper status for a package that is en route -> O(1)
    def check_status_en_route(self, time):
        if self.time_delivered.hour == (23):
            time_delivered_str = ''
        else:
            if self.time_delivered < time:
                time_delivered_str = ', Time Delivered: ' + str(self.time_delivered)
            elif self.time_delivered >= time:
                time_delivered_str = ', Expected Delivery Time: ' + str(self.time_delivered)

        return 'ID = ' + str(self.id) + ', Address: ' + str(self.address) + ', Deadline: ' + str(self.deadline) \
               + ', City: ' + str(self.city) + ', Zip Code: ' + str(self.zip) + ', Weight: ' + str(self.mass) \
               + ', Status: ' + str(self.status) + ', Notes: ' + str(self.package_notes) + time_delivered_str

    # Returns proper status for a package that is at the hub -> O(1)
    def check_status_at_hub(self):
        if self.time_delivered.hour == (23):
            time_delivered_str = ''
        else:
            time_delivered_str = ', Expected Delivery Time: ' + str(self.time_delivered)

        return 'ID = ' + str(self.id) + ', Address: ' + str(self.address) + ', Deadline: ' + str(self.deadline) \
               + ', City: ' + str(self.city) + ', Zip Code: ' + str(self.zip) + ', Weight: ' + str(self.mass) \
               + ', Status: ' + str(self.status) + ', Notes: ' + str(self.package_notes) + time_delivered_str

    # Returns special formatting for when a package is printed. Package's time delivered hour are set to a default of
    # 23:59. All the trucks finish before then and set the package delivered time as something else. If the package
    # time delivered has not changed, than the package has not been delivered and should not be displayed -> O(1)
    def __str__(self):
        if self.time_delivered.hour == (23):
            time_delivered_str = ''
        else:
            time_delivered_str = ', Time Delivered: ' + str(self.time_delivered)

        return 'ID = ' + str(self.id) + ', Address: ' + str(self.address) + ', Deadline: ' + str(self.deadline) \
               + ', City: ' + str(self.city) + ', Zip Code: ' + str(self.zip) + ', Weight: ' + str(self.mass) \
               + ', Status: ' + str(self.status) + ', Notes: ' + str(self.package_notes) + time_delivered_str

    # Returns special formatting for when a package is printed. Package's time delivered hour are set to a default of
    # 23:59. All the trucks finish before then and set the package delivered time as something else. If the package
    # time delivered has not changed, than the package has not been delivered and should not be displayed -> O(1)
    def str(self):
        if self.time_delivered.hour == (23):
            time_delivered_str = ''
        else:
            time_delivered_str = ', Time Delivered: ' + str(self.time_delivered)

        return 'ID = ' + str(self.id) + ', Address: ' + str(self.address) + ', Deadline: ' + str(self.deadline) \
               + ', City: ' + str(self.city) + ', Zip Code: ' + str(self.zip) + ', Weight: ' + str(self.mass) \
               + ', Status: ' + str(self.status) + ', Notes: ' + str(self.package_notes) + time_delivered_str
