class Vehicle:
    def _init_(self, merk, tahun, warna):
        self,merk = merk
        self.tahun = tahun
        self.warna = warna

    def tampilkan_info(self):
        print(f"merk: {self,merk}")
        print(f"Tahun: {self,tahun}")
        print(f"warna: {self,warna}")

class Car(Vehicle):
    def _init_(self, merk, tahun, warna, model):
        super()._init_(merk, tahun, warna)
        self.model = model

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Model: {self.model}")
        
if _name_ == "_main_":
   car = Car("Toyota", 2022, "Merah", "Camry")
   print("Info Kendaraan: ")
   car.tampilkan_info()