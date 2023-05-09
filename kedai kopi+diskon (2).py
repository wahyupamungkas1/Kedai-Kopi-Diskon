class CoffeeMenu:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class CoffeeOrder:
    def __init__(self, menu, jumlah):
        self.__menu = menu
        self.__jumlah = jumlah

    def get_menu(self):
        return self.__menu

    def get_jumlah(self):
        return self.__jumlah

    def hitung(self):
        harga = self.__menu.get_price() * self.__jumlah
        ppn = int(harga * 0.1)
        diskon = Discount(self.__jumlah, harga).get_discount()
        totalharga = int(harga - diskon + ppn)
        return harga, diskon, ppn, totalharga


class Discount:
    def __init__(self, jumlah, harga):
        self.__jumlah = jumlah
        self.__harga = harga

    def get_discount(self):
        if self.__jumlah >= 10:
            return int(self.__harga * 0.3)
        elif self.__jumlah >= 7:
            return int(self.__harga * 0.2)
        elif self.__jumlah >= 5:
            return int(self.__harga * 0.1)
        elif self.__jumlah >= 3:
            return int(self.__harga * 0.05)
        else:
            return 0


# Daftar menu kopi
menu_items = {
    "a": CoffeeMenu("ES Kopi Susu", 11000),
    "b": CoffeeMenu("ES Kopi Coklat", 12000),
    "c": CoffeeMenu("ES Kopi Hitam", 11000),
    "d": CoffeeMenu("Ice Americano", 14000)
}


while True:
    input_awal = input("Apakah ingin memesan? (Y/N): ").lower()
    if input_awal == "y":
        break
    elif input_awal == "n":
        quit()
    else:
        print("Input tidak valid. Masukkan 'y' atau 'n'.")


while True:
    print("""
    ==============================
    
    Ananda Coffee
    List Menu Minuman Kopi
 
    ==============================
    A. ES Kopi Susu    : Rp 11.000
    B. ES Kopi Coklat  : Rp 12.000
    C. ES Kopi Hitam   : Rp 11.000
    D. Ice Americano   : Rp 14.000
    ==============================
    """)

    print("-------------------------------------")
    print("            Sebelum Memesan")
    print("         Silahkan masukkan Nama")
    print("-------------------------------------")

    name = input("Nama Anda                            : ")
    while name.strip() == "":
        print("Nama tidak boleh kosong.")
        name = input("Nama Anda                            : ")

    pesanan = {}

    while True:
        pilih_menu = input("Masukkan abjad menu kopi (A/B/C/D)   : ").lower()
        if pilih_menu not in menu_items:
            print("Menu tidak tersedia.")
        else:
            while True:
                try:
                    jumlah = int(input("Masukan Jumlah Pesanan               : "))
                    break
                except ValueError:
                    print("Input tidak valid. Masukkan angka.")

            # Membuat objek pesanan kopi
            menu = menu_items[pilih_menu]
            order = CoffeeOrder(menu, jumlah)
            pesanan[menu.get_name()] = order

            # Menanyakan apakah ingin menambahkan pesanan
            input_tambah = input("Apakah ingin menambahkan pesanan? (Y/N): ").lower()
            if input_tambah == "n":
                break
            elif input_tambah == "y":
                continue
            else:
                print("Input tidak valid. Masukkan 'y' atau 'n'.")

    # Menampilkan semua pesanan
    print("=====================================================================================")
    print("                                 Rincian Pesanan")
    print("=====================================================================================")
    print("Nama                              : ", name)

    while True:
        total_semua_harga = 0
        nomor_pesanan = 1
        for menu_name, order in pesanan.items():
            harga, diskon, ppn, totalharga = order.hitung()
            order.total_harga = totalharga  # update nilai total_harga di dalam object order
            total_semua_harga += order.total_harga
            print("Nomor Pesanan                     : {:<15}".format(nomor_pesanan))
            print("Pesanan                           : {:<15}".format(menu_name))
            print("Diskon                            : Rp{:<15}".format(diskon)) 
            print("PPN                               : Rp{:<15} ".format(ppn))
            print("Harga({:<1} x {:<1})         : Rp {:<10} ".format(menu_name ,order.get_jumlah(), harga))
            print("Total Harga Setelah diskon & PPN  : Rp {:<10}".format(order.total_harga))
            print("=====================================================================================")
            nomor_pesanan += 1

        print("Total Harga Semua Pesanan         : Rp", total_semua_harga)
        print("=====================================================================================")

        # menanyakan apakah pengguna ingin menghapus data pesanan
        hapus_data = input("Apakah Anda ingin menghapus data pesanan? (y/n): ")
        if hapus_data.lower() == 'y':
            nomor_hapus = int(input("Masukkan nomor pesanan yang ingin dihapus: "))
            menu_hapus = list(pesanan.keys())[nomor_hapus-1]  # dapatkan menu yang ingin dihapus berdasarkan nomor pesanan
            if nomor_hapus <= len(pesanan) and nomor_hapus > 0:
                del pesanan[menu_hapus]
                print("=====================================================================================")
                print("Data menu", menu_hapus, "berhasil dihapus dari pesanan.")
                print("=====================================================================================")
            else:
                print("Nomor pesanan tidak ditemukan dalam pesanan.")
        elif hapus_data.lower()=='n':
            break
        else:
            print("Input tidak valid. Masukkan 'y' atau 'n'.")


    # Menanyakan apakah ingin melakukan pesanan kembali
    input_lagi = input("Apakah ingin melakukan pesanan lagi? (Y/N): ").lower()
    if input_lagi == "n":
        break
    elif input_lagi == "y":
        continue
    else:
        print("Input tidak valid. Masukkan 'y' atau 'n'.")
