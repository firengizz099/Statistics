""" Soru 1:
Piknik yapmayi dusunen bir grup sabah havanin bulutlu oldugunu goruyor. 
Yagmurlu gunlerin %50'sinin bulutlu bir gunle basladigi biliniyor.
Gunun %40'i bulutlu baslamaktadir. Bir gunun yagmurlu gun olma olasiligi %10'dur. 
Buna gore bulutlu  baslanan bir gunde yagmur gorulme
olasiligi nedir?"""

# P(yagmurlu/bulutlu) = ?
# Bayes - Formul: P(A/B) = P(A) * P(B/A) / P(B)
# P(bulutlu/yagmurlu) = 0,50
# P(bulutlu) = 0,40
# P(yagmur) = 0,10
# P(yagmurlu/bulutlu) = P(yagmurlu) * P(bulutlu/yagmurlu) / P(bulutlu)


# P(yagmurlu/bulutlu) = ?
p_bulutlu_yagmurlu = 0.50
p_bulutlu = 0.40
p_yagmurlu = 0.10

p_yagmurlu_bulutlu = (p_yagmurlu * p_bulutlu_yagmurlu) / p_bulutlu
print('bulutlu  baslanan bir gunde yagmur gorulme olasiligi',p_yagmurlu_bulutlu)

###########################################################################################################################

"""Soru 2: Bir tıp testi, belirli bir hastalığı doğru pozitif sonuç verme olasılığı %95 ve sağlıklı bir kişiyi yanlış
pozitif olarak tanıma olasılığı %10'dur. Toplumun %1'inde bu hastalık gerçekten bulunmaktadır.
Eğer test pozitif çıkarsa, kişinin gerçekten hastalığa sahip olma olasılığı nedir?"""

# P(pozitif/hasta) = ?
# Bayes - Formul: P(A/B) = P(A) * P(B/A) / P(B)
# P(dogru/pozitif) = %95
# P(pozitif_hastalik_yok) = %10
# P(hasta) = %1

# Verilen olasılıklar
P_pozitif_hasta = 0.95
P_pozitif_hastalik_yok = 0.10
P_hasta = 0.01

"""
P(pozitif) hesaplanırken iki durumu dikkate alıyoruz: Birincisi, gerçekten hastalığa sahip olan 
bir kişinin test sonucunun pozitif çıkma olasılığı (P(pozitif|hasta) * P(hasta)), ikincisi ise hastalığı olmayan 
bir kişinin test sonucunun pozitif çıkma olasılığı ((P(pozitif|hastalik_yok) * P(hastalik_yok)). 
Bu iki durumun toplamı, test sonucunun pozitif çıkma olasılığını verir (P(pozitif))."""
# P(pozitif) hesaplanıyor
P_pozitif = (P_pozitif_hasta * P_hasta) + (P_pozitif_hastalik_yok * (1 - P_hasta))

# Bayes Teoremi uygulanarak kişinin hastalığa sahip olma olasılığı hesaplanıyor
P_hasta_pozitif = (P_pozitif_hasta * P_hasta) / P_pozitif

print("Kişinin test pozitif çıktığında gerçekten hastalığa sahip olma olasılığı:", P_hasta_pozitif)

####################################################################################################
"""
Soru 3 :
Diabet testi alan insanin %20'sinin gercekten dibaet hastasi oldugu tesit edilmistir. 
Belli bir markanin isbaet oranlari ise asagidaki sekilde:
-- Testi yapan kisi gercekten diabet hastasiysa %90 ihtimal ile testi pozitif sonuc vermektedir.
-- Testi yapan kisi diabet hastasi degilse %80 ihtimali ile test negatif sonuc vermektedir.
Tum bu verileri dikkate alarak eger kisi testi almissa ve sonuc poztifse gercekten diabet hastasi olmasi olasiligi nedir?"""

# B1 = diabet hastasi
# B2 = diabet hastasi degil
# A = test pozitif
# P(B1/A) = ?
# Formul: eger ornek uzayi 2 tane olaya ayrilabiliyorsa bu sekilde yazila bilir formul:
#               P(A/B1) * P(B1)
#  P(B1/A) = --------------------------------
#               P(A/B1) * P(B1) + P(A/B2) * P(B2)

# Veriler
# P(B1) = Diabet hastası olma olasılığı = 0.2
# P(B2) = Diabet hastası olmama olasılığı = 0.8
# P(A/B1) = Test pozitif sonuç verme olasılığı eğer gerçekten diabet hastasıysa = 0.9
# P(A/B2) = Test pozitif sonuç verme olasılığı eğer diabet hastası değilse = 0.2

# Verilen olasılıklar

p_b1 = 0.2  # P(B1)
p_b2 = 0.8  # P(B2)
p_a_b1 = 0.9  # P(A/B1)
p_a_b2 = 0.2  # P(A/B2)

# P(B1/A) hesaplama
p_b1_a = (p_a_b1 * p_b1) / (p_a_b1 * p_b1 + p_a_b2 * p_b2)

print('testi almissa ve sonuc poztifse gercekten diabet hastasi olmasi olasiligi',p_b1_a)

####################################################################################################

"""
Soru 4:
Bir şehirde yaşayan insanlar arasında, COVID-19 testi pozitif çıkan bir kişinin gerçekten
enfekte olmuş olma olasılığı %95'tir. Ancak şehirdeki insanların sadece %2'si enfekte durumdadır. 
COVID-19 testi negatif çıkan bir kişinin gerçekten enfekte olmamış olma olasılığı ise %90'dır.
Bir kişinin COVID-19 testi pozitif çıkmışsa, gerçekten enfekte olma olasılığı nedir?"""

# Verilen Olasılıklar:

# P(B1) = Gerçekte enfekte olma olasılığı = 0.95 (veya %95)
# P(B2) = Toplam enfekte olmama olasılığı = 0.05 (veya %5)
# P(A|B1) = Test pozitif çıkarsa gerçekten enfekte olma olasılığı = 0.90 (veya %90)
# P(A|B2) = Test pozitif çıkarsa gerçekten enfekte olmama olasılığı = 0.10 (veya %10)


p_b1 = 0.95  # P(B1)
p_b2 = 0.02  # P(B2)
p_a_b1 = 0.90  # P(A/B1)
p_a_b2 = 0.10  # P(A/B2)

p_b1_a_sonuc = (p_a_b1 * p_b1) / (p_a_b1 * p_b1 + p_a_b2 * p_b2)

print('COVID-19 testi pozitif çıkmışsa, gerçekten enfekte olma olasılığı', p_b1_a_sonuc)
