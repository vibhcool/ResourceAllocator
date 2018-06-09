
class User(object):
    '''
        User to whom, the servers are allocated, This class can be inherited
        to add more features like authentication, etc
    '''

    def __init__(self, name, email, servers=None):
        '''
            Return self object with attributes:

            1) name: Name of the user
            2) email: Email of the user
            3) servers: List of Servers grouped according to the regions
        '''
        self.name = name
        self.email = email
        if servers is None:
            self.servers = servers
        else:
            self.servers = []

    def __str__(self):
        ''' Returns self as string object '''
        output = ''
        output += 'Name:\t' + self.name + '\n'
        output += 'Email:\t' + self.email + '\n'
        output += 'Servers per Regions:\n'
        output = self.print_servers(output)
        return output

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_email(self, price):
        self.email = email

    def set_servers(self, servers):
        self.servers = servers

    def get_servers(self):
        return self.servers

    def print_servers(self, output):
        for servers_group in self.servers:
            for i in servers_group:
                if i is not 'servers':
                    output += '\t' + i + ' :\t' + str(servers_group[i]) + '\n'
                else:
                    output += '\t\tServers:' + '\n'
                    for server in servers_group['servers']:
                        output += '\t\t\tserver-type:' + server[0]
                        output += '\t\t server-count:' + str(server[1]) + '\n'
        return output
