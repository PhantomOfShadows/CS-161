#print a whole number in decimal, binary, and hex
w_num = 31 #whole number
print(f'Decimal: {w_num}, Binary: {bin(w_num)}, Hex: {hex(w_num)}')

print('----------------------')

#find error for printing floating point numbers
d_num = 18 #decimal 18
print(f'Decimal: {d_num}, Binary: {bin(d_num)}, Hex: {hex(d_num)}')
#TypeError: 'float' object cannot be interpreted as an integer
#bin() and hex() require integers, not floating point numbers

print('----------------------')

#using binary and hex numbers for variables
b_num = 0b1011 #binary 11
h_num = 0xA3 #hex 163
print(b_num, h_num)

print('----------------------')

#adding different number systems
adding = d_num + b_num + h_num
print(f'The sum is: ', adding)

print('----------------------')

#percent of compression
ot_size = 240 #original text size
d_size = 25 #dictionary size
ct_size = 148 #compressed text size
pc_ur = (1 - ((ct_size + d_size) / ot_size)) * 100 #percent of compression un-rounded
pc_r = round(pc_ur, 2) #percent of compression rounded to the first 2 decimal points
print(f'Compressed Text Size: {ct_size} characters\n'
      f'     Dictionary Size: {d_size} characters\n'
      f'               Total: {ct_size + d_size} characters\n'
      f'  Original Text Size: {ot_size} characters\n'
      f'         Compression: {pc_r}%')

print('----------------------')
