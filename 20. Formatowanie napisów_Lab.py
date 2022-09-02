helloMessage = 'Hello %s!'
print(helloMessage % ('Kate'))
print(helloMessage % ('Chris'))

helloMessage1 = 'Hello {0:s}!'
print(helloMessage1.format('Kate'))
print(helloMessage1.format('Chris'))

helloMessage2 = '%s has %d %s'
print(helloMessage2 % ('Kate', 1, 'animal'))
print(helloMessage2 % ('Chris', 100000, '$'))

helloMessage3 = '{0:s} has {1:d} {2:s}'
print(helloMessage3.format('Kate', 1, 'animal'))
print(helloMessage3.format('Chris', 100000, '$'))

line = '{0:20s} costs {1:6d} €'
print(line.format('Ice Cream',3))
print(line.format('Trip do Venice', 119))
print(line.format('Pizza Hawai', 6))

line1 = '{0:s} {1:d}'
print(line1.format('Ice Cream', 3))
print(line1.format('Trip to Venice', 119))
print(line1.format('Pizza Hawai', 6))

