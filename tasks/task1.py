from random import randint
import numpy

number_list = []
for _ in range(10):
    number_list.append(randint(-100, 100))

arithmetic_mean = numpy.mean(number_list)
variance = numpy.var(numpy.array(number_list))

print(number_list)
print(round(variance, 3))
print(arithmetic_mean)
