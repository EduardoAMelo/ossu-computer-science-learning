import os
script_path = os.path.dirname(os.path.realpath(__file__))
path = f'{script_path}/teste.txt'

x = open(path)
file_test = x.read()
print(len(file_test))
print(file_test[:20])
