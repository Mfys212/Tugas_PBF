# fungsi enkripsi
def enkripsi(password):
  # jika panjang karakter lebih dari 100
  if len(password) > 100 or len(password) == 0:
    print("Enter 1-100 characters")
  else:
    # merubah setiap karakter menjadi kode ascii dan ditampung dalam list
    ascii = [str(ord(i)) for i in password]
    # membuat 3 value dari setiap kode ascii dan menggabungkan semuanya
    enkri = ''.join(chr((int(j)//26)+80)+chr((int(j)%26)+80)+('+' if (int(j)//26)+80 > (int(j)%26)+80 else '-') for j in ascii)
    # menampilkan hasil enkripsi
    print("The encryption password is: ", enkri)

# fungsi dekripsi
def dekripsi(password):
  # split 3 value 
  split_ps = [(password[k:k+3]) for k in range(0, len(password), 3)]
  # membuat 3 value kembali ke kode ascii lalu ke karakter asli dan menggabungkan semuanya
  dekri = ''.join(chr(((ord(list(z)[0])-80)*26)+(ord(list(z)[1])-80)) for z in split_ps)
  # menampilkan hasil dekripsi
  print("The password is: ", dekri)
