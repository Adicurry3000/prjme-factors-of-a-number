num = [2]
pfn = []

def prime(a):
    tem = []
    de = [1,a]
    p = int((a+1)/2) + 1
    for j in range(1,p):
        if a%j == 0:
            tem.append(j)
    tem.append(a)
    if tem == de:
        num.append(a)



def pf(a):
    for k in range(0,len(num)):
        if a%num[k] == 0:
            pfn.append(num[k])
    print('prime factor numbers are')
    print(pfn)
    if pfn == []:
        print(a ,"is a prime number")

    

def main():
    
    a = int(input("enter \n"))
    i=3
    while i<=a/2:
        prime(i)
        i+=1
    pf(a)
    # print(num)

main()