#ahmad luthfi hanif, tutorial 10

try:
    x=input('penyebut : ')
    y=input('pembilang : ')
    result=y/x
except ValueError:
    print('salah masukin data bang')
except ZeroDivisionError:
    print('masukkkin penyebut hati-hati boy')
finally:
    print('program selesai')
if y>3:
    raise Exception('pembilangnya banyak cuy')

print(result)
