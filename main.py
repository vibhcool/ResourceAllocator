from Model.Server import Server
from Model.User import User

type_server = {
    'large': 1,
    'xlarge': 2,
    '2xlarge': 4,
    '4xlarge': 8,
    '8xlarge': 16,
    '10xlarge': 32,
}

k = {
        "us-east": {
            "large": 0.12,
            "xlarge": 0.23,
            "2xlarge": 0.45,
            "4xlarge": 0.774,
            "8xlarge": 1.4,
            "10xlarge": 2.82
        },
        "us-west": {
            "large": 0.14,
            "2xlarge": 0.413,
            "4xlarge": 0.89,
            "8xlarge": 1.3,
            "10xlarge": 2.97
        },
        "us-north": {
            "large": 0.04,
            "2xlarge": 0.113,
            "4xlarge": 0.99,
            "8xlarge": 0.3,
            "10xlarge": 2.07
        },
    }

def get_server_list(instances, hours):
    server_list = []
    for data_center in instances.keys():
        for server in instances[data_center].keys():
            a = Server(type_server[server], instances[data_center][server], data_center, hours, server)
            server_list.append(a)
    return server_list

def format_result(allocated_servers, data_centers):
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
        server_list.sort(key=lambda x: x.cpu_count)
        while i < n and cpus > 0:
            if cpus >= server_list[i].cpu_count:
                total = cpus // server_list[i].cpu_count
                servers_allocated[server_list[i]] = total
                cpus -= total * server_list[i].cpu_count
                data_centers.add(server_list[i].data_center)
            i += 1
    return servers_allocated, data_centers

def get_costs(instances, hours, cpus=-1, money=-1.0):

    server_list = get_server_list(instances, hours)
    result = []
    allocated_servers, data_centers = servers_allocate(server_list, hours, cpus, money)
    result = format_result(allocated_servers, data_centers)
    return result

print(get_costs(k, 10, 20, 23.02))
