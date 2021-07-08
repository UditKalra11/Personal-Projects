import calendar
import datetime
print("Welcome To Calender")
while True:
    print("Choose from the following options :\n1. Show Year \n2. Show Month \n3. Go to date\n4.Today's Date\n5.Exit")
    option = int(input("\nENTER : "))

    if option == 1:
        year = int(input("Year : "))
        x = calendar.TextCalendar(calendar.SUNDAY)
        y = x.formatyear(year)
        print(y,"\n")

    if option == 2:
        year = int(input("Year : "))
        month = input("Month : ")
        month_name = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
                      'September': 9, 'October': 10, 'November': 11, 'December': 12}
        while month not in month_name:
            month = input("Please Input Valid Month : ")

        x = calendar.TextCalendar(calendar.SUNDAY)
        y = x.formatmonth(year, month_name[month])
        print(y,"\n")

    if option == 3:
        year = int(input("Year : "))
        month = input("Month : ")
        month_name = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
                      'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11',
                      'December': '12'}
        while month not in month_name:
            month = input("Please Input Valid Month : ")
        d = int(input("Date : "))
        if len(str(d)) == 1:
            d = "0" + str(d)
        else:
            d = str(d)

        date = d + " " + month_name[month] + " " + str(year)

        x = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        y = calendar.day_name[x]
        print(y,"\n")

    if option == 4:
        x = str(datetime.datetime.today()).split()[0]
        print("\nToday's Date :", x,"\n")

    if option == 5:
        exit()