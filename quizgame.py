import random
from tkinter import *
from pygame import mixer 


mixer.init()

 
window = Tk()
window.geometry("800x600")
window.title("genel kültür test (Beta)")


window.configure(background="Powder blue")
mi = PhotoImage(file="BUTTON.png")
home = PhotoImage(file="home.png")
musici = PhotoImage(file="music.png")
nextb = PhotoImage(file="next.png")
question = PhotoImage(file="question.png")
exitb=PhotoImage(file="exit.png")
back=PhotoImage(file="back.png")
home32=PhotoImage(file="page.png")

settings=PhotoImage(file="settings.png")
play=PhotoImage(file="play.png")
pauseb=PhotoImage(file="pause.png")
language=PhotoImage(file="language.png")
bayrak=PhotoImage(file="bayrak.png")
bayrak2=PhotoImage(file="bayrak2.png")
def playmusic():


            mixer.music.load("c418-sweden-minecraft-volume-alpha.mp3")
            mixer.music.load("c418-subwoofer-lullaby-minecraft-volume-alpha.mp3")
            mixer.music.load("y2mate.com - C418 - Mice on Venus - Minecraft Volume Alpha_DZ47H84Bc_Q.mp3")
            mixer.music.load("y2mate.com - C418 - Haggstrom - Minecraft Volume Alpha_laZusNy8QiY.mp3")    
            mixer.music.play()
        

playmusic()

