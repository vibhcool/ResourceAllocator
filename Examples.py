from main import *

server_dict = {
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
    }

# For min CPUs 23 and max price 23.5
print(get_costs(server_dict, 10, 23, 23.5))

# For min CPUs 23
print(get_costs(server_dict, 10, cpus=23))

# For max price 23.5
print(get_costs(server_dict, 10, price=23.5))
