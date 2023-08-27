import math
from scipy.stats import norm
# Papulasyon varyansi biliniyorken hipotez testi

"""Beirli bir hastaligin tedavisi icin yeni bir ilac gelistirildi. Ilac tedavi edilen hastalarin ortalama iylesme suresinin
10 gunden az oldugunu ifade eder. Ratgele secilen 7 hasta sozu edilen ilac ile teadvi edilmistir ve kac gunde iyilestikleri
asagida verilmistir
----------2,4,11,3,4,6,8------------ sigma kare = 4, alfa = 0,01 .Bu idda icin kararniz ne olur?"""

# Papulasyon varyansi biliniyor ( o zaman z testi kullanilir )
# z_test = x(bar) - M(mu) / sigma / karekok(n)
veriler = [2,4,11,3,4,6,8]
ortalama = sum(veriler) / len(veriler)
print('ortalama', ortalama)

# sigma kare = 4
sigma_kare = 4

# alfa = 0,01 - anlamlilik duzeyi 
# alfadan cikan sonucun z tablosundan bulacagiz;

alfa = 1 - 0.01

# adim 1 : Hipotezi kur:
# H0: M = 10
# H1: M < 10
m = 10

# z tablosundan 0.99 baktigimizda 2.3 ve 0.03'e denk geliyor. Bu sonuclari topla 2.3+0.03 kritik deger ortaya cikiyor.

# adim 2: Kritik değeri al
kritik_deger = norm.ppf(alfa)
print(kritik_deger)

# adim 3 : 
z_test = (ortalama - m) / math.sqrt(sigma_kare / len(veriler))



print("Z-test değeri:", z_test)
print("Kritik değer:", kritik_deger)


# adim 4: Karar verme
if z_test < kritik_deger:
    print("H0 hipotezi reddedilir. Yani, ortalama 10'dan farklıdır.")
else:
    print("H0 hipotezi kabul edilir. Yani, ortalama 10'dan farklı değildir.")


