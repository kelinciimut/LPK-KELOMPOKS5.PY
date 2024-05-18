import streamlit as st
import math

# Fungsi untuk setiap menu
def Aboutus():
    st.balloons()
    st.header("Halo Users! Selamat Datang di Web kami💁🏻‍♀️")
    st.write("Kami hadir untuk membantu Anda mencari Bobot Atom beserta ketidakpastiannya dan juga Perhitungan Ketidakpastian pengukuran, Bobot Molekul, dan Mol.")
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.image('https://github.com/kelinciimut/ggggg/blob/64451931026653cfe859995ee5853445354b79a7/e8014dd6-d9cd-4348-b3d0-c875f5eb4621.jpeg?raw=true', caption='KELOMPOK 5', use_column_width=True)
   
def Pendahuluan():  
    st.header("Latar Belakang Pembuatan Web")
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.write("Aplikasi ini dapat digunakan untuk mencari Bobot Atom beserta Ketidakpastiannya  dan juga terdapat berbagai perhitungan.")
    st.write("Di Era sekarang Mahasiswa Politeknik AKA Bogor membutuhkan suatu aplikasi yang ringkas untuk membantu dalam mendapatkan informasi Bobot atom berserta ketidakpastiannya (U) untuk memenuhi keperluan pada Mata Kuliah Titrimetri. Selain itu, web kami juga dilengkapi dengan Perhitungan yang terdiri dari Perhitungan Ketidakpastian Pengukuran Bobot Atom, Perhitungan Bobot Molekul Senyawa,dan Perhitungan Mol.")
    st.header("Tujuan Pembuatan Web")
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.write("Tujuan utama dari pembuatan aplikasi ini adalah untuk memberikan platform yang mudah digunakan kepada mahasiswa Politeknik AKA Bogor dalam menghitung bobot molekul dan ketidakpastiannya, sehingga mendukung pembelajaran mereka dalam Mata Kuliah Titrimetri. Beberapa tujuan khusus dari pembuatan aplikasi ini adalah sebagai berikut:")
    
    st.write("1. Memberikan Akses yang Mudah: Aplikasi ini memberikan akses mudah bagi mahasiswa untuk mencari dan memahami bobot atom dari unsur kimia tertentu. Dengan hanya memasukkan simbol unsur, mereka bisa mendapatkan informasi yang relevan dengan cepat.")
    st.write("2. Menghitung Ketidakpastian: Aplikasi ini akan memungkinkan pengguna untuk menghitung ketidakpastian pengukuran bobot atom, yang penting untuk penelitian yang akurat dan dapat diandalkan.")
    st.write("3. Memfasilitasi Pembelajaran: Dengan memberikan akses mudah dan menyediakan informasi yang relevan, aplikasi ini akan membantu mahasiswa Politeknik AKA Bogor dalam memahami konsep-konsep kimia yang mendasari, serta meningkatkan efisiensi belajar mereka dalam Mata Kuliah Titrimetri.")
    st.subheader("Perhitungan Ketidakpastian Pengukuran Bobot Atom (miu)")
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.write("Ketidakpastian (U) dalam perhitungan Bobot Atom yang sudah dicari dapat dimasukkan ke dalam persamaan:")
   # Rumus untuk jumlah mol
    rumus_miu = r'miu = \frac{U}{K}'

    # Menampilkan rumus menggunakan st.latex()
    st.latex(rumus_miu)
    st.write("Di mana U adalah ketidakpastian dalam Bobot atom yang dapat kita peroleh dari menu pencarian dan K adalah konstantanya.")
    st.subheader("Perhitungan Bobot Molekul senyawa (BM)")
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.write("BM dalam senyawa dapat kita hitung dengan memasukkan Bobot atom yang sudah kita peroleh dari halaman pencarian dan banyaknya atom yang diketahui melalui persamaan berikut:")
    # Rumus untuk bobot atom x jumlah atom
    rumus = r'BM = b_i \times j_i'

    # Menampilkan rumus menggunakan st.latex()
    st.latex(rumus)
    st.write("di mana bi adalah Bobot atom yang bisa kita peroleh dari menu pencarian dan ji adalah jumlah atomnya.")
    st.subheader("Perhitungan Mol (n)")
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.write("Mol dalam senyawa dapat kita hitung melalui persamaan berikut:")
    rumus_mol = r'n = \frac{m}{bm}'
    # Menampilkan rumus menggunakan st.latex()
    st.latex(rumus_mol)
    st.write("di mana m adalah massa atom yang telah kita ketahui dan bm adalah bobot atom yang telah kita peroleh dari persamaan mencari BM diatas.")
    st.subheader('note: Aplikasi ini dibuat berdasarkan Tabel data dalam IUPAC')
