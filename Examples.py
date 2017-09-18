from main import *

#For min CPUs 23 and max price 23.5
print(get_costs(k, 10, 23, 23.5))

#For min CPUs 23
print(get_costs(k, 10, cpus=23))

#For max price 23.5
print(get_costs(k, 10, money=23.5))
