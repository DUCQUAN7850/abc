from multiprocessing.pool import ThreadPool
def sum(a,b):#hàm tính tổng dãy số bắt đầu từ a và kết thúc ở b
    s=0
    n=int(a)
    m=int(b)
    for num in range (n, m):
        s=s+num
    return s

n=int(input('Nhap n: '))
pool = ThreadPool(processes=3)
#sau khi nhập vào n, thì sẽ chia dãy từ 1 đến n thành 3 phần bằng nhau, rồi tính tổng từng phần
t1 = pool.apply_async(sum, ('1',int(n/3)))
t2 = pool.apply_async(sum, (int(n/3),int(2*n/3)))
t3 = pool.apply_async(sum, (2*n/3,n))

k1 = t1.get()
k2 = t2.get()
k3 = t3.get()
#kết quả cuối cùng sẽ được cộng từ 3 phần vừa tính
print('Tong tu 1 den n la: ',k1+k2+k3)