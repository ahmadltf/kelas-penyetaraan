#ahmad luthfi hanif

class orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def jalan(self):
        print("orang jalan")

    def makan(self, nama):
        print(nama + "suka makan")

    def umur(self,nama,umur):
        print("umur teman "+namateman+" "+str(self.umur)+" tahun")

#inheritance
#overriding
class orangtua(orang):
    def sakit(self):
        print(self.nama + ' cuma bisa makan enak')

    def __init__(self,nama,umur,waktmakan):
        super().__init__(self,nama,umur) #super bisa buat nambah
        self.waktumakan=waktumakan

class orangorang:
    def __init__(self,*args):
        self.arg=args
        self.counter=0

    def __iter__(self,*args): #(*) berarti bisa lebih dari 1
        self.a=args[0]

    def __next__(self):
        self.counter=1
        x=self.args[self.counter]

def penjumlahan(a,b):
    sum = a+b
    return sum

def pengurangan(a,b):
    min=b-a
    return min