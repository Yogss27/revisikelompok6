import streamlit as st

# Fungsi untuk menghitung pH
def hitung_ph(H):
    pH = -1 * (10**-H)
    return round(pH, 2)

# Tampilan aplikasi
def app():
    st.title("Alat Hitung pH menggunakan Konsentrasi (mol/L)")
    st.write("Masukkan nilai konsentrasi ion hidrogen (H+) dalam mol/L")

    # Input nilai konsentrasi ion hidrogen
    H = st.number_input("Nilai H+ (mol/L)", value=0.0, format="%.5f", step=0.00001)

    # Hitung pH menggunakan fungsi yang telah dibuat
    pH = hitung_ph(H)

    # Tampilkan hasil perhitungan
    st.write("Nilai pH:", pH)

# Jalankan aplikasi
if __name__ == "__main__":
    app()
