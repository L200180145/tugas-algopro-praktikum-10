import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
print "Menghitung Luas Segiempat"

while pesan != 'keluar':
           pesan = raw_input('Pesan: ')
           s.send(pesan)
           if pesan.lower() == 'keluar':
                      response = s.recv(1024)
                      print 'respom: -'
                      s.close()
                      breal
           elif pesan.lower() != 'keluar':
                      response = s.recv(1024)
                      print 'respon: ', response
s.close()
