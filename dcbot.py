import pyrogram
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPrivileges
import time
import configparser
from pyrogram.enums import ChatType

config = configparser.ConfigParser()
config.read('config.ini')
groupdb = set()
userdb = set()
api_id = config.get('default', 'api_id')
api_hash = config.get('default', 'api_hash')
bot_token = config.get('default', 'bot_token')
app = Client("dcbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

question = [
    "Sevgilin varmı?",
    "Dürüst ol, eyni anda neçə nəfərlə flörtləşmisən?",
    "Ən sevdiyin yemək nədir?",
    "Ən sevdiyin film hansıdır?",
    "Qrupda sevdiyin və ya xoşuna gələn biri var?",
    "Sevgi sənin üçün nədir? xarici görünüş ya daxili?",
    "İnternetdən tanıdığın biri ilə sevgili olardınmı?",
    "Sanal sevgiyə inanırsan?",
    "neçə sevgilin olub?",
    "Heç xəyanət etmisən? və ya xəyanətə uğramısan?",
    "Ən böyük xəyalın nədir?",
    "Sevgilinin, qarşı cinsdən dostu olmasına razı olarsan?",
    "Sevgilinin geyiminə qarışarsan?",
    "Söyüş və ya argo işlədən qızlara münasibətin necədir?",
    "qaqa və ya cool tiplər haqda nə düşünürsən?",
    "səncədə, söyüş üstdə birini öldürüb ilərlə həbs yatmaq düzdürmü?",
    "Ən sevdiyin ölkə hansıdır və niyə?",
    "bir səhər, qarşı cins olaraq oyansan ilk nə edərdin?",
    "Sevgilinin maddi sıxıntıları olarsa, ona dəsdək olarsan?",
    "sevib açılmadığın olub?",
    "elə biri olub ki, hələdə onu unuda bilmirsən?",
    "Sevdiyinlə evlənməyə ailən razı olmasa, ailənə qarşı çıxarsan?",
    "səncə müasirləşmək insanların istədiyi şeyləri etməsidirmi?",
    "şortik geyinənə necə baxırsan? :D",
    "Dini inancın nədir?",
    "Başqalarını inancına görə yarğılayar və ya fərqli münasibət göstərərsən?",
    "Düzünü de,  4000 dini araşdırıb ən doğru dinin sənin ki, olduğuna inanaraq seçmisən?",
    "Başqalarına yox deməkdə çətinlik çəkirsən?",
    "İndiyə qədər ən böyük peşmanlığın nə olub?",
    "Elə bir sirrin varmı ki, onu heç kim bilmir.",
    "Qrupda ən son danışdığın yalan nə olub?",
    "Qrupdan biri ilə görüşmək şansın olsa kim olardı?",
    "Dünyada sadəcə bu grupdakılar sağ qalsaydı, və evlənməyə məcbur olsaydın qrupdan kimlə evlənərdin?",
    "Sevmədiyin millət varmı? hansıdır?",
    "İnsanların hansı hərəkətləri sənə mənasız gəlir?",
    "Sırf ilgi almaq üçün sevmədiyin birini ümidləndirmisənmi?",
    "Ən yaxın dostun kimdir? və ona ölümünə güvənərsənmi?",
    "İnsanın son gününə qərər çabalayıb-çırpınması və sonda etdiyi hər şeyin puç olaraq ölməsi qəribə deyilmi?",
    "bir cinayətə şahid olsanız ama cinayəti törədən şəxs dostunuz olsa onu qoruyarsızmı?",
    "Dostunun haqsız olduğunu bildiyin halda tərəfini tutarsanmı?",
    "Son dəfə sevgilin nə vaxt olub?",
    "Yemək bişirə bilirsən?",
    "Sevgilin, sənin uğrunda ölərsə, bir müddət sonra başqalarını sevrəsənmi?",
    "Həyat yoldaşın sənə xəyanıt etsə, onu öldürərsənmi?",
    "Atanın, anana xəyanət etdiyini öyrənsən bunu anana deyərsən ya gizli saxlayarsan?",
    "Ən böyük travman nədir?",
    "hər-hansı idmanla məşğul olursan?",
    "ölməkdən qorxursan?",
    "Ölümcül xəstəliyə tutulmusan və evdəkilər bunu səndən gizlədir. Onlara öyrəndiyini deyərdin ya ölənə qədər gizli saxlayardın?",
    "Ən uzun dostluğun nə qədər davam edib? və niyə bitib? yenidən barışarsanmı?",
    "Sevgilindən ayrılma səbəbin nə olub?",
    "Neçə nəfəri sevmisən?",
    "Ailələriniz icazə verməsə, sevdiyinlə qaçarsanmı?",
    "Sənəcə siqaret çəkənlər cool olur ya iyrənc?",
    "Son 3 gününün qaldığını bilsən nə edərdin?",
    "Bir xəyanətə şahid olsan, digər tərəfə xəbər edərsənmi?",
    "Sevdiyinizi ən yaxın dostunuzda sevsə, sevginizdən ən çəkərsiz ya, dostunuzla yolları ayırarsız? ",
    "Səncə dost ya sevgili?",
    "İdeal evlilik yaşı neçədir?",
    "Qohumlarını sevirsənmi?",
    "Ən son etdiyin qanunsuz şey nə olub?",
    "Bir toplumda haqqını tələb edə bilirsənmi?",
    "Bürclərə inanırsan? və niyə?",
    "ilk maaşın nə qədər olub?",
    "lazımsız yerlərə pul xərcləyirsən?",
    "Aylıq nə qədər pul xərcləyirsən?",
    "hələdə kaş elə olmazdı dediyin birşey varmı? varsa o nədi?",
    "Sənə görə maşınlar, bir yerdən başqa yerə getmək üçündürmü? ya bir tutqudurmu?",
    "maşın yoxsa motosikl sevirsən? və niyə?",
    "Aldığın ən dəyərli hədiyyə nə olub?",
    "Ad günün nə vaxtdır?",
    "Səncə pul hərşeydirmi?",
    "Pul olmadan da sevgi olurmu? və niyə?",
    "Biri ilə puluna görə birlikdə olarsanmı?",
    "Adını sevirsənmi? adının nə olmasını istərdin?",
    "Xaricdə oxumaq istərdinmi və niyə?",
    "Birni sevdiyinə görə peşman olmusanmı?",
    "Dostunun danışdığı qıza/oğlana yürüyərsən?",
    "Səncə ilk addımı hansı tərəf atmalıdır?",
    "Avtobus/metroda baxışıb danışa bilməyəcək qədər çəkindiyiniz vəziyyətlər olub?",
    "Səncə savadlı olmağın ali təhsillə əlaqəsi varmı?",
    "Heçnə bilməyən ama hər mövzuda bir fikri olan insanlar haqda nə düşünürsən?",
    "Görünməz olsan ilk hara gedərdin?",
    "Bir qız/oğlana yürümək üçün taktika verin:",
    "Prezident olmaq istərdin? niyə?",
    "Dünya düzdür ya kürə? ",
    "Qarşı tərəfdə diqqətini çəkən ilk şey nədir?",
    "Neçə uşağının olmağını istərdin?",
    "Qız ya oğlan övlad istərdin? niyə?",
    "Həyat yoldaşının uşağı olmasa, ondan ayrılarsanmı?",
    "Səncə, kişilərin yükü ağırdır ya xanımların?",
    "mentalitetə bağlısan?",
    "Qrupdakıların hamısı bir evdə yansa, ilk kimi çıxardardın?",
    "limitsiz yemək, içki verirlər. 3 ay boyunca ada da villada qalacan, grupdan 3 nəfəri özünlə apara bilərsən. Onlar kimdir? ",
    "Şaxta babaya inanırsan?",
    "Cinayət işləsən və heç kim bilməsə, yenədə polisə təslim olarsan?",
    "Qorxu filminə gedirsən, qrupdan 2 nəfəri özünlə aparacan kimdir onlar?",
    "Qrupun ən əyləncəlisi kimdir?",
    "Qrupda heç sevmədiyin biri varmı?",
    "Qrupun ən ərgəni kimdir?",
    "Sevdiyin qız/oğlanın yaşadığı şəhər?",
    "Məsafələr sevgiyə əngəldirmi?",
    "Bu gün etdiyin bir yaxşılığı de",
    "İntiqam almağı sevirsən?",
    "Sevdiyin bir dizi varmı?",
    "Ən sevdiyin kitab?",
    "Hansı vərdişini tərgitmək istərdin?",
    "Sevgilinin ürək çatışmazlığı olsa, öz ürəyini verərsən?",
    "Səncə evlənmək üçün toy şərtdir?",
    "1 milyonun olsa ilk nə alardın?",
    "Xəyallarını gerçəkləşdirməyinə nə əngəl olur?",
    "Sevdyin şəxsin adını :D yada baş hərfini yaz.",
    "Qrupdan, kaş yanımda olsa desidiyiniz biri varmı?",
    "özgüvənsizsən?",
    "son dəfə nəyə və niyə ağlamısan?",
    "Ailənə yük olduğunu düşünürsən?",
    "Evladlıq olduğunu bilsən yenədə ailəni sevərdin?",
    "Gərçək ailənin milyarder olduöunu, ama səni atdıqlarını və kasıb bir ailənin səni baxıb böyütdüyün öyrənsən. Gərçək ailəni seçərsən ya səni böyüdən?",
    "Problemlərinin öhdəsindən necə gəlirsən?",
    "maşın sürə bilirsən?",
    "maşınla gedirsiz və sürücü sizsiz anidən qarşınıza balaca uşaq qaçır. Saxlaya bilmeyəcək qədər sürətlisiz. Ancaq rolu çevirsəz maşın aşacaq və maşında ailəniz var. Nə edərdiz?",
    "Oğruluq sərbəst olsa yenədə edərdinizmi?",
    "Bu qrupda, sevdiyin yada xoşuna gələn biri varmı?",
    "Qarşı tərəfin hansı hərəkəti sizi soyudar?",
    "İnsanları xarici gönüşünə görə yarqılayırsızmı?",
    "lgbt dəstəkləyirsən? və niyə",
    "Özünün ölməyini istərdin ya tanımadığın, başqa 1000 nəfərin?",
    "Bu gün nə qədər pul xərcləmisən?",
    "Səncə niyə sevgilin yoxdur?",
    "Qızların dostluğu əbədi olur ya oğlanların?",
    "Ən son nə vaxt aşiq oldumusan?",
    "Ən böyük arzun nədir?",
    "Sənin ən xoşuna gələn xüsusiyyətin nədir və onu niyə sevirsən?",
    "Neçə yaşda evlənməyi düşünürsən?",
    "Uşaqlarının sevgilisi olmağına icazə verərsənmi?",
    "Uşağın lgbt üzvü olduğunu sənə desə reaksiyan necə olar?",
    "Səncə, ailə qurmaq daha önəmlidir ya kariyera?",
    "Hansı rəngdə geyinməyi sevirsən?",
    "Son yediyin yemək nə idi?",
    "Ən sevdiyin yemək hansıdır?",
    "Xəyalındakı iş nədir?"
    "Gözəl/yaraşıqlı olduğunu düşünürsənmi?",
    "Hansı tezliklə, insanlardan xarici görünüşünə görə tərif alırsan?",
    "İndiyə qədər aldığın ən dəyərli hədiyyə nə olub?",
    "Ad günlərini sevirsənmi?",
    "Sənə görə, indiyə qədər əldə etdiyin ən böyük uğurun nə olub?",
    "Bizə hədəflərindən danış",
    "Getmək istədiyin ölkə hansıdır? Bə niyə ora?"
    "Sevgilinin geyiminə qarışarsanmı?",
    "Dar və qısa geyimləri xoşlayırsan?",
    "Gündəlik həyatda necə geyim tərzin var",
    "Bizə geyim tərzinin şəklini at",
    "Ayaq nömrən neçədir?",
    "Mentalitet olmasa nə edərdiz?",
    "Sənlə eyni dini inancı bölüşməyən biri ilə dostluq edərsənmi?"
    "1 milyon manat ya hər gün 200 manat pul?",
    "etdikdən sonra peşman olduğun ama yenədə etdiyin bir şey varmı?",
    "Bir ölkə yaratmaq imkanın olsaydı adını nə qoyardın?",
    "Uşağının adını nə qoyacaqsan?",
    "Sevmədiyin insanlarla eyni ortamda olduqda nə edirsən?",
    "Ünlü olmaq istərdinmi və niyə?",
    "elə bir şey olubmu ki, onu edəndə tutulmusan ve çox utanmısan?
]

task = [
    "İnstagram dm qismini ss at",
    "telegram sohbətlər hissəsini ss at",
    "whatsapp son yazışmanı ss at",
    "telegram son yazışmanı ss at",
    "instagram son yazışmanı ss at",
    "Hər hansı bir şey deyərək səs at",
    "Google axtarış keçmişini ss at",
    "Youtube keçmişini ss at",
    "instagram istifadəçi adını de",
    "Telefon nömrənin son 4 rəqəmini de",
    "whatsapp və ya instagram storyni ss at",
    "zəng vurulanlar hissəsini ss at (normal zəng)",
    "Whatsapp zəng hissəsini ss at",
    "Qrupdan birinə sevgi etirafı et",
    "Üyeler qismindən, yuxarıdan 3 cü adama sevgi etrafı et",
    "Şəklini at, üzünü qaralaya və ya gizləyə bilırsən.",
    "galerindəki sondan 7 ci şəkli at",
    "galeriyanı ss at",
    "Normal sms'ləri ss at",
    "Müəlliminə, dərsə/məşqə gələ bilməyəcəyini yaz",
    "Səndən əvvəlki adama, 3 tur boyunca sevgilim deyə xitab et.",
    "Bir dərs qrupuna gir və beynimi satıram, mənə lazım deyil yaz. ss at",
    "Ən son whatsapdan danışdığın şəxsə zəng vurub söndür və üzürlü say əlim dəydi yaz",
    "Sevdiyin bir şəklini bizimlə bölüş",
    "Telefonun Ana ekranını ss at",
    "Telefonun kilid ekranını ss at",
    "uuuuuu deyə səs at",
    "sağ tərəfindəki əşyanın şəklini çək at",
    "@ bas 7 ci çıxana sevgi etırafı et",
    "@ bas 3 cü çıxana instagramını at",
    "bloka atdığın adamlardan birni, çıxar və bir şans verirəm yaz.",
    "Mən badımcanam, gəlin yeyin məni, yaz stiker et və ifsala!",
    "Əlinə Olivia yaz çək at",
    "Göydə milyonlarla ulduz var ama mənim ulduzum sənsən yazıb, qrupdan əks cinsə at.",
    "Qrupdan bəyəndiyin birnin baş hərfini yaz",
    "Qrupda tanımadığın birinə, dünyada qalan son insan olsan yenə sənlə evlənmərəm yaz ss at.",
    "Qrupun ən gözəl/yaraşıqlı üzvünə iltifat et",
    "Qrupun ən yarşıqlı 3 oğlanını etiketlə ",
    "Qrupun ən gözəl 3 qızını etiketlə",
    "Qrupda xasiyətini sevdiyin birini tag et",
    "Qrupdan istədiyin birinə səni sevirəm deyə səs at",
    "Anlıq şəkil at. (üzünü qaralaya bilərsən)",
    "Uşaqlıq şəklini at",
    "Telegram söhbətlərində ki, 3 cü şəxsə ondan nifrət etsiyi yaz",
    "Cəsarətin varsa telefon nömrəni yaz. Yoxdursa ilk 3 rəqəmini :D",
    "Tik-tok hesabını bizimlə paylaş",
    "Tik-tok da like etdiklərinə gir ss at",
    "Mən malam deyə səs at",
    "Bilmədiyimiz bir şey etiraf et",
    "Son zəngindən bir şəkil paylaş",
    "Qrupda ölümünə güvəndiyin biri varmı? varsa kimdi?",
    "Ən son aldığınız mesajı səsli oxuyub atın",
    "Telefonunuzdakı son fotonu atın və nə olduğunu açıqlayın",
    "Telefonunuzda yükləyib işlətmədiyiniz proqramın şəklini atın",
    "Profil fotonuza, Şakiranın şəklini qoyun",
    "Bio'nuza, gedirdi messi  əlində pepsi. messi yıxlıdı pepsi dağılıdı ağlama messi alaram pepsi yaz oyun bitənə qədər dursun",
    "Səndən əvvəlki oyunçunun adını, sevgilim deyə qeyd et.",
    "Bir sevgi etirafı et",
    "Başına ütü qoy çək at. (üzünü qaralasanda olar)",
    "Qrupdan birnin nömrəsini alın və wp dan mesaj yazıb ss atın",
    "wp da dostuna men hamileyem yaz cavabını ss at",
    "Bio -na afrikada vəziyyət zordu yaz. 1 saatlıq",
    "Wp-statusunda hamınız malsız blokladım yaz. 3 dq sonra baxanlarla birlikdə ss al at və sil.",
    "Bio-na qrupdan birini tağ edib səni çoox sevirəm yaz.",
    "Qrupdam 3 adama 'Hamiləyəm' mesajını göndər",
    "Normal olan ancaq, olduğunda utandığın şey nədir?",
    "Ləhcəylə danışıb səs at.",
    "Ən yaxın dostuna yaz ki,  'sən nə iki üzlü insan imişsən, ayıb olsun abırsız' ss et at",
    "Əlinə, badımcan yaz çək qrupa at.",
    "Cip-cip cücələrim oxu qrupa at",
    "İnternetdə son axtardığın şeyi screen edərək bura at",
    "Wp-dan birinə lazım deyildi onsuz 😒 yaz. Cavabını ss al at",
    "Dərs oxuduğun masanın şəklini çək at.",
    "Qrupdan birinə: salam xaaam  komentimi bəyənmişdiz. Yaz cavabını ss at",
    "Profilinə, 5 dəqiqəlik, eşşək şəkli qoy.",
    "Instagramda ən son save etdiyin paylaşımı at.",
    "Dostuna/rəfiqənə 'Mən pis yola düşmüşəm' yaz ss elə at",
    "Həmcinsinə səni sevirəm yaz",
    "Telegram profil şəklinə Hitlerin şəklin qoy !",
    "Kontaktından rast gələ birinə hansısa bir heyvan olmaq istədiyini yaz !",
    "Qrupdan birinə şəklini at və ss et",
    "Telegram profil şəklinə Stalinin şəklin qoy",
    "🎀 ŞANSLI MESAJ 🎊 Qrupdan bir nefərin Google/Youtube/Instagram Axtarış Tarixçəsini tələb edin",
    "bir qız dostuna səndəki bığ dayımda yoxdu. yaz cavabını ss at",
    "Qarşı cinsdən birinə yazıb özünüzü tərifləyin",
    "ayrıldığın sevgilinə, yenidən barışmaq istədiyini yaz",
    "@ bas çıxan 4 cü adama, əgər oğlandısa, təbriklər ata olursan, qızdırsa, təbriklər ana olursan yaz ss at ",
    "Mən dəliyəm, 5 dəfə təkrar edərək səs at",
    "Qrupdn birinə, {flankes} mənimlə evlənərsən? deyə səs at",
    "Hər-hanaı qrupdan bir qıza yazın və bu qrupa qatılmasını istəyin",
    "Səndən əvvəlki oyunçunun adını əlinə, ürək çəkib içinə yaz və şəklini at",
    "Qrupda bəyəndiyin biri varmı? varsa kimdir?",
    "Məcbur olaan qrupdan kimlə evlənərdin. Qarşı cins olması mütləqdir!",
    "Instagramını paylaş cəsarətin varsa",
    "whatsapp statusuna, bir gün gələr ama o gün gəlməz yaz paylaş. 3 dəqiqə sonra, baxanlarla birlikdə ss at",
    "Instada çox səmimi olmadığın birinin storysnə alov at",
    "Atana mən pişiyəm yaz cavabını ss at",
    "YouTube dan  barbi mahnısını aç  və ss edib storydə paylaş.",
    "İnstada takib etdiklərindən, 7 ci adama, kaş yanında ola bilsəm yaz ss at",
    "Grupdan sevdiyin birni tag et",
    "tanımadığın birinə gözlərin çox qəşəydi yaz ss at",
    "Gülməli olmayan bir zarafat et səsli",
    "Wp statusuna, bir gün məni tanığınıza şükr edəcəksiz yaz paylsş",
    "bir söhbət qrupuna girib, lgbt-yə azadlıq. Yaz ss at",
    "Qarşı cinsdən dostuna, onu bir aydır sevdiyini de və cavabını ss at",
    "Adminlərdən birinə iltifat et",
    "Özündən əvvəlki oyunçunun nömrəsini al və wp dan mesaj yaz",
    "Get kontakt taglarını ss edib bura at",
    "Dostuna, deyəsən hamiləyəm, tez-tez ürəyim bulanır, çox şey yeyə bilmirəm ciddən nə edəcəm bilmirəm. yaz cavabını ss at",
    "instada storynə, 2+2=? Yaz paylaş",
    "aldığın son səsli mesaji bura yönləndir",
    "telegramdakı, sonuncu yazismanı ss at",
    "Wp biona 🏳️‍🌈 bayrağı qoy",
    "instada, dm de 2 ci adama, az reels atda eh bezdim yaz",
    "instagram keşfetini ss at",
    "Ən sevdiyin mahnını at",
    "Telefon şifrəni bizimlə bölüş",
    "Cəsarətin varsa, grupa boydan  şəklini at",
    "Beyaz atlı prensinin adı nədir?",
]



@app.on_message(filters.command("start"))
def start_command(client, message):
    user = message.from_user
    caption = f"**Salam, {user.mention}!!\n\nMən, Telegramın ən yaxşı Doğruluq və Cəsarət oyun botuyam 🦣**"
    
    keyboard = [
        [InlineKeyboardButton("🌴 𝐐𝐫𝐮𝐩𝐚 𝐞𝐥𝐚𝐯𝐞 𝐞𝐭 🌴", url="https://t.me/EnoDCbot?startgroup=true")],
        [InlineKeyboardButton("🌀 𝐊𝐚𝐧𝐚𝐥", url="https://t.me/Enobots"), InlineKeyboardButton("🎒 𝐢𝐬𝐭𝐢𝐟𝐚𝐝𝐞", callback_data="button3")],
        [InlineKeyboardButton("⚡ 𝐒𝐚𝐡𝐢𝐛𝐢𝐦 ⚡", url="http://t.me/Mrsherrman")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    client.send_message(
        chat_id=message.chat.id,
        text=caption,
        reply_markup=reply_markup
    )

@app.on_callback_query(filters.regex("button3"))
def button3_callback(client, callback_query):
    caption = "**⚙️ Bütün əmrlər:\n\n• Sadəcə Adminlər: \n\n/dcbasla - oyuna qeydiyyatı başlat\n/dcstart - oyunu başlat\n/dcstop - oyunu saxla\n/sonraki - növbəti oyunçuya keç\n/cixar - mövcud oyunçunu çıxar\n\n• Bütün oyunçular:\n\n/qosul - oyuna qoşul \n/cix - oyundan çıx.\n\nV:2.2.2**"
    
    keyboard = [
        [InlineKeyboardButton("🌀 𝐊𝐚𝐧𝐚𝐥", url="https://t.me/Enobots"), InlineKeyboardButton("👈🏻 𝐆𝐞𝐫𝐢", callback_data="button6")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    callback_query.message.edit_text(
        text=caption,
        reply_markup=reply_markup
    )

@app.on_callback_query(filters.regex("button6"))
def button6_callback(client, callback_query):
    user = callback_query.from_user
    caption = f"**Salam {user.mention}!!\n\nMən, Telegramın ən yaxşı Doğruluq və Cəsarət oyun botuyam 🦣**"
    
    keyboard = [
        [InlineKeyboardButton("🌴 𝐐𝐫𝐮𝐩𝐚 𝐞𝐥𝐚𝐯𝐞 𝐞𝐭 🌴", url="https://t.me/EnoDCbot?startgroup=true")],
        [InlineKeyboardButton("🌀 𝐊𝐚𝐧𝐚𝐥", url="https://t.me/Enobots"), InlineKeyboardButton("🎒 𝐢𝐬𝐭𝐢𝐟𝐚𝐝𝐞", callback_data="button3")],
        [InlineKeyboardButton("⚡ 𝐒𝐚𝐡𝐢𝐛𝐢𝐦 ⚡",url="http://t.me/Mrsherrman")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    callback_query.message.edit_text(
        text=caption,
        reply_markup=reply_markup
  )


database = {}

@app.on_message(filters.command("dcbasla") & filters.group)
def start_game(client, message):
    chat_id = message.chat.id

    member = client.get_chat_member(chat_id, message.from_user.id)
    if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        message.reply_text("**❕Yalnız adminlər oyun başlada bilər**")
        return

    if chat_id not in database:
        database[chat_id] = {"game_started": False, "current_player_index": 0}

    if database[chat_id]["game_started"]:
        message.reply_text("**Mövcud oyun var əgər oynayan yoxdursa, /dcstop əmri ilə oyunu dayandıra bilərsən**")
        return

    database[chat_id]["game_started"] = True

    database[chat_id]["players"] = []

    text = "𝘰𝘺𝘶𝘯𝘶 𝘣𝘢𝘴𝘭𝘢𝘵𝘮𝘢𝘲 𝘶𝘤𝘶𝘯 /dcstart 𝘺𝘢𝘻𝘪𝘯\n\n💡**𝙊𝙮𝙪𝙣𝙖 𝙌𝙖𝙩𝙞𝙡𝙖𝙣𝙡𝙖𝙧:**"
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🧌 Oyuna Qatıl", callback_data="join")]])
    reply_message = message.reply_text(text, reply_markup=keyboard)

    database[chat_id]["message_id"] = reply_message.id

@app.on_callback_query(filters.regex("join"))
def handle_callback(client, callback_query):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.id

    if message_id != database[chat_id]["message_id"]:
        return

    user_id = callback_query.from_user.id

    if user_id in database[chat_id]["players"]:
        callback_query.answer("Sən artıq oyundasan!")
        return

    database[chat_id]["players"].append(user_id)
    mention = callback_query.from_user.first_name

    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🧌 Oyuna Qatıl", callback_data="join")]])
    text = callback_query.message.text + f"\n{mention}"
    client.edit_message_text(chat_id, message_id, text, reply_markup=keyboard)

@app.on_message(filters.command("dcstop") & filters.group)
def stop_game(client, message):
    chat_id = message.chat.id

    member = client.get_chat_member(chat_id, message.from_user.id)
    if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        message.reply_text("**❕Sadəcə adminlər oyunu saxlaya bilər**")
        return

    if chat_id not in database or not database[chat_id]["game_started"]:
        message.reply_text("Davam edən oyun yoxdur")
        return

    database[chat_id]["game_started"] = False
    database[chat_id]["players"] = []  # Oyuna katılan kullanıcıları sıfırla
    message.reply_text("Oyun dayandırıldı")


@app.on_message(filters.command("dcstart") & filters.group)
def start_game(client, message):
    chat_id = message.chat.id
    
    member = client.get_chat_member(chat_id, message.from_user.id)
    if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        message.reply_text("**❕Yalnız adminlər oyun başlada bilər**")
        return

    if chat_id not in database or not database[chat_id]["game_started"] or not database[chat_id]["players"]:
        message.reply_text("**Oyunçu sayı azdır və ya Qeydiyyat üçün /dcbasla istifadə edin**")
        return

    current_player_index = database[chat_id]["current_player_index"]
    current_player_id = database[chat_id]["players"][current_player_index]
    current_player = client.get_users(current_player_id)
    current_player_mention = current_player.mention

    text = f"**‏‏‏‏‏‏‏‏   \n{current_player_mention}🌴\nSizin sıranızdır, seçiminizi edin:**‏‏‏‏‏‏‏‏"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🧸 Doğruluq", callback_data="Doğruluk"), InlineKeyboardButton("🎃 Cəsarət", callback_data="Cesaret")]
        ]
    )

    if "message_id" in database[chat_id]:
        client.delete_messages(chat_id, database[chat_id]["message_id"])

    new_message = message.reply_text(text, reply_markup=keyboard)
    database[chat_id]["message_id"] = new_message.id


@app.on_callback_query(filters.regex("Doğruluk"))
def handle_truth(client, callback_query):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.id
    user_id = callback_query.from_user.id

    if message_id != database[chat_id]["message_id"]:
        return

    current_player_index = database[chat_id]["current_player_index"]
    current_player_id = database[chat_id]["players"][current_player_index]
    current_player = client.get_users(current_player_id)
    current_player_mention = current_player.mention

    if user_id != current_player_id:
        client.answer_callback_query(callback_query.id, text="Sizin sıranız deyil!")
        return

    selected_question = random.choice(question)

    new_message_text = f"**🧸 Doğruluğu seçdiniz:**\n\n{selected_question}\n\n**Cavab verəcək:** {current_player_mention}"
    ready_button = InlineKeyboardButton("🕯️Hazır", callback_data="ready")
    keyboard = InlineKeyboardMarkup([[ready_button]])
    client.send_message(chat_id, new_message_text, reply_markup=keyboard)

    # Eski mesajı sil
    client.delete_messages(chat_id, message_id)


@app.on_callback_query(filters.regex("Cesaret"))
def handle_dare(client, callback_query):
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.id
    user_id = callback_query.from_user.id
    
    if message_id != database[chat_id]["message_id"]:
        return

    current_player_index = database[chat_id]["current_player_index"]
    current_player_id = database[chat_id]["players"][current_player_index]
    current_player = client.get_users(current_player_id)
    current_player_mention = current_player.mention

    if user_id != current_player_id:
        client.answer_callback_query(callback_query.id, text="Sizin sıranız deyil!")
        return

    selected_task = random.choice(task)
    new_message_text = f"**🎃 Cəsarəti seçdiniz:**\n\n{selected_task}\n\n**Cavab verəcək:** {current_player_mention}"
    ready_button = InlineKeyboardButton("🕯️Hazır", callback_data="ready")
    keyboard = InlineKeyboardMarkup([[ready_button]])
    client.send_message(chat_id, new_message_text, reply_markup=keyboard)

    client.delete_messages(chat_id, message_id)


@app.on_callback_query(filters.regex("ready"))
def handle_ready(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id

    current_player_index = database[chat_id]["current_player_index"]
    current_player_id = database[chat_id]["players"][current_player_index]
    current_player = client.get_users(current_player_id)
    current_player_mention = current_player.mention

    if user_id != current_player_id:
        client.answer_callback_query(callback_query.id, text="Sizin sıranız deyil!")
        return
    callback_query.answer("Siz hazıra basdınız")
    next_player_index = (current_player_index + 1) % len(database[chat_id]["players"])
    database[chat_id]["current_player_index"] = next_player_index
    next_player_id = database[chat_id]["players"][next_player_index]
    next_player = client.get_users(next_player_id)
    next_player_mention = next_player.mention
    text = f"**‏‏‏‏‏‏‏‏   \n{next_player_mention}🌴\nSizin sıranızdır, seçiminizi edin:**‏‏‏‏‏‏‏"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🧸 Doğruluq", callback_data="Doğruluk"), InlineKeyboardButton("🎃 Cəsarət", callback_data="Cesaret")]
        ]
    )

    new_message = client.send_message(chat_id, text, reply_markup=keyboard)
    database[chat_id]["message_id"] = new_message.id

@app.on_message(filters.command("qosul") & filters.group)
def join_game(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_m = message.from_user.mention

    if chat_id not in database or not database[chat_id]["game_started"]:
        message.reply_text("**Hazırda oyun yoxdur. başlatmaq üçün /dcbasla yazın.**")
        return

    if user_id not in database[chat_id]["players"]:
        database[chat_id]["players"].append(user_id)
        message.reply_text(f"**😻 vuhuuu, {user_m} oyuna qatıldı!**")
    else:
        message.reply_text("**Səni unutduğumu sanma... 🤗 onsuz da, oyundasan!**")

@app.on_message(filters.command("cix") & filters.group)
def leave_game(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if chat_id not in database or not database[chat_id]["game_started"]:
        message.reply_text("**Mövcud oyun yoxdur**")
        return

    if user_id in database[chat_id]["players"]:
        database[chat_id]["players"].remove(user_id)
        message.reply_text("**Sən, sənsizliyi hardan biləcən?!🥹 Oyundan ayrıldın ama qəlbimdən əsla!**")
    else:
        message.reply_text("**🫦 Onsuz oyunda deyilsən, ama olmağını çox istərdim!**")

@app.on_message(filters.command("sonraki") & filters.group)
def next_player(client, message):
    chat_id = message.chat.id
    
    member = client.get_chat_member(chat_id, message.from_user.id)
    if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        message.reply_text("**❕Yalnız adminlər bu əmrdən istifadə edə bilər**")
        return

    if chat_id not in database or not database[chat_id]["game_started"]:
        message.reply_text("**Oyunçu sayı azdır və ya oyun başladılmayıb**")
        return
        
    current_player_index = database[chat_id]["current_player_index"]
    next_player_index = (current_player_index + 1) % len(database[chat_id]["players"])
    database[chat_id]["current_player_index"] = next_player_index
    current_player_id = database[chat_id]["players"][current_player_index]
    current_player_info = app.get_users(current_player_id)
    current_player_first_name = current_player_info.first_name
    current_player_mention = f"[{current_player_first_name}](tg://user?id={current_player_id})"
    next_player_id = database[chat_id]["players"][next_player_index]
    next_player_info = app.get_users(next_player_id)
    next_player_first_name = next_player_info.first_name
    next_player_mention = f"[{next_player_first_name}](tg://user?id={next_player_id})"
    message.reply_text(f"**{current_player_mention} oynamadığı üçün, sırası keçdi!**")
    time.sleep(1)
    text = f"‏‏‏‏‏‏‏‏   \n**{next_player_mention}🌴\nSizin sıranızdır, seçiminizi edin:‏‏‏**"      
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🧸 Doğruluq", callback_data="Doğruluk"), InlineKeyboardButton("🎃 Cəsarət", callback_data="Cesaret")]
        ]
    )

    if "message_id" in database[chat_id]:
        client.delete_messages(chat_id, database[chat_id]["message_id"])
        
    new_message = message.reply_text(text, reply_markup=keyboard)
    database[chat_id]["message_id"] = new_message.id
    
@app.on_message(filters.command("cixar") & filters.group)
def remove_player(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    member = client.get_chat_member(chat_id, message.from_user.id)
    if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        message.reply_text("**❕Yalnız adminlər oyundan kənarlaşdıra bilər. Yaxşısı bir adminə xəbər et!**")
        return

    if chat_id not in database or not database[chat_id]["game_started"] or not database[chat_id]["players"]:
        message.reply_text("**mövcud oyun yoxdur və ya oyunçu sayı azdır**")
        return

    current_player_index = database[chat_id]["current_player_index"]
    current_player_id = database[chat_id]["players"][current_player_index]
    current_player_info = app.get_users(current_player_id)
    current_player_first_name = current_player_info.first_name
    current_player_mention = f"[{current_player_first_name}](tg://user?id={current_player_id})"
    if user_id in database[chat_id]["players"]:
        del database[chat_id]["players"][current_player_index]
        message.reply_text(f"**{current_player_mention} aktiv olmadığı üçün oyundan çıxarıldı!**")

        if len(database[chat_id]["players"]) == 0:
            database[chat_id]["game_started"] = False
            database[chat_id]["players"] = []
            message.reply_text("**Oyuçu qalmadığı üçün oyunu dayandırdım**")

        elif current_player_id == user_id:
            next_player_index = (current_player_index + 1) % len(database[chat_id]["players"])
            database[chat_id]["current_player_index"] = next_player_index
        else: 
            database[chat_id]["current_player_index"] = 0

    else:
        message.reply_text("**Oyunçu onsuz oyunda deyil**")
        return

    current_player_index = database[chat_id]["current_player_index"]
    current_player_id = database[chat_id]["players"][current_player_index]
    current_player_info = app.get_users(current_player_id)
    current_player_first_name = current_player_info.first_name
    current_player_mention = f"[{current_player_first_name}](tg://user?id={current_player_id})"
    text = f"‏‏‏‏‏‏‏‏   \n**{current_player_mention}🌴\nSizin sıranızdır, seçiminizi edin:‏‏‏‏‏‏‏‏**"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🧸 Doğruluq", callback_data="Doğruluk"), InlineKeyboardButton("🎃 Cəsarət", callback_data="Cesaret")]
        ]
    )

    if "message_id" in database[chat_id]:
        client.delete_messages(chat_id, database[chat_id]["message_id"])

    new_message = message.reply_text(text, reply_markup=keyboard)
    database[chat_id]["message_id"] = new_message.id

@app.on_message(filters.command('reyting') & filters.user('Mrsherrman'))
def reyting_command(client, message):
    user_count = len(userdb)
    group_count = len(groupdb)
    response = f"user: {user_count} grup: {group_count}"
    message.reply_text(response)

@app.on_message(filters.command("greklam") & filters.user("@Mrsherrman"))
def greklam_command(client, message):
    # Yanıtlanan mesajı al
    replied_message = message.reply_to_message
    if replied_message is None:
        message.reply_text("Bu komut bir yanıt gerektirir.")
        return

    # Yanıtlanan mesajı groupdb'deki ID'lere iletiş
    for group_id in groupdb:
        client.forward_messages(group_id, message.chat.id, replied_message.id)

# /preklam komutunu işleyen fonksiyon
@app.on_message(filters.command("preklam") & filters.user("@Mrsherrman"))
def preklam_command(client, message):
    # Yanıtlanan mesajı al
    replied_message = message.reply_to_message
    if replied_message is None:
        message.reply_text("Bu komut bir yanıt gerektirir.")
        return

    # Yanıtlanan mesajı userdb'deki ID'lere iletiş
    for user_id in userdb:
        client.forward_messages(user_id, message.chat.id, replied_message.id)


@app.on_message(filters.private | filters.group)
def listen_messages(client, message):
    chat_type = message.chat.type
    
    if chat_type in [ChatType.PRIVATE, ChatType.BOT]:
        # Özel mesajı gönderen kişinin ID'sini kontrol ediyoruz
        if message.from_user.id not in userdb:
            userdb.add(message.from_user.id)
    elif chat_type in [ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL]:
        # Grup ID'sini kontrol ediyoruz
        if message.chat.id not in groupdb:
            groupdb.add(message.chat.id)
        

app.run()
