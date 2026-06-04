num=int(input("Enter a number:"))
count=0
rem=0
while(num!=0):
    rem=num%10
    count=count+1
    num=num//10
print(f"coun of digits {count}")