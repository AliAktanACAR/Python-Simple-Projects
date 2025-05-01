class Cinar:
    kalan_can=10
    def saldır(self):
        print("çınar öleceksin")
        self.kalan_can -=1
    def hayatta_mı(self):
        if (self.kalan_can <= 0):
            print("öldü")
        else:
            print(str(self.kalan_can)+"hayatta")

Cinar1 = Cinar()
Cinar2 = Cinar()

Cinar1.saldır()
Cinar1.saldır()
Cinar1.saldır()
Cinar1.saldır()
Cinar2.hayatta_mı()