questions = [["Hangisi tarihteki Rus devlet yöneticilerinden biridir?","deli putin","sezar","kazıklı voyvoda","deli petro"]]
questions.append(["Türkiye’de Erozyonla mücadele amacıyla kurulan vakfın kısa adı nedir?","kızılay","tema","umke","afad"])
questions.append(["Altın Palmiye Ödülleri hangi şehrimizde verilmektedir?","malatya","istanbul","muğla","antalya"])
questions.append(["Amerika kıtasını 2’ye ayıran önemli su geçidinin adı nedir?","missouri","kızıl nehir","fırat nehri","panama"])
questions.append(["Dünyanın ilk haritasını çizen ünlü Türk denizcisi kimdir?","ibni sina","barbaros hayrettin paşa","kaptanı derya","piri reis"])
questions.append(["Tarihte Türk adıyla kurulan ilk devlet hangisidir?","köktürk","urartular","uygurlar","göktürk"])
questions.append(["Türkiye’nin uluslararası otomatik telefon kod numarası kaçtır?","70","95","80","90"])
questions.append(["Mimar Sinan'ın Ustalık Dönemi eseri sayılan Edirne'deki eserinin adı nedir?","mimar-i edirne","edirne","mimar-i selimiye","selimiye"])
questions.append(["Nobel ödülleri hangi ülkede verilmektedir?","Türkiye","ABD","almanya","isveç"])
questions.append(["Gece gündüz eşitliği (ekinoks) bir yılda kaç kez gerçekleşir?","3","4","1","2"])
questions.append(["UEFA Kupasını alan ilk Türk takımı hangisidir?","beşiktaş","fenerbahçe","trabzonspor","galatasaray"])
questions.append(["Osmanlı Devleti'nde ilk nüfus sayımı hangi padişah zamanında yapılmıştır?","1.mahmut","2.mehmet","kanuni sultan süleyman","2.mahmut"])
questions.append(["‘ Türk Devleti bir Cumhuriyettir.’ ifadesi anayasamızın kaçıncı maddesidir?","4","2","3","1"])
questions.append(["İlk Türkçe sözlük hangisidir?","divanı türk","türkçe sözlük","türk-i divan","Divan-ı Lugat-it türk"])
questions.append(["Ülkemiz Avrupa Birliğine tam üyelik müzakerelerine hangi yılda başlamıştır ?","2008","2007","2006","2005"])
questions.append(["Pusulada ( N ) harfi hangi yönü ifade eder ?","güney","doğu","batı","kuzey"])
questions.append(["Çocuk hakları günü hangi tarihte kutlanmaktadır ?","20 mart","20 nisan","19 nisan","20 kasım"])
questions.append(["Türkçe hangi dil grubuna girmektedir ?","Osmanlı","farsça","türkçe","uray-altay"])
questions.append(["Avrupa Birliğini iki kez halk oylamasıyla reddeden ülke hangisidir ?","isvicre","ingiltere","ispanya","norveç"])
questions.append([" Kadınlara seçme ve seçilme hakkı tanıyan ilk ülke hangisidir ?","çin","ABD","almanya","Türkiye"])
questions.append(["İstiklal Marşımızın bestecisi kimdir?","namık kemal","yahya kemal","mehmet akif ersoy","Osman Zeki Üngör"])
questions.append([" İnternet üzerinde en fazla kullanılan arama motoru hangisidir ?","yandex","bing","yaho","google"])
questions.append(["Eurovision ‘da Türkiyeye birincilik getiren sanatçımız kimdir ?","serdar ortaç","hadise","hande yener","sertap erener"])
questions.append(["Türkiyenin en büyük gölünün adı nedir ?","tuz gölü","eğridir gölü","ankara gölü","van gölü"])
questions.append(["Pisagor teoremi hangi bilim dalıyla ilgilidir ?","felsefe","coğrafya","biyoloji","matematik"])
questions.append([" ‘İnce Memed’ adli eserin sahibi kimdir ?","tehvik fiket","yahya kemal","reşat nuri","yaşar kemal"])
questions.append([" Aşağıda Verilen İlk Çağ Uygarlıklarından Hangisi Yazıyı İcat Etmiştir?","akadlar","hititler","elamlar","sümerler"])
questions.append([" Mustafa Kemal Atatürk’ün Nüfusa Kayıtlı Olduğu İl Hangisidir?","bursa","ankara","istanbul","gaziantep"])
questions.append(["Romen Rakamında Hangi Sayı Yoktur?","101","50","100","0"])
questions.append(["Bir Gün Kaç Saniyedir?","86000","88600","84000","86400"])
questions.append(["Üç Büyük Dince Kutsal Sayılan Şehir Hangisidir?","medine","mekke","roma","kudüs"])
questions.append(["Hangi Ülkenin İki Tane Başkenti Vardır?","nijerya","senegal","el salvador","güney afrika"])
questions.append([" Aspirinin Hammaddesi Nedir?","zeytin","köknar","meşe","söğüt"])
questions.append(["Bir Sebepten Dolayı Tek Kulağına Küpe Takan Osmanlı Padişahı Kimdir?","Kanuni Sultan Süleyman","2.mehmet","orhanbey","yavuz selim"])
questions.append(["Fatih Sultan Mehmet’in babası kimdir?","yıldırım beyazıt","1.mehmet","2.mehmet","2.murat"])
questions.append(["Hangisi periyodik tabloda bulunan bir element değildir?","demir","azot","oksijen","su"])
questions.append(["Hangisi tarihteki Türk devletlerinden biri değildir?","hun imparatorluğu","avar kağanlığı","Osmanlı","emevi devleti"])
questions.append(["Galatasaray hangi yıl UEFA kupasını almıştır?","2000","2003","2002","2001"])
questions.append(["Kıbrıs Barış harekatı hangi tarihte gerçekleşmiştir?","1970","1972","1975","1974"]) 
questions.append(["Hangi ülke Asya kıtasındadır?","libya","peru","madagaskar","singapur"])
questions.append(["Hangisi Kanuni Sultan Süleyman’ın eşidir?","safiye sultan","fatma sultan","kösem sultan","hürrem sultan"])
questions.append(["Osmanlı’da Lale devri hangi padişah döneminde yaşamıştır?","III.mahmut","IV.murat","III.selim","III.ahmet"])
questions.append(["Osmanlı İmparatorluğu yaklaşık kac asır hüküm sürmüştür?","5","4","7","6"])
questions.append(["Duvara asılı bir haritanın sağı her zaman hangi yönü gösterir ?","kuzey","batı","güney","doğu"])
questions.append(["Aşağıdaki illerden hangisinde Akdeniz iklimi görülür?","aydın","izmir","muğla","mersin"])
questions.append(["Aşağıdakilerden hangisi çocuk hastalığıdır?","nezle","kızamık","grip","kabakulak"])
questions.append(["1071'de yapılan Malazgirt Savaşıyla Anadolu’nun kapılarını Türklere açan Selçuklu Sultanı kimdir?","sultan alladdin","fatih sultan","sultan mehmet","sultan alparslan"])
questions.append(["Aşağıdaki hangi coğrafi bölgede dağlar denize dik uzanır?","karadeniz bölgesi","iç anadolu bölgesi","Akdeniz bölgesi","ege bölgesi"])
questions.append(["Keçinin erkeğine ne ad verilir?","take","tiki","taka","teke"])
questions.append(["İçerisinde yüksek oranda demir minerali bulunduran sebze hangisidir?","havunç","pırasa","marul","ıspanak"])
questions.append(["Köylülerin el birliği ile köyün işini birlikte yapmalarına ne ad verilir?","el birliği","imce","merasim","imece"])
questions.append(["İlk evcilleştirilmiş hayvan aşağıdakilerden hangisidir?","kedi","tavşan","koyun","köpek"])
questions.append(["Hangisi vücudumuzdaki kemik türlerinden değildir?","yassı","düz","kıkırdak","sert"])
questions.append(["Bozkırın tezenesi lakaplı rahmetli halk ozanı kimdir?","müslüm gürses","kıvırcık ali","aşık veysel","neşet ertaş"])
questions.append(["En büyük uydusu olan gezegen aşağıdakilerden hangisidir?","dünya","mars","uranüs","jüpiter"])
questions.append(["Türkiye’ de kaç tane coğrafi bölge bulunmaktadır?","8","6","5","7"])
questions.append(["Pirinç hangi ürünün kabuğunun soyulması ile elde edilir?","çitlek","yulaf","arpa","çeltik"])
questions.append(["Milli mücadele döneminde işgallere karşı direnen düzensiz birliklerin adı nedir?","kuvay-i milliye","halk ordusu","düzensiz halk ordusu","tekalif-i milliye",])
questions.append(["Çinlilerin Hun, Tunguz ve Moğol akımlarını durdurmak için inşa ettiği yapı hangisidir?","çin duvarı","çin kalesi","çin hendeği","çin seddi"])
questions.append(["Ses en hızlı hangi ortamda yayılır?","gaz","sıvı","plazma","katı"])
questions.append(["Yön bulmak için aşağıdakilerden hangisi kullanılır?","bulut","toprak","ay","kutup yıldızı"])
questions.append(["Uçaklarda pilot kabinine ne ad verilir?","pitkok","kabin","kobin","kokpit"])
questions.append(["Depremin büyüklüğünü ve süresini ölçen alete ne ad verilir ?","tomograf","jeograf","simograf","sismograf"])
questions.append(["Aşağıdaki balık türlerinden hangisi memelidir?","hamsi","köpek balığı","yunus","balina"])
questions.append(["Gülü ile meşhur olan ilimiz hangisidir?","tekirdağ","konya","edirne","ısparta"])
questions.append(["Osmanlı Devletinin kurucusu olan Osmanlı ailesi hangi Türk boyuna mensuptur?","bozöyük","bozok","uygurlar","kayı"])
questions.append(["Tiger Woods hangi sporun en önemli temsilcisidir? ","hendbol","basketbol","futbol","golf"])
questions.append(["FIFA’ya göre futbolun doğduğu ülke hangisidir?","Türkiye","brezilya","ingiltere","çin"])
questions.append(["Demir Adam filminin yapımcısına göre, Demir Adam karakterinin yaratılması için kimden ilham alınmıştır?","bill gates","steve jobs","nikola tesla","elon musk"])
questions.append(["NBA tarihinin en skorer oyuncusu kimdir?","ceddi osman","michael jordan","wilt chamberlian","kerim abdül cabbar"])
questions.append(["Yerleşim yerleri içinde otomobiller için hız limiti saatte kaç kilometredir?","40","60","70","50"])
questions.append(["Hollywood tabelası 1923 yılında hangi sektörün tanıtımı için dikilmiştir?","turizm","sinema","sağlık","emlak"])
questions.append(["Bovling oyununda bir oyuncunun alabileceği en yüksek puan kaçtır?","200","250","350","300"])
questions.append(["Evrende görebildiğimiz en uzak gök cisimleri hangileridir?","nova","süpernova","nötron yıldızı","kuasar"])
questions.append(["Atatürk'ün okulda alıştığını söylediği ve çok sevdiği yemek hangisidir?","köfte ve pilav","makarna ve dolma","patates ve köfte","kurufasulye ve pilav"])
questions.append(["Bir zarın kaç köşesi vardır?","4","6","9","8"])
questions.append(["Olimpiyat bayrağı üzerinde bulunan iç içe geçmiş 5 renkli halka hangilerini temsil eder?","Olimpiyatları","madalyaları","spor dallarını","kıtaları"])
questions.append(["Bir ay içerisinde meydana gelen ikinci dolunaya ne ad verilir?","sarı ay","yeşil ay","kızıl ay","mavi ay"])
questions.append(["Otomobillerde hava yastıklarının şişmesi için kullanılan gaz hangisidir?","hidrojen","oksijen","metan","nitrojen"])
questions.append(["Mesir macunuyla iyileştiği söylenen Ayşe Hafsa Sultan hangi padişahın eşidir?","II.mehmet","kanuni sultan süleyman","II.mahmud","yavuz sultan selim"])
questions.append(["Eurovision Şarkı Yarışması'nda ülkemizi temsil eden ilk sanatçı kimdir?","hande yener","ajda pekkan","çetin alp","semiha yankı"])
questions.append(["Dilimize Arapçadan geçen 'tuhaf' kelimesinin anlamı hangisidir?","hayaller","şekiller","renkler","hediyeler"])
questions.append(["Göksel Kürelerin Devinimleri Üzerine kitabında Güneş merkezli evren teorisini anlatan bilim insanı kimdir?","gelileo","aristo","batlamyus","kopernik"])
questions.append(["Yere düştüğünde darbelerden korunması için genellikle hangisi kılıf takılarak kullanılır?","kalem","televizyon","mikro dalga","cep telefonu"])
questions.append(["Ankara ne zaman başkent olmuştur?","1933","1919","1930","1923"])
questions.append([" Kullandığımız kağıt banknotların üstünde hangi cümle yazmaktadır?","14 Ocak 1950 tarih ve 1211 sayılı kanuna göre çıkarılmıştır.","14 Ocak 1933 tarih ve 1211 sayılı kanuna göre çıkarılmıştır.","14 Ocak 1953 tarih ve 1211 sayılı kanuna göre çıkarılmıştır.","14 Ocak 1970 tarih ve 1211 sayılı kanuna göre çıkarılmıştır."])
questions.append(["Sergen Yalçın hangi futbol takımında forma giymiştir?","etilerspor","gaziantepspor","beşiktaş","etimesgut şekerspor"])
questions.append([" Avrupa Birliğinin en fazla önemsediği, her alanda geleceğin teknolojisi olarak adlandırılan bilim dalının adı nedir?","nükleer enerji","güneş enerjisi","astronomi","nanoteknoloji"])
questions.append(["Kuzey Atlantik Paktı’nın kısa yazılışı nedir?","WHO","UNİCEF","UNESCO","NATO"])
questions.append(["İlk atom bombası hangi şehre atılmıştır?","Shanghai","Hong Kong","Tokyo","Hiroşima"])
questions.append(["Türk Medeni Kanunu hangi ülkenin medeni kanunundan esinlenerek hazırlanmıştır?","Almanya","Danimarka","Hollanda","İsviçre"])
questions.append(["Bulgaristan’ın başkenti neresidir?","Tahran","Atina","Erivan","Sofya"])
questions.append(["Yeni Türk Lira’sındaki “Yeni” sözcüğü hangi tarihte atılmıştır?","01.01.2006","01,01.2007","12,12.2008","01.01.2009"])
questions.append(["Dünyanın en fazla 1000 yıllık bir ömrü kaldığı teorisinin öne süren Kıyamet teorisi kime aittir?","Jhon Forbes Nash","Jhon maynard Keynes","Elon Musk","Stephen Hawking"])
questions.append(["Hz. Muhammed ve Sahabelerinin Mekke'den Medine'ye göç ettikleri 'Hicret' olayı hangi tarihte gerçekleşmiştir?","5 Temmuz - 3 Ağustos(620)","18 Mayıs - 1 Ağustos(621)","12 mayıs - 20 Temmuz(623)","17 Haziran - 2 Temmuz(622)"])
questions.append(["İtalya'da bulunan her 100 yılda bir yere 7 cm yaklaşan Pisa Kulesi hangi yöne doğru eğilmektedir?","Batı","Kuzey","Doğu","Güney"])
questions.append(["Resimlerimizin vazgeçilmezi 7 renkten oluşan gökkuşağının tam ortasındaki renk hangisidir?","lacivert","Sarı","Kırmızı","Yeşil"])
questions.append(["Ünlü fizikçi Albert Einstein hangi yıl Amerikan vatandaşı olmuştur?","1930","1941","1944","1940"])
questions.append(["Mustafa Kemal Atatürk, cumhurbaşkanı olduğunda kaç yaşındaydı?","44","47","45","42"])
questions.append(["Türkiye yüz ölçümü olarak dünyada kaçıncı büyük ülkedir?","11","97","43","37"])
questions.append(["Dünya Güneş'e uzaklığı bakımından kaçıncı gezegendir?","4","5","2","3"])
questions.append(["Berlin duvarı hangi sene yıkılmıştır?","1992","1987","1984","1989"])
questions.append(["Budizmde ulaşılabilecek en üst mertebeye ne ad verilir?","keşiş","Buddha","Buddahiz","Nirvana"])
questions.append(["Yüz ölçümü en küçük ilimiz hangisidir?","Düzce","Bartın","kırıkkale","Yalova"])
questions.append(["Malazgirt Savaşı nerede olmuştur?","Bitlis","Van","istanbul","Muş"])
questions.append(["Sovyetler Birliği’nin son devlet başkanı kimdir","Josef Stalin","Georgi Malenkov","Deli petro","Mihail Gorbaçov"])
questions.append(["Venedik Film Festivali'nde verilen en büyük ödül hangisidir?","Altın ayı","Altın küre","Altın kase","Altın aslan"])
questions.append([" ‘’Espresso’’ tam olarak ne anlama gelmekte?","ince","koyu","sert","hızlı"])
questions.append(["Tarihte ilk kez daimi orduyu kuran uygarlık hangisidir?","Sümerler","Asurlar","Hititler","Akadlar"])
questions.append(["Futbol hangi uygarlık tarafından ortaya çıkarıldı?","mısır","pers","uygurlar","çin"])
questions.append(["Robinson Crusoe'un yazarı kimdir?","Jules Verne","Jack London","Victor Hugo","Daniel Defoe"])
questions.append(["1972’de Apollo 17 uzay aracı mürettebatınca çekilen ve yerküreyi bütün olarak gösteren ünlü fotoğrafın adı nedir?","Mavi Boncuk","Mavi Gezegen","Mavi dünya","Mavi Bilye"])
questions.append(["Aşağıdakilerden Hangisi Dünya Sağlık Örgütünün Kısaltılmış İsmidir?","UHW","UNICEF","HWO","WHO"])
questions.append(["Bugüne kadar gelmiş geçmiş en geniş sınırlara sahip ülke/imparatorluk hangisidir?","SSCB","Moğol İmparatorluğu","Osmanlı İmparatorluğu","Britanya İmparatorluğu"])
questions.append(["Türkiye Cumhuriyeti ne zaman kurulmuştur?","23 Nisan 1920","29 Ekim 1920","23 Nisan 1923","29 Ekim 1923"])
questions.append(["Hz.Muhammed'e kaç yaşındayken peygamberlik görevi gelmiştir?","38","41","42","40"])
questions.append(["Son Osmanlı padişahı Sultan Vahdettin'in mezarı şu an hangi ülkededir?","Suudi Arabistan","Filistin","Kudüs","Suriye"])
questions.append(["İltica kelimesinin anlamı nedir?","Gericilik","Taşınma","Saygı","Sığınma"])
questions.append(["Filolog ne demektir?","fil uzmanı","Antik çağ uzmanı","alfabe bilimci","Dil bilimci"])
questions.append(["Avrupa Birliği'nin başkenti neresidir?","Berlin","Lüksemburg","New york","Brüksel"])
questions.append(["Nutuk'ta Atatürk'ün atıfta bulunduğu tek yabancı eser olan 'The Outline of History' kitabı hangi İngiliz yazara aittir?","E.S. Creasy","E. Adcock","A.J. Toynbee","H.G. Wells"])
questions.append(["Aşağıdaki yazarlar arasından hangisi Nobel Edebiyat Ödülüne layık görülmüştür?","Marcel Proust","Virginia Woolf","Jorge Luis Borges","Ernest Hemingway"])
questions.append(["Dönemin Fransa'sını çok iyi bir şekilde özetleyen Notre Dame'ın Kamburu kitabının yazarı kimdir?","Alexandre Dumas","Honore de Balzac","Emile Zola","Victor Hugo"])
questions.append(["2. Dünya Savaşı'nda propagandanın adeta kitabını yazmış ve hatta Nazi Almanyasında Propaganda Bakanı olmuş Nazi yöneticisi kimdir?","Heinrich Himmler","Hermann Göring","Rudolf Hess","Joseph Goebbels"])
questions.append(["Osmanlı Devletinin Kuzey Afrika'daki hükmünü kaybettiği Uşi Antlaşması hangi İsviçre şehrinde imzalanmıştır?","Bern","Luzern","Zurih","Lozan"])
questions.append(["Oscar Ödülü kazanan ilk siyahi oyuncu kimdir?","Butterfly McQueen","Louise Beavers","Morgan Freeman","Hattie McDaniel"])
questions.append(["Eskiden 'yazıyor efendiler yazıyor' diye bağıran çoçuklar hangisini satarlardı","Kitap","Kalem","Mürekkep","Gazete"])
questions.append(["Halk arasına yoğurt ile birlikte neyin tüketilmesi önerilmez","Hindi","Tavuk","Biftek","Balık"])
questions.append(["Hangisinin üzerine genellikle'beni yıka' yazılır?","Bisiklet","Motosiklet","vapur","Araba"])
questions.append(["'uluslararası banka hesap numarası'anlamda kullanılan kısaltma hangisidir","EFT","SWIFT","APS","IBAN"])
questions.append(["Mojang tarafından geliştirilen ve en çok oynanan sanal oyun hangisidir","Tom","Angela","Pou","Minecraft"])
questions.append(["“Sinekli Bakkal” Romanının Yazarı Aşağıdakilerden Hangisidir?","Reşat Nuri Güntekin","Ziya Gökalp","Ömer Seyfettin","Halide Edip Adıvar"])
questions.append(["Tsunami Felaketinde En Fazla Zarar Gören Güney Asya Ülkesi Aşağıdakilerden Hangisidir?","Srilanka","Tayland","Hindistan","Endonezya"])
questions.append(["Aşağıdaki Ülkelerden Hangisinin Nüfusu Daha Fazladır?","İspanya","Fransa","İngiltere","Almanya"])
questions.append(["Mantı dendiğinde ilk akla gelen ilimiz hangisidir?","Muğla","Hatay","Malatya","Kayseri"])
questions.append(["Ülkemizin kaç ülkeyle sınırı var?","5","6","7","8"])
questions.append(["Horozu ile Meşhur İlimiz Hangisi?","Konya","Bursa","Muğla","Denizli"])
questions.append(["'Sorgulanmamış bir hayat, yaşanmaya değmez.' sözü kime aittir?","Platon","René Descates","Aristo","Sokrates"])
questions.append(["Işık ne kadar hızlıdır?","200.000 kilometre/saniye","150.000 kilometre/saniye","350.000 kilometre/saniye","300.000 kilometre/saniye"])
questions.append(["Simgesi ( Ca ) olan elementin adı nedir?","Çinko","Krom","Demir","Kalsiyum"])
questions.append(["Vücuttaki en güçlü kas hangisidir?","Bacak kası","Karın kası","Kol kası","Dil kası"])
questions.append(["İzafiyet teorisi kime aittir?","Isaac Newton","Nikola Tesla","Thales","Albert Einstein"])
questions.append(["Kahve ilk nerede keşfedildi?","Yemen'de","Türkiye'de","Amerika'da","Etiyopya'da"])
questions.append(["Türkiye'nin ilk internet ağı projesi kaç yılında başlatılmıştır?","1990","1992","1993","1991"])
questions.append(["Tarihte kaç bağımsız Türk devleti vardır?","14","15","17","16"])
questions.append(["Yer çekimi hangi bilim adamı tarafından keşfedilmiştir?","Gergor Mendel","Galileo Galilei","Johannes Kepler","Isaac Newton"])
questions.append(["Çelik elde etmek için demiri ne ile karıştırmak gerekir?","Bakır","Gümüş","Alüminyum","Karbon"])


