#ahmad luthfi hanif, tutorial 7
# procedure : diharapkan untuk berjalan tanpa ada expected output
# def = function : manggil kata lain

r = 12

def luaslingkaran(r):
    r=r+1
    luas=3.14*r*r

print (r)
print(luaslingkaran(r))


####################################

def input():
    x =int(input("masukkan angka :"))
    return x

def kalkulasi(x):
    y = [0,0,0]
    y[1]=x+2
    y[2]=3+x+1
    y[3]=x**2+2*x+1
    print (y)
    return y

def printdata(asal):
    for f in asal:
        print(f)

printdata(kalkulasi(inputdata()))

######################################################################

def penjumlahan(x):
    x=x+1
    if(x==10):
        pass
    else:
        penjumlahan(x+1)
    return

print(penjumlahan(3))

#####################################################################
#mungkin bisa tapi harus pake fungsi

for f in range(10):
    print(f)
    print(-f)

#####################################################################
def rumah(x):
    x=x+1
    if x<3:
      rumah(x)
    x=x+1
    print(x)

rumah(2)