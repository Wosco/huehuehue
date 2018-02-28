from phue import Bridge

b = Bridge('192.168.1.13')

sombraName=b.get_light(1,'name')

print(sombraName)