def clear():

    list = window.grid_slaves()
    for n in list:
        n.destroy()

 
class Quiz:
    def __init__(self,quest):
        clear()

        self.Soruget = []
        for n in quest:
            self.Soruget.append(n)
        self.a1=""
        self.a2=""
        self.a3=""
        self.a4=""
        self.Ra=""
        self.RaBtn = Button(window, text="",font=("Arial",14))
        self.antw1 = Button(window, text="",font=("Arial",14))
        self.antw2 = Button(window, text="",font=("Arial",14))
        self.antw3 = Button(window, text="",font=("Arial",14))
        self.antw4 = Button(window, text="",font=("Arial",14))
        self.lock=False
        self.right=0
        self.sonraki = Button(window,command=self.Soru)
  
        self.nummer=0
        self.Max=15
        self.Soru()

    def Soru(self):
        self.sonraki.grid(column=0,row=5,pady=5)
        if len(self.Soruget) > 0 and self.nummer < self.Max:
            self.nummer += 1
            self.lock = False
            randNum = random.randint(0,len(self.Soruget)-1)
            soruText = self.Soruget[randNum][0]
            self.Ra = self.Soruget[randNum][-1]
            answers = []
            for i in range(1,5):
                answers.append(self.Soruget[randNum][i])
            random.shuffle(answers)
 
            self.a1 = answers[0]
            self.a2 = answers[1]
            self.a3 = answers[2]
            self.a4 = answers[3]
            self.backg=Label(window)
            soru = Text(window, font=("Arial", 14), width=58, height=4)
            soru.configure(bg="cyan")
            soru.insert(END,soruText)
            soru.grid(column=0,row=0,padx=80,pady=(100,50))
            self.Menu = Button(window,bg="Powder blue",command=menuCreator)
   
            self.antw1 = Button(window, text="A) "+self.a1, font=("Arial",14),width=39,height=1, command = self.control1)
            self.antw2 = Button(window, text="B) "+self.a2, font=("Arial",14),width=39,height=1, command = self.control2)
            self.antw3 = Button(window, text="C) "+self.a3, font=("Arial",14),width=39,height=1, command = self.control3)
            self.antw4 = Button(window, text="D) "+self.a4, font=("Arial",14),width=39,height=1, command = self.control4)
            self.antw1.configure(bg="yellowgreen")
            self.antw2.configure(bg="yellowgreen") 
            self.antw3.configure(bg="yellowgreen")
            self.antw4.configure(bg="yellowgreen")
            self.Menu.configure(image=home)
            self.sonraki.configure(image=nextb,bg="Powder blue")
     
            self.Menu.grid(column=0,row=0,pady=(8,200),padx=(700,1)) 
            self.antw1.grid(column=0,row=1,pady=(8,5))
            self.antw2.grid(column=0,row=2,pady=5)
            self.antw3.grid(column=0,row=3,pady=5)
            self.antw4.grid(column=0,row=4,pady=5)
 
            if self.a1 == self.Ra:
                self.RaBtn = self.antw1
            elif self.a2 == self.Ra:
                self.RaBtn = self.antw2
            elif self.a3 == self.Ra:
                self.RaBtn = self.antw3
            elif self.a4 == self.Ra:
                self.RaBtn = self.antw4
            self.Soruget.pop(randNum)
        else:
            clear()
            lb = Label(window, text="Toplam " + str(self.Max) + " tane sorudan " + str(self.right) + " tane doğru cevapladınız ",font=("Arial",14),width=40,height=3)
            lb.grid(column=0,row=0,padx=180,pady=(150,20))
            lb1=Label(window,text="TEBRİKLER",font=("Arial",14))
            lb1.configure(bg="green")
            lb.configure(bg="green")
            lb1.grid(column=0,row=0,padx=100,pady=(60,50))
            lb2=Label(window,text="""
    0 p = salaksın ki
  1-2 p = cahil
  3-4 p = kültürsüz      
  5-6 p = yetersiz
  7-8 p = eh işte
 9-10 p = fena değil 
11-12 p = yeterli
13-14 p = iyi
   15 p = muhteşemm
                
                """,font=("Arial",14))
            

            if self.right == 1 :
                sonuc=Label(window,text="cahil",font=("Arial",20,"bold"),bg="red",width=20,height=2)
            elif self.right == 2 :
                sonuc=Label(window,text="cahil",font=("Arial",20,"bold"),bg="red",width=20,height=2)
            elif self.right == 3 :
                sonuc=Label(window,text="kültürsüz",font=("Arial",20,"bold"),bg="red",width=20,height=2)
            elif self.right == 4 :
                sonuc=Label(window,text="kültürsüz",font=("Arial",20,"bold"),bg="red",width=20,height=2)
            elif self.right == 5 :
                sonuc=Label(window,text="yetersiz",font=("Arial",20,"bold"),bg="red",width=20,height=2)
            elif self.right == 6 :
                sonuc=Label(window,text="yetersiz",font=("Arial",20,"bold"),bg="red",width=20,height=2)
            elif self.right == 7 :
                sonuc=Label(window,text="eh işte",font=("Arial",20,"bold"),bg="grey",width=20,height=2)
            elif self.right == 8 :
                sonuc=Label(window,text="eh işte",font=("Arial",20,"bold"),bg="grey",width=20,height=2)
            elif self.right == 9 :
                sonuc=Label(window,text="fena değil",font=("Arial",20,"bold"),bg="yellow",width=20,height=2)
            elif self.right == 10 :
                sonuc=Label(window,text="fena değil",font=("Arial",20,"bold"),bg="yellow",width=20,height=2)
            elif self.right == 11 :
                sonuc=Label(window,text="yeterli",font=("Arial",20,"bold"),bg="orange",width=20,height=2)
            elif self.right == 12 :
                sonuc=Label(window,text="yeterli",font=("Arial",20,"bold"),bg="orange",width=20,height=2)
            elif self.right == 13 :
                sonuc=Label(window,text="iyi",font=("Arial",20,"bold"),bg="light green",width=20,height=2)
            elif self.right == 14 :
                sonuc=Label(window,text="iyi",font=("Arial",20,"bold"),bg="light green",width=20,height=2)
            elif self.right == 15 :
                sonuc=Label(window,text="MÜKEMMELL",font=("Arial",20,"bold"),bg="green",width=20,height=2)
            else:
                sonuc=Label(window,text="salaksın ki",font=("Arial",20,"bold"),bg="red",width=20,height=2)
                                                                    



            sonuc.grid(column=0,row=0,padx=100,pady=(10,120))    



            lb2.grid(column=0,row=1)
            lb2.configure(bg="cyan")
            zumMenu = Button(window, command=menuCreator)
            zumMenu.grid(column=0,row=2)
            zumMenu.configure(image=home32,bg="Powder blue")
 
    def control1(self):
        if self.lock == False:
            if self.Ra != self.a1:
                self.antw1.configure(bg="red")
            else:
                self.antw1.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True
 
    def control2(self):
        if self.lock == False:
            if self.Ra != self.a2:
                self.antw2.configure(bg="red")
            else:
                self.antw2.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True
 
    def control3(self):
        if self.lock == False:
            if self.Ra != self.a3:
                self.antw3.configure(bg="red")
            else:
                self.antw3.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True
 
    def control4(self):
        if self.lock == False:
            if self.Ra != self.a4:
                self.antw4.configure(bg="red")
            else:
                self.antw4.configure(bg="green")
                self.right += 1
            self.RaBtn.configure(bg="green")
            self.lock = True

