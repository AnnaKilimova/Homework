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

f = open('data.txt', 'x')
f.writelines(['Hello world\n', 'Hello world\n', 'Hello world\n'])
f.close()


