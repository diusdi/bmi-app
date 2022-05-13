#Input untuk mendapatkan variabel
tb= float(input("masukkan tinggi badan anda dalam cm="))
bb= float(input("masukkan berat badan anda dalam kg="))
umur=float(input("masukkan umur badan anda dalam tahun="))
JK=float(input("jenis kelamin (1= Laki-laki ; 2=Perempuan) ?"))

print("=============================")
print("tinggi badan anda", tb)
print("berat badan anda", bb)
print("=============================")

#Menghitung indeks masa tubuh
imt=bb/ ((tb/100)*(tb/100))
print("Indeks Masa Tubuh anda adalah= ",imt)

#kategori indeks masa tubuh
kateg="==="
if imt<18.5 :
    kateg="kurang"
else :
        if 18.5 <= imt <= 22.9: kateg="Normal"
        else:
            if 22.9 < imt <= 29.9: kateg="Berat badan berlebih beresiko obesitas"
            else: kateg="Obesitas"
print("kateg =", kateg)
print("=============================")

#Menghitung persentase lemak tubuh
if JK==1: lemak=(1.2*imt)+(0.23*umur)-10.8-5.4
if JK==2: lemak=(1.2*imt)+(0.23*umur)-5.4
print("lemak tubuh anda sebesar ",lemak, " persen")


#Kategori lemak tubuh
if JK==1:
    kateg_lemak="==="
    if lemak<=13 :
        kateg_lemak="atlet"
    else :
        if 13 < lemak <= 17: kateg_lemak="Anda Rajin olahraga"
        else:
            if 17 < lemak <= 25: kateg_lemak="Berat badan berlebih beresiko obesitas"
            else: kateg_lemak="Obesitas"

if JK==2:
    kateg_lemak="==="
    if lemak<=20 :
        kateg_lemak="atlet"
    else :
        if 20 < lemak <= 24: kateg_lemak="Anda Rajin olahraga"
        else:
            if 24 < lemak <= 31: kateg_lemak="Berat badan berlebih beresiko obesitas"
            else: kateg_lemak="Obesitas"
print("kategori lemak tubuh anda adalah ", kateg_lemak)





            

