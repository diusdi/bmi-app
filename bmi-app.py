import streamlit as st
#Input untuk mendapatkan variabel
st.write("""
# Aplikasi Kalkulator BMI
""")

tinggi = st.number_input("Masukkan tinggi badan anda (cm)", 0.0)
berat = st.number_input("Masukkan berat badan anda (kg)", 0.0)
umur = st.number_input("Masukkan umur anda ", 0.0)
JK = st.text_input("Jenis Kelamin")
jenisKelamin = JK.upper()
hitung = st.button("Hitung")

#Menghitung indeks masa tubuh
if hitung:
    imt=berat/ ((tinggi/100)*(tinggi/100))
    st.write("Indeks Masa Tubuh anda adalah= ",imt)

#kategori indeks masa tubuh
    kategori=''
    if imt<18.5 :
        kategori="kurang"
    else :
        if 18.5 <= imt <= 22.9: kategori="Normal"
        else:
            if 22.9 < imt <= 29.9: kategori="Berat badan berlebih beresiko obesitas"
            else: kategori="Obesitas"
    st.write("Kategori:", kategori)


#Menghitung persentase lemak tubuh
    if jenisKelamin=="LAKI-LAKI" or jenisKelamin=="PRIA": lemak=(1.2*imt)+(0.23*umur)-10.8-5.4
    if jenisKelamin=="PEREMPUAN" or jenisKelamin=="WANITA": lemak=(1.2*imt)+(0.23*umur)-5.4

    st.write("Lemak tubuh anda sebesar",lemak, "%")

#Kategori lemak tubuh
    if jenisKelamin=="LAKI-LAKI" or jenisKelamin=="PRIA":
        kateg_lemak=""
        if lemak<=13 :
            kateg_lemak="atlet"
        else :
            if 13 < lemak <= 17: kateg_lemak="Anda Rajin olahraga"
            else:
                if 17 < lemak <= 25: kateg_lemak="Berat badan berlebih beresiko obesitas"
                else: kateg_lemak="Obesitas"

    if jenisKelamin=="PEREMPUAN" or jenisKelamin=="WANITA":
        kateg_lemak=""
        if lemak<=20 :
            kateg_lemak="atlet"
        else :
            if 20 < lemak <= 24: kateg_lemak="Anda Rajin olahraga"
            else:
                if 24 < lemak <= 31: kateg_lemak="Berat badan berlebih beresiko obesitas"
                else: kateg_lemak="Obesitas"

    st.write("Kategori lemak tubuh anda adalah ", kateg_lemak)
