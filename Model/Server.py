
class Server():

    cpu_count = 0
    price = 0
    price_per_cpu = 0
    data_center = ''
    server_type = ''

    def __init__(self, cpu_count, price, data_center, hours, server_type):
        self.cpu_count = cpu_count
        self.price = price * hours
        self.data_center = data_center
        self.price_per_cpu = (self.price/self.cpu_count)
        self.server_type = server_type

    def price_per_cpu(self):
        return self.price_per_cpu

    def set_cpu_count(self, cpu_count):
        self.cpu_count = cpu_count

    def get_cpu_count(self):
        return self.cpu_count

    def get_price(self):
        return self.cpu_count

    def set_price(self, price):
        self.price = price

    def set_data_center(self, data_center):
        self.data_center = data_center

    def get_data_center(self):
        return self.cpu_count
