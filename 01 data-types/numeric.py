### Integers: represents positive or negative whole numbers without decimal points.
# Examples
integer1 = 10
integer2 = 85
integer3 = -120
integer4 = -6
integer5 = 0

# Use type() to get data type and print it on screen
print(type(integer1))


## Float: data type that represents real numbers with decimals.
# Examples
float1 = 10.23
float2 = 85.87
float3 = -120.61
float4 = -6.98732
float5 = 0.4

# Use type() to get data type and print it on screen
print(type(float4))


### Complex number: type of number that includes a real part and an imaginary part, represented by "j" (which is equivalent to the square root of -1).
# Examples
complex1 = complex(2, 3j)
complex2 = complex(18, 6j)
complex3 = complex(49, 12j)
complex4 = complex(67, 1j)
complex5 = complex(9, 98j)

# Use type() to get data type and print it on screen
print(type(complex1))


# More about complex numbers
data = complex(13.68, 98.74)

print('-----------------')
print(data)

print('-----------------')
print('Real part of data:', data.real)
print('Imaginary part of data:', data.imag)
print('-----------------')

el = 15j

print('el =',el)
print('Type of el is', type(el))
print('-----------------')