while True:
    print("Enter E to exit")
    x=str(input('Enter the string :'))
    if x=="E":
      break
    x1=x.replace(" ","")
    if x1==x1[::-1]:
        print("Yes")
    else:
        print("No")
