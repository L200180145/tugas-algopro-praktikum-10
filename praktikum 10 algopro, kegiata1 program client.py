import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50001))
print("Mesin penjawab otomatis sudah siap")

while pesan.lower() != 'q':
           pesan = raw_input('Pertanyaan: ')
           s.send(pesan)
           if pesan.lower() == 'Keluar':
                      response = s.recv(1024)
                      print 'Jawaban: ',response
                      s.close()
                      break
           elif pesan.lower() != 'keluar':
                      response = s.recv(1024)
                      print 'Jawaban:', response
s.close()
