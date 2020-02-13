import datetime

data1 = datetime.date(day=5, month=3, year=2019)

data2 = datetime.date(day=20, month=1, year=31)

data2-data1

diferenca = abs((data1 - data2).date)



print (diferenca)
