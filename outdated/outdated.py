dates = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        da = input("Date: ")
        if "/" in da:
            mmm, ddd, yyy = da.split("/")
            mmm, ddd, yyy = int(mmm), int(ddd), int(yyy)
            if int(mmm) > 12:
                continue
            elif int(ddd) > 31:
                continue
            elif int(mmm) < 10 and int(ddd) > 9:
                print(f"{yyy}-0{mmm}-{ddd}")
                break
            elif int(ddd) < 10 and int(mmm) > 9:
                print(f"{yyy}-{mmm}-0{ddd}")
                break
            elif int(ddd) < 10 and int(mmm) < 10:
                print(f"{yyy}-0{mmm}-0{ddd}")
                break
            else:
                print(f"{yyy}-{mmm}-{ddd}")
                break
        elif "/" not in da:
            md, y = da.split(",")
            yy = y.strip(" ")
            m, d = md.split(" ")
            mm = dates.index(m)
            mm, d = int(mm), int(d)
            if not any (item in m for item in dates):
                continue
            elif int(d) > 31:
                continue
            elif int(mm) > 11:
                continue
            elif int(mm) < 9 and int(d) > 9:
                print(f"{yy}-0{mm+1}-{d}")
                break
            elif int(d) < 10 and int(mm) > 8:
                print(f"{yy}-{mm+1}-0{d}")
                break
            elif int(d) < 10 and int(mm) < 9:
                print(f"{yy}-0{mm+1}-0{d}")
                break
            else:
                print(f"{yy}-{mm+1}-{d}")
                break
    except ValueError:
        continue
