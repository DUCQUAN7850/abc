from collections import Counter
#doc file
f = open('input2.txt', 'r')
strs= f.read()
print ('Noi dung file la:\n', strs)
#đếm số lần  xuất hiện của mỗi từ phân biệt nhau bằng dấu cách
print ('So lan xuat hien cua moi tu la: ',Counter(map(str.lower,strs.split())))
#ghi ra file kết quả thu được
file = open("output2.txt", "w")
file.write(str(Counter(map(str.lower,strs.split()))))
file.close()