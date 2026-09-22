from faker import Faker

import random
import string

class Random_Data:
    def __init__(self):
        self.fake = Faker()

    def get_first_name(self):
        return self.fake.first_name()
    def get_last_name(self):
        return self.fake.last_name()
    def get_full_name(self):
        return self.fake.full_name()
    def get_email(self):
        return self.fake.email()
    def get_phone_number(self):
        return self.fake.phone_number()
    def get_address(self):
        return self.fake.address()
    def get_city(self):
        return self.fake.city()
    def get_state(self):
        return self.fake.state()
    def get_country(self):
        return self.fake.country()
    def get_zip_code(self):
        return self.fake.zipcode()
    def get_company_name(self):
        return self.fake.company()
    def get_date_of_birth(self):
        return self.fake.date_of_birth()
    def get_random_string(self, length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
    def  get_randon_number(self,start=0,end=1000):
        return random.randint(start,end)
    
