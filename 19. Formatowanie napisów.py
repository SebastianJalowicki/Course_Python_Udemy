message1 = 'Processing file %s'
print(message1 % ('file_1.txt'))

message2 = 'File %s has size %d KB'
print(message2 % ('file_1.txt',100))

# wartośc po % zakłada islość znaków zarezerwowanych do wyświetlenia

message3 = 'File %20s has size %10d KB'
print(message3 % ('file_1.txt',100))

message4 = 'Proccesing file {0:s}'
print(message4.format('file_1.txt'))

message5 = 'File {0:s} has size {1:d} KB'
print(message5.format('file_1.txt',100))

# zamiana miejscem d->s
message5_1 = 'File {1:s} has size {0:d} KB'
print(message5_1.format(100,'file_1.txt'))

# wartośc przed s...d zakłada islość znaków zarezerwowanych do wyświetlenia
message6 = 'File {0:20s} has size {1:10d} KB'
print(message6.format('file_1.txt',100))
