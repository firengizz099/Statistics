# Statistics
![App Screenshot](https://github.com/firengizz099/Statistics/blob/main/statistics-vector-6410096.jpg?raw=true)
**p_degeri_oran_h.t.py**

P degeri ile oran icin Hipotez Testi:

Bu kod, verilen veriler üzerinden hipotez testi gerçekleştiriyor. Kodun adım adım açıklaması:

Gerekli kütüphaneler ve verileri içe aktarın. Verilen sorunun tanımını ve kurulan hipotezleri yorumlayın. Örneklemdeki oranı hesaplayın: p_sapka = 35/100.

Alfa seviyesini belirleyin: alfa = 0.01/2. Z testi istatistiğini hesaplayın: z_test = (p_sapka - p_hipotez) / math.sqrt(p_hipotez * (1 - p_hipotez) / n). Z testi sonucunu ekrana yazdırın. Z test istatistiğini kullanarak p değerini hesaplayın. Negatif olduğu için mutlak değer alıyoruz: p_degeri = 2 * norm.cdf(-abs(z_test)). P değerini ekrana yazdırın. Karar aşamasına geçin: Eğer alfa seviyesi p değerinden büyükse, H0 hipotezi kabul edilir. Aksi halde, reddedilir.

# Paulasyon Varyansi bilinirken Hipotez Testi
**Paulasyon Varyansi biliniyorken_hipotez_testi.py**

Bu kod, bir hipotez testi örneği üzerinden çalışmaktadır. İlaç tedavisinin etkisini göstermek için örnek veriler kullanılmıştır. Hipotez testinin genel mantığı, bir iddiayı (null hipotezi) test ederek, verilerin istatistiksel olarak iddia edilen durumdan farklı olup olmadığını belirlemektir. Eğer hesaplanan z-test istatistiği, belirlenen anlamlılık düzeyine karşılık gelen kritik değeri aşarsa, null hipotezi reddedilir ve alternatif hipotezi kabul edilir. Aksi durumda, null hipotezi kabul edilir.

# Bayes Theorem
**Bayes.py**

![App Screenshot](https://github.com/firengizz099/Statistics/blob/main/Baye's-Theorem-(1).png?raw=true)

Bayes Teoremi, genellikle "şartlı olasılık" olarak adlandırılan kavramı işler. Şartlı olasılık, bir olayın başka bir olayın gerçekleştiği bir koşula göre olasılığını ifade eder. Bu teorem, iki olay arasındaki ilişkiyi açıklarken şu formülle ifade edilir: P(A/B) = P(A) * P(B/A) / P(B) Burada: P(A∣B): B koşulu altında A'nın olasılığı (A'nın B'ye göre şartlı olasılığı) P(B∣A): A koşulu altında B'nin olasılığı (B'nin A'ya göre şartlı olasılığı) P(A): A'nın genel olasılığı P(B): B'nin genel olasılığı Bayes Teoremi, bir olayın sonucunu daha fazla bilgiyle güncellemek istediğimiz durumları ele almak için kullanılır. Özellikle tıp, istatistik, yapay zeka ve veri analizi gibi alanlarda sıkça kullanılır. Teorem, bize önceden bilinen ve yeni elde edilen bilgileri bir araya getirerek daha hassas sonuçlar elde etmemize yardımcı olur.
