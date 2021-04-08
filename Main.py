# Saya Diffa Al Farrisztqi mengerjakan evaluasi Tugas Praktikum 3 DPBO 
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk 
# keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

from tkinter import *
import sqlite3
from tkinter import messagebox

# membuat label judul dan window
root = Tk()
root.title("TP3")

#konekan dengan data base
conn = sqlite3.connect("Perkerjaan.db")

c = conn.cursor()

# membuat tabel
# c.execute(""" CREATE TABLE pgwi(
#         nomorinduk integer,
#         name text,
#         var text,
#         listAsal text,
#         gabung text)
# """)

# fungsi untuk menambahkan data
def masukan():

    gabung = StringVar()
    cek = 0

    #menggabungkan string checbox
    if(cek == 0):
        if(var1.get() != 0):
            gabung = var1.get()
            cek = 1
    else:
        if(var1.get() != 0):
            gabung = gabung + " , " + var1.get()
    if(cek == 0):
        if(var2.get() != 0):
            gabung = var2.get()
            cek = 1
    else:
        if(var2.get() != 0):
            gabung = gabung + " , " + var2.get()
    if(cek == 0):
        if(var3.get() != 0):
            gabung = var3.get()
            cek = 1
    else:   
        if(var3.get() != 0):
            gabung = gabung + " , " + var3.get()

    #konekan dengan data base
    conn = sqlite3.connect("Perkerjaan.db")

    c = conn.cursor()

    #cek apakah masukannya ada atau tidak
    if(nomorinduk.get() == "" or name.get() == "" or var.get() == "" or listAsal.get() == ""):
        #jika gagal akan menampilkan
        messagebox.showwarning("Gagal", "Tolong isi semua data!")
    else:
        #jika ada masukannya
        c.execute("INSERT INTO pgwi VALUES(:nomorinduk, :name, :var, :listAsal, :gabung)",
            {
                "nomorinduk": nomorinduk.get(),
                "name": name.get(),
                "var": var.get(),
                "listAsal" : listAsal.get(),
                "gabung" : gabung
            })
        #jika ada masukannya akan menampilkan
        messagebox.showinfo("Success", "Data berhasil ditambahkan!")


    conn.commit()

    conn.close()

    #kosongkan kembali
    nomorinduk.delete(0, END)
    name.delete(0, END)
    var.set("Cowo")
    listAsal.set("Bandung")
    c1.deselect()
    c2.deselect()
    c3.deselect()

#fungsi untuk menampilkan semua data yang ada
def semua():
    # membuat label judul dan window baru
    top = Toplevel()
    top.title("Data Pegawai")

    # konekan dengan data base
    conn = sqlite3.connect("Perkerjaan.db")

    c = conn.cursor()

    #select data dari tabel
    c.execute("SELECT *,oid FROM pgwi")
    records = c.fetchall()
    index = 0

    #cetak
    for record in records:
        labelQuery = Label(top, text=str(record))
        labelQuery.grid(row=index, column="0")

        btnDelete = Button(top, text="Delete", command=hapus).grid(row=index, column=1)
        index += 1

    conn.commit()

    conn.close()

#fungsi untuk menghapus data yang ada tapi gagal, dah ngantuk jadi ga d lanjut kang
def hapus():
    #konekan dengan database
    conn = sqlite3.connect("Perkerjaan.db")

    c = conn.cursor()

    c.execute("DELETE from pgwi WHERE oid=PLACEHOLDER")
    
    conn.commit()

    conn.close()

#fungsi untuk menampilkan tentang aplikasi
def tentang():
    #membuat judul dan window baru
    top = Toplevel()
    top.title("About Aplikasi")

    #frame untuk menampilkan about dari aplikasi sendiri
    d_frame = LabelFrame(top, text="Cari Kerja di Valorant", padx=10, pady=10)
    d_frame.pack(padx=5, pady=10)
    opts = LabelFrame(root, padx=5, pady=10)
    b_exit = Button(d_frame, text="Exit", command=top.destroy)
    b_exit.grid(row=5, column=0)

    d_about = Label(d_frame, text="Aplikasi ini dibuat untuk memudahkan para desainer dan developer mendapatkan perkerjaan mereka di Valorant untuk mengembangkan game (*Bukan sebagai gamers)",
                    anchor="w").grid(row=0, column=0, sticky="w")

#label judul dari form
lblJudul = Label(root, text = "Form Data Pegawai", padx="20", pady="20")
lblJudul.config(font=("Ubuntu", 15))
lblJudul.pack()

#label deskripsi dari form
lblDeskripsi = Label(root, text="Berikut adalah Form untuk mengikuti seleksi di PT Valorant Indonesia", padx="15")
lblDeskripsi.pack()

frameForm = LabelFrame(root, text = "Masukan data diri anda", padx="15", pady="10")
frameForm.pack(padx="10", pady="10")

#label nama dari form
nama = Label(frameForm, text="Nama")
nama.grid(row="0", column="0")

#kotak masukan data
name = Entry(frameForm)
name.grid(row="0", column="1")

#label nik dari form
nik = Label(frameForm, text="NIK")
nik.grid(row="1", column="0")

#kotak masukan data
nomorinduk = Entry(frameForm)
nomorinduk.grid(row="1", column="1")

#dropdown untuk asalkotanya
asal = Label(frameForm, text="Asal Kota")
asal.grid(row="2", column="0")

#Pilih kotanya
listAsalKota = ['Bandung','Jakarta','Surabaya','Jogjakarta','Purwakarta']
listAsal=StringVar()
droplist = OptionMenu(frameForm, listAsal, *listAsalKota)
droplist.config(width=15)
listAsal.set('Pilih')
droplist.grid(row="2", column="1")

#label Jenis kelamin
jeniskelamin = Label(frameForm, text="Jenis Kelamin")
jeniskelamin.grid(row="3", column="0")

#lalu pilih secara radio button
var = StringVar()
var.set("Cowo")
Radiobutton(frameForm, text="Laki-laki", variable = var, value = "Cowo").grid(row="3", column="1")
Radiobutton(frameForm, text="Perempuan", variable = var, value = "Cewe").grid(row="3", column="2")

#label perkerjaan yang mau d ambil
perkerjaan = Label(frameForm, text="Perkerjaan")
perkerjaan.grid(row="4", column="0")

#lalu pilih secara check box
var1 = StringVar()
c1 = Checkbutton(frameForm, text="Desain", variable=var1, onvalue="Desain", offvalue="0")
c1.deselect()
c1.grid(row="4", column="1")


var2 = StringVar()
c2 = Checkbutton(frameForm, text="Frontend", variable=var2, onvalue="Frontend", offvalue="0")
c2.deselect()
c2.grid(row="4", column="2")

var3 = StringVar()
c3 = Checkbutton(frameForm, text="Backend", variable=var3, onvalue="Backend", offvalue="0")
c3.deselect()
c3.grid(row="4", column="3")

# button submit untuk mengumpulkan
# button see all submissons untuk melihat data yang ada
# button clear submissons untuk di clear
# button about tentang apknya
# button exit untuk aplikasi keluar
Button(frameForm, text="SUBMIT", command=masukan).grid(row="5", column="1", pady=10)
Button(frameForm, text="SEE ALL SUBMISSONS", command=semua).grid(row="6", column="0", pady=10)
Button(frameForm, text="CLEAR SUBMISSONS").grid(row="6", column="2", pady=10)
Button(frameForm, text="ABOUT", command=tentang).grid(row="6", column="1", pady=10)
Button(frameForm, text="EXIT", command=quit).grid(row="7", column="1", pady=10)


root.mainloop()
