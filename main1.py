#Flask modülünü kulabilmek amacıyla kendi kod dosaymın içerinse komutları import ettim.
from flask import Flask
import random

# app adında bir değişken oluşturup bir uyguluma yaratıyoruz.
# Burada Flask uygulamasının bir örneğini oluşturmuş olursunuz. Bu sayede isimlendirmesiyle yep yeni bir backend uygulaması başlatırsınız. 
app = Flask(__name__)

# Dekaratörler: Belirli bir olay olduğu zaman altındaki fonksiyonu çalıştırır.
# URL Rotalarını belirler bu sayede hangi sayfa hangi URL'de açılacak ve hangi fonksiyon hangi URL'de tetiklenecek bunu öğrenebiliriz.
# URL = Uniform Resource Loader
@app.route("/")
def hello_world():
    return  '''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <link rel="stylesheet" href="./static/proje2.css">
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device=width, ininitial-scale=1.0">
                    <title>Document</title>
                </head>
                <body>
                    <h1>Teknoloji Bağımlılığı </h1>
                    <p>Teknoloji Bağımlılığı çok önemli bir sorundur.</p>
                    <h3>bağımlılık nedir</h3>
                    <strong>nasıl başa çıkılır</strong>
                    <en> bağımlılıklar</en>
                    <br>
                    <img src = "https://i.pinimg.com/564x/41/23/05/41230590a0ff35dd78f8856bd993affb.jpg" alt = "resim bulunamadı">
                    <ul>
                        <li>Teknolojiye bağımlı kalmamalıyız</li>
                        <li>bol bol dışarı çıkmalıyız</li>
                        <li>sadece belli saatlerde teknolojik aletleri kullanmalıyız</li>
                    </ul>
                    <ol>
                        <li>ufdıodu</li>
                        <li>çilek</li>
                        <li>elma</li>
                    </ol>
                    <a href="https://www.yesilay.org.tr/tr/bagimlilik/teknoloji-bagimliligi">Bu makaleyle daha iyiy anlarsınız</a>
                    <h3 class = "abc">Anladınız mı</h3>

                    <body>
                        <iframe src="https://weather.com/tr-TR/weather/tenday/l/Çanakkale+Çanakkale?canonicalCityId=212fdb254bdefa542c48e1b8e3afedff254649847a597903cd0d22a1c2aa27a4" width="500px" height="250px">

                    <a href="/sayfa2">2. bir sayfa için tıkla</a>

                <body>
                </html>
            '''

@app.route('/sayfa2')
def bilgi():
    liste = ['Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.',
             '2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin yüzde 50 den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.',
             'Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.',
             "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
             "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
             "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
             "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
             "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."
             ]
    rastgelebilgi = random.choice(liste)

    return f'<p>{rastgelebilgi}</p>'


app.run(debug=True)


