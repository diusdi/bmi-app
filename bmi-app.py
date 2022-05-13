import streamlit as st
#Input untuk mendapatkan variabel
st.write("""
# Aplikasi Kalkulator BMI
""")

tinggi = st.number_input("Masukkan tinggi badan anda (cm)", 0)
berat = st.number_input("Masukkan berat badan anda (kg)", 0)
umur = st.number_input("Masukkan umur anda ", 0)
JK = st.number_input("Jenis Kelamin [1. laki-laki, 2. perempuan] ", 0)

#Menghitung indeks masa tubuh
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
if JK==1: lemak=(1.2*imt)+(0.23*umur)-10.8-5.4
if JK==2: lemak=(1.2*imt)+(0.23*umur)-5.4

st.write("Lemak tubuh anda sebesar",lemak, "%")

#Kategori lemak tubuh
if JK==1:
    kateg_lemak=""
    if lemak<=13 :
        kateg_lemak="atlet"
    else :
        if 13 < lemak <= 17: kateg_lemak="Anda Rajin olahraga"
        else:
            if 17 < lemak <= 25: kateg_lemak="Berat badan berlebih beresiko obesitas"
            else: kateg_lemak="Obesitas"

if JK==2:
    kateg_lemak=""
    if lemak<=20 :
        kateg_lemak="atlet"
    else :
        if 20 < lemak <= 24: kateg_lemak="Anda Rajin olahraga"
        else:
            if 24 < lemak <= 31: kateg_lemak="Berat badan berlebih beresiko obesitas"
            else: kateg_lemak="Obesitas"

st.write("Kategori lemak tubuh anda adalah ", kateg_lemak)
