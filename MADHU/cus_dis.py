bill =int(input("enter your total bill="))

if(bill>500):
    disBill = bill *0.9
    print(f"your bill is above 500 you have 10% discount the total bill is {disBill}")
else:
    print(f"your bill is belowe 500 you not get the discount")