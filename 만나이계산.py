from datetime import datetime, timedelta

birth  = input("when was your birthday? YYYY.MM.DD : ")

yy = int(birth[0:4])
mm = int(birth[5:7])
dd = int(birth[8:10])

ny = datetime.today().year
nm = datetime.today().month
nd = datetime.today().day

age = ny - yy

if (nm>=mm and nd >= dd): #생일과 현재 날짜 비교
    print(age) # 생일 지났으면 -1살
else:
    print(age-1) #생일 안 지났으면 -2살
