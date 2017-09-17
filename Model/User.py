
class User(object):

    servers = []

    def __init__(name, email):
        self.name = name
        self.email = email

    def __init__(name, email, servers):
        self.name = name
        self.email = email
        self.servers = servers

    def set_name(name):
        self.name = name

    def get_name():
        return self.name

    def get_email():
        return self.email

    def set_email(price):
        self.email = email

    def set_servers(data_center):
        self.servers = servers

    def get_servers():
        return self.servers
