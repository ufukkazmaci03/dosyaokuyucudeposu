#DOSYA VERİ OKUMA
f = open("metin.txt" , "r" , encoding="UTF-8")


yazilar = f.read()
print(yazilar)
f.close()

#DOSYA YAZI YAZMA
f2 = open("bilgi.txt" , "w+", encoding="UTF-8")

bilgi = "Türkiye'nin başkenti Ankar'dır."
f2.write(bilgi)
f2.close()