def Pencarian():
    st.subheader("Masukkan informasi di bawah ini untuk menemukan Bobot Atom dan Ketidakpastiannya:")
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    kode_unsur = st.text_input("Silahkan Masukkan Simbol Atom")
    cari = st.button("Memuat Hasil")

    if cari :
        if (kode_unsur =="Al"): 
             st.header('Nama Atom : Aluminium ')
             st.subheader('Bobot Atom : 26.9815386 ')
             st.write('Ketidakpastian Bobot Atom : ±0.000008')
        elif (kode_unsur =="Sb"): 
             st.header('Nama Atom : Antimony')
             st.subheader('Bobot Atom : 121.760')
             st.write('Ketidakpastian Bobot Atom : ±0,001 ')
        elif(kode_unsur =='Ar'):
              st.header('Nama Atom : Argon')
              st.subheader('Bobot Atom : 39.948')
              st.write('Ketidakpastian Bobot Atom: ±0,001')
        elif(kode_unsur == 'As'):
             st.header('Nama Atom: Arsenik')
             st.subheader('Bobot Atom: 74.92160')
             st.write('Ketidakpastian Bobot Atom: ±0,00002')
        elif(kode_unsur == 'Ba' ):
            st.header('Nama Atom: Barium ')
            st.subheader('Bobot Atom: 171.327')
            st.write('Ketidakpastian Bobot Atom: ±0,007')
        elif(kode_unsur=='Be'):
            st.header('Nama Atom: Berillium ')
            st.subheader('Bobot Atom: 9.012182')
            st.write('Ketidakpastian Bobot Atom: ±0,000003')
        elif(kode_unsur=='Bi'):
            st.header('Nama Atom: bismuth ')
            st.subheader('Bobot Atom: 208.98040')
            st.write('Ketidakpastian Bobot Atom: ±0,00001')
        elif(kode_unsur=='B'):
            st.header('Nama Atom: Boron ')
            st.subheader('Bobot Atom: 10.811')
            st.write('Ketidakpastian Bobot Atom: ±0,007')
        elif(kode_unsur=='Br'):
            st.header('Nama Atom: Bromin ')
            st.subheader('Bobot Atom: 79.904')
            st.write('Ketidakpastian Bobot Atom: ±0,001')
        elif(kode_unsur=='Cd'):
            st.header('Nama Atom: Cadmium ')
            st.subheader('Bobot Atom: 112.411')
            st.write('Ketidakpastian Bobot Atom: ±0,008')
        elif(kode_unsur=='Cs'):
            st.header('Nama Atom: Cesium ')
            st.subheader('Bobot Atom: 132.9054519')
            st.write('Ketidakpastian Bobot Atom: ±0,0000002')
        elif(kode_unsur=='Ca'):
            st.header('Nama Atom: calcium ')
            st.subheader('Bobot Atom: 40.078')
            st.write('Ketidakpastian Bobot Atom: ±0,004')
        elif(kode_unsur=='C'):
            st.header('Nama Atom: carbon ')
            st.subheader('Bobot Atom: 12.0107')
            st.write('Ketidakpastian Bobot Atom: ±0,0008')
        elif(kode_unsur=='Ce'):
            st.header('Nama Atom: cerium ')
            st.subheader('Bobot Atom: 140.116')
            st.write('Ketidakpastian Bobot Atom: ±0,001') 
        elif(kode_unsur=='Cl'):
            st.header('Nama Atom: chlorine ')
            st.subheader('Bobot Atom: 35.453')
            st.write('Ketidakpastian Bobot Atom: ±0,002') 
        elif(kode_unsur=='Cr'):
            st.header('Nama Atom: Chromium ')
            st.subheader('Bobot Atom: 51.9961')
            st.write('Ketidakpastian Bobot Atom: ±0,0006')
        elif(kode_unsur=='Co'):
            st.header('Nama Atom: cobalt')
            st.subheader('Bobot Atom: 58.933195')
            st.write('Ketidakpastian Bobot Atom: ±0,000005')
        elif(kode_unsur=='Cu'):
            st.header('Nama Atom: Copper')
            st.subheader('Bobot Atom: 63.546')
            st.write('Ketidakpastian Bobot Atom: ±0,003')
        elif(kode_unsur=='Dy'):
            st.header('Nama Atom: Dysprosium')
            st.subheader('Bobot Atom: 162.500')
            st.write('Ketidakpastian Bobot Atom:±0,001') 
        elif(kode_unsur=='Er'):
            st.header('Nama Atom: Erbium')
            st.subheader('Bobot Atom:167.259')
            st.write('Ketidakpastian Bobot Atom:±0,003')
        elif(kode_unsur=='Eu'):
            st.header('Nama Atom: Europium')
            st.subheader('Bobot Atom:151.964')
            st.write('Ketidakpastian Bobot Atom:±0,001')
        elif(kode_unsur=='F'):
            st.header('Nama Atom:Fluorine')
            st.subheader('Bobot Atom: 18.9984032')
            st.write('Ketidakpastian Bobot Atom:±0,0000005')
        elif(kode_unsur =="Al"): 
             st.header('Nama Atom : Aluminium ')
             st.subheader('Bobot Atom : 26.9815386 ')
             st.write('Ketidakpastian Bobot Atom : ±0.000008')
        elif (kode_unsur =="Sb"): 
             st.header('Nama Atom : Antimony')
             st.subheader('Bobot Atom : 121.760')
             st.write('Ketidakpastian Bobot Atom : ±0,001 ')
        elif(kode_unsur =='Ar'):
              st.header('Nama Atom : Argon')
              st.subheader('Bobot Atom : 39.948')
              st.write('Ketidakpastian Bobot Atom: ±0,001')
        elif(kode_unsur == 'As'):
             st.header('Nama Atom: Arsenik')
             st.subheader('Bobot Atom: 74.92160')
             st.write('Ketidakpastian Bobot Atom: ±0,00002')
        elif(kode_unsur == 'Ba' ):
            st.header('Nama Atom: Barium ')
            st.subheader('Bobot Atom: 171.327')
            st.write('Ketidakpastian Bobot Atom: ±0,007')
        elif(kode_unsur=='Be'):
            st.header('Nama Atom: Berillium ')
            st.subheader('Bobot Atom: 9.012182')
            st.write('Ketidakpastian Bobot Atom: ±0,000003')
        elif(kode_unsur=='Bi'):
            st.header('Nama Atom: bismuth ')
            st.subheader('Bobot Atom: 208.98040')
            st.write('Ketidakpastian Bobot Atom: ±0,00001')
        elif(kode_unsur=='B'):
            st.header('Nama Atom: Boron ')
            st.subheader('Bobot Atom: 10.811')
            st.write('Ketidakpastian Bobot Atom: ±0,007')
        elif(kode_unsur=='Br'):
            st.header('Nama Atom: Bromin ')
            st.subheader('Bobot Atom: 79.904')
            st.write('Ketidakpastian Bobot Atom: ±0,001')
        elif(kode_unsur=='Cd'):
            st.header('Nama Atom: Cadmium ')
            st.subheader('Bobot Atom: 112.411')
            st.write('Ketidakpastian Bobot Atom: ±0,008')
        elif(kode_unsur=='Cs'):
            st.header('Nama Atom: Cesium ')
            st.subheader('Bobot Atom: 132.9054519')
            st.write('Ketidakpastian Bobot Atom: ±0,0000002')
        elif(kode_unsur=='Ca'):
            st.header('Nama Atom: calcium ')
            st.subheader('Bobot Atom: 40.078')
            st.write('Ketidakpastian Bobot Atom: ±0,004')
        elif(kode_unsur=='C'):
            st.header('Nama Atom: carbon ')
            st.subheader('Bobot Atom: 12.0107')
            st.write('Ketidakpastian Bobot Atom: ±0,0008')
        elif(kode_unsur=='Ce'):
            st.header('Nama Atom: cerium ')
            st.subheader('Bobot Atom: 140.116')
            st.write('Ketidakpastian Bobot Atom: ±0,001') 
        elif(kode_unsur=='Cl'):
            st.header('Nama Atom: chlorine ')
            st.subheader('Bobot Atom: 35.453')
            st.write('Ketidakpastian Bobot Atom: ±0,002') 
        elif(kode_unsur=='Cr'):
            st.header('Nama Atom: Chromium ')
            st.subheader('Bobot Atom: 51.9961')
            st.write('Ketidakpastian Bobot Atom: ±0,0006')
        elif(kode_unsur=='Co'):
            st.header('Nama Atom: cobalt')
            st.subheader('Bobot Atom: 58.933195')
            st.write('Ketidakpastian Bobot Atom: ±0,000005')
        elif(kode_unsur=='Cu'):
            st.header('Nama Atom: Copper')
            st.subheader('Bobot Atom: 63.546')
            st.write('Ketidakpastian Bobot Atom: ±0,003')
        elif(kode_unsur=='Dy'):
            st.header('Nama Atom: Dysprosium')
            st.subheader('Bobot Atom: 162.500')
            st.write('Ketidakpastian Bobot Atom:±0,001') 
        elif(kode_unsur=='Er'):
            st.header('Nama Atom: Erbium')
            st.subheader('Bobot Atom:167.259')
            st.write('Ketidakpastian Bobot Atom:±0,003')
        elif(kode_unsur=='Eu'):
            st.header('Nama Atom: Europium')
            st.subheader('Bobot Atom:151.964')
            st.write('Ketidakpastian Bobot Atom:±0,001')
        elif(kode_unsur=='F'):
            st.header('Nama Atom:Fluorine')
            st.subheader('Bobot Atom: 18.9984032')
            st.write('Ketidakpastian Bobot Atom: ±0,0000005')
        elif(kode_unsur=='Gd'):
            st.header('Nama Atom: Gadolinium ')
            st.subheader('Bobot Atom: 157.25')
            st.write('Ketidakpastian Bobot Atom: ±0,03')
        elif(kode_unsur=='Ga'):
            st.header('Nama Atom: Gallium ')
            st.subheader('Bobot Atom: 69.723')
            st.write('Ketidakpastian Bobot Atom: ± 0.001')
        elif(kode_unsur=='Ge'):
            st.header('Nama Atom: Germanium')
            st.subheader('Bobot Atom: 72.64')
            st.write('Ketidakpastian Bobot Atom: ± 0.01')
        elif(kode_unsur=='Au'):
            st.header('Nama Atom: Gold')
            st.subheader('Bobot Atom: 196.966569')
            st.write('Ketidakpastian Bobot Atom: ± 0,000004')
        elif(kode_unsur=='Hf'):
            st.header('Nama Atom: hafnium')
            st.subheader('Bobot Atom: 178.49')
            st.write('Ketidakpastian Bobot Atom: ± 0,02')
        elif(kode_unsur=='He'):
            st.header('Nama Atom: Helium ')
            st.subheader('Bobot Atom: 4.002602')
            st.write('Ketidakpastian Bobot Atom: ± 0,000002')
        elif(kode_unsur=='Ho'):
            st.header('Nama Atom: Holmium ')
            st.subheader('Bobot Atom: 164.93032')
            st.write('Ketidakpastian Bobot Atom: ± 0,00002') 
        elif(kode_unsur=='H'):
            st.header('Nama Atom: Hydrogen ')
            st.subheader('Bobot Atom: 1.00794')
            st.write('Ketidakpastian Bobot Atom: ± 0,00007')
        elif(kode_unsur=='In'):
            st.header('Nama Atom: Indium ')
            st.subheader('Bobot Atom: 114.818')
            st.write('Ketidakpastian Bobot Atom: ± 0,003')
        elif(kode_unsur=='I'):
            st.header('Nama Atom: Iodine ')
            st.subheader('Bobot Atom: 126.90447')
            st.write('Ketidakpastian Bobot Atom: ± 0,00003') 
        elif(kode_unsur=='Ir'):
            st.header('Nama Atom: Iridium ')
            st.subheader('Bobot Atom:  192.217')
            st.write('Ketidakpastian Bobot Atom: ± 0,003')
        elif(kode_unsur=='Fe'):
            st.header('Nama Atom: Iron ')
            st.subheader('Bobot Atom:  55.845')
            st.write('Ketidakpastian Bobot Atom: ± 0,003')
        elif(kode_unsur=='Kr'):
            st.header('Nama Atom: krypton ')
            st.subheader('Bobot Atom:  83.798')
            st.write('Ketidakpastian Bobot Atom: ± 0,002')
        elif(kode_unsur=='La'):
            st.header('Nama Atom: lanthanum ')
            st.subheader('Bobot Atom:  138.90547')
            st.write('Ketidakpastian Bobot Atom: ± 0,00007')
        elif(kode_unsur=='Pb'):
            st.header('Nama Atom: lead ')
            st.subheader('Bobot Atom:  207.2')
            st.write('Ketidakpastian Bobot Atom: ± 0,1') 
        elif(kode_unsur=='Li'):
            st.header('Nama Atom: lithium ')
            st.subheader('Bobot Atom:  [6.941]†')
            st.write('Ketidakpastian Bobot Atom: ± 0,002')                   
        elif(kode_unsur=='Li'):
            st.header('Nama Atom: lutetium  ')
            st.subheader('Bobot Atom:  [6.941]†')
            st.write('Ketidakpastian Bobot Atom: ± 0,002')
        elif(kode_unsur=='Mg'):
            st.header('Nama Atom: magnesium  ')
            st.subheader('Bobot Atom:  24.3050')
            st.write('Ketidakpastian Bobot Atom: ± 0,0006')  
        elif(kode_unsur=='Hg'):
            st.header('Nama Atom: Mercury  ')
            st.subheader('Bobot Atom:  200.59')
            st.write('Ketidakpastian Bobot Atom: ± 0,02')       
        elif(kode_unsur=='Mo'):
            st.header('Nama Atom: molybdenum  ')
            st.subheader('Bobot Atom:  95.96')
            st.write('Ketidakpastian Bobot Atom: ± 0,02')
        elif(kode_unsur=='Nd'):
            st.header('Nama Atom: Neodymium  ')
            st.subheader('Bobot Atom:  144.242')
            st.write('Ketidakpastian Bobot Atom: ± 0,003') 
        elif(kode_unsur=='Ne'):
            st.header('Nama Atom: Neon  ')
            st.subheader('Bobot Atom:  20.1797')
            st.write('Ketidakpastian Bobot Atom: ± 0,0006')
        elif(kode_unsur=='Ni'):
            st.header('Nama Atom: Nickel  ')
            st.subheader('Bobot Atom:  58.6934')
            st.write('Ketidakpastian Bobot Atom: ± 0,0004')
        elif(kode_unsur=='Nb'):
            st.header('Nama Atom: Niobium ')
            st.subheader('Bobot Atom:  92.906 38')
            st.write('Ketidakpastian Bobot Atom: ± 0,00002')
        elif(kode_unsur=='N'):
            st.header('Nama Atom: Nitrogen ')
            st.subheader('Bobot Atom:  14.0067')
            st.write('Ketidakpastian Bobot Atom: ± 0,0002')
        elif(kode_unsur=='Os'):
            st.header('Nama Atom: Osmium ')
            st.subheader('Bobot Atom:  190.23')
            st.write('Ketidakpastian Bobot Atom: ± 0,03')
        elif(kode_unsur=='O'):
            st.header('Nama Atom: Oxygen ')
            st.subheader('Bobot Atom:  15.9994')
            st.write('Ketidakpastian Bobot Atom: ± 0,0003')
        elif(kode_unsur=='Pd'):
            st.header('Nama Atom: Palladium ')
            st.subheader('Bobot Atom:  106.42')
            st.write('Ketidakpastian Bobot Atom: ± 0,01')
        elif(kode_unsur=='P'):
            st.header('Nama Atom: Phosphorus  ')
            st.subheader('Bobot Atom:  30.973762')
            st.write('Ketidakpastian Bobot Atom: ± 0,000002')
        elif(kode_unsur=='Pt'):
            st.header('Nama Atom: Platinum  ')
            st.subheader('Bobot Atom:  195.084')
            st.write('Ketidakpastian Bobot Atom: ± 0,009')
        elif(kode_unsur=='K'):
            st.header('Nama Atom: Potassium ')
            st.subheader('Bobot Atom:  potassium')
            st.write('Ketidakpastian Bobot Atom: ± 0,0001')
        elif(kode_unsur=='Pr'):
            st.header('Nama Atom: Praseodymium ')
            st.subheader('Bobot Atom:  140.90765')
            st.write('Ketidakpastian Bobot Atom: ± 0,00002')
        elif(kode_unsur=='Pa'):
            st.header('Nama Atom: Protactinium ')
            st.subheader('Bobot Atom:  231.03588')
            st.write('Ketidakpastian Bobot Atom: ± 0,00002')
        elif(kode_unsur=='Re '):
            st.header('Nama Atom: Rhenium')
            st.subheader('Bobot Atom: 186.207')
            st.write('Ketidakpastian Bobot Atom: ± 0,001')
        elif(kode_unsur=='Rh'):
            st.header('Nama Atom: Rhodium')
            st.subheader('Bobot Atom: 102.90550')
            st.write('Ketidakpastian Bobot Atom: ± 0,00002')
        elif(kode_unsur=='Rb'):
            st.header('Nama Atom: Rubidum')
            st.subheader('Bobot Atom: 85.4678')
            st.write('Ketidakpastian Bobot Atom: ± 0,0003')
        elif(kode_unsur=='Ru'):
            st.header('Nama Atom: Ruthenium')
            st.subheader('Bobot Atom: 101.07')
            st.write('Ketidakpastian Bobot Atom: ± 0,02')
        elif(kode_unsur=='Sm'):
            st.header('Nama Atom: Samarium')
            st.subheader('Bobot Atom: 150.36')
            st.write('Ketidakpastian Bobot Atom: ± 0,02')
        elif(kode_unsur=='Sc'):
            st.header('Nama Atom: Scandium')
            st.subheader('Bobot Atom: 44.955912')
            st.write('Ketidakpastian Bobot Atom: ± 0,000006')
        elif(kode_unsur=='Se'):
            st.header('Nama Atom: Selenium')
            st.subheader('Bobot Atom: 78.96')
            st.write('Ketidakpastian Bobot Atom: ± 0,03')
        elif(kode_unsur=='Si'):
            st.header('Nama Atom: Silicon')
            st.subheader('Bobot Atom: 28.0855')
            st.write('Ketidakpastian Bobot Atom: ± 0,0003')
        elif(kode_unsur=='Ag'):
            st.header('Nama Atom: Silver')
            st.subheader('Bobot Atom: 107.8682')
            st.write('Ketidakpastian Bobot Atom: ± 0,0002')
        elif(kode_unsur=='Na'):
            st.header('Nama Atom: Sodium')
            st.subheader('Bobot Atom: 22.98976928')
            st.write('Ketidakpastian Bobot Atom: ± 0,00000002')
        elif(kode_unsur=='Sr'):
            st.header('Nama Atom: Strontium')
            st.subheader('Bobot Atom: 87.62')
            st.write('Ketidakpastian Bobot Atom: ± 0,01')
        elif(kode_unsur=='S'):
            st.header('Nama Atom: Sulfur')
            st.subheader('Bobot Atom: 32.065')
            st.write('Ketidakpastian Bobot Atom: ± 0,005')
        elif(kode_unsur=='Ta'):
            st.header('Nama Atom: Tantalum')
            st.subheader('Bobot Atom: 180.94788')
            st.write('Ketidakpastian Bobot Atom: ± 0,00002')
        elif(kode_unsur=='Te'):
            st.header('Nama Atom: Tellurium')
            st.subheader('Bobot Atom: 127.60')
            st.write('Ketidakpastian Bobot Atom: ± 0,03')
        elif(kode_unsur=='Tb'):
            st.header('Nama Atom: Terbium')
            st.subheader('Bobot Atom: 158.92535')
            st.write('Ketidakpastian Bobot Atom: ± 0,00002')
        elif(kode_unsur=='Tl'):
            st.header('Nama Atom: Thallium')
            st.subheader('Bobot Atom: 204.3833')
            st.write('Ketidakpastian Bobot Atom: ± 0,0002')
        elif(kode_unsur=='Th'):
            st.header('Nama Atom: Thorium')
            st.subheader('Bobot Atom: 232.03806')
            st.write('Ketidakpastian Bobot Atom: ± 0,00002')
        elif(kode_unsur=='Tm'):
            st.header('Nama Atom: Thulium')
            st.subheader('Bobot Atom: 168.93421')
            st.write('Ketidakpastian Bobot Atom: ± 0,00002')
        elif(kode_unsur=='Sn'):
            st.header('Nama Atom: Tin')
            st.subheader('Bobot Atom: 118.710')
            st.write('Ketidakpastian Bobot Atom: ± 0,007')
        elif(kode_unsur=='Ti'):
            st.header('Nama Atom: Titanium')
            st.subheader('Bobot Atom: 47.867')
            st.write('Ketidakpastian Bobot Atom: ± 0,001')
        elif(kode_unsur=='W'):
            st.header('Nama Atom: Tungsten')
            st.subheader('Bobot Atom: 183.84')
            st.write('Ketidakpastian Bobot Atom: ± 0,01')
        elif(kode_unsur=='U'):
            st.header('Nama Atom: Uranium')
            st.subheader('Bobot Atom: 238.02891')
            st.write('Ketidakpastian Bobot Atom: ± 0,00003')
        elif(kode_unsur=='V'):
            st.header('Nama Atom: Vanadium')
            st.subheader('Bobot Atom: 50.9415')
            st.write('Ketidakpastian Bobot Atom: ± 0,0001')
        elif(kode_unsur=='Xe'):
            st.header('Nama Atom: Xenon')
            st.subheader('Bobot Atom: 131.293')
            st.write('Ketidakpastian Bobot Atom: ± 0,006')
        elif(kode_unsur=='Yb'):
            st.header('Nama Atom: Ytterbium')
            st.subheader('Bobot Atom: 173.054')
            st.write('Ketidakpastian Bobot Atom: ± 0,005')
        elif(kode_unsur=='Y'):
            st.header('Nama Atom: Yttrium')
            st.subheader('Bobot Atom: 88.90585')
            st.write('Ketidakpastian Bobot Atom: ± 0,00002')
        else:
            st.write('Silahkan Masukkan Kode  dengan Benar')
