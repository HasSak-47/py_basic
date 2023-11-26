#!/bin/python/

length = int(input('lenght: '))
arr = []

for i in range(length):
    arr.append(int(input('val: ')))

total = 0.
for v in arr:
    total += v
total /= length

print('average: ', total)
