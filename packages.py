import datetime

date = datetime.date.today()


class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, package_notes, status='At the hub', time_delivered = datetime.datetime(date.year, date.month, date.day, 23, 59, 0),
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

    def get_id(self):
        return self.id

    def check_status_en_route(self):
        if self.time_delivered.hour == (23):
            time_delivered_str = ''
        else:
            time_delivered_str = ', Expected Delivery Time: ' + str(self.time_delivered)

        return 'ID = ' + str(self.id) + ', Address: ' + str(self.address) + ', Deadline: ' + str(self.deadline) \
               + ', City: ' + str(self.city) + ', Zip Code: ' + str(self.zip) + ', Weight: ' + str(self.mass) \
               + ', Status: ' + str(self.status) + ', Notes: ' + str(self.package_notes) + time_delivered_str

    def check_status_at_hub(self):
        if self.time_delivered.hour == (23):
            time_delivered_str = ''
        else:
            time_delivered_str = ', Expected Delivery Time: ' + str(self.time_delivered)

        return 'ID = ' + str(self.id) + ', Address: ' + str(self.address) + ', Deadline: ' + str(self.deadline) \
               + ', City: ' + str(self.city) + ', Zip Code: ' + str(self.zip) + ', Weight: ' + str(self.mass) \
               + ', Status: ' + str(self.status) + ', Notes: ' + str(self.package_notes) + time_delivered_str

    def __str__(self):
        if self.time_delivered.hour == (23):
            time_delivered_str = ''
        else:
            time_delivered_str = ', Time Delivered: ' + str(self.time_delivered)

        return 'ID = ' + str(self.id) + ', Address: ' + str(self.address) + ', Deadline: ' + str(self.deadline) \
               + ', City: ' + str(self.city) + ', Zip Code: ' + str(self.zip) + ', Weight: ' + str(self.mass) \
               + ', Status: ' + str(self.status) + ', Notes: ' + str(self.package_notes) + time_delivered_str

    def str(self):
        if self.time_delivered.hour == (23):
            time_delivered_str = ''
        else:
            time_delivered_str = ', Time Delivered: ' + str(self.time_delivered)

        return 'ID = ' + str(self.id) + ', Address: ' + str(self.address) + ', Deadline: ' + str(self.deadline) \
               + ', City: ' + str(self.city) + ', Zip Code: ' + str(self.zip) + ', Weight: ' + str(self.mass) \
               + ', Status: ' + str(self.status) + ', Notes: ' + str(self.package_notes) + time_delivered_str
