# f = open('data.txt', 'r')
#
# data = f.readline()
#
# while data:
#     print(data)
#     data = f.readline()
# else:
#     print('EDF')

# f.close()

# f = open('data.txt', 'w')
# # f.write('Hello world\n')
# f.writelines(['Hello world\n', 'Hello world\n', 'Hello world\n'])
# f.close()

# f = open('data__3.txt', 'x')
# f.write('Hello world\n')
# f.close()

# f = open('data.txt', '')
# f.writelines(['Hello world\n', 'Hello world\n', 'Hello world\n'])
# f.close()

# f = open('data.txt', 'ab')
# # f.write(b'\nHello world\n')
# f.writelines([b'\nHello world\n', b'\nHello world\n', b'\nHello world\n'])
# f.close()

# with open('data.txt', 'a') as f:
#     f.write('Hello world\n')
#     f.write('Hello world 2\n')
#     f.write('Hello world 3\n')


# import os
#
# os.rename('data.txt', 'dataTest.txt')

contacts = {
    'John': {
        'age': 25,
        'phone': '+380000000001'
    },
    'Petr': {
        'age': 30,
        'phone': '+380000000002'
    }
}

# print(contacts)

# with open('contacts.txt', 'w') as f:
#     f.write(str(contacts))

# import pickle

# with open('contacts.txt', 'wb') as f:
#     pickle.dump(contacts, f)
#     bytes_source = pickle.dumps(contacts)
#     print(bytes_source)

#или

# with open('contacts.txt', 'wb') as f:
#     bytes_source = pickle.dumps(contacts)
#     f.write(bytes_source)
#     print(bytes_source)

# with open('contacts.txt', 'rb') as f:
#     from_file = pickle.loads(f.read())
#     #from_file = pickle.load(f)
# print(from_file)

import json

with open('contacts.json', 'w') as f:
    json.dump(contacts, f)

with open('contacts.json', 'r') as f:
    from_file = json.loads(f.read())
print(from_file)



