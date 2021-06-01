import numpy

num = numpy.arange(0, 20)

my_mean = numpy.mean(num)
my_var = numpy.var(num)
my_dev = numpy.std(num)


print("The mean is: ", my_mean)
print("The variance is: ", my_var)
print("The standard deviation is: ", my_dev)
