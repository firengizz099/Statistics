import math
from scipy.stats import norm

# P degeri ile oran icin Hipotez Testi:
# Z tablosu kullanilir:

"""Soru:
Turkiyedeki universitelerde bulunduklari bolume isteyerek gelen ogrencilerin orani 0,50'den farklidir iddasinda bulunmaktadir. 
Bu iddayi test etmek icin rasgele secilen 100 ogrenciden 35'nin kayitli oldugu bolume isteyerek geldiklerini saptanmistir. Bu bbilgilere
gore, alfa(0,01) icin bu idda hakkinda karariniz ne olur?"""

# Formul
# z test = P(sapka) - P / (kok icinde)  P * (1-P) / n
# P(sapka) - orneklemdeki oran
# P - papulasyondaki idda edilen hipotezdeki oran

# Hesaplama
# adim 1: Hipotezi kur

# H0: P = 0,50
# H1: P != 0,50

# adim 2: 
# orneklemdeki oran p(sapka) = 35/100

# Veriler
n = 100
x = 35
p_sapka = x / n
p_hipotez = 0.50

# alfayi ikiye bolunmesinin sebebi: Cesid bu sekilde oldugu icin H0: P = 0,50 : H1: P != 0,50
alfa = 0.01/2

# z testinin formulunu  uygula 
z_test = (p_sapka - p_hipotez) / math.sqrt(p_hipotez * (1 - p_hipotez) / n)
print(z_test) # z testinin sonucu -3 

# 3 cu adim p degerini hesaplama 
"""z test sonucu negativ(-) oldugu icin z'nin z testden kucuk olma olasiligini olucak. 
Bu olasiligi bulup 2 ile carpdigimizda p degerine ulasacagiz. p_degeri = 2*P(z<-3) """

# Z tablosuna bak hangi sayiya denk geliyor
p_degeri = 2 * norm.cdf(-abs(z_test))  
print("P değeri:", p_degeri)

# 4 adim

if alfa > p_degeri:
    print("H0 hipotezi kabul edilir.")
else:
    print("H0 hipotezi reddedilir.")
