import math
from Model.Server import Server
from Model.User import User

'''
    Object to store processed info to not to process again i.e. Dynamic
    Programming Data Structure
'''
dp = []

price_list = []

''' Types of servers and number of CPUs they have '''
type_server = {
    'large': 1,
    'xlarge': 2,
    '2xlarge': 4,
    '4xlarge': 8,
    '8xlarge': 16,
    '10xlarge': 32,
}


def get_server_list(instances, hours):
    '''
        Get list of all servers from dictionary of servers grouped according
        to data centers they belong
    '''
    server_list = []
    for data_center in instances.keys():
        for server in instances[data_center].keys():
            server_obj = Server(
                    type_server[server],
                    instances[data_center][server],
                    data_center,
                    hours,
                    server,
            )
            server_list.append(server_obj)
    return server_list


def format_result(allocated_servers, data_centers):
    '''
        Format the result in a data structure before output
        Like:
            [
                {'region': 'us-west',
                'total_cost': 13.0,
                'servers': [('8xlarge', 1.0)]
                },
                {'region': 'us-east',
                'total_cost': 10.040000000000001,
                'servers': [('4xlarge', 1.0),
                            ('xlarge', 1.0)]
                }
            ]
    '''
    result = []
    for data_center in data_centers:
        result_region = {'region': data_center}
        total_cost = 0.0
        servers = []
        for server in allocated_servers.keys():
            if server.data_center == data_center:
                total_cost += server.price * allocated_servers[server]
                server_tuple = server.server_type, allocated_servers[server]
                servers.append(server_tuple)
        result_region['total_cost'] = total_cost
        result_region['servers'] = servers
        result.append(result_region)
    return result


def servers_allocate(server_list, hours, cpus, money):
    ''' Allocating Servers program according to constraints given '''
    servers_allocated = {}
    data_centers = set()
    result = {}
    n = len(server_list)
    i = 0
    total = 0
    if cpus == -1:
        server_list.sort(key=lambda x: x.price_per_cpu)
        while i < n and money > 0:
            if money > server_list[i].price:
                total = money // server_list[i].price
                servers_allocated[server_list[i]] = total
                money -= total * server_list[i].price
                data_centers.add(server_list[i].data_center)
            i += 1
    elif money == -1:
        server_list.sort(key=lambda x: x.cpu_count, reverse=True)
        while i < n and cpus > 0:
            if cpus >= server_list[i].cpu_count:
                total = cpus // server_list[i].cpu_count
                servers_allocated[server_list[i]] = total
                cpus -= total * server_list[i].cpu_count
                data_centers.add(server_list[i].data_center)
            i += 1
    else:
        server_list.sort(key=lambda x: x.price_per_cpu)
        optimize(server_list, cpus)
        servers_allocated = get_best_price(cpus, money)
        for server in servers_allocated:
            data_centers.add(server.data_center)
    return servers_allocated, data_centers


def optimize(wt, W):
    '''
        Optimize the result before outputing allocated result. Algorithm used
        is a variant of Integer Knapsack problem.
    '''
    if len(dp) > W:
        return

    for x in range(len(dp), W - len(dp) + 1):
        dp.append([])
        price_list.append(0.0)

    n = len(wt)
    for i in range(0, W+1):
        if i != 0:
            dp[i] = []
            price_list[i] = math.inf
        for j in range(0, n):
            if wt[j].cpu_count <= i:
                if price_list[i] > price_list[i-wt[j].cpu_count] + wt[j].price:
                    dp[i] = list(dp[i-wt[j].cpu_count])
                    dp[i].append(wt[j])
                    price_list[i] = price_list[i-wt[j].cpu_count]+wt[j].price


def get_best_price(cpus, money):
    '''
        Allocate servers according to only 1 constraint, i.e. cost
    '''
    allocated = {}
    for i in range(cpus, len(dp)):
        if price_list[i] <= money:
            for i in dp[i]:
                try:
                    allocated[i] = allocated[i] + 1
                except KeyError:
                    allocated[i] = 1
            return allocated


def get_costs(instances, hours, cpus=-1, price=-1.0):
    '''
        Main driver function for allocation of servers according to
        specifications of the user
        Arguments are:

        1) instances: Dictionary of Servers with their type and respective
            price grouped according to the regions
        2) hours: No. of hours the servers needed by user

        3) cpus: minimum no. of CPUs needed by user. If there is no
            constraint, then it is set to -1.
        4) price: Maximum price user can pay for the servers. If no such
            constraint, set it to -1.0.
    '''
    server_list = get_server_list(instances, hours)
    result = []
    allocated_servers, data_centers = servers_allocate(
            server_list,
            hours,
            cpus,
            price
    )
    result = format_result(allocated_servers, data_centers)
    return result
