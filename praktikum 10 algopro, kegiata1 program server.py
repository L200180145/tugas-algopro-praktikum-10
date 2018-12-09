import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50001))
s.listen(5)
print("Server penjawab otomatis sudah siap")
data = ''
kamus = {'nama': 'Safira Putri Kinanti','NIM':'L200180145','Angkatan':'2018','keluar':'Siap!'}
while data.lower() != 'keluar':
   komm, addr = s.accept()
   while data.lower() != 'Keluar':
              data = komm.recv(1024)
              print "Perintah:", data
              if kamus.has_key(data):
                         komm.send(kamus[data])
              else:
                         komm.send('Pertanyaan anda tidak relevan')
