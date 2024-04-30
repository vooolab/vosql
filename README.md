<h1 align="center">
VoSql v1.0.1
</h1>
SQL Zaafiyetli siteleri aramakta zorluk çektiğinizi tahmin edebiliyorum. Tarayıcı üzerinde teker teker denemek yerine aynı dorku araç üzerinde tarayabilir ve çıkan yüzlerce sonuç arasından saniyeler içerisinde zaafiyetli siteleri bulabilirsiniz. Aoihttp ve Asyncio gibi yüksek iş parçacığına sahip araçlar sayesinde işlem 10 kat daha hızlı sonuç vermektedir. Ücretsiz ve Açık Kaynak olarak paylaşılan bu projeyi çalıştırmak için aşağıdaki dökümantasyonu inceleyiniz.

<h2 align="center">
Kurulum
</h2>
<h3>GitHub Kurulumu</h3>
<b>Termux</b>
<pre>pkg install python
git clone https://github.com/vooolab/vosql/
cd vosql
pip install -r requirements.txt
python vosql.py</pre>
<b>Linux Dağıtımları</b>
<pre>sudo apt-get install python python3 python-pip
git clone https://github.com/vooolab/vosql/
cd vosql
pip3 install -r requirements.txt
python3 vosql.py</pre>
<b>


<h2 align="center">
Güncelleme Notları
</h2>

- SQLMAP parametre önericisi eklendi.
- Bağlantı hataları düzeltildi.
- Dosya yazma problemi düzenlendi.
