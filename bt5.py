chieu_cao = int(input("nhap chieu cao:"))
can_nang = int(input("nhap can nang:"))
bmi = can_nang / (chieu_cao*2)
if bmi >40:
    print("beo phi cap do III")
elif bmi >= 35 and bmi <40:
    print("beo phi cap do II")
elif bmi >=30 and bmi <35:
    print("beo phi cap do I")
elif bmi >=25 and bmi <30:
    print("thua can")
elif bmi >=18.5 and bmi <25:
    print("binh thuong")
elif bmi >= 17 and bmi <18.5:
    print("gay cap do I")
elif bmi >= 16 and bmi <17:
    print("gay cap do II")
else:
    print("gay cap do III")
