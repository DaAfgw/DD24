numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
ind = numbers.index (None)
fgw= numbers[:ind] + numbers[(ind+1):]
znach = sum(fgw) / (len(fgw)+1)
numbers[ind] = znach
print("Измененный список:", numbers)
