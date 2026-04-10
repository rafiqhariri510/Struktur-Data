def cari_posisi_a():
    print("=== Program Pencarian Karakter 'a' ===")
    print("(Ketik 'exit' untuk berhenti)")
    
    while True:
        nama = input("\nMasukkan nama: ")
        
        if nama.lower() == 'exit':
            print("Program selesai. Sampai jumpa!")
            break
            
        posisi = [i + 0 for i, huruf in enumerate(nama) if huruf.lower() == 'a']
        
        if posisi:
            list_posisi = ", ".join(map(str, posisi))
            print(f"Hasil: Huruf 'a' ditemukan pada urutan ke: {list_posisi}")
        else:
            print("Hasil: Tidak ada huruf 'a' dalam nama tersebut.")

if _name_ == "__main__":
    cari_posisi_a()