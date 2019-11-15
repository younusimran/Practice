def digitoflife(a):
    str_list = list(str(a))
    cont = True
    sum = 0
    while cont:
        for i in str_list:
            sum += int(i)
        if sum < 10:
            cont = False
        else:
            str_list = list(str(sum))
            sum = 0
    return sum    

try:
    dob = int(input("Enter date of birth in DDMMYYYY or MMDDYYYY or YYYYMMDD: "))
    result = digitoflife(dob)
    print(result)
except:
    print("incorrect or in wrong format, date of birth is entered")

