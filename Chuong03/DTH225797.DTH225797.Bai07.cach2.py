print("Chương trình đếm ngày!!")
import datetime
day=int(input("Nhập ngày:"))
month=int(input("Nhập tháng:"))
year=int(input("Nhập năm:"))
date=datetime.datetime(year, month, day)
date += datetime.timedelta(days=1)
print("Ngày tiếp theo là ngày:",date.strftime("%d/%m/%Y"))