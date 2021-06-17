class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, package_notes, status='At the hub'):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.package_notes = package_notes
        self.status = status

    def get_id(self):
        return self.id

    def __str__(self):
        return 'ID: ' + str(self.id) + ' | Address: ' + str(self.address) + ' | Deadline: ' + str(self.deadline) \
               + ' | City: ' + str(self.city) + ' | Zip Code: ' + str(self.zip) + ' | Weight: ' + str(self.mass) \
               + ' | Status: ' + str(self.status)

    def str(self):
        return 'ID: ' + str(self.id) + ', Address: ' + str(self.address) + ', Deadline: ' + str(self.deadline) \
               + ', City: ' + str(self.city) + ', Zip Code: ' + str(self.zip) + ', Weight: ' + str(self.mass) \
               + ', Status: ' + str(self.status) + ', Notes: ' + str(self.package_notes)