class Menu:

    def __init__(self):
        clear()
        self.setting=Button(window,command=sett)
        self.baslık=Label(window,text=" Genel kültür test",font=("Arial",40,"italic","bold"),fg="deepskyblue",width=15,height=2,bg="Powder Blue")
        self.Quiz = Button(window,bg="Powder blue",command=quizCreator)
        self.hakkinda=Button(window,command=hakkindas)
        self.cik=Button(window,command=exit)
        self.Quiz.configure(image=mi,compound=RIGHT)
        self.setting.configure(image=settings,bg="Powder blue")
        self.hakkinda.configure(image=question,bg="Powder blue")
        self.cik.configure(image=exitb,bg="Powder blue")
        self.setting.grid(column=0,row=0,padx=(1,700),pady=8)
        self.hakkinda.grid(column=0,row=0,padx=(700,1),pady=8)
        self.baslık.grid(column=0,row=0)
        self.Quiz.grid(column=0,row=2,padx=280,pady=35)
        
        self.cik.grid(column=0,row=3)
class sett:
    def __init__(self):
        clear()
        self.kapa=Button(window,command=musickapa)
        self.ac=Button(window,command=musicac)
        self.lang=Label(window,bg="Powder blue")
        self.langb=Button(window,command=langs)
        self.langb2=Button(window,command=labgbs)
        self.menu=Button(window,text="Menu",font=("Arial",18),command=menuCreator,bg="Powder blue")
        self.lang.configure(image=language)
        self.langb2.configure(image=bayrak2,bg="Powder blue")
        self.langb.configure(image=bayrak,bg="Powder blue")
        self.kapa.configure(image=pauseb,bg="Powder blue")
        self.ac.configure(image=play,bg="Powder blue")
        
        self.musicl=Label(window)
        self.musicl.configure(image=musici,bg="Powder blue")
        self.musicl.grid(column=0,row=0,padx=(200),pady=(80,40))
        self.kapa.grid(column=1,row=0,padx=(20))
        self.ac.grid(column=2,row=0)
        self.lang.grid(column=0,row=1)
        self.langb.grid(column=1,row=1,padx=(40))
        self.langb2.grid(column=2,row=1)
        self.menu.grid(column=2,row=2,pady=(200))
        
        
        
