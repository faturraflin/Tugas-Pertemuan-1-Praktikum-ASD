class Buku:
    def __init__(self, nama, penerbit, stok, rak, tanggal_terbit):
        self.nama = nama
        self.penerbit = penerbit
        self.stok = stok
        self.rak = rak
        self.tanggal_terbit = tanggal_terbit

    def display_info(self):
        print(f"Nama Buku: {self.nama}")
        print(f"Penerbit: {self.penerbit}")
        print(f"Stok: {self.stok}")
        print(f"Rak: {self.rak}")
        print(f"Tanggal Terbit: {self.tanggal_terbit}")
        print()

class Perpustakaan:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku dengan judul '{buku.nama}' berhasil ditambahkan.")

    def hapus_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.nama == judul:
                self.daftar_buku.remove(buku)
                print(f"Buku dengan judul '{judul}' berhasil dihapus.")
                return
        print("Buku tidak ditemukan dalam daftar.")

    def tampilkan_daftar_buku(self):
        print("Daftar Buku:")
        for buku in self.daftar_buku:
            buku.display_info()

    def pinjam_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.nama == judul:
                if buku.stok > 0:
                    print(f"Anda berhasil meminjam buku '{judul}'.")
                    buku.stok -= 1
                    return
                else:
                    print("Maaf, stok buku habis.")
                    return
        print("Buku tidak tersedia untuk dipinjam.")

perpustakaan1 = Perpustakaan("Perpustakaan Kota", "Jl. Kusuma bangsa")

perpustakaan1.tambah_buku(Buku("Ordeal", "Webtoon", 5, "Rak 1", "13/08/2021"))
perpustakaan1.tambah_buku(Buku("The Extincts", "Bhuana Sastra", 3, "Rak 2", "05/03/2013"))
perpustakaan1.tambah_buku(Buku("Laut Bercerita", "Kepustakaan Populer Gramedia", 7, "Rak 3", "10/07/2017"))

while True:
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Hapus Buku")
    print("3. Tampilkan Daftar Buku")
    print("4. Pinjam Buku")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        nama_buku = input("Masukkan nama buku yang ingin ditambahkan: ")
        penerbit = input("Masukkan penerbit buku: ")
        stok = int(input("Masukkan jumlah stok buku: "))
        rak = input("Masukkan lokasi rak buku: ")
        tanggal_terbit = input("Masukkan tanggal terbit buku (dd/mm/yyyy): ")
        perpustakaan1.tambah_buku(Buku(nama_buku, penerbit, stok, rak, tanggal_terbit))
    elif pilihan == "2":
        judul_buku = input("Masukkan nama buku yang ingin dihapus: ")
        perpustakaan1.hapus_buku(judul_buku)
    elif pilihan == "3":
        perpustakaan1.tampilkan_daftar_buku()
    elif pilihan == "4":
        judul_buku = input("Masukkan nama buku yang ingin dipinjam: ")
        perpustakaan1.pinjam_buku(judul_buku)
    elif pilihan == "5":
        print("Terima kasih telah menggunakan layanan perpustakaan.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