def Perhitungan():
    st.header('Silahkan Pilih Jenis Perhitungan')
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    
    # Tombol untuk perhitungan ketidakpastian
    if st.button('Perhitungan Ketidakpastian Pengukuran Bobot Atom (miu)'):
        hitung_ketidakpastian()

    # Tombol untuk perhitungan bobot molekul
    if st.button('Perhitungan Bobot Molekul (BM)'):
        hitung_bobot_molekul()

    # Tombol untuk perhitungan jumlah mol
    if st.button('Perhitungan Mol (n)'):
        hitung_jumlah_mol()

def hitung_ketidakpastian():
    st.subheader('Masukkan Informasi di bawah ini untuk Menghitung Ketidakpastian Pengukuran Bobot Atom:')
    
    # Meminta pengguna untuk memasukkan nilai U
    U = st.number_input('Masukkan nilai U :', format="%.5f")
    
    # Memanggil fungsi untuk menghitung ketidakpastian
    hasil = U / math.sqrt(3)
    
    st.write(f'Ketidakpastian pengukurannya  {hasil} mg/mmol')

def hitung_bobot_molekul():
    st.subheader('Masukkan Informasi di bawah ini untuk Menghitung Bobot Molekul:')
    
    # Input bobot atom
    bobot_atom = st.number_input('Masukkan bobot atom ', step=0.01)  # Step disesuaikan dengan kebutuhan
    
    # Input jumlah atom
    jumlah_atom = st.number_input('Masukkan jumlah atom', step=1)  # Step disesuaikan dengan kebutuhan
    
    # Hitung bobot molekul
    bobot_molekul = bobot_atom * jumlah_atom
    
    # Tampilkan hasil
    st.write('Bobot Molekul (BM) adalah:', bobot_molekul, 'mg/mmol')

def hitung_jumlah_mol():
    st.subheader('Masukkan Informasi di bawah ini untuk Menghitung jumlah Mol:')
    
    # Formulir input untuk massa dan Mr
    massa = st.number_input("Masukkan Massa (mg)")
    Mr = st.number_input("Masukkan bm (Bobot Molekul)")
    hitung = st.button("Hitung")
    
    if hitung:
        # Perhitungan jumlah mol
        mol = massa / Mr
        st.write(f"Jumlah Mol: {mol} mol")

# Daftar menu
menu_items = {
    "About us": Aboutus,
    "Pendahuluan": Pendahuluan,
    "Pencarian Bobot Atom beserta Ketidakpastiannya" : Pencarian,
    "Kalkulator Perhitungan": Perhitungan, 
}
   
# Sidebar
selection = st.sidebar.radio("Menu", list(menu_items.keys()))

# Memilih menu yang dipilih
menu_items[selection]()