class hakinda:
    def __init__(self):
        clear()
        self.bilgi=Label(window,text="""
Not: Beta aşamasındadır !
Bu oyun python kullanılarak Tkinter kütüphanesinden yapılmıştır

   Basit bir Quiz oyunudur
   genel kültürünüzü test etmenize yardımcı olur
   iyi eğlenceler    

   hazırlayan: Kıvanç çoban
   İletişim: kivancccc48@gmail.com 
            
            """,font=("times new roman",14,"bold"),bg="cadetblue",width=50,height=20)
        self.bilgi.grid(column=0,row=0,padx=120,pady=30)
        self.zumMenu = Button(window, text="Menu",font=("Arial",14),command=menuCreator)
        self.zumMenu.configure(image=home32)
        self.zumMenu.grid(column=0,row=1)
 
def menuCreator():

    m = Menu()
 
def quizCreator():
    q = Quiz(questions)
def hakkindas():
    h = hakinda()
def musickapa():
    mixer.music.pause()
def musicac():
    mixer.music.unpause()
def labgbs():
    yazil=Label(window,text="Seçtiğiniz dil desteği mevcut değil",font=("Arial",18),height=1,width=28,bg="Powder blue")
    yazil.grid(column=0,row=2)
def langs():
    yazil=Label(window,text="Seçtiğiniz dil desteği mevcut ",font=("Arial",18),height=1,width=28,bg="Powder blue")
    yazil.grid(column=0,row=2)

menuCreator()

window.mainloop()
