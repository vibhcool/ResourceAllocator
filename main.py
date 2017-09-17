from Model.Server import Server

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

def get_costs(instances, hours, cpus=-1, money=-1.0):

    server_list = get_server_list(instances, hours)
    result = []
    return result

print(get_costs(k, 10, 20, 23.02))
