def isPrimerNumber(num):#kiem tra mot so co nguyen to hay ko
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        isPrimeNum = True;
        for i in range(2, num):
            if num % i == 0:
                isPrimeNum = False;
                break
        if isPrimeNum == True:
            return True
        else:
            return False

n = int(input("Nhap vao mot so nguyen: "))
for i in range(1,n):#duyet tu 1 den n
    if(isPrimerNumber(i) == True):
        print(i)