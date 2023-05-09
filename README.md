# Kedai-Kopi-Diskon

# Deskripsi Program

Program ini adalah sebuah program yang berfungsi sebagai menu pemesanan kopi. Program ini menggunakan Python sebagai bahasa pemrogramannya dan menggunakan konsep Object-Oriented Programming (OOP). Program ini dapat digunakan oleh pengguna untuk memesan beberapa jenis kopi dan menampilkan rincian pesanan yang telah dipesan.

# Cara Menggunakan Program

1. Jalankan program dengan membuka file program pada IDE atau text editor.
2. Program akan meminta input dari pengguna apakah ingin memesan atau tidak. Masukkan 'Y' jika ingin memesan, atau 'N' jika tidak ingin memesan.
3. Jika pengguna memilih untuk memesan, program akan menampilkan daftar menu kopi yang tersedia beserta harga masing-masing menu.
4. Pengguna diminta untuk memasukkan nama untuk memesan kopi.
5. Pengguna diminta untuk memilih menu kopi dengan memasukkan abjad menu kopi (A/B/C/D) dan memasukkan jumlah pesanan.
6. Setelah pengguna memilih menu kopi dan memasukkan jumlah pesanan, program akan menanyakan apakah pengguna ingin menambahkan pesanan atau tidak. Jika pengguna memilih 'Y', program akan kembali ke langkah 5. Jika pengguna memilih 'N', program akan menampilkan rincian pesanan yang telah dipesan.
7. Program akan menampilkan rincian pesanan yang telah dipesan beserta total harga semua pesanan dan menanyakan apakah pengguna ingin menghapus data pesanan atau tidak. Jika pengguna memilih 'Y', pengguna diminta untuk memasukkan nomor pesanan yang ingin dihapus. Jika pengguna memilih 'N', program akan berakhir.

# Cara Kerja Program

Program ini terdiri dari beberapa class, yaitu CoffeeMenu, CoffeeOrder, dan Discount. 

Class CoffeeMenu digunakan untuk menyimpan informasi menu kopi, yaitu nama dan harga. Setiap objek CoffeeMenu akan memiliki method get_name() dan get_price() untuk mengambil nama dan harga menu kopi.

Class CoffeeOrder digunakan untuk membuat objek pesanan kopi. Setiap objek CoffeeOrder memiliki atribut menu dan jumlah pesanan. Method hitung() digunakan untuk menghitung total harga pesanan kopi setelah diberikan diskon dan PPN. Method get_menu() dan get_jumlah() digunakan untuk mengambil nilai menu dan jumlah pesanan.

Class Discount digunakan untuk menghitung diskon berdasarkan jumlah pesanan kopi yang dipesan. Method get_discount() akan mengembalikan nilai diskon sesuai dengan jumlah pesanan kopi yang dipesan.

Pada program utama, program akan menampilkan daftar menu kopi yang tersedia dan meminta input nama dari pengguna. Setelah itu, program akan meminta pengguna untuk memilih menu kopi dan memasukkan jumlah pesanan. Jika pengguna ingin menambahkan pesanan, program akan kembali ke langkah memilih menu kopi. Setelah pengguna selesai memesan, program akan menampilkan rincian pesanan yang telah dipesan beserta total harga semua pesanan. Program akan menanyakan apakah pengguna ingin menghapus data pesanan atau tidak. Jika pengguna ingin menghapus data pesanan, program akan meminta nomor pesanan yang ingin dihapus dan menghapus data tersebut.
