try:
    date = input("Дата в формате Д.М.Г (в однозначном значении дня не писать ноль первым символом, "
                 "если значение месяца однозначное, "
                 "перед числом месяца написать ноль. Пример: 1.02.2025, 27.11.1111): ").split(".")
    day = date[0]
    if day[0] == '0':
        day = day[1]
    month = date[1]
    year = date[2]
    if ((int(day) > 31 or int(day) < 1) or (int(day) > 30 and (
            month == '02' or month == '04' or month == '06' or
            month == '09' or month == '11')) or (month == '02' and int(day) > 28 and not (int(year) % 400 == 0 or
                                                                                          (int(year) % 4 == 0 and
                                                                                           int(year) % 100 != 0))) or (
                not month[0] == '0'
                and 12 < int(month) > 1)
        or int(year) == 0) or month == '00' or (month[0] != '0' and month[0] != '1') or len(month) != 2:
        print("Даты не существует")
    else:
        print("Дата существует")
except:
    print("Дата введена неправильно и её не существует")
