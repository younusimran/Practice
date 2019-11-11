import re

l1 ={1:['###','#','###','###','# #','###','###','###','###','###' ],
    2:['# #','#','  #','  #','# #','#  ','#  ','  #','# #','# #' ],
    3:['# #','#','###','###','###','###','###','  #','###','###' ],
    4:['# #','#','#  ','  #','  #','  #','# #','  #','# #','  #' ],
    5:['###','#','###','###','  #','###','###','  #','###','###' ],
}   

try:
    number = input("Enter number. May include alphabets and character followed by number: ")
    lst = list(number)
    length = len(lst)
    for row in range(5):
        if not re.match('^[0-9]', number):
            print("must start with numbers")
            break
        for num in lst:
            try:
                print(l1[(row+1)][int(num)], end = "  ")
            except:
                #continue
                if row == 2:
                    print(num, end="  ")
                else:
                    print(" ", end="  ")
        print("  ")
except ValueError:
    print("Wrong input")