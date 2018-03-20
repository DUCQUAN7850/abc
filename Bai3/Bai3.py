import random
class So: #tạo đối tượng So với thuộc tính là 2 số
    def __init__(so, a, b):#hàm khởi tạo
        so.a=a;
        so.b=b;
    def tostring(so):#hàm trả đối tượng So thành dạnh chuỗi
        return((so.a,so.b))
l=list()#tạo danh sách để lưu các điểm
while len(l)<1000:
    s=So(random.uniform(1,10000),random.uniform(1,100000))
    if(l.count(s.tostring())==0):#nếu điểm vừa tạo không có trong danh sách thì mới được thêm vào
        l.append(s.tostring())


file = open("output3.txt", "w")
for i in range(0, len(l)):#duyệt và ghi các phần tử của danh sách ra file
   print (l[i])
   file.write(str(l[i]))
file.close()