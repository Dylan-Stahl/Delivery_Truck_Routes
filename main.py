from data_loader import load_packages
from data_loader import package_hash

load_packages('packages.csv')
result = package_hash.search(1)
print(result)
print('test git')
