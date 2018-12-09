import socket

def segiempat(s=0):
           L = s * s
           return L
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print "Server sudah siap"
data = ''

while 1:
           komm, addr = s.accept()
           while data.lower() != 'keluar':
                      data = komm.recv(1024)
                      print 'pesan: ', data
                      if data.find("parameter") != -1:
                                 param, value = data.split("=")
                                 if param == "parameter":
                                            s = float(value)
                                            x = value
                                            komm.send("parameter dicatat")
                                 elif data == "hitung":
                                            komm.send("luas segiempat dengan sisi () adalah {}". format(x, segiempat(s)))
                                 else:
                                            komm.send("Tidak ada")
