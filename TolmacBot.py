import telebot
from telebot.types import Message
from telebot import types

TOKEN = '839076133:AAFdjIQ1Bn9KvPoZ6smhrh7uoICEeqJc3f4'
bot = telebot.TeleBot(TOKEN)

markup_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_menu.row('Alphabets Алфавиты Abeceler')

hesbisey = '''🇬🇧 Nothing found, write other word. You can ask author to add this word, you can also write me your suggestions and comments if you notice a mistake @sibirli
Our chat: @tolmacchat
🇷🇺 Ничего не найдено, введите другое слово. Еще Вы можете попросить автора добавить это слово, также можете написать мне свои предложения и замечания если заметили ошибку @sibirli
Наш чат: @tolmacchat
🇹🇷 Hiçbirşey bulunamadı, başka bir kelime yazın. Bot yaratıcısından bu kelime eklemesini isteyebilirsiniz, ayrıca teklif ve hata hakkında bana yazabilirsiniz @sibirli
Sohbet: @tolmacchat'''

#send_message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '''🇬🇧 Write any word
🇷🇺 Введите слово
🇹🇷 Bir kelime yazın''', reply_markup=markup_menu)

@bot.message_handler(commands=['alphabets'])
def alphabets (message):
    bot.send_message(message.chat.id, '''Sounds for most languages:
Ä ä = [æ]
C c = [ʤ]
Ç ç = [ʧ]
E e = [ɛ], [e]
H h = [h]
X x = [x]
Ğ ğ = [ɣ], [ʁ]
J j = [ʒ]
I ı = [ɯ]
İ i = [ɪ], [i]
Ñ ñ or Ŋ ŋ = [ŋ]
Ö ö = [œ], [ø]
Ş ş = [ʃ]
Ü ü	= [y]
V v	= [v]
W w = [w]
Y y	= [j]
Ā ā = long [a]
Ē ē = long [e]
Ï ï = long [i]
Ī ī = long [ɯ]
Ō ō = long [o]
Ȫ ȫ = long [ø]
Ū ū = long [u]
Ǖ ǖ = long [y]

Other differences are listed below:

🇦🇿 Türkcə: 
Ə ə = [æ]
G g =  [gʲ]
K k = [kʲ] ([k] only in loanwords)
Q q = [g]

🇹🇲 Türkmençe:
F f = [ɸ]
G g = [g], [ʁ]
H h = [h], [χ]
I i = [ɪ]
K k = [k], [q]
J j = [dʒ]
Ň ň = [ŋ]
S s = [θ]
W w = [β]
Y y = [ɯ]
Ý ý = [j]
Z z = [ð]

🇺🇿 Oʻzbekcha: 
A a = [a], [æ]
J j = [ʤ], [ʒ]
O o = [ɑ]
V v = [v], [w]
Oʻ oʻ = [o]
Gʻ gʻ = [ɣ]
Sh sh = [ʃ]
Ch ch = [ʧ]
ng = [ŋ]

🇰🇿 Qazaqşa:
Ş ş = [ɕ]
E e = [jɪ]
J j = [ʑ]
W w = [w]
Ü ü = [ʏ]
H h = [h], [χ]

🇰🇬 Qırğızça: 
J j = [dʒ]

Uyghurche:
E e = [æ]
É é = [ɛ]
J j = [ʤ]
Sh sh = [ʃ]
Ch ch = [ʧ]
ng = [ŋ]
Gh gh = [ʁ]

Tatarça:
C c = [ʑ]
Ç ç = [ɕ]

Başqortsa: 
Þ þ = [θ]
Ð ð = [ð]
G g = [ɟ]
O o = [ʊ̞]

Çovaşla (Argadu alphabet):
C c = [ɕ], [ʑ]
Ç ç = [ʨ]
O o = [ə]
Ö ö = [ɘ]
Ş ş = [ʂ]

Qaraqalpaqsha:
Á á = [æ]
Ǵ ǵ = [ɣ]
Ń ń = [ŋ]
Ó ó = [œ]
Ú ú = [y]
Ch ch = [ʧ]
Sh sh = [ʃ]
I i = [i]
Í ı = [ə]

Qırımtatarca:
H h = [x]
V v = [v], [w]

Qumuqça:
E e	= [e], [æ]

Qaraçay-Malqar:
J j = [dʒ], [ʒ] (depends on dialect)

Sıbırca:
С с = [ts]

Gagauzça:
Ţ ţ = [ts]

Saqalī: 
E e = [æ], [e]
Q q = [x], [q]
J j = [ɟ]
Ń ń = [ɲ]

Dulgan-Hakalī:
E e = [æ], [e]
J j = [ɟ]
Ń ń = [ɲ]

Salırça:
C c = [ʤ], [d͡z]
' = Palatalization

Xakastap:
İ i = [ɨ], [ɪ]
Î î = [i]

Altay: 
C c = [ɟ], [d͡z]

Karaj:
C c = [ts]
J j = [j]
Č č = [ʧ]
Š š = [ʃ]
V v = [v], [w]
Y y = [ɯ]
H h = [ɣ], [h]
Ch ch = [χ]
Dž dž = [ʤ]
E e = [ɛ]
Ie ie = [e]
Io io = [œ]
Iu iu = [y]
Ń ń = [ɲ]
K k = [k], [q]
Ź ź = [ʑ]
’ = Palatalization

Qrımçahça:
H h = [χ]
L l = [lʲ]

Soyot: 
İ i = [ɨ], [ɪ]
Î î = [i]
E e = [e]
Ê ê = [ɛ]
â = Palatalization before [a]

Tofalap:
İ i = [ɨ], [ɪ]
Î î = [i]
E e = [e], [ɛ] (at the beginning of the word, and after T, D)
Ê ê = [ɛ]
â = Palatalization before [a]''')

@bot.message_handler(commands=['help'])
def help (message):
    bot.send_message(message.chat.id, '''🇬🇧 How to use the bot:
⚪️ Write the masculine variation of word, because in Turkic languages there is no concept of gender (eg, “tiger” instead of “tigress”).
⚪️ Write a noun without "the" or "a" (eg, “guest” instead of “the guest”).
⚪️ Often adverbs and adjectives are translated the same way from Russian into Turkic languages, so it is better to look for an adjective (eg. “easy” instead of “easily”).
⚪️ For the convenience of comparison and perception, verbs are translated not in the form of the infinitive, but in the imperative mood, 2nd person singular/informal (eg. "sev" ("love!") instead of "sevmek" ("to love")). But you should enter verbs with "to" so as not to be mixed up with nouns.
⚪️ Due to the peculiarities of the Cyrillic alphabet in some Turkic languages, the distinction between the sounds “ya” and “yä” has disappeared, because they are both denoted by the russian letter “я”, but due to system of vowel harmony, it can be assumed that “yä” is used in words where used front vowels "(eg. Törkiyä), and "ya" is used in words where used back vowels (eg. qaya), also in some words where used front vowels, the combination "ya" is still used if it is loanword from Russian and due to the lack of sound in Russian" yä ".
🇷🇺 Как пользоваться ботом:
⚪️ Пишите слово в мужском роде, так как в тюркских языках нет понятия рода (напр., "тигр" вместо "тигрица"), по этой же причине лучше искать прилагательное в мужском роде, а не женском (напр., "хороший" вместо "хорошая").
⚪️ Часто наречия и прилагательные переводятся одинаково с русского на тюркские языки, поэтому лучше искать прилагатльное (напр., "умный" вместо "умно").
⚪️ Вместо прилагательного, образованного от существительного пишите существительное, потому что в тюркских языках прилагательные от существительных почти не образуются, и в подобных случаях используется связка "существительное + существительное + изафет" вместо "прилагательное + существительное" (напр., "глаз волка" вместо "волчий глаз", поэтому нужно искать "волк", а не "волчий").
⚪️ Для удобства сравнения и восприятия, глаголы переведены не в форме инфинитива, а в повелительном наклонении, настоящего времени, единственного числа (напр., "sev" ("люби") вместо "sevmek" ("любить")).
⚪ В тюркских языках нет приставок, поэтому искать слово на русском тоже рекомендуется без приставок в случаях если приставка не меняет смысл слова (напр. "кушай" вместо "покушай").
⚪️ Из-за особенностей кириллического алфавита в некоторых тюркских языках исчезло отличие звуков "ya" и "yä", потому что они оба обозначаются буквой "я", но из-за закона сингармонизма, можно предположить, что в мягких словах используется сочетание "yä" (напр., Törkiyä), а в твердых "ya" (напр., qaya), также в некоторых слова мягких словах все равно исплользуется сочетание "ya" если это слово проникло из русского и из-за отсутствия в русском языке звука "yä"
🇹🇷 Bot nasıl kullanılır:
⚪️ İsimden oluşturulmuş sıfatlar yerine sadece isimi aramak gerekiyor, çünkü Türkiye Türkçesindeki gibi başka türk lehcelerinde de izafet kullanılır (örnek: "tarihsel adam" yerine "tarih adamı", "tarih" ve "adam" kelimelerini aramak gerekiyor).
⚪ Karşılaştırma ve algı kolaylığı için fiilleri -mak/-mek ekleri dışında yazılacak (örneğin, "sevmek" yerine "sev"), lâkin bazı kelimelerde karışmamak için (örneğin, "al" (renk) ve almak) mastar biçiminde yazın.
⚪️ Bazı Türk lehcelerinde Kiril alfabesinin özellikleri nedeniyle, “ya” ve “yä” sesleri arasındaki fark ortadan kalktı, çünkü ikisi de “я” harfiyle ifade edildi, ancak kalınlık-incelik kuralı nedeniyle, “yä”' ince kelimelerde (örnek: Törkiyä) “ya” ise kalın (örnek: qaya) kelimelerde kullanıldığı varsayılabilir. Ayrıca, Rusçada "yä" sesi olmaması nedeniyle ince sesler kullanılan bazı alınma kelimelerde, "ya" kullanılır.''')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.replace('İ', 'i').replace('ı', 'I').lower() == "alphabets алфавиты abeceler":
        bot.send_message(message.chat.id, '''Sounds for most languages:
Ä ä = [æ]
C c = [ʤ]
Ç ç = [ʧ]
E e = [ɛ], [e]
H h = [h]
X x = [x]
Ğ ğ = [ɣ], [ʁ]
J j = [ʒ]
I ı = [ɯ]
İ i = [ɪ], [i]
Ñ ñ or Ŋ ŋ = [ŋ]
Ö ö = [œ], [ø]
Ş ş = [ʃ]
Ü ü	= [y]
V v	= [v]
W w = [w]
Y y	= [j]
Ā ā = long [a]
Ē ē = long [e]
Ï ï = long [i]
Ī ī = long [ɯ]
Ō ō = long [o]
Ȫ ȫ = long [ø]
Ū ū = long [u]
Ǖ ǖ = long [y]

Other differences are listed below:

🇦🇿 Türkcə: 
Ə ə = [æ]
G g =  [gʲ]
K k = [kʲ] ([k] only in loanwords)
Q q = [g]

🇹🇲 Türkmençe:
F f = [ɸ]
G g = [g], [ʁ]
H h = [h], [χ]
I i = [ɪ]
K k = [k], [q]
J j = [dʒ]
Ň ň = [ŋ]
S s = [θ]
W w = [β]
Y y = [ɯ]
Ý ý = [j]
Z z = [ð]

🇺🇿 Oʻzbekcha: 
A a = [a], [æ]
J j = [ʤ], [ʒ]
O o = [ɑ]
V v = [v], [w]
Oʻ oʻ = [o]
Gʻ gʻ = [ɣ]
Sh sh = [ʃ]
Ch ch = [ʧ]
ng = [ŋ]

🇰🇿 Qazaqşa:
Ş ş = [ɕ]
E e = [jɪ]
J j = [ʑ]
W w = [w]
Ü ü = [ʏ]
H h = [h], [χ]

🇰🇬 Qırğızça: 
J j = [dʒ]

Uyghurche:
E e = [æ]
É é = [ɛ]
J j = [ʤ]
Sh sh = [ʃ]
Ch ch = [ʧ]
ng = [ŋ]
Gh gh = [ʁ]

Tatarça:
C c = [ʑ]
Ç ç = [ɕ]

Başqortsa: 
Þ þ = [θ]
Ð ð = [ð]
G g = [ɟ]
O o = [ʊ̞]

Çovaşla (Argadu alphabet):
C c = [ɕ], [ʑ]
Ç ç = [ʨ]
O o = [ə]
Ö ö = [ɘ]
Ş ş = [ʂ]

Qaraqalpaqsha:
Á á = [æ]
Ǵ ǵ = [ɣ]
Ń ń = [ŋ]
Ó ó = [œ]
Ú ú = [y]
Ch ch = [ʧ]
Sh sh = [ʃ]
I i = [i]
Í ı = [ə]

Qırımtatarca:
H h = [x]
V v = [v], [w]

Qumuqça:
E e	= [e], [æ]

Qaraçay-Malqar:
J j = [dʒ], [ʒ] (depends on dialect)

Sıbırca:
С с = [ts]

Gagauzça:
Ţ ţ = [ts]

Saqalī: 
E e = [æ], [e]
Q q = [x], [q]
J j = [ɟ]
Ń ń = [ɲ]

Dulgan-Hakalī:
E e = [æ], [e]
J j = [ɟ]
Ń ń = [ɲ]

Salırça:
C c = [ʤ], [d͡z]
' = Palatalization

Xakastap:
İ i = [ɨ], [ɪ]
Î î = [i]

Altay: 
C c = [ɟ], [d͡z]

Karaj:
C c = [ts]
J j = [j]
Č č = [ʧ]
Š š = [ʃ]
V v = [v], [w]
Y y = [ɯ]
H h = [ɣ], [h]
Ch ch = [χ]
Dž dž = [ʤ]
E e = [ɛ]
Ie ie = [e]
Io io = [œ]
Iu iu = [y]
Ń ń = [ɲ]
K k = [k], [q]
Ź ź = [ʑ]
’ = Palatalization

Qrımçahça:
H h = [χ]
L l = [lʲ]

Soyot: 
İ i = [ɨ], [ɪ]
Î î = [i]
E e = [e]
Ê ê = [ɛ]
â = Palatalization before [a]

Tofalap:
İ i = [ɨ], [ɪ]
Î î = [i]
E e = [e], [ɛ] (at the beginning of the word, and after T, D)
Ê ê = [ɛ]
â = Palatalization before [a]''')

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "привет" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hello"\
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hi"\
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "salam"\
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "merhaba"\
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "здравствуйте"\
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "здрасти"\
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "здарово"\
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "здорова"\
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "selam"\
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "салам"\
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "greating"\
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "greatings"\
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "säläm":
        bot.send_message(message.chat.id, '''🇬🇧 English: hi, hello
🇷🇺 Русский: привет, здравствуйте, здорово [zdorovo]
🇹🇷 Türkçe: selam, merhaba
🇦🇿 Türkcə: salam
🇹🇲 Türkmençe: salam
🇺🇿 Oʻzbekcha: salom
🇰🇿 Qazaqşa: sälem
🇰🇬 Qırğızça: salam
Uyghurche: salam
Tatarça: sälam, isänmesez
Başqortsa: säläm, hawmı, hawmıhığıð, iþänmehegeð
Çovaşla: salam
Qaraqalpaqsha: sálem
Qırımtatarca: selâm
Qumuqça: salam
Saqalıı: eğerde {neologism}, sorgu mende duguy {archaism}
Qaraçay-Malqar: salam
Tıvalap: bayır
Gagauzça: seläm 
Noğayşa: salam
Sıbırca: säläm, yaqşımısıs, sawmısıs
Xakastap: izen
Salırça: sāläm
Altay: ezender
Şor: ezen
Dolgan: dorōbo
Urumça: selam (selâm)
Karaj: kiuń jachšy, bazlych
Qrımçahça: selâm
Soyot: ekkîî (ekköö), bayır
Tofalap: ekkîî, mendi, doroobo''', reply_markup=markup_menu)
    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "август" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ağustos" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "august":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: august
🇷🇺 Русский: август
🇹🇷 Türkçe: ağustos
🇦🇿 Türkcə: avqust, sünbülə
🇹🇲 Türkmençe: Alp Arslan aýy
🇺🇿 Oʻzbekcha: avgust, sunbula
🇰🇿 Qazaqşa: tamız, sümbile
🇰🇬 Qırğızça: baş oona
Uyghurche: tomuz
Tatarça: awğıs, uraq, sönbelä
Başqortsa: urağay
Çovaşla: curla
Qaraqalpaqsha: avgust, súmbile
Qırımtatarca: avgust, arman
Qumuqça: avgust, turşu
Qaraçay-Malqar: avgust, qırqar
Noğayşa: avgust, sarıtambız
Sıbırca: avgust, sömpölä (sömböl), uraq (orğaq)
Gagauzça: harman
Saqalī: atırjaq ıya
Dulgan-Hakalī: ırgakta
Tıvalap: ses
Salırça: sehsinci
Xakastap: avgust
Xakastap (Sağay): orğax, ot
Xakastap (Pîltir): xıra kîsçeñ
Xakastap (Xaas): ot
Altaylap: avgust, quran
Şor: orğaq
Urumça: avğustos
Karajče: (they use Karaim calendar)
Qrımçahça: avgust
Soyot: avgust
Tofalap: aynaar''', reply_markup=markup_menu)
    elif message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azərbaycan" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "азербайджан" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azerbaijan" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azerbaıjan" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azerbaİjan" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azerbaycan" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azarbeycan" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azerbeycan" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "азербаджан" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azerbayjan" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azerbaydjan" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azerbaİdjan" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azerbaıdjan" \
             or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "azerbaidjan":
        bot.send_message(message.chat.id, '''
🇬🇧 English: Azerbaijan
🇷🇺 Русский: Азербайджан
🇹🇷 Türkçe: Azerbaycan, Azarbeycan (Azerbeycan) {dial.}
🇦🇿 Türkcə: Azərbaycan
🇹🇲 Türkmençe: Azerbaýjan
🇺🇿 Oʻzbekcha: Ozarbayjon
🇰🇿 Qazaqşa: Äzirbayjan
🇰🇬 Qırğızça: Azerbayjan
Uyghurche: Ezerbeyjan
Tatarça: Azärbaycan
Başqortsa: Äzerbayjan
Çovaşla: Azerbayʤan
Qaraqalpaqsha: Ázerbayjan
Qırımtatarca: Azerbaycan
Qumuqça: Azerbayjan
Qaraçay-Malqar: Azerbayjan
Noğayşa: Azerbaydjan
Sıbırca: Äzerbayjan
Gagauzça: Azerbaycan
Saqalī: Azerbayjan
Dulgan-Hakalī: Azerbayjan
Tıvalap: Azerbaydjan
Salırça: Azerbaycañ
Xakastap: Azerbaydjan
Altaylap: Azerbaydjan
Şor: Azerbaydjan
Urumça: Azerbacan (Azırbacan)
Karajče: Azierbajdžan
Qrımçahça: Azerbaycan
Soyot: Azerbaycan
Tofalap: Azerbaycan''', reply_markup=markup_menu)
    elif message.text.replace('İ', 'i').replace('ı', 'I').lower() == "алгебра" \
            or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "algebra" \
            or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "альджабр" \
            or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "аль-джабр" \
            or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "cebr" \
            or message.text.replace('İ', 'i').replace('ı', 'I').lower() == "cebir":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): cäbr
🇬🇧 English: algebra
🇷🇺 Русский: алгебра
🇹🇷 Türkçe: cebir
🇦🇿 Türkcə: cəbr
🇹🇲 Türkmençe: algebra, jebir (archaism)
🇺🇿 Oʻzbekcha: algebra, aljabr (archaism)
🇰🇿 Qazaqşa: algebra
🇰🇬 Qırğızça: algebra, jabır (archaism)
Uyghurche: algébra, hésab, eljebr (archaism)
Tatarça: algebra, ğilme cäber
Başqortsa: algebra
Çovaşla: algebra
Qaraqalpaqsha: algebra
Qırımtatarca: cebir
Qumuqça: cabru
Qaraçay-Malqar: algebra
Noğayşa: algebra
Sıbırca: algebra
Gagauzça: algebra
Saqalī: algebra
Dulgan-Hakalī: algebra
Tıvalap: algebra
Salırça: cebir
Xakastap: algebra
Altaylap: algebra
Şor: algebra
Urumça: algebra
Karajče: algebra
Qrımçahça: algebra
Soyot: algebra
Tofalap: algebra''', reply_markup=markup_menu)
    elif message.text.lower() == "аллах" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "alla" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "allah" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "allax" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "алла" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "аллаh":
        bot.send_message(message.chat.id, '''
🇬🇧 English: Allah
🇷🇺 Русский: Аллах
🇹🇷 Türkçe: Allah
🇦🇿 Türkcə: Allah 
🇹🇲 Türkmençe: Allah
🇺🇿 Oʻzbekcha: Alloh (Olloh)
🇰🇿 Qazaqşa: Allah (Ala, Alla, Alah, Alda)
🇰🇬 Qırğızça: Allah (Alla)
Uyghurche: Allah
Tatarça: Allah (Alla)
Başqortsa: Allah (Alla)
Çovaşla: Allah
Qaraqalpaqsha: Alla (Allah)
Qırımtatarca: Allah (Alla)
Qumuqça: Allah
Qaraçay-Malqar: Allah
Noğayşa: Alla
Sıbırca: Alla
Gagauzça: Allah (Allaa)
Saqalī: Allāh (Allāq)
Dulgan-Hakalī: Allāh
Tıvalap: Alla
Salırça: Allah (Alah)
Xakastap: Allax
Altaylap: Alla
Şor: Alla
Urumça: Alla (Allax)
Karajče: Allah
Qrımçahça: Alla (Allah)
Soyot: Allah
Tofalap: Allah''', reply_markup=markup_menu)
    elif message.text.lower() == "andrew" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "андрей" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "andreas" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "andrey":
        bot.send_message(message.chat.id, '''
🇬🇧 English: Andrew
🇷🇺 Русский: Андрей [Andrey]
🌍 Çovaşla: Yentöri (Entri, Untri, Entöruk, Entyuk)
🌍 Qaraçay-Malqar: Endirew''', reply_markup=markup_menu)
    elif message.text.lower() == "апостол" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "apostol" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "apostle" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "havari":
        bot.send_message(message.chat.id, '''🐺 Old Turkic: yalawıç
🇬🇧 English: apostle
🇷🇺 Русский: апостол
🇹🇷 Türkçe: havari
🇦🇿 Türkcə: həvari
🇹🇲 Türkmençe: apostol
🇺🇿 Oʻzbekcha: havoriy, apostol
🇰🇿 Qazaqşa: apostol, elşi
🇰🇬 Qırğızça: apostol
Uyghurche: elchi
Tatarça: apostol
Başqortsa: apostol
Çovaşla: apostol
Qaraqalpaqsha: apostol
Qırımtatarca: avariy
Qumuqça: apostol
Qaraçay-Malqar: abıstol
Noğayşa: apostol
Sıbırca: hawari (archaism)
Gagauzça: apostol
Saqalī: opuostal
Dulgan-Hakalī: opuostal
Tıvalap: ???
Salırça: ???
Xakastap: ???
Altaylap: ???
Şor: ???
Urumça: apostolos, resül
Karajče: ???
Qrımçahça: ???
Soyot: ???
Tofalap: ???''', reply_markup=markup_menu)
    elif message.text.lower() == "апрель" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "april" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nisan":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: april
🇷🇺 Русский: апрель
🇹🇷 Türkçe: nisan
🇦🇿 Türkcə: aprel, neysan (nisan, leysan)
🇹🇲 Türkmençe: gurbansoltan
🇺🇿 Oʻzbekcha: aprel, savr
🇰🇿 Qazaqşa: säwir, kökek
🇰🇬 Qırğızça: çın quran
Uyghurche: ümid
Tatarça: äpril, yañarış, säwer
Başqortsa: alağaray
Çovaşla: aka
Qaraqalpaqsha: aprel, sáwir
Qırımtatarca: aprel, çiçek
Qumuqça: aprel, yaysan (maysan)
Qaraçay-Malqar: aprel, toturnu art ayı, awuznu art ayı
Noğayşa: aprel, kökek
Sıbırca: aprel, säwer (saur), per (birneñ)
Gagauzça: çiçek
Saqalī: mūs ustar
Dulgan-Hakalī: taba emiydir
Tıvalap: dört
Salırça: tütinci
Xakastap: aprel
Xakastap (Sağay): kiçig körik, soñ körik
Xakastap (Pîltir): kiçig körik
Xakastap (Xaas): xosxar
Altaylap: aprel, tulaan
Şor: añ
Urumça: epril
Karajče: (they use Karaim calendar)
Qrımçahça: aprel
Soyot: aprel
Tofalap: ıtalaar''', reply_markup=markup_menu)
    elif message.text.lower() == "армения" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гейклуб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гей клуб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гей-клуб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "armenia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "armenıa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ermenistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gay club" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gay-club" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gayclub" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hayastan":
        bot.send_message(message.chat.id, '''🇬🇧 English: Armenia
🇷🇺 Русский: Армения [Armeniya]
🇹🇷 Türkçe: Ermenistan
🇦🇿 Türkcə: Ermənistan
🇹🇲 Türkmençe: Ermenistan
🇺🇿 Oʻzbekcha: Armaniston
🇰🇿 Qazaqşa: Ärmenstan, Ärmeniya (Armeniya)
🇰🇬 Qırğızça: Armeniya, Ermenstan
🌏 Uyghurche: Erméniye
🌍 Tatarça: Ärmänstan
🌍 Başqortsa: Ärmänstan
🌍 Çovaşla: Ermeni
🌍 Qaraqalpaqsha: Ármeniya
🌍 Qırımtatarca: Ermenistan
🌍 Qumuqça: Ermenistan, Armeniya
🌍 Qaraçay-Malqar: Ermen, Ermeniya
🌍 Noğayşa: Ermelistan, Armeniya
🌏 Sıbırca: Ärmänestan
🌍 Gagauzça: Ermeniya
🌏 Saqalī: Ermēn Sire, Armeniya
🌏 Dulgan-Hakalī: Armeniya, Ermēn Hire
🌏 Tıvalap: Armeniya
🌏 Salırça: Armenstan
🌏 Xakastap: Armenîya
🌏 Altaylap: Armeniya
🌏 Şor: Armeniya
🌍 Urumça: Ermänistan (Ermenistan)
🌍 Karajče: Ėrmienistan
🌍 Qrımçahça: Ermenistan
🌏 Soyot: Armenîya
🌏 Tofalap: Armenîya
in Armenian: Hayastan''', reply_markup=markup_menu)
    elif message.text.lower() == "бастард" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бастдард" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ублюдок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "piç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "haramzade" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "veledizina" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bastard" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "выродок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ублюдина" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "внебрачный ребенок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "внебрачный ребёнок":
        bot.send_message(message.chat.id, '''🇬🇧 English: bastard
🇷🇺 Русский: бастард, ублюдок
🇹🇷 Türkçe: piç, haramzade, veledizina
🇦🇿 Türkcə: bic, haramzada (dialect), bicbala (dialect)
🇹🇲 Türkmençe: haramzada, haramy
🇺🇿 Oʻzbekcha: haromzoda, haromi
🇰🇿 Qazaqşa: kerdemşe, qıztalaq
🇰🇬 Qırğızça: nikesiztuwulğan
Uyghurche: buzuqning balisi, haramzade
Tatarça: uynaştan tuğan, nikaxsız tuğan bala
Başqortsa: nikaxhıð tıwğan bala
Çovaşla: tupolça, moşorlanmasor curatno aça
Qaraqalpaqsha: nekesiz tuwılğan bala
Qırımtatarca: piç, piç bala, aramzade, calaqay (dialect)
Qumuqça: piç, qantuluq, zinadan tuwğan
Qaraçay-Malqar: gıbışı
Noğayşa: nekesiz tuwğan
Sıbırca: suras, üz uruginä uxşamaz
Gagauzça: piç, baystruk
Saqalıı: körsǖ oğoto, bulumńu oğo, bulūnńa oğo
Dulgan-Hakalıı: körsühe ogoto
Tıvalap: suras
Salırça: zabula, zağali
Xakastap: suras, suras pala
Altay: suras
Şor: ???
Urumça: piç, taşlama
Karajče: pič, ginech ulany (giuniach ulany)
Qrımçahça: ???
Soyot: ???
Tofalap: ???''', reply_markup=markup_menu)
    elif message.text.lower() == "биология" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "biology" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "biyoloji" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bioloji":
        bot.send_message(message.chat.id, '''
🇬🇧 English: biology
🇷🇺 Русский: биология [biologiya]
🇹🇷 Türkçe: biyoloji, dirim bilimi (neologism), hayatiyyat (ottoman archaism)
🇦🇿 Türkcə: biologiya, təbiətşünaslıq (acrhaism), həyatiyyat (acrhaism), elmi həyat (archaism)
🇹🇲 Türkmençe: biologiýa
🇺🇿 Oʻzbekcha: biologiya
🇰🇿 Qazaqşa: biyologiya (biologiya), tirşiliktanıw
🇰🇬 Qırğızça: biologiya
Uyghurche: bi'ologiye
Tatarça: biyalugiä (biologiya)
Başqortsa: biologiä
Çovaşla: biologi
Qaraqalpaqsha: biologiya
Qırımtatarca: ayatiyat
Qumuqça: biologiya
Qaraçay-Malqar: biologiya
Noğayşa: biologiya
Sıbırca: biologiä
Gagauzça: biologiya
Saqalī: biologiya
Dulgan-Hakalī: biologiya
Tıvalap: biologiya
Salırça: biyoloci
Xakastap: bîologiya
Altaylap: biologiya
Şor: biologiya
Urumça: biologiya
Karajče: biologija
Qrımçahça: biologiya
Soyot: bîologiya
Tofalap: bîologiya''', reply_markup=markup_menu)
    elif message.text.lower() == "бог" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "богиня" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "god" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "the god" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tanrı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tanri" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "божество" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tengri" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tenri" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тенгри" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тэнгри" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тангры":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱅𐰭𐰼𐰃 
🇬🇧 English: god
🇷🇺 Русский: бог
🇹🇷 Türkçe: tanrı, yaradan, hüda
🇦🇿 Türkcə: tanrı, yaradan, xuda
🇹🇲 Türkmençe: taňry, ýaradyjy, hudaý
🇺🇿 Oʻzbekcha: tangri, xudo
🇰🇿 Qazaqşa: täŋir, jaratqan, quday
🇰🇬 Qırğızça: teñir, quday
Uyghurche: teñri, xuda
Tatarça: täñre, xoday
Başqortsa: täñre, xoðay
Çovaşla: turo, tankor
Qaraqalpaqsha: taʼnʼir, quday
Qırımtatarca: tañrı, yaradan, huda
Qumuqça: teñiri, xuday
Qaraçay-Malqar: teyri, quday
Noğayşa: täñri, quday
Sıbırca: tañqır, qotay
Gagauzça: allaa
Saqalī: tañara
Tıvalap: burğan
Salırça: tanru, xuda (xuta, xuday, xūda)
Xakastap: xuday
Altay: quday
Şor: quday
Dolgan: tañara
Urumça: tañır (tanırı, tanır), yaradan (yaratan), mevla
Karaj: tieńri
Qrımçahça: tañrı, quday, yaradan, mevlâ
Soyot: burhan, cayaaçı
Tofalap: burhan''', reply_markup=markup_menu)
    elif message.text.lower() == "богатырь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "багатур" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bahadur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "batır" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "batir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "batur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "батыр" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "батур" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bogatyr" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "baghatur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bahadır" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bağatur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bator":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰉𐱃𐰆𐰺 
🐺 Old Turkic (bef. 13th c.): bağatur, batur, sökmän, alp, alp er, alpağut (alpağu)
🇬🇧 English: bogatyr, baghatur ("batır" also means "hero" in most Turkic languages)
🇷🇺 Русский: богатырь, багатур (батыр, батур)
🇯🇵 Nihongo: bagatoru
🇰🇷 Hangug-eo: bagatuleu
🇭🇺 Magyar: bator
🇲🇳 Mongol: baatar
🇹🇷 Türkçe: bahadır (bağatur, batur)
🇦🇿 Türkcə: bahadır (bahadur, batır)
🇹🇲 Türkmençe: batyr
🇺🇿 Oʻzbekcha: bahodir, botir
🇰🇿 Qazaqşa: batır, bahadur (bahadür)
🇰🇬 Qırğızça: baatır
🌏 Uyghurche: batur
🌍 Tatarça: bahadir, batır
🌍 Başqortsa: bahadir, batır
🌍 Çovaşla: poxattir (pokattir), pattor
🌍 Qaraqalpaqsha: batır
🌍 Qırımtatarca: batır
🌍 Qumuqça: batır
🌍 Qaraçay-Malqar: batır, tulpar
🌍 Noğayşa: bätir, tulpar, alıp
🌏 Sıbırca: bahadir, batır
🌍 Gagauzça: baatır (baatur)
🌏 Saqalī: buqatīr, bātır (bōtur)
🌏 Dulgan-Hakalī: bukatīr
🌏 Tıvalap: maadır
🌏 Salırça: qaramañ
🌏 Xakastap: matır, alıp
🌏 Altaylap: baatır, alıp
🌏 Şor: alıp
🌍 Urumça: bağatır, batır (baatır)
🌍 Karajče: bahatyr (batyr)
🌍 Qrımçahça: bahatır, batır
🌏 Soyot: titim kîşî
🌏 Tofalap: bogatır, mergen''', reply_markup=markup_menu)
    elif message.text.lower() == "большой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "болшой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "большая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "большое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "крупный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "крупная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "крупное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "крупные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "big" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "large" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "büyük" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "большие":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰆𐰞𐰆𐰍
🇬🇧 English: big, large
🇷🇺 Русский: большой, крупный (-ая, -ое)
🇹🇷 Türkçe: büyük
🇦🇿 Türkcə: böyük, yekə, iri
🇹🇲 Türkmençe: uly, iri
🇺🇿 Oʻzbekcha: katta, buyuk, ulkan
🇰🇿 Qazaqşa: zor, ülken, iri
🇰🇬 Qırğızça: çoñ, iri, zor
Uyghurche: chong, yoghan, büyük, zor
Tatarça: zur, däw, ere
Başqortsa: ður, däw, ere
Çovaşla: pısok, mon (mono)
Qaraqalpaqsha: úlken, zor
Qırımtatarca: büyük, iri
Qumuqça: ullu, aslam
Qaraçay-Malqar:	ullu
Noğayşa: üyken
Sıbırca: ollo (ollı, ulu), äwgän, äri
Gagauzça: büük, iyri
Saqalıı: ulaqan, bödöñ
Dulgan-Hakalıı: ulakan, bödöñ
Tıvalap: ulug
Salırça: ullı, tā, tatıx
Xakastap: uluğ, îrem
Altay: caan (coon), qozır
Şor: uluğ, qozur
Urumça: büyük (beyük)
Karaj: bijik, ullu, iri, zor
Qrımçahça: buyuk, balaban
Soyot: ulığ
Tofalap: uluğ''', reply_markup=markup_menu)

    elif message.text.lower() == "брат" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бро" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bro" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kardeş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "erkek kardeş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "abi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ağabey" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "brother" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gardaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kardaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "братишка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "братишкин":
        bot.send_message(message.chat.id, '''
🐺 Old Turkic (bef. 13th c.): qarındaş, qadaş, aqa (older), eçi (older), ini (younger)
🇬🇧 English: brother
🇷🇺 Русский: брат [brat]
🇹🇷 Türkçe: kardeş (erkek kardeş), ağabey (older), abi (older)
🇦🇿 Türkcə: qardaş, ici (dialect), qada (dialect), çöçüy (dialect), lələ (dialect) (older), ağa (dialect) (older), ağadadaş (dialect) (older), dadaş (dialect) (older), qağa (dialect) (older), qaqa (informal), qaqaş (informal)
🇹🇲 Türkmençe: gardaş, dogan, aga (older), ini (younger)
🇺🇿 Oʻzbekcha: qardosh, birodar, aka (older), uka (younger)
🇰🇿 Qazaqşa: ağa (older), ini (younger)
🇰🇬 Qırğızça: bir tuuğan, uyalaş tuugan, ağa (older), ini (younger)
🌏 Uyghurche: qérindash (erkek qérindash), brader, aka (older), uka (younger), ini (younger)
🌍 Tatarça: bertuğan, abıy (abzıy) (older), ene (younger), qardäş (comrade)
🌍 Başqortsa: ir tuğan, ağay (older), ene (younger), qustı (younger)
🌍 Çovaşla: ar tovan, piççe (older), tete (dialect) (my older brother), şollom (my younger brother)
🌍 Qaraqalpaqsha: tuwısqan, aǵa (older), ini (younger)
🌍 Qırımtatarca: ağa (older), kadâ (younger), qardaş (younger)
🌍 Qumuqça: qardaş, ağa (older), ini (younger)
🌍 Qaraçay-Malqar: qarındaş (qarnaş)
🌍 Noğayşa: qardaş, ağa (older), ini (younger), bebe (younger)
🌏 Sıbırca: äkä (ağa, aqa) (older), ene (younger)
🌍 Gagauzça: batü (older), kardaş (younger)
🌏 Saqalī: ubay (older), bï (older), ini (younger), surus (towards sister)
🌏 Dulgan-Hakalī: tāy (older), ubay (older), balıs (younger)
🌏 Tıvalap: akıy (older), duñmay (younger)
🌏 Salırça: kaka (kaga) (older), ini (younger)
🌏 Xakastap: xarındas, abaa (older), tuñma (younger)
🌏 Altaylap: qarındaş, aqa (older), iyi (younger)
🌏 Şor: er qarındaş, aça (older), tuñma (younger)
🌍 Urumça: ğardaş, ağa (older), gada (younger)
🌍 Karajče: karyndaš (kardaš), aka (older)
🌍 Qrımçahça: aqay (ağa) (older), qardaş (younger)
🌏 Soyot: haqı (older), duñma (younger)
🌏 Tofalap: aha (older), duñma (younger)''', reply_markup=markup_menu)

    elif message.text.lower() == "be" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to be" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "будь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бывай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "olmak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ol" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "являйся" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "являться" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бывать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "быть":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): bol
🇬🇧 English: be
🇷🇺 Русский: будь, являйся
🇲🇳 Mongol: bolo
🇹🇷 Türkçe: ol
🇦🇿 Türkcə: ol
🇹🇲 Türkmençe: bol
🇺🇿 Oʻzbekcha: boʻl
🇰🇿 Qazaqşa: bol
🇰🇬 Qırğızça: bol
🌏 Uyghurche: bol
🌍 Tatarça: bul
🌍 Başqortsa: bul
🌍 Çovaşla: pul
🌍 Qaraqalpaqsha: bol
🌍 Qırımtatarca: ol
🌍 Qumuqça: bol
🌍 Qaraçay-Malqar: bol
🌍 Noğayşa: bol
🌏 Sıbırca: pul
🌍 Gagauzça: ol
🌏 Saqalī: buol
🌏 Dulgan-Hakalī: buol
🌏 Tıvalap: bol
🌏 Salırça: vol
🌏 Xakastap: pol
🌏 Altaylap: bol
🌏 Şor: pol
🌍 Urumça: ol (bol)
🌍 Karajče: ė, bol
🌍 Qrımçahça: ol
🌏 Soyot: bol
🌏 Tofalap: bol''', reply_markup=markup_menu)

    elif message.text.lower() == "в" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "во" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "in" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "-da" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "-de" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "+da" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "+de":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): -da/-dä/-ta/-tä
🇬🇧 English: in
🇷🇺 Русский: в
🇹🇷 Türkçe: -da/-de
🇦🇿 Türkcə: -da/-də
🇹🇲 Türkmençe: -da/-de
🇺🇿 Oʻzbekcha: -da
🇰🇿 Qazaqşa: -da/-de/-ta/-te
🇰🇬 Qırğızça: -da/-do/-de/-dö/-ta/-to/-te/-tö
🌏 Uyghurche: -da/-de/-ta/-te
🌍 Tatarça: -da/-dä
🌍 Başqortsa: -la/-lä/-da/-dä/-ta/-tä/-ða/-ðä
🌍 Çovaşla: -ra/-re, -ta/-te
🌍 Qaraqalpaqsha: -da/-de/-ta/-te
🌍 Qırımtatarca: -da/-de/-ta/-te
🌍 Qumuqça: -da/-de
🌍 Qaraçay-Malqar: -da/-de
🌍 Noğayşa: -da/-de/-ta/-te
🌏 Sıbırca: -ta/-tä
🌍 Gagauzça: -da/-de
🌏 Saqalī: ihiger
🌏 Dulgan-Hakalī: ihiger
🌏 Tıvalap: -da/-de/-ta/-te
🌏 Salırça: -da/-de/-ta/-te
🌏 Xakastap: -da/-de/-ta/-te
🌏 Altaylap: -da/-de/-ta/-te
🌏 Şor: -da/-de/-ta/-te
🌍 Urumça: -da/-dä (-da/-de/-ta/-te)
🌍 Karajče: -da/-de/-ta/-te
🌍 Qrımçahça: -da/-de/-ta/-te
🌏 Soyot: -da/-de/-ta/-te
🌏 Tofalap: -da/-de/-ta/-te''', reply_markup=markup_menu)
    elif message.text.lower() == "вася" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "василий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "basil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "basileios" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "vasiliy":
        bot.send_message(message.chat.id, '''🇬🇧 English: Basil
🇷🇺 Русский: Василий, Вася
🇹🇷 Türkçe: Basileios
🇦🇿 Türkcə: Basil, Vasili (Vasiliy)
🇹🇲 Türkmençe: Wasiliý
🇺🇿 Oʻzbekcha: Vasiliy
🇰🇿 Qazaqşa: Wasiliy
🇰🇬 Qırğızça: Vasiliy
Uyghurche: ???
Tatarça: Vasiliy
Başqortsa: Vasiliy
Çovaşla: Vacley, Macci
Qaraqalpaqsha: ???
Qırımtatarca: ???
Qumuqça: ???
Qaraçay-Malqar: Başil
Noğayşa: ???
Sıbırca: ???
Gagauzça: Vasiliy
Saqalī: ???
Dulgan-Hakalī: ???
Tıvalap: ???
Salırça: ???
Xakastap: ???
Altaylap: ???
Şor: ???
Urumça: ???
Karajče: ???
Qrımçahça: ???
Soyot: ???
Tofalap: ???''', reply_markup=markup_menu)
    elif message.text.lower() == "great" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "grand" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "великий" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "великая" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "великое" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "великие" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ulu" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yüce" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "велико":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰆𐰞𐰆𐰍
🇬🇧 English: great, grand
🇷🇺 Русский: великий (-ая, -ое)
🇹🇷 Türkçe: ulu, yüce
🇦🇿 Türkcə: ulu, uca
🇹🇲 Türkmençe: beýik, roýal, ullakan
🇺🇿 Oʻzbekcha: ulug', yirik
🇰🇿 Qazaqşa: ulı
🇰🇬 Qırğızça: uluu
Uyghurche: uluq
Tatarça: olı (oluğ), böyek
Başqortsa: olo, böyök
Çovaşla: aslo, çaplo, muxtavlo
Qaraqalpaqsha: ully
Qırımtatarca: ulu, yüce
Qumuqça: ullu, zor
Qaraçay-Malqar:	ullu
Noğayşa: ullı
Sıbırca: ülkän, püyük, azım
Gagauzça: ulu, azman
Saqalıı: ulū, sǖne
Dulğan-Hakalıı: ulakan
Tıvalap: ulug, öndür
Salırça: ullı (ulli, ol)
Xakastap: uluğ, îlbek
Altay: ulu
Şor: uluğ
Urumça: ulu, yiri, mağara, meğalı, mafir (mafif)
Karaj: ullu (ulu), zor
Qrımçahça: buyuk, balaban
Soyot: ulığ
Tofalap: ooda uluğ''', reply_markup=markup_menu)
    elif message.text.lower() == "вода" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "su" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "water" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "водный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "h20" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "h2o":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰽𐰆𐰉
🐺 Old Turkic (bef. 13th c.): sub (suğ, suv, suw)
🇬🇧 English: water
🇷🇺 Русский: вода
🇲🇳 Mongol: us
🇹🇷 Türkçe: su
🇦🇿 Türkcə: su
🇹🇲 Türkmençe: suw
🇺🇿 Oʻzbekcha: suv
🇰🇿 Qazaqşa: suw
🇰🇬 Qırğızça: suu
🌏 Uyghurche: su
🌍 Tatarça: su
🌍 Başqortsa: hıw
🌍 Çovaşla: şıv
🌍 Qaraqalpaqsha: suw
🌍 Qırımtatarca: suv
🌍 Qumuqça: suw
🌍 Qaraçay-Malqar: suw
🌍 Noğayşa: suw
🌏 Sıbırca: sıw
🌍 Gagauzça: su
🌏 Saqalī: uu
🌏 Dulgan-Hakalī: uu
🌏 Tıvalap: sug
🌏 Salırça: su
🌏 Xakastap: suğ
🌏 Altaylap: suu
🌏 Şor: suğ
🌍 Urumça: su
🌍 Karajče: suv (suj)
🌍 Qrımçahça: suv
🌏 Soyot: suğ
🌏 Tofalap: suğ''', reply_markup=markup_menu)

    elif message.text.lower() == "волк" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "волчица" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "wolf" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "börü" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurt" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "böri":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰋𐰇𐰼𐰃
🇬🇧 English: wolf
🇷🇺 Русский: волк
🇹🇷 Türkçe: kurt, börü
🇦🇿 Türkcə: canavar, qurd, börü
🇹🇲 Türkmençe: böri, gurt
🇺🇿 Oʻzbekcha: boʻri, qashqir
🇰🇿 Qazaqşa: böri, qasqır
🇰🇬 Qırğızça: börü, qarışqır
    Uyghurche: böre, qurt
    Tatarça: büre
    Başqortsa: büre
    Çovaşla: kaşkor
    Qaraqalpaqsha: bo'ri, qasqır
    Qırımtatarca: börü, qaşqır, qurt
    Qumuqça: börü
    Saqalī: börö
    Qaraçay-Malqar: börü, canlı
    Tıvalap: börü
    Gagauzça: canavar, kurd
    Noğayşa: böri
    Salırça: puri (pore, pure, pūre, pura)
    Xakastap: püür
    Sıbırca: püre
    Altay: börü
    Şor: pörü
    Dolgan: börö
    Urumça: börü, canavar
    Karaj: bioriu
    Qrımçahça: boru, qaşqır
    Soyot: börî, köqqay, çelär (celär)
    Tofalap: börü, dağ ıtı''', reply_markup=markup_menu)

    elif message.text.lower() == "вошь" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вша" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вши" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "louse" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bit" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pediculus":
        bot.send_message(message.chat.id, '''
🇬🇧 English: louse
🇷🇺 Русский: вошь
🇹🇷 Türkçe: bit
🇦🇿 Türkcə: bit, siñək (dialect), yovşaq (dialect), saqırtqa (dialect)
🇹🇲 Türkmençe: bit
🇺🇿 Oʻzbekcha: bit
🇰🇿 Qazaqşa: biyt
🇰🇬 Qırğızça: bit
    Uyghurche: pit
    Tatarça: bet
    Başqortsa: bet
    Çovaşla: pıyto (pıtyo)
    Qaraqalpaqsha: biyt
    Qırımtatarca: bit
    Qumuqça: bit
    Qaraçay-Malqar:	bit (bi)
    Noğayşa: biyt
    Sıbırca: pet
    Gagauzça: bit
    Saqalī: bıt
    Dulgan-Hakalī: bıt
    Tıvalap: bıt
    Salırça: pit
    Xakastap: pit
    Altaylap: biyt
    Şor: ???
    Urumça: bit (pit)
    Karajče: bit
    Qrımçahça: bit
    Soyot: bıt
    Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.lower() == "каждый" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "всё" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "каждая" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "каждое" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "all" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "every" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "все" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "her" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tüm" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bütün" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hep" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "everybody" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "everyone":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰉𐰺
🇬🇧 English: I. all, every II. everybody, everyone
🇷🇺 Русский: I. всё, каждый (каждая, каждое) II. все
🇹🇷 Türkçe: I. tüm, bütün, hep, her II. herkes, hepsi
🇦🇿 Türkcə: I. bütün, hər II. hamı, hər kəs
🇹🇲 Türkmençe: I. bary, hemme, ähli, her II. hemmeler, hemme kişi
🇺🇿 Oʻzbekcha: I~II barcha, hamma, butun, bari, borliq, har
🇰🇿 Qazaqşa: I. bäri, bükil, barlıq, barşa, er II. är adam
🇰🇬 Qırğızça: I. baarı, bardıq, bütkül, ar II. ar bir adam
    Uyghurche: I. hemme, barche, pütün, barliq, her II. hemmisi, barliq kishiler, hemme kishi
    Tatarça:	I. böten, barı, hämmä, här II. härkem
    Başqortsa: I. bötä, här II. här kem
    Çovaşla: I. pötöm, pur, purte, kaşni II. pulan, pur cın ta, kaşni cın
    Qaraqalpaqsha: I. barlıq, pútkil, pútin, hár II. hár kim, hár adam
    Qırımtatarca: I. bütün, ep, er II. epi, episi, er kes, er kim
    Qumuqça: I. barı, bütün, har [гьар] II. har kim, har-birisi
    Qaraçay-Malqar:	I. barı, bitew II. kim da
    Noğayşa: I. bäri, sawlay är II. är kim, är birew
    Sıbırca: I. keläñ, kölle, pötä, pötörä, är II. keläñ, tulay (tōlay), är kem (är kim)
    Gagauzça: I. hep, her II. hepsi, herkes (her kez)
    Saqalıı: I. barı, bütün (büttǖn), āyı II. kim dağanı, qas bïrdï
    Dulgan-Hakalıı: I. barı, bütün, āyı II. barı
    Tıvalap: I. bügü, xamık, dögere II. şuptuzu, bügüdezi, şuptu kijiler, bügü kijiler
    Salırça: I. neñ, neñkisi (neñgisi), hemme (heme), her II. tunya (tünya, tönya), neñleñ, hämmä (heme), çoşı
    Xakastap: I. pray, tîksi, tooza II. polğanı la, polğan na kizi
    Altay: I. bastıra, üze II. qajızı, qajı la, qandıy la
    Şor: I. tügeze, tooza, saya II. parçazı, parçın kiji
    Urumça: I. bütün, barı, cemi II. äp, epsi, cemisi
    Karaj: I. biutiuń (butun, bitin, bitiuń), bar, har II. hepisi, har biri, har kiši
    Qrımçahça: I. butun, cumle, er, ep II. erkez, epsı
    Soyot: I. barşa, bügedä, bolğan, tuşqan II. kîşî bolğan
    Tofalap: I. barşa, tödi (tödü), sanı, bolğan, tuşqan II. kîşî bolğan, kîşî sanı''', reply_markup=markup_menu)

    elif message.text.lower() == "вы" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "you" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "siz" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sizler" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "you all" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "you guys" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "y'all":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰾𐰃𐰔
🇬🇧 English: you (plural) (write "sen" for singular)
🇷🇺 Русский: вы
🇹🇷 Türkçe: siz, sizler
🇦🇿 Türkcə: siz, sizler
🇹🇲 Türkmençe: siz, sizler
🇺🇿 Oʻzbekcha: siz, sizlar, senlar
🇰🇿 Qazaqşa: siz, sizder, sender
🇰🇬 Qırğızça: siz, sizder, siler
    Uyghurche: siz, sizler, siler, senler
    Tatarça: sez, sezlär
    Başqortsa: heð, heððär
    Çovaşla: esir
    Qaraqalpaqsha: siz, sizler
    Qırımtatarca: siz, sizler
    Qumuqça: siz
    Qaraçay-Malqar:	siz
    Noğayşa: siz
    Sıbırca: ses (sez), seslär (sizlär)
    Gagauzça: siz, sizler
    Saqalıı: ehigi
    Hakalıı (Dulğan): en
    Tıvalap: siler
    Salırça: seler (sälär, siler)
    Xakastap: sirer
    Altay: sler
    Şor: siler
    Urumça: siz
    Karaj: siź
    Qrımçahça: sız
    Soyot: siler (silär, sler, slär), slärlär
    Tofalap: siler (sler)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "где" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nerede" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "where" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hani":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰣𐰃
🇬🇧 English: where
🇷🇺 Русский: где
🇲🇳 Mongol: khaana
🇹🇷 Türkçe: nerede, hani
🇦🇿 Türkcə: harada, hanı, hayızda (dialect)
🇹🇲 Türkmençe: nirede
🇺🇿 Oʻzbekcha: qayerda, qayda
🇰🇿 Qazaqşa: qayda, qay jerde, käne
🇰🇬 Qırğızça: qayda, qana
    Uyghurche: nede, qay yerde, qeni
    Tatarça: qayda
    Başqortsa: qayða
    Çovaşla: octa
    Qaraqalpaqsha: qayda
    Qırımtatarca: qayda
    Qumuqça: qayda
    Qaraçay-Malqar:	qayda
    Noğayşa: qayda
    Sıbırca: qayta, qayısta, qalı
    Gagauzça: neredä, ani
    Saqalıı: qanna
    Dulgan-Hakalıı: kanna
    Tıvalap: kayda
    Salırça: qayda (qayta, kayta, qāta, qāte), qāle (kala, kāla, kālā, q'āle)
    Xakastap: xayda
    Altay: qayda
    Şor: qayda
    Urumça: nerede (nerada), nas yerde, ne yerde, xayda
    Karaj: kajda (kaa)
    Qrımçahça: qayerde, qayda
    Soyot: qayda, cüdä (cüde, jüdä, jüde)
    Tofalap: qayda, qaê, cüde''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "глаза" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "моргало" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "глаз" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "göz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eye" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eyes":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰚𐰇𐰔
🐺 Old Turkic (bef. 13th c.): köz, qaraq ("eye", "eyeball")
🇬🇧 English: eye
🇷🇺 Русский: глаз
🇹🇷 Türkçe: göz, karak (acrhaism)
🇦🇿 Türkcə: göz
🇹🇲 Türkmençe: göz, garak
🇺🇿 Oʻzbekcha: koʻz
🇰🇿 Qazaqşa: köz
🇰🇬 Qırğızça: köz
    Uyghurche: köz
    Tatarça: küz
    Başqortsa: küð
    Çovaşla: kuc
    Qaraqalpaqsha: kóz
    Qırımtatarca: köz
    Qumuqça: göz
    Qaraçay-Malqar:	köz
    Noğayşa: köz
    Sıbırca: küs
    Gagauzça: göz
    Saqalī: qaraq
    Dulgan-Hakalī: karak
    Tıvalap: karak
    Salırça: köz
    Xakastap: xarax
    Altaylap: kös
    Şor: qaraq
    Urumça: göz (köz)
    Karajče: kioź
    Qrımçahça: köz (göz)
    Soyot: qaraq
    Tofalap: qaraq''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "год" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лет" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "year" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yıl" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yil" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "years":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰘𐰃𐰞
🐺 Old Turkic: yıl (yīl)
🇬🇧 English: year
🇷🇺 Русский: год
🇲🇳 Mongol: jil
🇹🇷 Türkçe: yıl, sene
🇦🇿 Türkcə: il, sənə
🇹🇲 Türkmençe: ýyl
🇺🇿 Oʻzbekcha: yil
🇰🇿 Qazaqşa: jıl
🇰🇬 Qırğızça: jıl
    Uyghurche: yil
    Tatarça: yıl
    Başqortsa: yıl
    Çovaşla: cul
    Qaraqalpaqsha: jıl
    Qırımtatarca: yıl, sene
    Qumuqça: yıl
    Qaraçay-Malqar:	jıl
    Noğayşa: yıl
    Sıbırca: yıl
    Gagauzça: yıl
    Saqalī: sıl, cıl
    Dulgan-Hakalī: cıl
    Tıvalap: çıl
    Salırça: yıl (yil)
    Xakastap: çıl
    Altaylap: cıl
    Şor: çıl
    Urumça: el (yıl)
    Karajče: jyl (il)
    Qrımçahça: yıl, sene
    Soyot: çıl (cıl)
    Tofalap: çıl''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "голова" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "head" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kafa" \
        or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "baş":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰉𐱁
🐺 Old Turkic: baş
🇬🇧 English: head
🇷🇺 Русский: голова
🇹🇷 Türkçe: baş, kafa
🇦🇿 Türkcə: baş
🇹🇲 Türkmençe: baş
🇺🇿 Oʻzbekcha: bosh
🇰🇿 Qazaqşa: bas
🇰🇬 Qırğızça: baş
    Uyghurche: bash
    Tatarça: baş
    Başqortsa: baş
    Çovaşla: puc
    Qaraqalpaqsha: bas
    Qırımtatarca: baş
    Qumuqça: baş
    Qaraçay-Malqar: baş
    Noğayşa: bas
    Sıbırca: paş
    Gagauzça: baş, kafa
    Saqalī: bas, töbö
    Dulgan-Hakalī: bas, meńï
    Tıvalap: baş
    Salırça: baş (paş)
    Xakastap: pas
    Altaylap: baş
    Şor: paş
    Urumça: baş
    Karajče: baš (bas)
    Qrımçahça: baş
    Soyot: baş
    Tofalap: baş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dağ" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dag" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гора" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mountain":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱃𐰍
🇬🇧 English: mountain
🇷🇺 Русский: гора
🇹🇷 Türkçe: dağ
🇦🇿 Türkcə: dağ, tov (dialect), təll (dialect)
🇹🇲 Türkmençe: dag
🇺🇿 Oʻzbekcha: togʻ
🇰🇿 Qazaqşa: taw
🇰🇬 Qırğızça: too
    Uyghurche: tagh
    Tatarça: taw
    Başqortsa: taw
    Çovaşla: tu
    Qaraqalpaqsha: taw
    Qırımtatarca: dağ, bayır, qır
    Qumuqça: taw
    Qaraçay-Malqar: taw
    Noğayşa: taw
    Sıbırca: taw
    Gagauzça: bayır, daa (meaning may vary)
    Saqalī: qaya
    Dulgan-Hakalī: kaya
    Tıvalap: dag
    Salırça: tağ
    Xakastap: tağ
    Altaylap: tuu, qır
    Şor: tağ
    Urumça: dağ (tav)
    Karajče: tav
    Qrımçahça: dağ, bayır, qır
    Soyot: dağ
    Tofalap: dağ (tağ)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "грузин" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "грузинка" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "грузинский" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "грузинская" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "грузинское" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "georgian" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gürcü" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gürci":
        bot.send_message(message.chat.id, '''
🇬🇧 English: georgian
🇷🇺 Русский: грузин, грузинка
🇹🇷 Türkçe: gürcü
🇦🇿 Türkcə: gürcü
🇹🇲 Türkmençe: gürjü
🇺🇿 Oʻzbekcha: gurji
🇰🇿 Qazaqşa: gürji
🇰🇬 Qırğızça: gruzin
🌏 Uyghurche: gruzin
🌍 Tatarça: görci
🌍 Başqortsa: gruzin
🌍 Çovaşla: gruzin, kartvel
🌍 Qaraqalpaqsha: gruzin, gúrji
🌍 Qırımtatarca: gürci
🌍 Qumuqça: gürjü
🌍 Qaraçay-Malqar: gürjülü
🌍 Noğayşa: gürji, gruzin
🌏 Sıbırca: görji
🌍 Gagauzça: gürcü, gruzin
🌏 Saqalī: gruzin
🌏 Dulgan-Hakalī: gruzin
🌏 Tıvalap: gruzin
🌏 Salırça: gürci
🌏 Xakastap: gruzîn
🌏 Altaylap: gruzin
🌏 Şor: gruzin
🌍 Urumça: gürcü (gürci)
🌍 Karajče: giurdži
🌍 Qrımçahça: gürci
🌏 Soyot: gruzîn
🌏 Tofalap: gruzîn''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sakartvelo" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "грузия" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gürcistan" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gürcüstan" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "georgia" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "georgıa":
        bot.send_message(message.chat.id, '''
🇬🇧 English: Georgia
🇷🇺 Русский: Грузия [ɡrˈuzʲɪjə]
🇹🇷 Türkçe: Gürcistan (Gürcüstan)
🇦🇿 Türkcə: Gürcüstan
🇹🇲 Türkmençe: Gürjüstan
🇺🇿 Oʻzbekcha: Gurjiston, Gruziya
🇰🇿 Qazaqşa: Gürjistan, Gruziya
🇰🇬 Qırğızça: Gruziya
🌏 Uyghurche: Gruziye
🌍 Tatarça: Görcistan
🌍 Başqortsa: Gruziya
🌍 Çovaşla: Gruzi
🌍 Qaraqalpaqsha: Gruziya, Gúrjistan
🌍 Qırımtatarca: Gürcistan
🌍 Qumuqça: Gürjüstan
🌍 Qaraçay-Malqar: Gürjü
🌍 Noğayşa: Gürjistan, Gruziya
🌏 Sıbırca: Görjistan
🌍 Gagauzça: Gürcüstan, Gruziya
🌏 Saqalī: Gruziya
🌏 Dulgan-Hakalī: Gruziya
🌏 Tıvalap: Gruziya
🌏 Salırça: Gürcistan
🌏 Xakastap: Gruzîya
🌏 Altaylap: Gruziya
🌏 Şor: Gruziya
🌍 Urumça: Gürcüstan (Gürcistan)
🌍 Karajče: Giurdžistan
🌍 Qrımçahça: Gürcistan
🌏 Soyot: Gruzîya
🌏 Tofalap: Gruzîya
in Georgian: Sakartvelo''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "да" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yes" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yeah" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "evet" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yep" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yea":
        bot.send_message(message.chat.id, '''🐺 Old Turkic: evät (emät, yemät), yah
🇬🇧 English: yes
🇷🇺 Русский: да
🇹🇷 Türkçe: evet
🇦🇿 Türkcə: hə (informal), bəli (formal)
🇹🇲 Türkmençe: hawa
🇺🇿 Oʻzbekcha: ha
🇰🇿 Qazaqşa: iyä, ja (dialect)
🇰🇬 Qırğızça: ooba
    Uyghurche: he (he'e)
    Tatarça: äye
    Başqortsa: äye
    Çovaşla: iye
    Qaraqalpaqsha: awa
    Qırımtatarca: e, ebet
    Qumuqça: dür
    Qaraçay-Malqar: xaw (xo)
    Noğayşa: äyi, äşe (äşi)
    Sıbırca: an, anan, yä, bäli
    Gagauzça: ölä, ha, evet, ya
    Saqalī: ēq, söp, onnuk
    Dulgan-Hakalī: höp, höpkö
    Tıvalap: iye
    Salırça: ira (irar), iter
    Xakastap: ya
    Altaylap: eye
    Şor: eze
    Urumça: xä, ağa
    Karajče: ė (he)
    Qrımçahça: e
    Soyot: şêêñ
    Tofalap: şêêñ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "2" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iki" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "two" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "два" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "две" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "двое":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰚𐰃 
🇬🇧 English: two
🇷🇺 Русский: два, две, двое
🇹🇷 Türkçe: iki
🇦🇿 Türkcə: iki
🇹🇲 Türkmençe: iki
🇺🇿 Oʻzbekcha: ikki
🇰🇿 Qazaqşa: eki
🇰🇬 Qırğızça: eki
    Uyghurche: ikki
    Tatarça: ike
    Başqortsa: ike
    Çovaşla: ikö (ik, ikkö)
    Qaraqalpaqsha: eki
    Qırımtatarca: eki
    Qumuqça: eki
    Qaraçay-Malqar: eki
    Noğayşa: eki
    Sıbırca: ikä
    Gagauzça: iki
    Saqalıı: ikki
    Tıvalap: iyi
    Salırça: iki (işki, ikki)
    Xakastap: iki
    Altay: eki
    Şor: iygi
    Dolgan: ikki
    Urumça: eki (iki)
    Karaj: ėki
    Qrımçahça: ekı
    Soyot: îhî
    Tofalap: îhî''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "december" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "decembre" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "aralık" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "aralik" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "декабрь" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dekabr":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: december
🇷🇺 Русский: декабрь
🇹🇷 Türkçe: aralık
🇦🇿 Türkcə: dekabr, qanuni-əvvəl
🇹🇲 Türkmençe: bitaraplyk
🇺🇿 Oʻzbekcha: dekabr, jadiy
🇰🇿 Qazaqşa: jeltoqsan, jädiy
🇰🇬 Qırğızça: beştin ayı
    Uyghurche: künek
    Tatarça: dikäber, keräw
    Başqortsa: aqyulay
    Çovaşla: raştav
    Qaraqalpaqsha: dekabr, jeddi
    Qırımtatarca: dekabr, aralıq
    Qumuqça: dekabr, tunlu, qaraqış
    Qaraçay-Malqar: dekabr, endirewük
    Noğayşa: dekabr, qarağıs
    Sıbırca: dekabr, cätte (cattı), ollo sıwıq
    Gagauzça: kırım (kıran)
    Saqalī: aqsınńı
    Dulgan-Hakalī: karaña kıhın
    Tıvalap: on iyi
    Salırça: onikinci
    Xakastap: dekabr
    Xakastap (Sağay): uluğ xırlas
    Xakastap (Pîltir): uluğ xırlas
    Xakastap (Xaas): alay
    Altaylap: dekabr, canar
    Şor: iyginçi añ, iyginçi kiçig qırlaş
    Urumça: dekembrioz, azıx
    Karajče: (they use Karaim calendar)
    Qrımçahça: dekabr
    Soyot: dekabr
    Tofalap: sooq''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "день" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "днем" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "днём" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "day" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gün" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "daytime" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дневное время" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "day time" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gündüz":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰾. 𐰚𐰇𐰤 𐰾𐰾. 𐰚𐰇𐰦𐰔 (𐰚𐰇𐰤𐱅𐰔)
🐺 Old Turkic: I. kün II. kündüz (küntüz)
🇬🇧 English: I. day II. daytime
🇷🇺 Русский: I. день II. днём (дневное время)
🇹🇷 Türkçe: I. gün II. gündüz (ışık veren gün sonucu için "güneş" girin)
🇦🇿 Türkcə: I. gün II. gündüz
🇹🇲 Türkmençe: I. gün II. gündiz
🇺🇿 Oʻzbekcha: I. kun II. kunduz
🇰🇿 Qazaqşa: I. kün II. kündiz
🇰🇬 Qırğızça: I. kün II. kündüz
    Uyghurche: I. kün II. kündüz
    Tatarça: I. kön II. köndez
    Başqortsa: I. kön II. köndöð
    Çovaşla: I. kun, kontor II. kunön, kontorla
    Qaraqalpaqsha: I. kún II. kúndiz
    Qırımtatarca: I. kün II. kündüz
    Qumuqça: I. gün II. gündüz
    Qaraçay-Malqar: I. kün II. kündüz
    Noğayşa: I. kün II. kündiz
    Sıbırca: I. kön (kün) II. köndöz (kündüz)
    Gagauzça: I. gün II. gündüz
    Saqalī: I. kün II. künüs
    Dulgan-Hakalī: I. kün II. künüs
    Tıvalap: I. xün II. xündüs
    Salırça: I. kün II. küntiz (kuncisı)
    Xakastap: I. kün II. kündüs, künörte
    Altaylap: I. kün II. tüşte
    Şor: I. kün II. kündüs
    Urumça: I. gün (kün) II. gündüz (kündüz)
    Karajče: I. kiuń II. kiuńdiuź
    Qrımçahça: I. kün (gün) II. künduz
    Soyot: I. hün (kün, gün) II. kündüs (hündis)
    Tofalap: I. hün (kün) II. hündüs (kündüs)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дерево" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "древо" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tree" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "wood" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ağaç":\
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰃𐰍𐰲
🇬🇧 English: I. tree II. wood
🇷🇺 Русский: дерево
🇹🇷 Türkçe: ağaç, dıraht (archaism)
🇦🇿 Türkcə: ağac, dirəxt (poetry)
🇹🇲 Türkmençe: agaç, daragt
🇺🇿 Oʻzbekcha: yogʻoch, daraxt
🇰🇿 Qazaqşa: ağaş
🇰🇬 Qırğızça: jığaç, daraq
    Uyghurche: yaghach, derex
    Tatarça:	ağaç
    Başqortsa: ağas
    Çovaşla: yıvoc
    Qaraqalpaqsha: agʻash
    Qırımtatarca: terek, ağaç (archaism)
    Qumuqça: I. terek II. ağaç
    Qaraçay-Malqar:	I. terek II. ağaç
    Noğayşa: I. terek II. ağaş
    Sıbırca: ağac
    Gagauzça: aaç, fidan
    Saqalıı: mas
    Dulgan-Hakalıı: mas
    Tıvalap: ıyaş
    Salırça: ağaç (ağaş), tal
    Xakastap: ağas
    Altay: ağaş
    Şor: ağaş
    Urumça: ağaç, derek (tirek, terek, direk)
    Karajče: ahač (ahac), direk (terek)
    Qrımçahça: I. dırek II. ağaç
    Soyot: nâş (nâc)
    Tofalap: neş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "long" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uzun" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "длинный" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "длиный" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "длинная" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "длинно" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "длинные" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "длинное":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰆𐰔𐰣
🇬🇧 English: long
🇷🇺 Русский: длинный (-ая, -ое)
🇹🇷 Türkçe: uzun
🇦🇿 Türkcə: uzun
🇹🇲 Türkmençe: uzyn
🇺🇿 Oʻzbekcha: uzun
🇰🇿 Qazaqşa: uzın
🇰🇬 Qırğızça: uzun
    Uyghurche: uzun
    Tatarça: ozın
    Başqortsa: oðon
    Çovaşla: vorom
    Qaraqalpaqsha: uzın
    Qırımtatarca: uzun
    Qumuqça: uzun
    Qaraçay-Malqar:	uzun, uzaq
    Noğayşa: uzın
    Sıbırca: oson (osson)
    Gagauzça: uzun
    Saqalıı: uhun
    Dulğan-Hakalıı: uhun
    Tıvalap: uzun
    Salırça: uzın, coñ
    Xakastap: uzun
    Altay: uzun
    Şor: uzun
    Urumça: uzun
    Karaj: uzun, uzach
    Qrımçahça: uzun
    Soyot: uzun (uzın)
    Tofalap: uzun''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иной" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иная" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иное" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "прочий" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "прочее" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "прочие" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "другой" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "другая" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "other" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "прочая" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "öbür" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "diğeri" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "diğer" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "başka" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "başkası" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "another":
        bot.send_message(message.chat.id, '''
🇬🇧 English: other
🇷🇺 Русский: другой, иной, прочий (-ая, -ое)
🇹🇷 Türkçe: başka, öbür, diğer
🇦🇿 Türkcə: başqa, ayrı, o biri, özgə, digər
🇹🇲 Türkmençe: başga, aýry, özge, beýleki
🇺🇿 Oʻzbekcha: boshqa, g'ayri, o'zga
🇰🇿 Qazaqşa: basqa, özge, böten
🇰🇬 Qırğızça: başqa, bötön
    Uyghurche: bashqa, özge
    Tatarça: başqa, bütän
    Başqortsa: başqa, bütän
    Çovaşla: urox, tepör (tepöri)
    Qaraqalpaqsha: basqa, bóten
    Qırımtatarca: başqa, ğayrı, o biri, diger
    Qumuqça: başğa, özge
    Qaraçay-Malqar:	başxa, ol biri, özge
    Noğayşa: basqa, özge
    Sıbırca: paşqa, üzkä, üñgä
    Gagauzça: başka, öbür
    Saqalıı: atın, tuspa
    Dulğan-Hakalıı: atın, horok
    Tıvalap:	başka, baza bir, öske
    Salırça: paşqa, ārtıncı, māyi
    Xakastap: pasxa
    Altay: başqa, öskö
    Şor: paşqa, tigi
    Urumça: öbür, ayrı, başxa
    Karaj: bašcha, öźgia, obiri
    Qrımçahça: başqa, öbır, oñğaraq
    Soyot: başqa, öske (öskö), ındıı
    Tofalap: başqa, öske, ındıı''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жена" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "wife" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "karı" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "avrat" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eş" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "zevce":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰆𐰨𐰖, 𐰴𐱃𐰆𐰣
🇬🇧 English: wife
🇷🇺 Русский: жена
🇹🇷 Türkçe: karı, avrat, eş, zevce
🇦🇿 Türkcə: arvad, əyal, zövcə, qarı
🇹🇲 Türkmençe: aýal, keýwany
🇺🇿 Oʻzbekcha: xotin, ayol
🇰🇿 Qazaqşa: äyel, qatın
🇰🇬 Qırğızça: ayal, qatın
    Uyghurche: xotun, ayal
    Tatarça: xatın
    Başqortsa: qatın, bisä
    Çovaşla: arom
    Qaraqalpaqsha: hayal, qatın
    Qırımtatarca: apay, zevce, apaqay (dialect), qarı (dialect)
    Qumuqça: qatın
    Qaraçay-Malqar:	qatın, üy biyçe, üydegi
    Noğayşa: xatın, pişe
    Sıbırca: picä, qatın, öygeşe (üwkeje)
    Gagauzça: karı, avrat (avrad)
    Saqalıı: oyoq
    Dulğan-Hakalıı: caktar
    Tıvalap: kaday, amdıı kiji
    Salırça: kiyin (keyn)
    Xakastap: îpçizi
    Altay: emegen, ej 
    Şor: emdegi, qat, epçi
    Urumça: xarı, xatın (xatun), tisexli
    Karajče: katyn (chatyn)
    Qrımçahça: avrad, qarı, hatın
    Soyot: qurhayaq, öğdää
    Tofalap: qorhınâq, öğdääkîî (öğdääsi), hodeêm''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "женщина" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "woman" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "women" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kadın":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐱃𐰆𐰣
🇬🇧 English: woman
🇷🇺 Русский: женщина
🇹🇷 Türkçe: kadın
🇦🇿 Türkcə: qadın, arvad
🇹🇲 Türkmençe: zenan, aýal
🇺🇿 Oʻzbekcha: ayol, xotin
🇰🇿 Qazaqşa: äyel, qatın
🇰🇬 Qırğızça: ayal
    Uyghurche: ayal, xotun
    Tatarça: xatın, xatın-qız, xatın-keşe
    Başqortsa: qatın, qatın-qıð
    Çovaşla: xörarom
    Qaraqalpaqsha: hayal, qatın
    Qırımtatarca: qadın
    Qumuqça: qatıngişi
    Qaraçay-Malqar:	tişirıw
    Noğayşa: qısqayaqlı, xatın-qız
    Sıbırca: qatın, picä
    Gagauzça: karı, avrad (avrat), kadın
    Saqalıı: jaqtar
    Dulğan-Hakalıı: jaktar
    Tıvalap: xereejen
    Salırça: qatın
    Xakastap: îpçi, xat
    Altay: üy kiji
    Şor: tiji kiji
    Urumça: xatun (xatın), xısxayaxlı (xısayaxlı), evret (avret)
    Karajče: katyn (chatyn), katyn kiši, kary
    Qrımçahça: hatın
    Soyot: qaday, qaday kîşî, qurhayaq, epşi, epşi kîşî
    Tofalap: qorhınâq, epşi kîşî, pılaattığ kîşî, öğdääkîî''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "animal" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hayvan" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "животное" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "животные" \
         or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фауна":
        bot.send_message(message.chat.id, '''
🇬🇧 English: animal
🇷🇺 Русский: животное
🇹🇷 Türkçe: hayvan
🇦🇿 Türkcə: heyvan
🇹🇲 Türkmençe: haýwan
🇺🇿 Oʻzbekcha: hayvon
🇰🇿 Qazaqşa: haywan (aywan), janıwar
🇰🇬 Qırğızça: ayban, janıbar
    Uyghurche: haywan, janivar
    Tatarça: xaywan
    Başqortsa: xaywan
    Çovaşla: çörçun, vılyox-çörlöx
    Qaraqalpaqsha: haywan
    Qırımtatarca: ayvan
    Qumuqça: hayvan
    Qaraçay-Malqar:	xayıwan, janıwar
    Noğayşa: aywan, yanuwar
    Sıbırca: xäywan, yännek
    Gagauzça: hayvan
    Saqalıı: qaramay
    Dulğan-Hakalıı: hüöhü
    Tıvalap: amıtan
    Salırça: hayvan
    Xakastap: jîvotnay
    Altaylap: tındu
    Şor: mal-quş (only livestock or pet), añ-quş (only wild animal)
    Urumça: xayvan (ayvan), canavar
    Karajče: hajvan
    Qrımçahça: ayvan
    Soyot: adığuusın
    Tofalap: hoyluğa (hoylığa)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yıldız" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yildiz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "star" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "звезда" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "звёзды" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "звездный":
        bot.send_message(message.chat.id, '''
🐺 Old Turkic (bef. 13th c.): yıldız (yulduz, yūltus) (also means "planet"), şıryu
🇬🇧 English: star
🇷🇺 Русский: звезда [zvezda]
🇹🇷 Türkçe: yıldız
🇦🇿 Türkcə: ulduz
🇹🇲 Türkmençe: ýyldyz
🇺🇿 Oʻzbekcha: yulduz
🇰🇿 Qazaqşa: juldız
🇰🇬 Qırğızça: jıldız
🌏 Uyghurche: yultuz
🌍 Tatarça: yoldız
🌍 Başqortsa: yondoð
🌍 Çovaşla: coltor
🌍 Qaraqalpaqsha: juldız
🌍 Qırımtatarca: yıldız
🌍 Qumuqça: yulduz
🌍 Qaraçay-Malqar: julduz
🌍 Noğayşa:	yuldız
🌏 Sıbırca: yoltos
🌍 Gagauzça: yıldız
🌏 Saqalī: sulus
🌏 Dulgan-Hakalī: hulus
🌏 Tıvalap: sıldıs
🌏 Salırça: yultus
🌏 Xakastap: çıltıs
🌏 Altaylap: cıldıs
🌏 Şor: çıltıs
🌍 Urumça: yıldız (eldız)
🌍 Karajče: julduz (jolduz, jyldyz, juldus)
🌍 Qrımçahça: yıldız
🌏 Soyot: sıltıs
🌏 Tofalap: sıltıs''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "звонить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "aramak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "telefon etmek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çağrı yapmak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to ring up" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ring up" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "telefon et" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çağri yap" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çağrı yap" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "позвони" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "звони" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ring up" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to phone":
        bot.send_message(message.chat.id, '''
🇬🇧 English: ring up, call, phone
🇷🇺 Русский: позвони (по телефону), сделай звонок
🇹🇷 Türkçe: ara, telefon et, çağrı yap
🇦🇿 Türkcə: zəng et, yığ
🇹🇲 Türkmençe: jaň et, telefon et
🇺🇿 Oʻzbekcha: zang ur, telefon qil, telefon qoq
🇰🇿 Qazaqşa: (telefon) soq, koŋır
🇰🇬 Qırğızça: telefon ur
🌏 Uyghurche: téléfon qil, téléfon qal, téléfon soq
🌍 Tatarça: şaltırat
🌍 Başqortsa: şıltırat
🌍 Çovaşla: telefonpa şonkoravla, şonkortattar
🌍 Qaraqalpaqsha: telefon ur, telefon ber
🌍 Qırımtatarca: telefon et
🌍 Qumuqça: telefon et
🌍 Qaraçay-Malqar: telefon bla söleş
🌍 Noğayşa: tel soq (telefon soq)
🌏 Sıbırca: telefonnan cannat
🌍 Gagauzça: telefonu aç, telefon et
🌏 Saqalī: telefonnā, sobuonnā, zvonoktā
🌏 Dulgan-Hakalī: zvonuoktā
🌏 Tıvalap: dolgaar, telefonna
🌏 Salırça: dienxua vur
🌏 Xakastap: sığdırat
🌏 Altaylap: telefon soq, telefonğo aldır
🌏 Şor: ???
🌍 Urumça: lafet telefonnan
🌍 Karajče: telefon ėt, čialma kulačla
🌍 Qrımçahça: telefon et
🌏 Soyot: telefonna
🌏 Tofalap: telefonna''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "здесь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "here" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тут" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тута" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "burada" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bura" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "манда" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "burda" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "burası":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰉𐰆𐰦𐰀, 𐰉𐰆𐰘𐰼𐰓𐰀
🇬🇧 English: here
🇷🇺 Русский: здесь, тут
🇹🇷 Türkçe: burada, bura, burası
🇦🇿 Türkcə: burada (burda), bura
🇹🇲 Türkmençe: şu taýda, onda, bäri
🇺🇿 Oʻzbekcha: bu yerda, bu yoqda, bu yonda
🇰🇿 Qazaqşa: munda, osında, osı jerde
🇰🇬 Qırğızça: bul jerde, mında
    Uyghurche: bu yerde, meshede, mana
    Tatarça:	monda, biredä, bu cirdä
    Başqortsa: bında, oşonda
    Çovaşla: kunta, cakonta
    Qaraqalpaqsha: bunda, bul jerde
    Qırımtatarca: mında, bu yerde, şu yerde, bu yaqta
    Qumuqça: munda, şunda
    Qaraçay-Malqar:	mında, bılayda (blayda)
    Noğayşa: munda
    Sıbırca: mınta, puyta, pura (para, bōra)
    Gagauzça: burada, burası, şura, şurası
    Saqalıı: manna
    Dulğan-Hakalıı: manna
    Tıvalap: mında, bo çerde
    Salırça: munda (mınta, mında)
    Xakastap: mında
    Altay: mında
    Şor: mında
    Urumça: mında (bunda), biyan, biyax, burada, burası
    Karaj: bunda (mynda, munda, muna), bu yakta, bierie
    Qrımçahça: mında (bunda), burada
    Soyot: mında, maa, bortta
    Tofalap: mında, bortta''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "змей" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "змея" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yilan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yılan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "snake" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "змий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "serpens" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "serpentis" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "serpent":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰘𐰃𐰞𐰣 (𐰖𐰃𐰞𐰣)
🇬🇧 English: snake, serpent
🇷🇺 Русский: змея, змей
🇹🇷 Türkçe: yılan
🇦🇿 Türkcə: ilan, şan (dialect), yatağan (dialect)
🇹🇲 Türkmençe: ýylan
🇺🇿 Oʻzbekcha: ilon
🇰🇿 Qazaqşa: jılan
🇰🇬 Qırğızça: jılan
    Uyghurche: yilan
    Tatarça: yılan
    Başqortsa: yılan
    Çovaşla: cölen
    Qaraqalpaqsha: jılan
    Qırımtatarca: yılan
    Qumuqça: yılan
    Qaraçay-Malqar:	jılan (jilân)
    Noğayşa: yılan
    Sıbırca: yılan
    Gagauzça: yılan
    Saqalī: moğoy, erien üön
    Dulğan-Hakalī: moñoy
    Tıvalap: çılan
    Salırça: yılan (yilän)
    Xakastap: çılan
    Altaylap: cılan
    Şor: çılan
    Urumça: yılan (ilan)
    Karajče: ilan (jylan)
    Qrımçahça: yılan
    Soyot: çılan (cılan), uzın-ğurt
    Tofalap: çulan, dağ balıı, çer balıı, uzun-qurt''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зуб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зубы" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "клык" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "клыки" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tooth" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "diş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tiş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fang" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "teeth":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): tiş
🇬🇧 English: tooth
🇷🇺 Русский: зуб
🇹🇷 Türkçe: diş
🇦🇿 Türkcə: diş, tiş (dialect)
🇹🇲 Türkmençe: diş
🇺🇿 Oʻzbekcha: tish
🇰🇿 Qazaqşa: tis
🇰🇬 Qırğızça: tiş
    Uyghurche: chish
    Tatarça: teş
    Başqortsa: teş
    Çovaşla: şol
    Qaraqalpaqsha: tis
    Qırımtatarca: tiş
    Qumuqça: tiş
    Qaraçay-Malqar:	tiş
    Noğayşa: tis
    Sıbırca: teş
    Gagauzça: diş
    Saqalī: tïs
    Dulgan-Hakalī: tïs
    Tıvalap: diş
    Salırça: tiş
    Xakastap: tis
    Altaylap: tiş
    Şor: tiş
    Urumça: tiş (diş)
    Karajče: tiš (diš, tis)
    Qrımçahça: çış
    Soyot: tiş (diş)
    Tofalap: diş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ваня" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "john" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jonny" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jone" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иван" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иоанн" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иоан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yahya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ivan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "djon" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "johannes" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iohannes" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "johan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıvan":
        bot.send_message(message.chat.id, '''🇬🇧 English: John
🇷🇺 Русский: Иван, Иоанн, Ваня
🇹🇷 Türkçe: Yahya
🇦🇿 Türkcə: Yəhya
🇹🇲 Türkmençe: Ýahýa
🇺🇿 Oʻzbekcha: Yahyo
🇰🇿 Qazaqşa: Jaqıya, Joqan
🇰🇬 Qırğızca: Jaqıya
    Uyghurche: Yehya
    Tatarça: Yaxya
    Başqortsa: Yaxya
    Çovaşla: Yovan
    Qaraqalpaqsha: ???
    Qırımtatarca: Yaya
    Qumuqça: ???
    Qaraçay-Malqar: ???
    Noğayşa: Yahıya
    Sıbırca: ???
    Gagauzça: Yahya
    Saqalıı: Uybān (İvan)
    Dulgan-Hakalıı: Uybān
    Tıvalap: ???
    Salırça: ???
    Xakastap: ???
    Altaylap: ???
    Şor: ???
    Urumça: Yovan
    Karajče: Jona
    Qrımçahça: ???
    Tofalap: ???
    Soyot: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "изо" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "искусство запечатления образов" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "изобразительное искусство" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "изобразительное искуство" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "изобразительное исскусство" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "изобразительное исскуство" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "görsel sanat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "görsel sanatlar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "görsel sanat işi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "visual art" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "visual arts":
        bot.send_message(message.chat.id, '''🇬🇧 English: visual art(s)
🇷🇺 Русский: искусство запечатления образов (ИЗО), изобразительное искусство
🇹🇷 Türkçe: görsel sanat(lar)
🇦🇿 Türkcə: təsviri incəsənət
🇹🇲 Türkmençe: şekillendiriş sungatı
🇺🇿 Oʻzbekcha: tasviriy sanʼat
🇰🇿 Qazaqşa: beynelew öneri
🇰🇬 Qırğızça: körköm süröt önörü
    Uyghurche: teswiriy sen'et
    Tatarça: sınlı sänğät
    Başqortsa: hınlı sänğät
    Çovaşla: süretle üner, sonarlo üner, ükerü ostaloxö
    Qaraqalpaqsha: körkem öneri
    Qırımtatarca: tasviriy sanat
    Qumuqça: suratlaw inçesaniyatı
    Qaraçay-Malqar: suratlawçu sanağat
    Noğayşa: süwretlendirilgen säniyet
    Sıbırca: sınnı säñät
    Gagauzça: resimlemaa sanatı
    Saqalī: cühünnǖr iskusstvolar
    Dulgan-Hakalī: ???
    Tıvalap: çurumaldıg uran çüül
    Salırça: ???
    Xakastap: ???
    Altaylap: ???
    Şor: ???
    Urumça: ???
    Karajče: kiork senat
    Qrımçahça: ???
    Soyot: ???
    Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ısa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "isa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "isus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iisus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jesus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иисус" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "исус" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "есус" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ийсус" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ииссус":
        bot.send_message(message.chat.id, '''
🇬🇧 English: Jesus
🇷🇺 Русский: Иисус
🇹🇷 Türkçe: İsa
🇦🇿 Türkcə: İsa
🇹🇲 Türkmençe: Isa
🇺🇿 Oʻzbekcha: Iso
🇰🇿 Qazaqşa: Aysa, Iysa
🇰🇬 Qırğızça: Iysa, İsa
    Uyghurche: Eysa
    Tatarça: Ğaysä
    Başqortsa: Ğaysa, İsa
    Çovaşla: İisus (Yisus)
    Qaraqalpaqsha: İsa (İysa)
    Qırımtatarca: İsa
    Qumuqça: İsa
    Saxalıı: İsus
    Qaraçay-Malqar: İssa
    Gagauzça: İsa, İisus
    Sıbırca: Äysä
    Salırça: İsa
    Urumça: İsa, Xurtoz baba
    ???
    Islamic Prophet: Isa (Jesus)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "июль" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "july" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "temmuz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "temuz":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: july
🇷🇺 Русский: июль
🇹🇷 Türkçe: temmuz
🇦🇿 Türkcə: iyul, təmuz
🇹🇲 Türkmençe: gorkut
🇺🇿 Oʻzbekcha: iyul, asad
🇰🇿 Qazaqşa: şilde, äset
🇰🇬 Qırğızça: teke
    Uyghurche: chille
    Tatarça: iyül, peçän, tämmuz
    Başqortsa: mayay
    Çovaşla: uto
    Qaraqalpaqsha: iyul, háset
    Qırımtatarca: iyül, oraq
    Qumuqça: iyul, innır	
    Qaraçay-Malqar: iyul, eliya
    Noğayşa: iyul, şille
    Sıbırca: iyul, äsät, ollo esse
    Gagauzça: orak
    Saqalī: ot ıya
    Dulgan-Hakalī: kumār tüher
    Tıvalap: çedi
    Salırça: yitinci
    Xakastap: iyul
    Xakastap (Sağay): ot, tos
    Xakastap (Pîltir): tos
    Xakastap (Xaas): xara çuluğ
    Altaylap: iyul, caan izü
    Şor: piçen
    Urumça: eyil (yulios)
    Karajče: (they use Karaim calendar)
    Qrımçahça: iyul
    Soyot: iyul
    Tofalap: kök qahar''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "июнь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "june" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "haziran" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hazıran":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: june
🇷🇺 Русский: июнь
🇹🇷 Türkçe: haziran
🇦🇿 Türkcə: iyun, həziran
🇹🇲 Türkmençe: oguz
🇺🇿 Oʻzbekcha: iyun, saraton
🇰🇿 Qazaqşa: mawsım, saratan
🇰🇬 Qırğızça: qulja
    Uyghurche: seretan
    Tatarça: iyün, çereşmä, häziran
    Başqortsa: hötay
    Çovaşla: cörtme
    Qaraqalpaqsha: iyun, saratan
    Qırımtatarca: iyün, kiraz
    Qumuqça: iyun, kürjan
    Qaraçay-Malqar: iyun, nikkol, lukkur (lukkum, lukkul)
    Noğayşa: iyun, tambız
    Sıbırca: iyun, särtän, kece esse
    Gagauzça: kirez
    Saqalī: bes ıya
    Dulgan-Hakalī: kömüöl
    Tıvalap: aldı
    Salırça: altıncı (alçıncı)
    Xakastap: iyun
    Xakastap (Sağay): paar, xandıx
    Xakastap (Pîltir): tos
    Xakastap (Xaas): çuluğ
    Altaylap: iyun, kiçü, izü
    Şor: öleñ-tos
    Urumça: eyin
    Karajče: (they use Karaim calendar)
    Qrımçahça: iyun
    Soyot: iyun
    Tofalap: tayğalaar''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qazaq eli" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kazak eli" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "казакстан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "казахстан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kazakistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kazağıstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kazakıstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "казахстанский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kazakstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qazaqstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kazakhstan":
        bot.send_message(message.chat.id, '''🇬🇧 English: Kazakhstan
🇷🇺 Русский: Казахстан
🇹🇷 Türkçe: Kazakistan
🇦🇿 Türkcə: Qazaxıstan, Qazaxstan (archaism)
🇹🇲 Türkmençe: Gazagystan
🇺🇿 Oʻzbekcha: Qozogʻiston
🇰🇿 Qazaqşa: Qazaqstan, Qazağıstan (archaism)
🇰🇬 Qırğızça: Qazaqstan
    Uyghurche: Qazaqistan (Qazaqstan, Qazaghistan)
    Tatarça: Qazaqstan
    Başqortsa: Qazağstan
    Çovaşla: Kazaxstan
    Qaraqalpaqsha: Qazaqstan
    Qırımtatarca: Qazahistan
    Qumuqça: Qazaxstan
    Qaraçay-Malqar: Qazaxstan
    Noğayşa: Qazaxstan
    Sıbırca: Qasağıstan
    Gagauzça: Kazakistan
    Saqalī: Kazaqstān
    Dulgan-Hakalī: Kazakstān
    Tıvalap: Kazaxstan
    Salırça: Qazakstan
    Xakastap: Xazaxstan
    Altaylap: Qazaxstan
    Şor: Kazaxstan
    Urumça: Xazaxstan
    Karajče: Kazakstan
    Qrımçahça: Qazahistan
    Soyot: Kazaxstan
    Tofalap: Kazaxstan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "как" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "how" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nasıl" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nasil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "каким образом":
        bot.send_message(message.chat.id, '''🇷🇺 Слово "как" указано в значении "каким образом", для значения подобия, введите "подобно".
        
🇬🇧 English: how
🇷🇺 Русский: как, каким образом
🇹🇷 Türkçe: nasıl
🇦🇿 Türkcə: necə, nətər, nəcür, hancar (dialect)
🇹🇲 Türkmençe: nähili, niçik
🇺🇿 Oʻzbekcha: qalay, qanday, nechik
🇰🇿 Qazaqşa: qalay
🇰🇬 Qırğızça: qanday, neçik
    Uyghurche: qandaq
    Tatarça: niçek
    Başqortsa: nisek
    Çovaşla: mönle, eple
    Qaraqalpaqsha: qalay
    Qırımtatarca: nasıl, neday (dialect)
    Qumuqça: neçik
    Qaraçay-Malqar:	qalay
    Noğayşa: qalay
    Sıbırca: nicek, qaydıy
    Gagauzça: nicä, nasıl
    Saqalıı: qaydaq
    Dulğan-Hakalıı: kaytak
    Tıvalap: kandık
    Salırça: nēçux (nïçux, neçux, niçux), näcili (niçili, nicili, nïçixli)
    Xakastap: xaydî
    Altay: qandıy, qanay
    Şor: qayde
    Urumça: nas, niçek, nasıl (nasın), nek
    Karaj: niečik (neсik, nečik)
    Qrımçahça: nas
    Soyot: qanca, qancap
    Tofalap: qanca, qancap, qancaalı''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "картофель" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "картошка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "картофельный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "potatos" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "potato" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "patates" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "potates" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "картопля":
        bot.send_message(message.chat.id, '''🇬🇧 English: potato
🇷🇺 Русский: картофель, картошка
🇹🇷 Türkçe: patates
🇦🇿 Türkcə: kartof, yeralma (yeralması) (dialect, archaism), moqu (dialect)
🇹🇲 Türkmençe: kartofel, ýeralma
🇺🇿 Oʻzbekcha: kartoshka
🇰🇿 Qazaqşa: kartop, kärtöpiyä (dialect), aqtüynek
🇰🇬 Qırğızça: kartofel, kartöşkö
    Uyghurche: yangiyu
    Tatarça: bäräñge, qartuf (qartup, qartuq), cir alması
    Başqortsa: bäräñge, kartuf
    Çovaşla: cörulmi
    Qaraqalpaqsha: kartofel, kartoshka
    Qırımtatarca: qartop
    Qumuqça: kartop
    Qaraçay-Malqar: gardoş, kartof
    Noğayşa: yeralma, kartofel
    Sıbırca: kärtüp (kartup), päräñke, yomalaq
    Gagauzça: kartofi, patetes
    Saqalıı: qortuoppuy, qortuoska
    Dulgan-Hakalıı: kortuoppuy
    Tıvalap: kartofel
    Salırça: yangyü
    Xakastap: yablax
    Altay: kartoşko
    Şor: kartöpke
    Urumça: kartop (gardof, kartof)
    Karaj: jer čybany, jerler, jercek, kartof, bul'ba (bul'va)
    Qrımçahça: qartof
    Soyot: yaaval (yaavalxa), hartaapha
    Tofalap: hortooqa (hortoopqa)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "когда" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "when" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ne zaman" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ne vakit" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "haçan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kaçan":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰲𐰣
🇬🇧 English: when
🇷🇺 Русский: когда
🇹🇷 Türkçe: ne zaman
🇦🇿 Türkcə: nə vaxt, nə zaman, haçan, havaxt
🇹🇲 Türkmençe: haçan
🇺🇿 Oʻzbekcha: qachon
🇰🇿 Qazaqşa: qaşan
🇰🇬 Qırğızça: qaçan
    Uyghurche: qachan
    Tatarça: qayçan
    Başqortsa: qasan
    Çovaşla: xocan
    Qaraqalpaqsha: qashan
    Qırımtatarca: qaçan
    Qumuqça: qaçan
    Qaraçay-Malqar:	qaçan
    Noğayşa: qaşan
    Sıbırca: qacan
    Gagauzça: nezaman, açan
    Saqalıı: qahan
    Dulğan-Hakalıı: kahan
    Tıvalap: kajan
    Salırça: qaçañ (qayçañ, xacañ)
    Xakastap: xacan
    Altay: qaçan
    Şor: qaçan
    Urumça: navax (nävax), xaçan (açan)
    Karaj: kačan (kacan)
    Qrımçahça: qaçan, ne vahıt
    Soyot: qahân (qaşan, qaşân)
    Tofalap: qahîn (qahân)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кожа" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шкура" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кожаный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "deri" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "skin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "leather":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱅𐰼𐰃
🐺 Old Turkic: teri, quyqa, kön
🇬🇧 English: skin, leather
🇷🇺 Русский: кожа, шкура
🇹🇷 Türkçe: deri
🇦🇿 Türkcə: dəri, gön
🇹🇲 Türkmençe: deri
🇺🇿 Oʻzbekcha: teri
🇰🇿 Qazaqşa: teri
🇰🇬 Qırğızça: teri
    Uyghurche: tére
    Tatarça: tire
    Başqortsa: tire
    Çovaşla: tire
    Qaraqalpaqsha: teri
    Qırımtatarca: teri
    Qumuqça: teri
    Qaraçay-Malqar:	teri
    Noğayşa: teri
    Sıbırca: tire (tärä)
    Gagauzça: deri
    Saqalī: tirï
    Dulğan-Hakalī: tirï
    Tıvalap: keş
    Salırça: tir
    Xakastap: teer
    Altaylap: tere
    Şor: tere
    Urumça: deri (teri), kön (gön)
    Karajče: tieri (teri), gioń
    Qrımçahça: terı
    Soyot: keş
    Tofalap: keş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "computer" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bilgisayar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bilgi sayar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "comp" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "комп" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "компьютер" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "компъютер" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "компутер" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кампьютер" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "компьютерный":
        bot.send_message(message.chat.id, '''🇬🇧 English: computer
🇷🇺 Русский: компьютер [kompyuter]
🇹🇷 Türkçe: bilgisayar
🇦🇿 Türkcə: bilgisayar, kompüter
🇹🇲 Türkmençe: kompýuter, bilgisaýar
🇺🇿 Oʻzbekcha: kompyuter
🇰🇿 Qazaqşa: kompüter, sanawır {KazakGrammar}
🇰🇬 Qırğızça: kompyuter, esepker {rarely, unofficial}
🌏 Uyghurche: kompyutér
🌍 Tatarça: sanaq, kompyuter
🌍 Başqortsa: kompyuter
🌍 Çovaşla: kompyuter
🌍 Qaraqalpaqsha: kompyuter
🌍 Qırımtatarca: bilgisayar, kompyuter
🌍 Qumuqça: kompyuter
🌍 Qaraçay-Malqar: kompyuter
🌍 Noğayşa: kompyuter
🌏 Sıbırca: kompyuter, sanaq
🌍 Gagauzça: bilgisayar, kompüter
🌏 Saqalī: kömpǖter
🌏 Dulgan-Hakalī: kömpǖter
🌏 Tıvalap: kompyuter
🌏 Salırça: diennao
🌏 Xakastap: kompyuter
🌏 Altaylap: kompyuter
🌏 Şor: kompyuter
🌍 Urumça: kompyuter
🌍 Karajče: kompiuter
🌍 Qrımçahça: kompyuter
🌏 Soyot: kompyuter
🌏 Tofalap: kompyuter''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "конституция" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "constitution" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "anayasa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "контитуционный":
        bot.send_message(message.chat.id, '''
🇬🇧 English: constitution
🇷🇺 Русский: конституция
🇹🇷 Türkçe: anayasa, kanun-u esasi (archaism)
🇦🇿 Türkcə: konstitusiya, anayasa, qanun-əsasi (archaism), məşrutə (archaism)
🇹🇲 Türkmençe: konstitusiýa, esasy kanun, mäşrüte (archaism)
🇺🇿 Oʻzbekcha: konstitutsiya, mashruta (archaism)
🇰🇿 Qazaqşa: konstitusiya, ata zaŋ
🇰🇬 Qırğızça: konstitutsiya, başmıyzam
    Uyghurche: konstitutsiye, asasiy qanun
    Tatarça: konstitutsiä
    Başqortsa: konstitutsiä
    Çovaşla: konstitutsi (konctitutsi)
    Qaraqalpaqsha: konstitutsiya, tiyqarǵı nızam
    Qırımtatarca: anayasa, konstitutsiya, esas qanun, meşrutiyet (archaism)
    Qumuqça: konstitutsiya
    Qaraçay-Malqar: konstitutsiya
    Noğayşa: konstitutsiya
    Sıbırca: konstituciä
    Gagauzça: konstitutsiya, anayasa
    Saqalī: konstituciya
    Dulgan-Hakalī: konstituciya
    Tıvalap: konstitutsiya
    Salırça: anayasa, şenfa
    Xakastap: konstîtutsıya
    Altaylap: konstitutsiya
    Şor: konstitutsiya
    Urumça: konstitutsiya
    Karajče: konstitucija
    Qrımçahça: konstitutsiya
    Soyot: konstîtutsıya
    Tofalap: konstîtutsıya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "корень" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "root" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kök" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "köken" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "корневой":
        bot.send_message(message.chat.id, '''
🐺 Old Turkic (bef. 13th c.): kök, yıldız, tüp
🇬🇧 English: root
🇷🇺 Русский: корень
🇭🇺 Magyar: gyök, gyökér
🇹🇷 Türkçe: kök
🇦🇿 Türkcə: kök, damar (dialect)
🇹🇲 Türkmençe: kök
🇺🇿 Oʻzbekcha: ildiz
🇰🇿 Qazaqşa: tamır
🇰🇬 Qırğızça: tamır
    Uyghurche: yiltiz
    Tatarça: tamır
    Başqortsa: tamır
    Çovaşla: tımar, kok
    Qaraqalpaqsha: tamır
    Qırımtatarca: tamır
    Qumuqça: tamur
    Qaraçay-Malqar:	tamır
    Noğayşa: tamır
    Sıbırca: tamır
    Gagauzça: kök
    Saqalī: silis
    Dulgan-Hakalī: hilis
    Tıvalap: dazıl
    Salırça: omca, özex
    Xakastap: çîlege, tamır
    Altaylap: tazıl
    Şor: tazıl, çıltıs
    Urumça: kök, damar (tamar, tamur)
    Karajče: kiok, tamur
    Qrımçahça: tamar
    Soyot: tazıl (dazıl)
    Tofalap: tazıl''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "короткий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "короткая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "короткое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "короткие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "short" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kısa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gödek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kisa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kıska" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киска":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰃𐱁𐰍𐰀	
🇬🇧 English: short
🇷🇺 Русский: короткий (-ая, -ое)
🇹🇷 Türkçe: kısa
🇦🇿 Türkcə: qısa, gödək
🇹🇲 Türkmençe: gysga
🇺🇿 Oʻzbekcha: qisqa
🇰🇿 Qazaqşa: qısqa, şolaq, kelte
🇰🇬 Qırğızça: qısqa
    Uyghurche: qisqa
    Tatarça: qısqa
    Başqortsa: qısqa
    Çovaşla: köske
    Qaraqalpaqsha: qısqa
    Qırımtatarca: qısqa
    Qumuqça: qısğa
    Qaraçay-Malqar:	qısxa
    Noğayşa: qısqa
    Sıbırca: qısqa
    Gagauzça: kısa, gücük
    Saqalıı: kılgas
    Dulğan-Hakalıı: kılgas
    Tıvalap: kıska, çoldak
    Salırça: xısxa
    Xakastap: xısxa
    Altay: qısqa, çoltıq
    Şor: qısqa
    Urumça: xısxa (xısa, ğıssa)
    Karajče: kyscha (kyska)
    Qrımçahça: qısqa
    Soyot: qısqa
    Tofalap: qısqa''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bone" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kemik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кость" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "костяной":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰾𐰇𐰭𐰜
🐺 Old Turkic: söñük, ğaytsı
🇬🇧 English: bone
🇷🇺 Русский: кость
🇹🇷 Türkçe: kemik, sümük (dialect)
🇦🇿 Türkcə: sümük
🇹🇲 Türkmençe: süňk
🇺🇿 Oʻzbekcha: suyak
🇰🇿 Qazaqşa: süyek
🇰🇬 Qırğızça: söök
    Uyghurche: süyek, söngek
    Tatarça: söyäk
    Başqortsa: höyäk
    Çovaşla: şomo
    Qaraqalpaqsha: súyek
    Qırımtatarca: kemik, süyek (dialect)
    Qumuqça: süyek
    Qaraçay-Malqar:	süyek
    Noğayşa: süyek
    Sıbırca: söyäk (sȫȫk), yañrıq
    Gagauzça: kemik
    Saqalī: uñuoq
    Dulğan-Hakalī: uñuok
    Tıvalap: söök
    Salırça: senix (sıñıx)
    Xakastap: söök
    Altaylap: söök
    Şor: söök
    Urumça: süyek, kämik (kämük, kemik)
    Karajče: siujek (sivek, siuviek), kemik, siumiuk (small bone)
    Qrımçahça: süyek, kemık
    Soyot: söök
    Tofalap: söök''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "крест" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cross" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "haç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "put" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "salip" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хач" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хачик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "херасе" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ни хера себе" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıstavroz":
        bot.send_message(message.chat.id, '''
🇬🇧 English: cross
🇷🇺 Русский: крест [krest]
🇹🇷 Türkçe: haç, put, salip, ıstavroz
🇦🇿 Türkcə: xaç, səlib
🇹🇲 Türkmençe: haç, atanak
🇺🇿 Oʻzbekcha: xoch, but, salib
🇰🇿 Qazaqşa: kires
🇰🇬 Qırğızça: krest, çırım
    Uyghurche: chapras
    Tatarça: xaç, salib
    Başqortsa: täre
    Çovaşla: xöres, xoc, xrec
    Qaraqalpaqsha: atanaq
    Qırımtatarca: haç
    Qumuqça: xaç
    Qaraçay-Malqar: gâwur qaç, jor, krest
    Noğayşa: qaç
    Sıbırca: täre, qac (qacı)
    Gagauzça: stavroz
    Saqalıı: kiries, süreq
    Tıvalap: krest
    Salırça: ???
    Xakastap: kirös (kirees), harçı
    Altay: kres, qarçı
    Şor: krest
    Dolgan: krest
    Urumça: xaç, stavroz
    Karaj: chač
    Qrımçahça: haç (ğaç)
    Soyot: herääsê
    Tofalap: herääsê''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "blood" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кровь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кровный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kan":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰣
🇬🇧 English: blood
🇷🇺 Русский: кровь
🇹🇷 Türkçe: kan
🇦🇿 Türkcə: qan
🇹🇲 Türkmençe: gan
🇺🇿 Oʻzbekcha: qon
🇰🇿 Qazaqşa: qan
🇰🇬 Qırğızça: qan
    Uyghurche: qan
    Tatarça: qan
    Başqortsa: qan
    Çovaşla: yun
    Qaraqalpaqsha: qan
    Qırımtatarca: qan
    Qumuqça: qan
    Qaraçay-Malqar: qan
    Noğayşa: qan
    Sıbırca: qan
    Gagauzça: kan
    Saqalī: qān
    Dulğan-Hakalī: kān
    Tıvalap: xan
    Salırça: qan
    Xakastap: xan
    Altaylap: qan
    Şor: qan
    Urumça: ğan (xan)
    Karajče: kan
    Qrımçahça: qan
    Soyot: qan (gan)
    Tofalap: qan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "crocodile" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "crocodil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "krokodil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "крокодил" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "timsah" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lacoste" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tımsah":
        bot.send_message(message.chat.id, '''
🐺 Old Turkic (bef. 13th c.): alavan, nek
🇬🇧 English: crocodile
🇷🇺 Русский: крокодил [krokodil]
🇹🇷 Türkçe: timsah
🇦🇿 Türkcə: timsah
🇹🇲 Türkmençe: krokodil, tymsak
🇺🇿 Oʻzbekcha: timsoh
🇰🇿 Qazaqşa: qoltırawın, tımsaq (archaism)
🇰🇬 Qırğızça: krokodil
🌏 Uyghurche: timsaq
🌍 Tatarça: timsax
🌍 Başqortsa: krokodil, diñgeð keþärtkehe
🌍 Çovaşla: krokodil
🌍 Qaraqalpaqsha: krokodil
🌍 Qırımtatarca: timsah
🌍 Qumuqça: krokodil
🌍 Qaraçay-Malqar: sarıwbek
🌍 Noğayşa: alawan, krokodil
🌏 Sıbırca: timsaq (timsax)
🌍 Gagauzça: krokodil
🌏 Saqalī: luobuya
🌏 Dulgan-Hakalī: krokodil
🌏 Tıvalap: krokodil
🌏 Salırça: ıyü
🌏 Xakastap: krokodîl
🌏 Altaylap: krokodil
🌏 Şor: krokodil
🌍 Urumça: krakadil
🌍 Karajče: krokodil
🌍 Qrımçahça: timsah
🌏 Soyot: krokodîl
🌏 Tofalap: krokodîl''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kanat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "крыло" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "wing" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "крылья":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰣𐱃 (𐰴𐰣𐰀𐱃)
🐺 Old Turkic: qanat
🇬🇧 English: wing
🇷🇺 Русский: крыло
🇹🇷 Türkçe: kanat
🇦🇿 Türkcə: qanad, qənət (dialect)
🇹🇲 Türkmençe: ganat
🇺🇿 Oʻzbekcha: qanot
🇰🇿 Qazaqşa: qanat
🇰🇬 Qırğızça: qanat
    Uyghurche: qanat
    Tatarça: qanat
    Başqortsa: qanat
    Çovaşla: cunat
    Qaraqalpaqsha: qanat
    Qırımtatarca: qanat
    Qumuqça: qanat
    Qaraçay-Malqar: qanat
    Noğayşa: qanat
    Sıbırca: qanat
    Gagauzça: kanat
    Saqalī: kınat
    Dulgan-Hakalī: kınat
    Tıvalap: çalgın
    Salırça: qanat
    Xakastap: xanat
    Altaylap: qanat
    Şor: qanat
    Urumça: ğanad (xanat, xanet)
    Karajče: kanat
    Qrımçahça: qanat
    Soyot: hanat, çalhın
    Tofalap: hanat''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kim" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kım" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "who" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кто":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰚𐰢
🇬🇧 English: who
🇷🇺 Русский: кто [kto]
🇹🇷 Türkçe: kim
🇦🇿 Türkcə: kim
🇹🇲 Türkmençe: kim
🇺🇿 Oʻzbekcha: kim
🇰🇿 Qazaqşa: kim
🇰🇬 Qırğızça: kim
    Uyghurche:	kim
    Tatarça: kem
    Başqortsa: kem
    Çovaşla: kam
    Qaraqalpaqsha: kim
    Qırımtatarca: kim
    Qumuqça: kim
    Qaraçay-Malqar:	kim
    Noğayşa: kim
    Sıbırca: kem (kim)
    Gagauzça: kim
    Saqalıı: kim
    Dulğan-Hakalıı: kim
    Tıvalap: kım
    Salırça: kem (k'em)
    Xakastap: kem
    Altay: kem
    Şor: kem
    Urumça: kim
    Karaj: kim
    Qrımçah: kım
    Soyot: qım (gım)
    Tofalap: qum''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ye" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to eat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кушай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кушать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сьешь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кушац" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "съесть" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сьесть" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ешь":
        bot.send_message(message.chat.id, '''
🐺 Old Turkic (bef. 13th c.): aşa, ye
🇬🇧 English: eat
🇷🇺 Русский: кушай [kushay], ешь [yesh']
🇹🇷 Türkçe: ye
🇦🇿 Türkcə: ye (yi), bığla (dialect), əvdi (dialect), herqıt (dialect), xırınc elə (dialect), iyə (dialect), məzzə (dialect), oxat (dialect), tikələ (dialect), üşələ (dialect)
🇹🇲 Türkmençe: iý
🇺🇿 Oʻzbekcha: ye
🇰🇿 Qazaqşa: je, asa
🇰🇬 Qırğızça: je
🌏 Uyghurche: yi (yé) 
🌍 Tatarça: aşa
🌍 Başqortsa: aşa
🌍 Çovaşla: ci
🌍 Qaraqalpaqsha: je
🌍 Qırımtatarca: aşa, ye (dialect)
🌍 Qumuqça: aşa
🌍 Qaraçay-Malqar: aşa
🌍 Noğayşa: ye, aşa
🌏 Sıbırca: aşa, ye
🌍 Gagauzça: yi (i)
🌏 Saqalī: ahā, sie
🌏 Dulgan-Hakalī: ahā, hie
🌏 Tıvalap: çi, çemnen
🌏 Salırça: yi
🌏 Xakastap: çi
🌏 Altaylap: ci
🌏 Şor: çii
🌍 Urumça: i (yiy, ye)
🌍 Karajče: aša (asa), je
🌍 Qrımçahça: aşa, ye
🌏 Soyot: çî (cî)
🌏 Tofalap: çî, nemnê (nemnä) ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "аслан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лев" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "арслан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "aslan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lion" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "asrlan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "львица" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "львиный":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰺𐰽𐰞𐰣 
🇬🇧 English: lion
🇷🇺 Русский: лев
🇭🇺 Magyar: oroszlán
🇲🇳 Mongol: arslan
🇹🇷 Türkçe: aslan
🇦🇿 Türkcə: aslan, şir
🇹🇲 Türkmençe: arslan, ýolbars
🇺🇿 Oʻzbekcha: arslon, sher
🇰🇿 Qazaqşa: arıstan
🇰🇬 Qırğızça: arstan
    Uyghurche: arslan, shir
    Tatarça: arıslan
    Başqortsa: arıþlan
    Çovaşla: aroslan
    Qaraqalpaqsha: arıslan
    Qırımtatarca: arslan, şir
    Qumuqça: arslan, arslanqaplan
    Saqalıı: xaxay, arsan
    Qaraçay-Malqar: aslan
    Tıvalap: arzılañ
    Gagauzça: aslan
    Noğayşa: arıslan
    Salırça: pās (pasır, pāsar), şizi
    Xakastap: ala parıs
    Sıbırca: arıslan
    Altay: arslan
    Şor: ala pars
    Urumça: aslan (astlan)
    Karaj: aslan (arslan, aryslan)
    Qrımçahça: aslan (arıslan)
    Soyot: arsılañ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лес" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "forest" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "orman" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ağaçlık":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰘𐰃𐰾 (𐰘𐰃𐱁)
🇬🇧 English: forest
🇷🇺 Русский: лес
🇫🇮 Suomea: metsä
🇹🇷 Türkçe: orman
🇦🇿 Türkcə: meşə, orman, ağaclıq, toğay (dialect), şibər (dialect), urım (dialect), atağar (dialect, forest with low trees)
🇹🇲 Türkmençe: tokaý
🇺🇿 Oʻzbekcha: oʻrmon, toʻqay
🇰🇿 Qazaqşa: orman, toğay
🇰🇬 Qırğızça: toqoy, ormon
    Uyghurche: orman, ormanliq
    Tatarça: urman
    Başqortsa: urman, ağaslıq
    Çovaşla: vorman
    Qaraqalpaqsha: toǵay
    Qırımtatarca: orman, dağ (dialect)
    Qumuqça: orman, ağaçlıq
    Qaraçay-Malqar: ağaç, çeget
    Noğayşa: orman, ağaşlıq
    Sıbırca: tös, ağaclıq, pöyläk, urmannıq, yış, celek (small forest in the swamps), urman (dialect, meaning may vary), qarağay (dialect, meaning may vary)
    Gagauzça: daa, orman (meaning may vary)
    Saqalī: tıa, oyūr
    Dulğan-Hakalī: tıa
    Tıvalap: arıg, ezim, arga (mountain forest)
    Salırça: arığ, xuy, xuyara
    Xakastap: arığ, ağastar, ağas
    Altaylap: ağaş, ağaş arazı, ağaştar
    Şor: ağaş arazı, ağaştar, ağaş, çış (dense forest)
    Urumça: meşä, orman, dağ (tav) (meaning may vary), dağlıx (dialect, meaning may vary)
    Karajče: orman, ormanlyk, dah (tav) (meaning may vary)
    Qrımçahça: orman, dağ (meaning may vary)
    Soyot: nâşqırı cer, arığ (floodplain forest), tayğa (mountain forest)
    Tofalap: arığ (floodplain forest), tayğa (mountain forest)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yaprak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yapırak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "leaf" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "leaves" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "листья" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лист":
        bot.send_message(message.chat.id, '''🐺 Old Turkic: yapırğaq (yalbırğaq, yapurğaq), yawışğu
🇬🇧 English: leaf
🇷🇺 Русский: лист (лист растения)
🇹🇷 Türkçe: yaprak
🇦🇿 Türkcə: yarpaq
🇹🇲 Türkmençe: ýaprak
🇺🇿 Oʻzbekcha: yaproq, barg
🇰🇿 Qazaqşa: japıraq
🇰🇬 Qırğızça: jalbıraq
    Uyghurche: yopurmaq
    Tatarça: yafraq
    Başqortsa: yapraq
    Çovaşla: culco
    Qaraqalpaqsha: japıraq
    Qırımtatarca: yaprak
    Qumuqça: yapıraq
    Qaraçay-Malqar:	çapraq
    Noğayşa: yapıraq
    Sıbırca: yapraq
    Gagauzça: yaprak
    Saqalī: sebirdeq
    Dulğan-Hakalī: hebirdek
    Tıvalap: bürü
    Salırça: yaprax
    Xakastap: pür
    Altaylap: calbıraq
    Şor: pür
    Urumça: yarpax (yaprax)
    Karajče: japrak (japrach)
    Qrımçahça: yaprah
    Soyot: bür
    Tofalap: bür''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "литва" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "litva" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lithuania" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "letuva" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "litvanya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lietuva":
        bot.send_message(message.chat.id, '''🇬🇧 English: Lithuania
🇷🇺 Русский: Литва
🇹🇷 Türkçe: Litvanya
🇦🇿 Türkcə: Litva, Litvaniya (archaism)
🇹🇲 Türkmençe: Litwa
🇺🇿 Oʻzbekcha: Litva
🇰🇿 Qazaqşa: Litva
🇰🇬 Qırğızça: Litva
🌏 Uyghurche: Litwaniye, Litwa
🌍 Tatarça: Litva
🌍 Başqortsa: Litva
🌍 Çovaşla: Litva
🌍 Qaraqalpaqsha: Litva
🌍 Qırımtatarca: Litvaniya
🌍 Qumuqça: Litva, Lituvaniya
🌍 Qaraçay-Malqar: Litva
🌍 Noğayşa: Litva
🌏 Sıbırca: Litva
🌍 Gagauzça: Litvaniya
🌏 Saqalī: Litva
🌏 Dulgan-Hakalī: Litva
🌏 Tıvalap: Litva
🌏 Salırça: Litvaniya
🌏 Xakastap: Litva
🌏 Altaylap: Litva
🌏 Şor: Litva
🌍 Urumça: Litva
🌍 Karajče: Letuva (Lietuva), Litvo
🌍 Qrımçahça: Letuva, Litvaniye
🌏 Soyot: Litva
🌏 Tofalap: Litva
In Lithuanian: Lietuva''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "литература" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "литра" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "literature" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "edebiyat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yazın":
        bot.send_message(message.chat.id, '''🇬🇧 English: literature
🇷🇺 Русский: литература
🇹🇷 Türkçe: edebiyat, yazın
🇦🇿 Türkcə: ədəbiyyat, yazın (rarely, purism)
🇹🇲 Türkmençe: edebiýat
🇺🇿 Oʻzbekcha: adabiyot
🇰🇿 Qazaqşa: ädebiyet
🇰🇬 Qırğızça: adabiyat
    Uyghurche: edebiyat
    Tatarça: ädäbiät
    Başqortsa: äðäbiät
    Çovaşla: literatura
    Qaraqalpaqsha: ádebiyat
    Qırımtatarca: edebiyat
    Qumuqça: adabiyat
    Qaraçay-Malqar: adabiyat
    Noğayşa: ädebiyet, literatura
    Sıbırca: ätäbiyät
    Gagauzça: edebiyat, literatura
    Saqalıı: literatura, surul (rarely, purism)
    Dulgan-Hakalıı: ???
    Tıvalap: çogaal
    Salırça: edebiyet
    Xakastap: ???
    Altay: ???
    Şor: ???
    Urumça: ???
    Karaj: literatura
    Qrımçahça: edebiyet
    Soyot: ???
    Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moon" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "month" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "luna" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "луна" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "месяц" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ay":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰖
🐺 Old Turkic (bef. 13th c.): ay
🇬🇧 English: I. moon II. month
🇷🇺 Русский: I. луна II. месяц
🇹🇷 Türkçe: ay
🇦🇿 Türkcə: ay
🇹🇲 Türkmençe: aý
🇺🇿 Oʻzbekcha: oy
🇰🇿 Qazaqşa: ay
🇰🇬 Qırğızça: ay
🌏 Uyghurche: ay
🌍 Tatarça: ay
🌍 Başqortsa: ay
🌍 Çovaşla: uyox
🌍 Qaraqalpaqsha: ay
🌍 Qırımtatarca: ay
🌍 Qumuqça: ay
🌍 Qaraçay-Malqar: ay
🌍 Noğayşa: ay
🌏 Sıbırca: ay
🌍 Gagauzça: ay
🌏 Saqalī: ıy
🌏 Dulgan-Hakalī: ıy
🌏 Tıvalap: ay
🌏 Salırça: ay
🌏 Xakastap: ay
🌏 Altaylap: ay
🌏 Şor: ay
🌍 Urumça: ay
🌍 Karajče: aj
🌍 Qrımçahça: ay
🌏 Soyot: ay
🌏 Tofalap: ay''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to love" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "люби" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "полюби" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "любить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sev" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sevmek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "возлюби":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): sev (seb), jaqşı kör, sev amra, amran
🇬🇧 English: love (v.)
🇷🇺 Русский: люби [lyubi]
🇹🇷 Türkçe: sev
🇦🇿 Türkcə: sev (to partner), çox istə (to family member, friend, relative, comrade etc)
🇹🇲 Türkmençe: söý
🇺🇿 Oʻzbekcha: sev
🇰🇿 Qazaqşa: süy, jaqsı kör
🇰🇬 Qırğızça: süy
🌏 Uyghurche: söy, yaxshi kör
🌍 Tatarça: yarat
🌍 Başqortsa: yarat
🌍 Çovaşla: yurat
🌍 Qaraqalpaqsha: súy, jaqsı kór
🌍 Qırımtatarca: sev
🌍 Qumuqça: süy
🌍 Qaraçay-Malqar: süy
🌍 Noğayşa: süy
🌏 Sıbırca: söy, yarat
🌍 Gagauzça: sev
🌏 Saqalī: taptā
🌏 Dolgan-Hakalī: bagar
🌏 Tıvalap: ınak tur
🌏 Salırça: söy
🌏 Xakastap: xın, marsa
🌏 Altay: süü, süüp tur
🌏 Şor: kölen
🌍 Urumça: sev
🌍 Karajče: siuv
🌍 Qrımçahça: süv
🌏 Soyot: ınaq tur
🌏 Tofalap: ekkisin''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "май" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "may" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mayıs" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mayis":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: may
🇷🇺 Русский: май
🇹🇷 Türkçe: mayıs
🇦🇿 Türkcə: may, mayıs
🇹🇲 Türkmençe: magtymguly
🇺🇿 Oʻzbekcha: may, javzo
🇰🇿 Qazaqşa: mamır, zawza
🇰🇬 Qırğızça: buğu
    Uyghurche: bahar
    Tatarça: may, saban
    Başqortsa: habanay
    Çovaşla: cu
    Qaraqalpaqsha: may, jawza
    Qırımtatarca: mayıs, quralay
    Qumuqça: may, güljan
    Qaraçay-Malqar: may, xıçawman
    Noğayşa: may, qural
    Sıbırca: may, cäwsä, tarmaq
    Gagauzça: hederlez
    Saqalī: ıam ıya
    Dulgan-Hakalī: tugut törǖr
    Tıvalap: beş
    Salırça: pişinci
    Xakastap: may
    Xakastap (Sağay): xıra tartçañ, tarlağ
    Xakastap (Pîltir): xıra tartçañ
    Xakastap (Xaas): siliker
    Altaylap: may, küük
    Şor: pes
    Urumça: mayıs (meyis)
    Karajče: (they use Karaim calendar)
    Qrımçahça: may
    Soyot: may
    Tofalap: şomur''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "little" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "small" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "маленький" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "малый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "маленькая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "маленькое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "малая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "малое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "küçük" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "маленькие":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰚𐰃𐰲𐰏
🇬🇧 English: little, small
🇷🇺 Русский: маленький, малый (-ая, -ое)
🇹🇷 Türkçe: küçük
🇦🇿 Türkcə: kiçik, balaca
🇹🇲 Türkmençe: kiçi, kiçijik
🇺🇿 Oʻzbekcha: kichik, kichkina
🇰🇿 Qazaqşa: kişi, kişkene, kişkentay
🇰🇬 Qırğızça: kiçine, kiçinekey
    Uyghurche: kichik
    Tatarça: keçe, keçkenä
    Başqortsa: bäläkäs, kese, bäläkäy
    Çovaşla: pöçök
    Qaraqalpaqsha: kishkentay, kishkene
    Qırımtatarca: kiçik
    Qumuqça: giççi
    Qaraçay-Malqar:	gitçe
    Noğayşa: kişkey
    Sıbırca: kece (kecek, kidzü), keckenä
    Gagauzça: küçük
    Saqalıı: kıra, aççıgıy, kuççuguy (kıççıgıy)
    Dulğan-Hakalıı: kıra, küççügüy, öççügüy
    Tıvalap: biçe, biçii
    Salırça: kiçi, kiçicux, kicar
    Xakastap: piçik, kiçicek
    Altay: kiçinek
    Şor: kiçig
    Urumça: küçük (çüçük), kiçi, kiçi, kiçene (kiçkine), kiçicik (kiçiçik)
    Karajče: kiči, kičik, kičkine (kičkene)
    Qrımçahça: kuçık, kıçkene
    Soyot: bîçe (bîçä), bîçîî
    Tofalap: bîçe, çaraş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "az" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "few" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "a little" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мало" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "a few":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰔
🇬🇧 English: few, a little
🇷🇺 Русский: мало
🇹🇷 Türkçe: az
🇦🇿 Türkcə: az
🇹🇲 Türkmençe: az
🇺🇿 Oʻzbekcha: oz
🇰🇿 Qazaqşa: az
🇰🇬 Qırğızça: az
    Uyghurche: az
    Tatarça: az
    Başqortsa: að (äð)
    Çovaşla: saxal
    Qaraqalpaqsha: az
    Qırımtatarca: az
    Qumuqça: az
    Qaraçay-Malqar:	az
    Noğayşa: az
    Sıbırca: as
    Gagauzça: az
    Saqalıı: ağıyaq
    Dulgan-Hakalıı: agıyan
    Tıvalap: eveeş
    Salırça: az, picä (piça)
    Xakastap: as
    Altay: as
    Şor: as
    Urumça: az
    Karaj: az
    Qrımçahça: az
    Soyot: eveş (eväş), bîçe (bîçä)
    Tofalap: bîçe''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "baby" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "малыш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "детка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "младенец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bebek":
        bot.send_message(message.chat.id, '''🇬🇧 English: baby
🇷🇺 Русский: малыш, детка, младенец
🇹🇷 Türkçe: bebek
🇦🇿 Türkcə: bəbə, bəbək, çağa
🇹🇲 Türkmençe: bäbek
🇺🇿 Oʻzbekcha: chaqaloq, go'dak
🇰🇿 Qazaqşa: böbek
🇰🇬 Qırğızça: böbök
    Uyghurche: gödek
    Tatarça: bäbi
    Başqortsa: bäpäy
    Çovaşla: papa, papak
    Qaraqalpaqsha: bóbek
    Qırımtatarca: bebey, bebek
    Qumuqça: bebey
    Qaraçay-Malqar:	jaşçıq
    Noğayşa: sabiy
    Sıbırca: päwäy
    Gagauzça: bebek
    Saqalıı: kıracān, oğokko
    Dulğan-Hakalıı: küççügüy ogo
    Tıvalap: çaş urug
    Salırça: palacux
    Xakastap: kiçîcek palaçax
    Altay: caş bala, kiçinek balaçaq
    Şor: kiçig pala
    Urumça: çüçük uşax, balaçıx
    Karajče: sebij, balačech
    Qrımçahça: babiy, balaçıh
    Soyot: cuuca
    Tofalap: çuuça''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mom" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mother" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мама" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "матерь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "anne" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ana":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰇𐰏𐰀, 𐰤
🇬🇧 English: mom, mother
🇷🇺 Русский: мама, мать
🇭🇺 Magyar: anya
🇹🇷 Türkçe: anne, ana
🇦🇿 Türkcə: ana
🇹🇲 Türkmençe: ene, eje
🇺🇿 Oʻzbekcha: ona, aya, oyi
🇰🇿 Qazaqşa: ana, şeşe, apa (dialect)
🇰🇬 Qırğızça: ene
    Uyghurche: ana, apa (dialect)
    Tatarça: ana
    Başqortsa: inä, äsä
    Çovaşla: anne, api (dialect)
    Qaraqalpaqsha: ana, ene
    Qırımtatarca: ana, anne (dialect)
    Qumuqça: ana
    Qaraçay-Malqar:	ana, annya (dialect)
    Noğayşa: ana
    Sıbırca: inä, ana
    Gagauzça: ana, anne
    Saqalī: iye
    Dulğan-Hakalī: ińe
    Tıvalap: iye, ava
    Salırça: ānne, ice (ici), ama
    Xakastap: îne, îce
    Altay: ene
    Şor: ene, içe
    Urumça: ana (ane), nene (nine)
    Karaj: ana
    Qrımçahça: ana
    Soyot: ava, îhä
    Tofalap: aba (ava), îhe''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "march" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "март" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mart" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мартовский":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: march
🇷🇺 Русский: март
🇹🇷 Türkçe: mart
🇦🇿 Türkcə: mart
🇹🇲 Türkmençe: nowruz
🇺🇿 Oʻzbekcha: mart, hamal
🇰🇿 Qazaqşa: nawrız, hamal
🇰🇬 Qırğızça: jalğan quran
    Uyghurche: newruz
    Tatarça: mart, buşay, näwrüz
    Başqortsa: buranay
    Çovaşla: puş
    Qaraqalpaqsha: mart, hamal
    Qırımtatarca: mart, saban
    Qumuqça: mart, örtkiy, nawruz
    Qaraçay-Malqar: mart, totur, awuznu al ayı
    Noğayşa: mart, nawruz
    Sıbırca: mart, ämäl, qarğa
    Gagauzça: baba marta
    Saqalī: kulun tutar
    Dulgan-Hakalī: hıray hılıyar
    Tıvalap: üş
    Salırça: üçinci
    Xakastap: mart
    Xakastap (Sağay): uluğ körik, pastağı körik
    Xakastap (Pîltir): körîk
    Xakastap (Xaas): xaañ
    Altaylap: mart, qandıq
    Şor: körük
    Urumça: mart
    Karajče: (they use Karaim calendar)
    Qrımçahça: mart
    Soyot: mart
    Tofalap: toorbaş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "butter" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жир" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "масло" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yağ":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰖𐰍
🐺 Old Turkic: yağ, öz
🇬🇧 English: oil, butter
🇷🇺 Русский: жир, масло
🇹🇷 Türkçe: yağ
🇦🇿 Türkcə: yağ
🇹🇲 Türkmençe: ýag
🇺🇿 Oʻzbekcha: yogʻ, moy
🇰🇿 Qazaqşa: may
🇰🇬 Qırğızça: may
    Uyghurche: yagh, may
    Tatarça: may
    Başqortsa: may
    Çovaşla: cu
    Qaraqalpaqsha: may
    Qırımtatarca: yağ, may
    Qumuqça: may, yaw
    Qaraçay-Malqar:	jaw
    Noğayşa: may
    Sıbırca: may
    Gagauzça: yaa
    Saqalī: sıa
    Dulgan-Hakalī: hıa
    Tıvalap:	çag, üs
    Salırça: yağ
    Xakastap: xayax, çağ, üs
    Altaylap: cuu, üs
    Şor: çağ, may, qayaq (dialect)
    Urumça: yağ, may
    Karajče: jav (jah), maj
    Qrımçahça: yağ
    Soyot: çağ (cağ), üs
    Tofalap: cağ, üs''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "автомобиль" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "автомашина" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "авторанспорт" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "car" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "automobile" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "otomobil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "motorlu araba":
        bot.send_message(message.chat.id, '''🇬🇧 English: car, automobile
🇷🇺 Русский: автомобиль, машина (автомашина)
🇹🇷 Türkçe: otomobil, araba (motorlu araba)
🇦🇿 Türkcə: avtomobil, maşın
🇹🇲 Türkmençe: awtomobil, maşyn
🇺🇿 Oʻzbekcha: avtomobil, mashina
🇰🇿 Qazaqşa: avtomobil, mäciyne (macıyna, maşina)
🇰🇬 Qırğızça: avtomobil, maşına
🌏 Uyghurche: aptomobil, mashina
🌍 Tatarça: avtomobil (aftomobil — acrhaism), maşına
🌍 Başqortsa: avtomobil, maşına
🌍 Çovaşla: avttomopil (avtomobil), maşşina (maşına)
🌍 Qaraqalpaqsha: avtomobil, mashına
🌍 Qırımtatarca: avtomobil, maşna
🌍 Qumuqça: avtomobil, maşın
🌍 Qaraçay-Malqar: avtomobil, maşına
🌍 Noğayşa: awtomobil, mäşin
🌏 Sıbırca: avtomobil, maşına (maşinä)
🌍 Gagauzça: avtomobil, avto, araba, maşına
🌏 Saqalī: avtomobil, massīna
🌏 Dulgan-Hakalī: avtomobil, massīna
🌏 Tıvalap: çıççan, avtomobil, maşina (maşına)
🌏 Salırça: çiçı (çizı, çiçe)
🌏 Xakastap: avtomobîl, maşına
🌏 Altaylap: avtomobil, maşına
🌏 Şor: avtomobil, maşına
🌍 Urumça: avtamabil, maşına (marışna, marşın, marşına)
🌍 Karajče: avtomobil, mašina (mašyna)
🌍 Qrımçahça: avtomobil, maşına
🌏 Soyot: maşîîn (maşıına, mahîîna)
🌏 Tofalap: maşîîn''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bear" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "медведь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "медвед" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ayı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "медвежий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "медвежья" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "медведица":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰑𐰃𐰍
🇬🇧 English: bear
🇷🇺 Русский: медведь
🇹🇷 Türkçe: ayı
🇦🇿 Türkcə: ayı
🇹🇲 Türkmençe: aýy
🇺🇿 Oʻzbekcha: ayiq
🇰🇿 Qazaqşa: ayıw
🇰🇬 Qırğızça: ayuu
    Uyghurche: éyiq
    Tatarça: ayu
    Başqortsa: ayıw
    Çovaşla: upa
    Qaraqalpaqsha: ayıw
    Qırımtatarca: ayuv
    Qumuqça: ayuw
    Qaraçay-Malqar:	ayıw (ayyu)
    Noğayşa: ayuw
    Sıbırca: aba (ava), ayıw (ayu)
    Gagauzça: ayı, martin
    Saqalıı: ehe
    Dulğan-Hakalıı: ebekē
    Tıvalap: adıg
    Salırça: atıx (ātıx, acıx)
    Xakastap: aba, azığ
    Altay: ayu
    Şor: apşaq, ulda (dialect)
    Urumça: ayu (ai, ayuv)
    Karajče: ajuv
    Qrımçahça: ayuv
    Soyot: adığ, hayraqan (hayraqqan), hayrhan, îre (îrey, îrä, îräy)
    Tofalap: îrezañ (îresañ, eresañ), îre (îrey), çoorhannığ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мёд" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мед" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "honey" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "медовый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "honney":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰉𐰞 
🐺 Old Turkic (bef. 13th c.): bal (bāl), arı yağı, şähd, 'asäl, mir (mır)
🇬🇧 English: honey
🇷🇺 Русский: мёд [myod]
🇲🇳 Mongol: bal
🇹🇷 Türkçe: bal
🇦🇿 Türkcə: bal
🇹🇲 Türkmençe: bal
🇺🇿 Oʻzbekcha: asal, bol
🇰🇿 Qazaqşa: bal
🇰🇬 Qırğızça: bal
🌏 Uyghurche: hesel, bal
🌍 Tatarça: bal
🌍 Başqortsa: bal
🌍 Çovaşla: pıl
🌍 Qaraqalpaqsha: pal
🌍 Qırımtatarca: bal
🌍 Qumuqça: bal
🌍 Qaraçay-Malqar: bal
🌍 Noğayşa: bal
🌏 Sıbırca: pal
🌍 Gagauzça: bal
🌏 Saqalī: müöt
🌏 Dulgan-Hakalī: müöt
🌏 Tıvalap: arı çigiri
🌏 Salırça: pal
🌏 Xakastap: mööt (myod)
🌏 Altaylap: möt, pal (archaism)
🌏 Şor: pal
🌍 Urumça: bal
🌍 Karajče: bal
🌍 Qrımçahça: bal
🌏 Soyot: möot
🌏 Tofalap: möot (nöot)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "минута" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "minute" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dakika" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "minutes" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dakka" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "minuta":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): altı qolu
🇬🇧 English: minute
🇷🇺 Русский: минута [minuta]
🇹🇷 Türkçe: dakika
🇦🇿 Türkcə: dəqiqə
🇹🇲 Türkmençe: minut, dakyka
🇺🇿 Oʻzbekcha: daqiqa
🇰🇿 Qazaqşa: miynut (minut), daqığa (daqıyğa) (archaism)
🇰🇬 Qırğızça: münöt (minuta)
🌏 Uyghurche: deqiqe, minut
🌍 Tatarça: minut, däqiqä
🌍 Başqortsa: minut, däqiqä (archaism)
🌍 Çovaşla: minut
🌍 Qaraqalpaqsha: minut
🌍 Qırımtatarca: daqqa
🌍 Qumuqça: minut
🌍 Qaraçay-Malqar: minut
🌍 Noğayşa: taqıyqa, minuta
🌏 Sıbırca: minut, däqiqä (archaism)
🌍 Gagauzça: dakika
🌏 Saqalī: münǖte
🌏 Dulgan-Hakalī: münǖte (minuta)
🌏 Tıvalap: minut (minuta)
🌏 Salırça: fençoñ
🌏 Xakastap: mînuta
🌏 Altaylap: minut
🌏 Şor: minut (minuta)
🌍 Urumça: dakika, menut (minut)
🌍 Karajče: dakka
🌍 Qrımçahça: daqa
🌏 Soyot: mînuut
🌏 Tofalap: mînuut''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "many" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "much" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "много" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çok":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰜𐰇𐰾
🇬🇧 English: many, much, lot
🇷🇺 Русский: много
🇹🇷 Türkçe: çok
🇦🇿 Türkcə: çox
🇹🇲 Türkmençe: köp
🇺🇿 Oʻzbekcha: koʻp
🇰🇿 Qazaqşa: köp
🇰🇬 Qırğızça: köp
    Uyghurche: köp
    Tatarça: küp
    Başqortsa: küp
    Çovaşla: numay
    Qaraqalpaqsha: kóp
    Qırımtatarca: çoq
    Qumuqça: köp
    Qaraçay-Malqar:	köp (köb)
    Noğayşa: köp
    Sıbırca: kän, cuq, küp, talay
    Gagauzça: çok
    Saqalıı: elbeq, ügüs
    Dulğan-Hakalıı: ügüs, bāl, elbek
    Tıvalap: xöy, kövey
    Salırça: köp (k'op)
    Xakastap: köp
    Altay: köp
    Şor: köp
    Urumça: çox (çok, çoğ), kop, talay
    Karaj: kiop (kiep)
    Qrımçahça: çoq, köp, bol
    Soyot: köp, köhäy (köfäy)
    Tofalap: köp, köpey (köfey)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "musa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "моисей" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moses" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мойша" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мойше" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moshe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moishe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moyshe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moyses":
        bot.send_message(message.chat.id, '''🇬🇧 English: Moses
🇷🇺 Русский: Моисей [Moisey]
🇹🇷 Türkçe: Musa
🇦🇿 Türkcə: Musa
🇹🇲 Türkmençe: Musa
🇺🇿 Oʻzbekcha: Muso
🇰🇿 Qazaqşa: Musa
🇰🇬 Qırğızça: Musa
    Uyghurche: Musa
    Tatarça: Musa
    Başqortsa: Musa
    Çovaşla: Mossa
    Qaraqalpaqsha: Musa
    Qırımtatarca: Musa
    Qumuqça: Musa
    Qaraçay-Malqar: Mussa
    Noğayşa: Musa
    Sıbırca: Musa
    Gagauzça: Musa
    Saqalıı: ???
    Dulğan-Hakalıı: ???
    Tıvalap: ???
    Salırça: ???
    Xakastap: ???
    Altaylap: ???
    Şor: ???
    Urumça: Musa
    Karajče: ???
    Qrımçahça: ???
    Soyot: ???
    Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "husband" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "муж" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "koca" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "er" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "husbant":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰼
🇬🇧 English: husband
🇷🇺 Русский: муж (в значении супруга)
🇲🇳 Mongol: er
🇹🇷 Türkçe: koca, er
🇦🇿 Türkcə: ər, qoca (archaism)
🇹🇲 Türkmençe: är, adamsy
🇺🇿 Oʻzbekcha: er
🇰🇿 Qazaqşa: er, küyew
🇰🇬 Qırğızça: er, küyöw
    Uyghurche: er
    Tatarça: ir
    Başqortsa: ir
    Çovaşla: upoşka
    Qaraqalpaqsha: er, kúyew
    Qırımtatarca: er, aqay, qoca
    Qumuqça: er
    Qaraçay-Malqar: er
    Noğayşa: er, kiyew, bay
    Sıbırca: ir
    Gagauzça: koca
    Saqalıı: er
    Dulğan-Hakalıı: er
    Tıvalap: er, aşak
    Salırça: kuyu, xar
    Xakastap: îri
    Altay: öbögön
    Şor: er
    Urumça: är (er), xoca (oca)
    Karajče: ėr, kodža, ėren
    Qrımçahça: er, qoca
    Soyot: er, aşşâq
    Tofalap: er, aşınâq (aşnâq)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "man" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мужчина" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мужик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "erkek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "adam":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰼
🇬🇧 English: man
🇷🇺 Русский: мужчина, мужик
🇲🇳 Mongol: er
🇹🇷 Türkçe: erkek, adam
🇦🇿 Türkcə: kişi
🇹🇲 Türkmençe: erkek
🇺🇿 Oʻzbekcha: erkak
🇰🇿 Qazaqşa: er, erkek
🇰🇬 Qırğızça: erkek, erkek kişi
    Uyghurche: er, erkek
    Tatarça: ir, ir keşe
    Başqortsa: ir, ir keşe
    Çovaşla: ar, arcın
    Qaraqalpaqsha: erkek
    Qırımtatarca: erkek, aqay
    Qumuqça: erkek, ergişi, eren
    Qaraçay-Malqar:	erkişi, erkengirıw
    Noğayşa: er, erkek
    Sıbırca: ir (är), irän
    Gagauzça: adam, erif, er, erkek
    Saqalıı: er kihi
    Dulğan-Hakalıı: er kihi
    Tıvalap: er kiji
    Salırça: är kişi (ır kiş)
    Xakastap: îr kizi
    Altay: er kiji
    Şor: er kiji
    Urumça: ärgişi (erkişi), er, erkek, er adam
    Karajče: ėr kiši, akaj, ėrien (ėren)
    Qrımçahça: er, erkek
    Soyot: aşşâq, er kîşî
    Tofalap: aşnâq (aşınâq), er kîşî''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "we" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мы" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "biz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bizler":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰋𐰃𐰔	
🇬🇧 English: we
🇷🇺 Русский: мы
🇹🇷 Türkçe: biz, bizler
🇦🇿 Türkcə: biz, bizlər
🇹🇲 Türkmençe: biz, bizler
🇺🇿 Oʻzbekcha: biz, bizlar
🇰🇿 Qazaqşa: biz, bizder
🇰🇬 Qırğızça: biz, bizder
    Uyghurche: biz, bizler
    Tatarça: bez, bezlär
    Başqortsa: beð, beððär
    Çovaşla: epir
    Qaraqalpaqsha: biz, bizler
    Qırımtatarca: biz, bizler
    Qumuqça: biz
    Qaraçay-Malqar: biz
    Noğayşa: biz
    Sıbırca: pes (bez, biz), bizlär (peslär)
    Gagauzça: biz, bizler
    Saqalıı: bihigi
    Hakalıı (Dulgan):	bihigi
    Tıvalap: bis, bister
    Salırça: piser (peser, pisä)
    Xakastap: pis
    Altay: bis
    Şor: pis
    Urumça: biz
    Karaj: biź (biz, bis)
    Qrımçahça: bız
    Soyot: bîs, bîstêr
    Tofalap: bîs, bîstêr''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "meat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "flesh" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мясо" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "et" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мяско":
        bot.send_message(message.chat.id, '''🇬🇧 English: meat, flesh
🇷🇺 Русский: мясо
🇹🇷 Türkçe: et
🇦🇿 Türkcə: ət
🇹🇲 Türkmençe: et
🇺🇿 Oʻzbekcha: et, goʻsht
🇰🇿 Qazaqşa: et
🇰🇬 Qırğızça: et
    Uyghurche: et, gösh
    Tatarça: it
    Başqortsa: it
    Çovaşla: aş, kakay
    Qaraqalpaqsha: et, gósh
    Qırımtatarca: et
    Qumuqça: et
    Qaraçay-Malqar:	et
    Noğayşa: et
    Sıbırca: it, küş
    Gagauzça: et, yaanı (yahnı)
    Saqalī: et
    Dulgan-Hakalī: et
    Tıvalap: et
    Salırça: ät
    Xakastap: ît
    Altaylap: et
    Şor: et
    Urumça: ät (et, yet)
    Karajče: ėt
    Qrımçahça: et
    Soyot: et
    Tofalap: et''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "not" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "не" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "değil":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰖𐰆𐰸
🇬🇧 English: not
🇷🇺 Русский: не
🇹🇷 Türkçe: değil, yok
🇦🇿 Türkcə: deyil, yox
🇹🇲 Türkmençe: däl
🇺🇿 Oʻzbekcha: emas, yo'q
🇰🇿 Qazaqşa: emes
🇰🇬 Qırğızça: emes
    Uyghurche: emes, yoq
    Tatarça: tügel
    Başqortsa: tügel
    Çovaşla: cuk
    Qaraqalpaqsha: emes
    Qırımtatarca: degil, yoq
    Qumuqça: tügül
    Qaraçay-Malqar:	tüyül, tüyüldü, tül
    Noğayşa: tuwıl
    Sıbırca: tügel (tügıl), imäs (imēs)
    Gagauzça: diil
    Saqalıı: suoq
    Dulgan-Hakalıı: huok
    Tıvalap:	eves, çok
    Salırça: emes, emesar, yox
    Xakastap: nîmes, çox
    Altay: emes
    Şor: ebes
    Urumça: dögül (dügül, döül, deyil, degil, tügül, döl, deil)
    Karaj: tiuviul´ (tivil, tiugiul´), joch
    Qrımçahça: dugul
    Soyot: emes (emäs), coq (çoq)
    Tofalap: emes, çoq''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "no" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "нет" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yok" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hayır" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hayir":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰖𐰸 (𐰖𐰆𐰸)
🐺 Old Turkic: I. yoq (yōq) II. yoq (yo)
🇬🇧 English: I. no (absence) II. no (abnegation)
🇷🇺 Русский: I. нет (отсутствие) II. нет (отрицание)
🇹🇷 Türkçe: I. yok II. hayır, yok
🇦🇿 Türkcə: I. yox II. xeyr (formal), yox (informal), yo (informal)
🇹🇲 Türkmençe: ýok
🇺🇿 Oʻzbekcha: yoq
🇰🇿 Qazaqşa: joq
🇰🇬 Qırğızça: joq
    Uyghurche: yoq
    Tatarça: yuq
    Başqortsa: yuq
    Çovaşla: cuk
    Qaraqalpaqsha: yaq
    Qırımtatarca: I. yoq II. yoq, hayır (archaism)
    Qumuqça: yoq
    Qaraçay-Malqar:	I. joq II. oğay, joq (archaism)
    Noğayşa: yoq
    Sıbırca: yoq
    Gagauzça: yok
    Saqalī: suoq
    Dulgan-Hakalī: huok
    Tıvalap: çok
    Salırça: yox
    Xakastap: çox
    Altaylap: coq
    Şor: çoq
    Urumça: I. yox II. xayır, yox (yo)
    Karajče: I. joch (jok) II. jo (joch, jok)
    Qrımçahça: yoh
    Soyot: I. çoq (coq) II. çoq (coq), tañ
    Tofalap: I. yoq (çoq, coq) II. yoq (çoq, coq), tañ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sky" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "heaven" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "небо" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "небеса" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "небесный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gök" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sema" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "asuman":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱅𐰭𐰼𐰃
🇬🇧 English: sky, heaven
🇷🇺 Русский: небо [nebo]
🇹🇷 Türkçe: gök, sema, asuman
🇦🇿 Türkcə: göy, səma, asiman, fələk, əsman (dialect)
🇹🇲 Türkmençe: gök, asman
🇺🇿 Oʻzbekcha: koʻk, osmon, falak
🇰🇿 Qazaqşa: aspan, kök
🇰🇬 Qırğızça: kök, asman
    Uyghurche: asman, kök
    Tatarça: kük, säma, asman
    Başqortsa: kük, säma, asman
    Çovaşla: pölöt, tüpe
    Qaraqalpaqsha: kók, aspan
    Qırımtatarca: kök, sema, felek
    Qumuqça: kök
    Qaraçay-Malqar:	kök
    Noğayşa: kök, aspan
    Sıbırca: kük, asman, fäläk, teñgeri (archaism)
    Gagauzça: gök
    Saqalī: qallān
    Dulgan-Hakalī: kallān
    Tıvalap: deer, deer-deñger
    Salırça: asman (asmän, asmen), sāmu (samo)
    Xakastap: tîgir
    Altaylap: teneri
    Şor: tegri
    Urumça: kök (gög)
    Karajče: kiok, feliek
    Qrımçahça: kök, felek
    Soyot: deêrî, asar-deêri
    Tofalap: deêri''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "several" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "a few" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "несколько" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "birkaç":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰽𐰣𐰍𐰞𐰃
🇬🇧 English: several, a few
🇷🇺 Русский: несколько
🇹🇷 Türkçe: birkaç
🇦🇿 Türkcə: bir neçə
🇹🇲 Türkmençe: birnäçe
🇺🇿 Oʻzbekcha: bir necha
🇰🇿 Qazaqşa: birneşe
🇰🇬 Qırğızça: bir neçe
    Uyghurche: bir nechche
    Tatarça:	berniçä
    Başqortsa: ber nisä
    Çovaşla: pörer, temice
    Qaraqalpaqsha: bir neshe
    Qırımtatarca: bir qaç, bir talay (dialect)
    Qumuqça: bir neçe
    Qaraçay-Malqar:	bur nença, bir talay
    Noğayşa: bir neşe
    Sıbırca: pernicä, az-awlaq, berär äwüs
    Gagauzça: birkaç
    Saqalıı: qas da
    Dulgan-Hakalıı: kas da
    Tıvalap: kaş, bir kaş
    Salırça: pir āhıs
    Xakastap: nince-de, köp nîmes
    Altay: bir qança
    Şor: köp ebes
    Urumça: birğaç (bir xaç)
    Karaj: bir niečia (birneče), bir kač
    Qrımçahça: bır qaç, talay
    Soyot: bir qaş, bir çehä
    Tofalap: bir qaş, bir çehe, bir kesek''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "николай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "николя" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "коля" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "колька" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nicholas" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "колясик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nikolay" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "никол" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nikol" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "niko":
        bot.send_message(message.chat.id, '''🇬🇧 English: Nicholas
🇷🇺 Русский: Николай, Коля
🇦🇿 Türkcə: Niqalay
🌍 Çovaşla: Mikka (Mikula, Mikulay)
🌍 Qaraçay-Malqar: Nikkol (Mikkol)
🌏 Şor: Muqayla
🌍 Urumça: Nokola (Nikola)
🌏 Soyot: Mıhılay
    ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "new" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "a new" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "новый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "новая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "новое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "новые" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yeni":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰖𐰭𐰃
🐺 Old Turkic (bef. 13th c.): yaŋı
🇬🇧 English: new
🇷🇺 Русский: новый (-ая, -ое) [novy]
🇹🇷 Türkçe: yeni
🇦🇿 Türkcə: yeni, təzə
🇹🇲 Türkmençe: täze
🇺🇿 Oʻzbekcha: yangi
🇰🇿 Qazaqşa: jaŋa
🇰🇬 Qırğızça: jaŋı
🌏 Uyghurche: yengi
🌍 Tatarça: yaña
🌍 Başqortsa: yañı
🌍 Çovaşla: cönö
🌍 Qaraqalpaqsha: jańa
🌍 Qırımtatarca: yañı
🌍 Qumuqça: yañı
🌍 Qaraçay-Malqar: jañı
🌍 Noğayşa: yañı
🌏 Sıbırca: yaña
🌍 Gagauzça: eni (yeni)
🌏 Saqalī: saña
🌏 Dulgan-Hakalī: haña
🌏 Tıvalap: çaa
🌏 Salırça: yañı
🌏 Xakastap: naa
🌏 Altaylap: canı
🌏 Şor: naa
🌍 Urumça: yañı (yeni, yana), teze (taze)
🌍 Karajče: jangy (janhy, jany)
🌍 Qrımçahça: yengı
🌏 Soyot: nâa
🌏 Tofalap: nâa''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fingernail" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tırnak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tirnak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ноготь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ногти" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ноготок":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): tırñaq (tıñraq, tıñaraq)
🇬🇧 English: fingernail
🇷🇺 Русский: ноготь [noɡotʲ]
🇹🇷 Türkçe: tırnak
🇦🇿 Türkcə: dırnaq
🇹🇲 Türkmençe: dyrnak
🇺🇿 Oʻzbekcha: tirnoq
🇰🇿 Qazaqşa: tırnaq
🇰🇬 Qırğızça: tırmaq
🌏 Uyghurche: tirnaq
🌍 Tatarça: tırnaq
🌍 Başqortsa: tırnaq
🌍 Çovaşla: çörne
🌍 Qaraqalpaqsha: tırnaq
🌍 Qırımtatarca: tırnaq
🌍 Qumuqça: tırnaq
🌍 Qaraçay-Malqar: tırnaq
🌍 Noğayşa: tırnaq
🌏 Sıbırca: tırnaq
🌍 Gagauzça: tırnak
🌏 Saqalī: tıñıraq
🌏 Dulgan-Hakalī: tıñırak
🌏 Tıvalap: dırgak
🌏 Salırça: tırnax
🌏 Xakastap: tırgax
🌏 Altaylap: tırmaq
🌏 Şor: tırbaq
🌍 Urumça: dırnax (tırnax)
🌍 Karajče: tyrnak (tyrnach)
🌍 Qrımçahça: tırnah
🌏 Soyot: dırğaq (tırğaq)
🌏 Tofalap: dırbaq''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nose" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nos" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "нос" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "burun":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): burun
🇬🇧 English: nose
🇷🇺 Русский: нос [nos]
🇹🇷 Türkçe: burun
🇦🇿 Türkcə: burun
🇹🇲 Türkmençe: burun
🇺🇿 Oʻzbekcha: burun
🇰🇿 Qazaqşa: murın
🇰🇬 Qırğızça: murun
🌏 Uyghurche: burun
🌍 Tatarça: borın
🌍 Başqortsa: tanaw, moron
🌍 Çovaşla: somsa
🌍 Qaraqalpaqsha: murın
🌍 Qırımtatarca:	burun
🌍 Qumuqça: burun
🌍 Qaraçay-Malqar: burun
🌍 Noğayşa: burın
🌏 Sıbırca: poron
🌍 Gagauzça: burnu
🌏 Saqalī: murun
🌏 Dulgan-Hakalī: munnu
🌏 Tıvalap: dumçuk, xaay, murnu
🌏 Salırça: purnu (purnı)
🌏 Xakastap: purun
🌏 Altaylap: tumçuq
🌏 Şor: purnu
🌍 Urumça: burun
🌍 Karajče: burun (borun)
🌍 Qrımçahça: burun
🌏 Soyot: haay
🌏 Tofalap: haay''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "night" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ночь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gece" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gice" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ночной":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱅𐰇𐰤
🐺 Old Turkic: tün, keçä
🇬🇧 English: night
🇷🇺 Русский: ночь [noch']
🇹🇷 Türkçe: gece
🇦🇿 Türkcə: gecə
🇹🇲 Türkmençe: gije
🇺🇿 Oʻzbekcha: tun, kecha
🇰🇿 Qazaqşa: tün
🇰🇬 Qırğızça: tün
    Uyghurche: tün, kéche, kech
    Tatarça: tön
    Başqortsa: tön
    Çovaşla: kac, cör, cörle
    Qaraqalpaqsha: tún
    Qırımtatarca: gece
    Qumuqça: geçe
    Qaraçay-Malqar:	keçe
    Noğayşa: tün
    Sıbırca: tön
    Gagauzça: gecä
    Saqalī: tǖn
    Dulgan-Hakalī: tǖn
    Tıvalap: dün
    Salırça: gece (kece)
    Xakastap: xaraa, tün
    Altaylap: tün
    Şor: tün
    Urumça: gecä (kece, yece)
    Karajče: kiečia (giedžie, kedže), kieč (kec), tiuń
    Qrımçahça: gece (keçe)
    Soyot: tün, tünnä (dünnä)
    Tofalap: tün, tünnê (dünnê)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "november" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "novembre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ноябрь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kasım" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kasim":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: november
🇷🇺 Русский: ноябрь [noyabr']
🇹🇷 Türkçe: kasım
🇦🇿 Türkcə: noyabr, təşrini-sani
🇹🇲 Türkmençe: sanjar
🇺🇿 Oʻzbekcha: noyabr, qavs
🇰🇿 Qazaqşa: qaraşa, qawıs
🇰🇬 Qırğızça: jetinin ayı
    Uyghurche: oghlaq
    Tatarça: nuyäber, qaraköz, qasım
    Başqortsa: qırpağay
    Çovaşla: çük
    Qaraqalpaqsha: noyabr, qawıs
    Qırımtatarca: noyabr, boş ay
    Qumuqça: noyabr, mayyilik
    Qaraçay-Malqar: noyabr, abıstol
    Noğayşa: noyabr, qaraşa
    Sıbırca: noyabr, qawıs, kece sıwıq
    Gagauzça: kasım
    Saqalī: setinńi
    Dulgan-Hakalī: kün tüher
    Tıvalap: on bir
    Salırça: ompirinci
    Xakastap: noyabr
    Xakastap (Sağay): kiçig xırlas
    Xakastap (Pîltir): kiçig xırlas
    Xakastap (Xaas): uluğ soox
    Altaylap: noyabr, küçürgen
    Şor: kiçig qırlaş
    Urumça: noyemberos
    Karajče: (they use Karaim calendar)
    Qrımçahça: noyabr
    Soyot: noyabr
    Tofalap: aldılaar''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "1" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "one" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "один":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰋𐰃𐰼 
🇬🇧 English: one
🇷🇺 Русский: один [odin]
🇹🇷 Türkçe: bir
🇦🇿 Türkcə: bir
🇹🇲 Türkmençe: bir
🇺🇿 Oʻzbekcha: bir
🇰🇿 Qazaqşa: bir
🇰🇬 Qırğızça: bir
    Uyghurche: bir
    Tatarça: ber
    Başqortsa: ber
    Çovaşla: pör
    Qaraqalpaqsha: bir
    Qırımtatarca: bir
    Qumuqça: bir
    Qaraçay-Malqar: bir
    Noğayşa: bir
    Sıbırca: per
    Gagauzça: bir
    Saqalıı: bïr
    Tıvalap: bir
    Salırça: pir (bir, per)
    Xakastap: pir
    Altay: bir
    Şor: pir
    Dolgan: bïr
    Soyot: bir
    Urumça: bir
    Karaj: bir
    Qrımçahça: bır
    Tofalap: bir''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "озеро" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "озёрный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "озерный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lake" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "göl":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰚𐰇𐰠
🐺 Old Turkic (bef. 13th c.): köl, kölman (little lake)
🇬🇧 English: lake
🇷🇺 Русский: озеро [ozero]
🇹🇷 Türkçe: göl
🇦🇿 Türkcə: göl
🇹🇲 Türkmençe: köl
🇺🇿 Oʻzbekcha: koʻl
🇰🇿 Qazaqşa: köl
🇰🇬 Qırğızça: köl
🌏 Uyghurche: köl
🌍 Tatarça: kül
🌍 Başqortsa: kül
🌍 Çovaşla: külö
🌍 Qaraqalpaqsha: kól
🌍 Qırımtatarca: göl
🌍 Qumuqça: köl
🌍 Qaraçay-Malqar: köl
🌍 Noğayşa: köl
🌏 Sıbırca: kül
🌍 Gagauzça: göl
🌏 Saqalī: küöl
🌏 Dulgan-Hakalī: küöl
🌏 Tıvalap: xöl
🌏 Salırça: göl
🌏 Xakastap: köl
🌏 Altaylap: köl
🌏 Şor: köl
🌍 Urumça: göl (köl)
🌍 Karajče: giol'
🌍 Qrımçahça: göl
🌏 Soyot: höl
🌏 Tofalap: höl''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "october" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "octobre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "октябрь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ekim" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ekim ayi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ekim ayı":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: october
🇷🇺 Русский: октябрь [oktyabr']
🇹🇷 Türkçe: ekim
🇦🇿 Türkcə: oktyabr, təşrini-əvvəl
🇹🇲 Türkmençe: garaşsyzlyk
🇺🇿 Oʻzbekcha: oktabr, aqrab
🇰🇿 Qazaqşa: qazan, aqırap
🇰🇬 Qırğızça: toğuzdun ayı
    Uyghurche: oghuz
    Tatarça: üktäber, bilek
    Başqortsa: qarasay
    Çovaşla: yupa
    Qaraqalpaqsha: oktyabr, aqirap
    Qırımtatarca: oktâbr, ekin
    Qumuqça: oktyabr, baysan
    Qaraçay-Malqar: oktyabr, etıyıq
    Noğayşa: oktyabr, qazan
    Sıbırca: oktyabr, aqrap, yalañ ağac
    Gagauzça: canavar
    Saqalī: altınńı
    Dulgan-Hakalī: būs toñor
    Tıvalap: on
    Salırça: onıncı
    Xakastap: oktyabr
    Xakastap (Sağay): çarığ
    Xakastap (Pîltir): çarığ
    Xakastap (Xaas): kiçig soox
    Altaylap: oktyabr, ülürgen
    Şor: qurtuyaq
    Urumça: oktovrioz
    Karajče: (they use Karaim calendar)
    Qrımçahça: oktyabr
    Soyot: oktyabr
    Tofalap: küzäär''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "o" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "he" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "she" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "он" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "она" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "оно":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰆𐰞 
🇬🇧 English: he, she, it
🇷🇺 Русский: он, она, оно
🇹🇷 Türkçe: o
🇦🇿 Türkcə: o
🇹🇲 Türkmençe: ol
🇺🇿 Oʻzbekcha: u
🇰🇿 Qazaqşa: ol
🇰🇬 Qırğızça: al
    Uyghurche: u
    Tatarça: ul
    Başqortsa: ul
    Çovaşla: vol
    Qaraqalpaqsha: ol
    Qırımtatarca: o
    Qumuqça: ol
    Qaraçay-Malqar: ol
    Noğayşa: ol
    Sıbırca: u (ul)
    Gagauzça: o
    Saqalıı: kini
    Tıvalap: ol
    Salırça: o (u, vu, ū)
    Xakastap: ol
    Altay: ol
    Şor: ol
    Dolgan: gini
    Soyot: ol
    Urumça: o
    Karaj: ol
    Qrımçahça: o (ol)
    Tofalap: oñ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "they" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "они" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "onlar":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰆𐰞𐰺
🇬🇧 English: they
🇷🇺 Русский: они [oni]
🇹🇷 Türkçe: onlar
🇦🇿 Türkcə: onlar
🇹🇲 Türkmençe: olar
🇺🇿 Oʻzbekcha: ular
🇰🇿 Qazaqşa: olar
🇰🇬 Qırğızça: alar
    Uyghurche: ular
    Tatarça: alar
    Başqortsa: ular
    Çovaşla: vösem
    Qaraqalpaqsha: olar
    Qırımtatarca: olar
    Qumuqça: olar
    Qaraçay-Malqar: ala
    Noğayşa: olar
    Sıbırca: alar (anlar)
    Gagauzça: onnar
    Saqalıı: kiniler
    Hakalıı (Dulğan): giniler
    Tıvalap: olar
    Salırça: ular (vullar)
    Xakastap: olar
    Altay: olor
    Şor: ılar
    Urumça: onnar (olar, alar, onlar, ular)
    Karaj: alar
    Qrımçahça: olar
    Soyot: olar, olarlar
    Tofalap: olar (oñnar)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "değnek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çubuk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "stick" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "палка":
        bot.send_message(message.chat.id, '''🇬🇧 English: stick
🇷🇺 Русский: палка
🇹🇷 Türkçe: değnek, çubuk, dayak
🇦🇿 Türkcə: çubuq, çöp, çomaq, əsa, əl ağacı, şıvırtı (dialect), tubulqu (dialect), milil (dialect)
🇹🇲 Türkmençe: çöp, taýak
🇺🇿 Oʻzbekcha: yogʻoch, tayoq
🇰🇿 Qazaqşa: tayaq, şıbıq
🇰🇬 Qırğızça: tayaq
    Uyghurche: choqmaq, tayaq, soyla
    Tatarça: tayaq
    Başqortsa: botaq, sıbıq
    Çovaşla: patak, tuya
    Qaraqalpaqsha: tayaq
    Qırımtatarca: çubuq
    Qumuqça: tayaq
    Qaraçay-Malqar:	tayaq
    Noğayşa: tayaq
    Sıbırca: tayaq
    Gagauzça: pardı, sopa, diynek, çıbık, çomag
    Saqalī: mas, tayaq
    Dulğan-Hakalī: mas
    Tıvalap: buduk, dayangıış, merge, sıp
    Salırça: tāğu, peñger
    Xakastap: tayax
    Altaylap: tayaq
    Şor: tayaq
    Urumça: tayax, çubux, dägänäk, sopa
    Karajče: tajak (tajach), čubuk, sopa
    Qrımçahça: tayax, sopa, çubuq
    Soyot: tayaq
    Tofalap: tayaq, merhe''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dad" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "daddy" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "father" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "папа" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "отец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "baba" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ata":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰲𐰃, 𐱃𐰀
🇬🇧 English: dad, father
🇷🇺 Русский: папа [papa], отец [otets]
🇹🇷 Türkçe: baba, ata
🇭🇺 Magyar: atya, apa
🇦🇿 Türkcə: ata, dədə, qaqa (qağa) (dialect)
🇹🇲 Türkmençe: kaka, däde, ata
🇺🇿 Oʻzbekcha: ota, ada
🇰🇿 Qazaqşa: äke, ata
🇰🇬 Qırğızça: ata
    Uyghurche: dada, ata
    Tatarça: ata (atay), äti
    Başqortsa: ata (atay)
    Çovaşla: atte
    Qaraqalpaqsha: áke, ata
    Qırımtatarca: ata, baba
    Qumuqça: ata
    Qaraçay-Malqar:	ata, attya (dialect)
    Noğayşa: ata, aqay
    Sıbırca: ätkä (ätkäw), ata, cicä
    Gagauzça: boba, tätü, ata, baka
    Saqalıı: ağa
    Dulğan-Hakalıı: aga, tēte
    Tıvalap: ada, aça
    Salırça: ata (eto), apa (aba, ava, apı)
    Xakastap: aba, ada
    Altay: ada
    Şor: aba, ada
    Urumça: baba, ata
    Karajče: ata, baba, avi
    Qrımçahça: ata, baba
    Soyot: ata, aça (aca)
    Tofalap: ata, aca''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "parlament" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "парламент" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "parliament" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "parlamento":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): qurultay
🇬🇧 English: parliament, Parliament of the United Kingdom of Great Britain and Northern Ireland 
🇷🇺 Русский: парламент, Федеральное собрание Российской Федерации
🇹🇷 Türkçe: parlamento, Türkiye Büyük Millet Meclisi
    🇨🇾🇹🇷 Türkçe: parlamento, Cumhuriyet Meclisi
🇦🇿 Türkcə: parlament, məclisi-dövlə (archaism), Azərbaycan Respublikasının Milli Məclisi
🇹🇲 Türkmençe: parlament, millet mejlisi (archaism), Türkmenistanyň Mejlisi
🇺🇿 Oʻzbekcha: parlament, vakillar majlisi (archaism), Oliy Majlis
🇰🇿 Qazaqşa: parlament, Qazaqstan Respublikasınıŋ Parlamenti (Senat & Mäjilis)
🇰🇬 Qırğızça: parlament, Qırğız Respublikasının Joğorqu Keñeşi
🌏 Uyghurche: parlamént
🌍 Tatarça: parlament
🌍 Başqortsa: parlament
🌍 Çovaşla: parlament
🌍 Qaraqalpaqsha: parlament
🌍 Qırımtatarca: parlament, toplaşma (archaism)
🌍 Qumuqça: parlament
🌍 Qaraçay-Malqar: parlament
🌍 Noğayşa: parlament
🌏 Sıbırca: parlament
🌍 Gagauzça: meclis, parlament
🌏 Saqalī: parlament
🌏 Dulgan-Hakalī: parlament
🌏 Tıvalap: parlament
🌏 Salırça: parlament
🌏 Xakastap: parlament
🌏 Altaylap: parlament
🌏 Şor: parlament
🌍 Urumça: parlament
🌍 Karajče: parlament
🌍 Qrımçahça: parlament
🌏 Soyot: parlament
🌏 Tofalap: parlament''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "karaciğer" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bağır" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "liver" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "печень" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kara ciğer" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ливерная":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): bağır
🇬🇧 English: liver
🇷🇺 Русский: печень [pechen']
🇹🇷 Türkçe: karaciğer, bağır
🇦🇿 Türkcə: ciyər, qaraciyər, bağır
🇹🇲 Türkmençe: bagyr
🇺🇿 Oʻzbekcha: baghir, jigar
🇰🇿 Qazaqşa: bawır
🇰🇬 Qırğızça: boor
🌏 Uyghurche: jiger, beghir
🌍 Tatarça: bawır
🌍 Başqortsa: bawır
🌍 Çovaşla: pöver
🌍 Qaraqalpaqsha: bawır
🌍 Qırımtatarca: qara ciger, bavur (dialect)
🌍 Qumuqça: bawur
🌍 Qaraçay-Malqar: bawur
🌍 Noğayşa:	bawır
🌏 Sıbırca: pawır
🌍 Gagauzça: cer, karacer
🌏 Saqalī: bıar
🌏 Dulgan-Hakalī: bıar
🌏 Tıvalap: baar
🌏 Salırça: bāğır
🌏 Xakastap: paar
🌏 Altaylap: buur
🌏 Şor: paar
🌍 Urumça: bağır (bavur), ğara cigär, ciger
🌍 Karajče: bavur (bavyr, bahyr), džijer (džyger)
🌍 Qrımçahça: bağır
🌏 Soyot: baar
🌏 Tofalap: baar''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "raf" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "полка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shelf" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "полочка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shelves":
        bot.send_message(message.chat.id, '''🇬🇧 English: shelf
🇷🇺 Русский: полка [polka]
🇹🇷 Türkçe: raf
🇦🇿 Türkcə: rəf, zeh (dialect), xiristan (dialect), xursan (dialect), irəmə (dialect), barımbaşı (dialect), ləmə (dialect), taxtavend (for dishes) (dialect), tərəh (tərək) (dialect)
🇹🇲 Türkmençe: tekje
🇺🇿 Oʻzbekcha: tokcha
🇰🇿 Qazaqşa: söre, tekşe
🇰🇬 Qırğızça: tekçe
    Uyghurche: tekche, jaza
    Tatarça: kiştä
    Başqortsa: käştä
    Çovaşla: sülök, xutlox, kaşta, poros (dialect), lapka (dialect)
    Qaraqalpaqsha: tekshe
    Qırımtatarca: raf
    Qumuqça: taqça
    Qaraçay-Malqar: tapxa (tapka)
    Noğayşa: ündirik
    Sıbırca: kiştä
    Gagauzça: sergen, raf
    Saqalī: dolbūr
    Dulgan-Hakalī: koloruk
    Tıvalap: booluk
    Salırça: cazi
    Xakastap: ilgör
    Altaylap: taqta
    Şor: aşqı
    Urumça: raf (rap), täräk (terek)
    Karajče: raf (rav), sustram
    Qrımçahça: raf
    Soyot: taq
    Tofalap: taq, orhu (cabinet shelf)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "польша" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "polska" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "poland" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "polonya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lehistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "стронг":
        bot.send_message(message.chat.id, '''🇬🇧 English: Poland
🇷🇺 Русский: Польша [Pol'sha]
🇹🇷 Türkçe: Polonya, Lehistan (archaism)
🇦🇿 Türkcə: Polşa, Lehistan (archaism), Löhüstan (archaism, dialect)
🇹🇲 Türkmençe: Polşa
🇺🇿 Oʻzbekcha: Polsha
🇰🇿 Qazaqşa: Polşa
🇰🇬 Qırğızça: Polşa
🌏 Uyghurche: Lehistan
🌍 Tatarça: Poloniä, Polşa, Läxstan
🌍 Başqortsa: Polşa, Läxstan
🌍 Çovaşla: Polşa
🌍 Qaraqalpaqsha: Polsha
🌍 Qırımtatarca: Lehistan, Poloniya, Köral (archaism)
🌍 Qumuqça: Polşa, Lehistan
🌍 Qaraçay-Malqar: Polşa
🌍 Noğayşa: Polşa
🌏 Sıbırca: Polşa, Läxstan
🌍 Gagauzça: Polşa, Lehistan, Poloniya
🌏 Saqalī: Polşa
🌏 Dulgan-Hakalī: Polşa
🌏 Tıvalap: Polşa
🌏 Salırça: Bolan
🌏 Xakastap: Polşa
🌏 Altaylap: Polşa
🌏 Şor: Polşa
🌍 Urumça: Polonia
🌍 Karajče: Liachistan, Liachija, Esav, Lech Jer, Polonija, Liach, Liach-bijligi
🌍 Qrımçahça: Esav
🌏 Soyot: Polşa
🌏 Tofalap: Polşa
In Polish: Polska''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oruç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "говенье" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fasting" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пост" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ураза" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oraza" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ruza" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oruc" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sawm" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "siyam" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ораза":
        bot.send_message(message.chat.id, '''🇬🇧 English: fasting
🇷🇺 Русский: пост (говенье)
🇹🇷 Türkçe: oruç
🇦🇿 Türkcə: oruc, ruzə
🇹🇲 Türkmençe: oraza, agyz bekleme
🇺🇿 Oʻzbekcha: roʻza
🇰🇿 Qazaqşa: oraza
🇰🇬 Qırğızça: orozo
    Uyghurche: roza
    Tatarça: uraza
    Başqortsa: uraða
    Çovaşla: tipö
    Qaraqalpaqsha: oraza
    Qırımtatarca: oraza
    Qumuqça: oraza
    Qaraçay-Malqar: oraza, tıyıw
    Noğayşa: oraza
    Sıbırca: urasa (ōraza, uraza)
    Gagauzça: horuç (oruç)
    Saqalıı: kurānaq künneï
    Hakalıı (Dulğan): kurānak künneï
    Tıvalap: mastık, şeer
    Salırça: ???
    Xakastap: oraza, çağban tuzı
    Altay: orozo
    Şor: oraza
    Urumça: oruc (oruç)
    Karaj: oruč (oryč, oruc)
    Qrımçahça: oruç
    Soyot: ???
    Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "prezident" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "president" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "президент" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cumhurbaşkanı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cumhurbaşkani" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cumhurbaşkan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cumhur başkanı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cumhur başkan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "praesidens":
        bot.send_message(message.chat.id, '''🇬🇧 English: president (head of state)
🇷🇺 Русский: президент [prezident]
🇹🇷 Türkçe: cumhurbaşkanı, başkan, reis-i cumhur (archaism)
🇦🇿 Türkcə: prezident, zeim (زعىم) (archaism), rəis cümhur (dialect)
🇹🇲 Türkmençe: prezident, jemhuriýet başlygy (archaism), il-han (archaism)
🇺🇿 Oʻzbekcha: prezident
🇰🇿 Qazaqşa: elbası, prezident
🇰🇬 Qırğızça: prezident
🌏 Uyghurche: prézidént, zuñtuñ, dölet reisi
🌍 Tatarça: prezident, räis, ilbaş (ilbaşı)
🌍 Başqortsa: prezident
🌍 Çovaşla: prezident
🌍 Qaraqalpaqsha: prezident
🌍 Qırımtatarca: prezident, baş (archaism)
🌍 Qumuqça: prezident
🌍 Qaraçay-Malqar: prezident
🌍 Noğayşa: prezident
🌏 Sıbırca: prezident
🌍 Gagauzça: başkan, prezident
🌏 Saqalī: beresijien
🌏 Dulgan-Hakalī: prezident
🌏 Tıvalap: prezident
🌏 Salırça: baş
🌏 Xakastap: prezîdent
🌏 Altaylap: prezident
🌏 Şor: prezident
🌍 Urumça: prizident
🌍 Karajče: prezident
🌍 Qrımçahça: ulusbaşqanı
🌏 Soyot: prezîdent
🌏 Tofalap: prezîdent''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "птица" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bird" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kuş":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰆𐰽
🇬🇧 English: bird
🇷🇺 Русский: птица [ptitsa]
🇹🇷 Türkçe: kuş
🇦🇿 Türkcə: quş
🇹🇲 Türkmençe: guş
🇺🇿 Oʻzbekcha: qush
🇰🇿 Qazaqşa: qus
🇰🇬 Qırğızça: quş
    Uyghurche: qush
    Tatarça: qoş
    Başqortsa: qoş
    Çovaşla: kayok, kayok-köşök
    Qaraqalpaqsha: qus
    Qırımtatarca: quş
    Qumuqça: quş
    Qaraçay-Malqar:	çıpçıq, quş
    Noğayşa: qus
    Sıbırca: qoş
    Gagauzça: kuş
    Saqalıı: kötör, çīçāq
    Dulğan-Hakalıı: kötör
    Tıvalap: kuş
    Salırça: quş
    Xakastap: xus
    Altaylap: quş
    Şor: quş
    Urumça: xuş (ğuş)
    Karajče: kuš (kus), čypčych (cypcyk)
    Qrımçahça: quş
    Soyot: quş, quşqaş
    Tofalap: quşqaş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пять" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "5" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "five" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "beş":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰋𐰾 ,𐰋𐰀𐱁
🇬🇧 English: five
🇷🇺 Русский: пять [pyat']
🇹🇷 Türkçe: beş
🇦🇿 Türkcə: beş
🇹🇲 Türkmençe: bäş
🇺🇿 Oʻzbekcha: besh
🇰🇿 Qazaqşa: bes
🇰🇬 Qırğızça: beş
    Uyghurche: besh
    Tatarça: biş
    Başqortsa: biş
    Çovaşla: pilök (pillök)
    Qaraqalpaqsha: bes
    Qırımtatarca: beş
    Qumuqça: beş
    Qaraçay-Malqar: beş
    Noğayşa: bes
    Sıbırca: biş
    Gagauzça: beş
    Saqalıı: bies
    Tıvalap: beş
    Salırça: peş (beş)
    Xakastap: pis
    Altay: beş
    Şor: peş
    Dolgan: bies
    Urumça: beş
    Karaj: bieš
    Qrımçahça: beş
    Soyot: beş
    Tofalap: beş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "child" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ребёнок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ребенок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çocukçocuk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "evlat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uşak":
        bot.send_message(message.chat.id, '''🇬🇧 English: child
🇷🇺 Русский: ребёнок
🇹🇷 Türkçe: çocuk, evlat, uşak (dialect)
🇦🇿 Türkcə: bala, uşaq, övlad, səbi (rarely)
🇹🇲 Türkmençe: çaga, perzent
🇺🇿 Oʻzbekcha: bola, farzand
🇰🇿 Qazaqşa: bala
🇰🇬 Qırğızça: bala
    Uyghurche: bala, bovaq
    Tatarça: bala, sabıy, näni
    Başqortsa: bala, sabıy, bäpes
    Çovaşla: aça
    Qaraqalpaqsha: bala
    Qırımtatarca: bala, evlât (evlâd), çocuq (dialect)
    Qumuqça: bala, sabiy
    Qaraçay-Malqar:	bala, sabiy
    Noğayşa: bala, äwlet
    Sıbırca: pala
    Gagauzça: uşak, evlât, çocuk
    Saqalıı: oğo
    Dulğan-Hakalıı: ogo
    Tıvalap: urug
    Salırça: pala (bala, vala)
    Xakastap: pala
    Altay: bala
    Şor: pala
    Urumça: uşax (uşak), bala, evlad, cocux (çocux), yavru
    Karajče: bala
    Qrımçahça: çocuq, bala
    Soyot: urığ, ürän
    Tofalap: uruğ, üren''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "река" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "river" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dere" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nehir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ırmak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "akarsu":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰇𐰏𐰔, 𐰽𐰆𐰉
🇬🇧 English: river
🇷🇺 Русский: река [reka]
🇹🇷 Türkçe: dere, çay, nehir, ırmak, akarsu
🇦🇿 Türkcə: çay, irmaq, nəhr, şam (dialect)
🇹🇲 Türkmençe: derýa
🇺🇿 Oʻzbekcha: daryo
🇰🇿 Qazaqşa: özen
🇰🇬 Qırğızça: darıya, özön
    Uyghurche: deriya
    Tatarça: yılğa, därya
    Başqortsa: yılğa, darya
    Çovaşla: yuxanşıv, şıv, cırma
    Qaraqalpaqsha: dárya, ózek
    Qırımtatarca: özen, neer
    Qumuqça: özen
    Qaraçay-Malqar:	çerek, qoban, suw, barğan suw
    Noğayşa: suw, yılğa suw
    Sıbırca: yılğa, äyre, darya
    Gagauzça: derä, su, akar su
    Saqalī: örüs
    Dulğan-Hakalī: ebe
    Tıvalap: xem
    Salırça: özen (uzen), mören (muren), qol (gol)
    Xakastap: suğ
    Altaylap: suu
    Şor: çulat, suğ
    Urumça: çay, özen, derya, oz, boy, su
    Karajče: öźen (öźian), dere, čyrnyk (čyrlach, čyrnak)
    Qrımçahça: çay, derya, özen
    Soyot: hem
    Tofalap: hem''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "respublika" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "республика" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "republic" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сumhuriyet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "res publica":
        bot.send_message(message.chat.id, '''🇬🇧 In many languages, different cognates of the word "cumhuriyet" were replaced by the word "respublika" by the Soviet Russia in the 30s, 40s of the 20th century, therefore at this moment it is a more used word.
🇷🇺 Мо многих языках разные когнаты слова "сumhuriyet" были заменены на слово "respublika" советской властью в 30-х, 40-х годах XX века, поэтому в данный момент оно является более используемым словом.
🇹🇷 Çok türk lehcelerinde "сumhuriyet" kelimesinin farklı köktaşları Sovyet Rusyası tarafından XX yüzyılın 30-cu, 40-cı yıllarında "respublika" kelimesi ile değiştirildi. Bu yüzden şu anda daha çok kullanılan bir kelimedir.

🇬🇧 English: republic
🇷🇺 Русский: республика [respublika]
🇹🇷 Türkçe: сumhuriyet
🇦🇿 Türkcə: cümhuriyyət, respublika
🇹🇲 Türkmençe: jemhuriýet (jemhuryýet), respublika
🇺🇿 Oʻzbekcha: jumhuriyat, respublika
🇰🇿 Qazaqşa: respublika
🇰🇬 Qırğızça: jumuriyat, respublika
    Uyghurche: jumhuriyet
    Tatarça: cömhüriät, respublika
    Başqortsa: yömhüriät, respublika
    Çovaşla: respublika
    Qaraqalpaqsha: respublika
    Qırımtatarca: cumhuriyet
    Qumuqça: cumhuriyat, respublika
    Qaraçay-Malqar:	respublika
    Noğayşa: yümeriyet, respublika
    Sıbırca: jömhüriät, respublika
    Gagauzça: cumhuriyet, respublika
    Saqalıı: öröspǖbülüke (respublika)
    Dulğan-Hakalıı: ???
    Tıvalap: respublika
    Salırça: cumhuriyet
    Xakastap: ???
    Altaylap: ???
    Şor: ???
    Urumça: cumhuriyet
    Karajče: džumhurijet, respublika
    Qrımçahça: cumhuriyet
    Soyot: respublîk
    Tofalap: respublîk	''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "horn" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рог" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "boynuz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рога" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "buynuz":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): miŋiz (müŋüz, müyüz, mügüz)
🇬🇧 English: horn
🇷🇺 Русский: рог, рога
🇹🇷 Türkçe: boynuz
🇦🇿 Türkcə: buynuz
🇹🇲 Türkmençe: buýnuz, şah
🇺🇿 Oʻzbekcha: muguz, shox
🇰🇿 Qazaqşa: müyiz
🇰🇬 Qırğızça: müyüz
🌏 Uyghurche: münggüz
🌍 Tatarça: mögez
🌍 Başqortsa: mögöð
🌍 Çovaşla: moyraka
🌍 Qaraqalpaqsha: múyiz, shaq
🌍 Qırımtatarca: müyüz, boynuz
🌍 Qumuqça: müyüz
🌍 Qaraçay-Malqar: müyüz
🌍 Noğayşa: müyiz
🌏 Sıbırca: möyes
🌍 Gagauzça: boynuz
🌏 Saqalī: muos
🌏 Dulgan-Hakalī: muos
🌏 Tıvalap: mıyıs
🌏 Salırça: moñaz (moñas)
🌏 Xakastap: müüs
🌏 Altaylap: müüs
🌏 Şor: müüs
🌍 Urumça: buynuz (boynuz, moynuz, miyüz, müyüz)
🌍 Karajče: miuniuz (miuviuź)
🌍 Qrımçahça: munguz
🌏 Soyot: mîîs
🌏 Tofalap: mîîs''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "россия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "русь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "российский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рашка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "russia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rashka" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rusya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rusiya":
        bot.send_message(message.chat.id, '''🐺 Old Turkic: Mosqov
🇬🇧 English: Russia
🇷🇺 Русский: Россия [Rossiya]
🇹🇷 Türkçe: Rusya
🇦🇿 Türkcə: Rusiya, Ərəsey (dialect), Urusyet (Ruset, Uruset, Ursyet, Rusyet) (dialect)
🇹🇲 Türkmençe: Orsýet, Russiýa
🇺🇿 Oʻzbekcha: Oʻrusiya, Rossiya
🇰🇿 Qazaqşa: Resey, Orıset (dialect)
🇰🇬 Qırğızça: Orusiya
    Uyghurche: Rusiye, Rossiye
    Tatarça: Räsäy
    Başqortsa: Räsäy
    Çovaşla: Raccey
    Qaraqalpaqsha: Rossiya
    Qırımtatarca: Rusiye
    Qumuqça: Aresey, Sari Yan
    Qaraçay-Malqar: Eresey, Orus
    Noğayşa: Resey
    Sıbırca: Räsäy
    Gagauzça: Rusiya
    Saqalī: Nūçça sire, Arassīya, Soğurū Doydu (archaism)
    Hakalī (Dulgan): Nūçça hire
    Tıvalap: Rossiya, Orus (archaism)
    Salırça: Russiya
    Xakastap: Rossîya
    Altay: Aresey
    Şor: Qazaq çeri, Orusiya, Rossiya
    Urumça: Uruset
    Karaj: Rusija
    Qrımçahça: Rusye
    Soyot: Rossîya
    Tofalap: Orusîya, Rossîya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рот" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mouth" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ağız" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ротовая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ротовой":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): ağız (ağaz)
🇬🇧 English: mouth
🇷🇺 Русский: рот [rot]
🇹🇷 Türkçe: ağız
🇦🇿 Türkcə: ağız
🇹🇲 Türkmençe: agyz
🇺🇿 Oʻzbekcha: ogʻiz
🇰🇿 Qazaqşa: awız
🇰🇬 Qırğızça: ooz
🌏 Uyghurche: aghiz
🌍 Tatarça: awız
🌍 Başqortsa: awıð
🌍 Çovaşla: covar
🌍 Qaraqalpaqsha: awız
🌍 Qırımtatarca: ağız
🌍 Qumuqça: awuz
🌍 Qaraçay-Malqar: awuz
🌍 Noğayşa: awız
🌏 Sıbırca: awız (äwüs, ağıs)
🌍 Gagauzça: aaz
🌏 Saqalī: ayaq
🌏 Dulgan-Hakalī: uos, ańak
🌏 Tıvalap: aas
🌏 Salırça: ağız (agız, ahıs, axıs, ağas)
🌏 Xakastap: aas, axsı
🌏 Altaylap: oos
🌏 Şor: aqsı
🌍 Urumça: ağız (avuz)
🌍 Karajče: avuz (avyz, ahyz)
🌍 Qrımçahça: ağız
🌏 Soyot: aas
🌏 Tofalap: aas''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hand" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "arm" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рука" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "əl" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kol" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "десница":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): I. el, elig II. qol (qōl)
🇬🇧 English: I. hand II. arm
🇷🇺 Русский: рука [ruka]
🇹🇷 Türkçe: I. el II. kol
🇦🇿 Türkcə: I. əl II. qol
🇹🇲 Türkmençe: I. el II. gol
🇺🇿 Oʻzbekcha: qoʻl
🇰🇿 Qazaqşa: qol
🇰🇬 Qırğızça: qol
🌏 Uyghurche: qol
🌍 Tatarça: qul
🌍 Başqortsa: qul
🌍 Çovaşla: alo
🌍 Qaraqalpaqsha: qol
🌍 Qırımtatarca: I. el II. qol
🌍 Qumuqça: qol
🌍 Qaraçay-Malqar: qol
🌍 Noğayşa: qol
🌏 Sıbırca: qul
🌍 Gagauzça: el, kol
🌏 Saqalī: ilï
🌏 Dulgan-Hakalī: ilï
🌏 Tıvalap: xol
🌏 Salırça: I. el II. qol
🌏 Xakastap: xol
🌏 Altaylap: qol
🌏 Şor: qol
🌍 Urumça: äl (el), ğol (xol)
🌍 Karajče: kol
🌍 Qrımçahça: I. el II. qol
🌏 Soyot: qol (gol, hol, ğol)
🌏 Tofalap: qol''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fish" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fishes" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рыба" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "balık" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "balik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "балык" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рыбка":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰉𐰞𐰶 
🇬🇧 English: fish
🇷🇺 Русский: рыба [ryba]
🇹🇷 Türkçe: balık
🇦🇿 Türkcə: balıq
🇹🇲 Türkmençe: balyk, luw
🇺🇿 Oʻzbekcha: baliq
🇰🇿 Qazaqşa: balıq
🇰🇬 Qırğızça: balıq
    Uyghurche: beliq
    Tatarça: balıq
    Başqortsa: balıq
    Çovaşla: pulo
    Qaraqalpaqsha: balıq
    Qırımtatarca: balıq
    Qumuqça: balıq
    Saqalıı: balık
    Qaraçay-Malqar: balıq, çabaq
    Tıvalap: balık
    Gagauzça: balık
    Noğayşa: balıq
    Xakastap: palıx
    Sıbırca: palıq
    Altay: balıq
    Şor: palıq
    Dolgan: balık
    Urumça: balıx (balık, balux)
    Karaj: balych
    Qrımçahça: balıh
    Soyot: balıq
    Tofalap: balıq''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "brother-in-law" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "brotherinlaw" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "brother in law" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "свояк" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "муж свояченицы" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шурин" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bacanak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pecheneg" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "печенег" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пегенеги" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "свояки":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): adaş böşük, öz kişi, uruğ özlüg
🇬🇧 English: brother-in-law
🇷🇺 Русский: свояк, муж свояченицы, шурин
🇲🇳 Mongol: baza (baz)
🇹🇷 Türkçe: bacanak
🇦🇿 Türkcə: bacanaq, baca (dialect) 
🇹🇲 Türkmençe: baja
🇺🇿 Oʻzbekcha: boja
🇰🇿 Qazaqşa: baja
🇰🇬 Qırğızça: baja
🌏 Uyghurche: baja
🌍 Tatarça: baca, bacay
🌍 Başqortsa: baja, bajay
🌍 Çovaşla: pucana
🌍 Qaraqalpaqsha: baja
🌍 Qırımtatarca: bacanaq, baca
🌍 Qumuqça: baja
🌍 Qaraçay-Malqar: baja
🌍 Noğayşa: baja
🌏 Sıbırca: baca (paca)
🌍 Gagauzça: bacanak
🌏 Saqalī: billeq
🌏 Dulgan-Hakalī: billek
🌏 Tıvalap: baja
🌏 Salırça: paca
🌏 Xakastap: xazınax (older), çurçu (younger)
🌏 Altaylap: ceste
🌏 Şor: negeeçi eri
🌍 Urumça: bacanax
🌍 Karajče: badžanak
🌍 Qrımçahça: bacanah
🌏 Soyot: baja, bajalışqı
🌏 Tofalap: baja''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "north" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "northern" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "север" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "северный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "северная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "северное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "северные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kuzey" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şimal":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰘𐰃𐰺𐰖𐰀
🐺 Old Turkic (bef. 13th c.): tün sarı, yırya, tağdın (tağtın)
🇬🇧 English: I. north I. northern
🇷🇺 Русский: I. север II. северный (-ая, -ое)
🇹🇷 Türkçe: kuzey, şimal (archaism)
🇦🇿 Türkcə: I. şimal, quzey II. şimali, quzey
🇹🇲 Türkmençe: I. gaýra, demirgazyk II. demirgazyk
🇺🇿 Oʻzbekcha: I. shimol II. shimoliy
🇰🇿 Qazaqşa: I. soltüstik, teriskey jak II. soltüstik, teriskey
🇰🇬 Qırğızça: tündük
🌏 Uyghurche: I. shimal II. shimaliy
🌍 Tatarça: tönyaq
🌍 Başqortsa: tönyaq
🌍 Çovaşla: curcör
🌍 Qaraqalpaqsha: arqa
🌍 Qırımtatarca: I. şimal, sırt II. şimaliy
🌍 Qumuqça: temirqazıq, şimal (archaism)
🌍 Qaraçay-Malqar: şimal
🌍 Noğayşa: kerüw, sırt
🌏 Sıbırca: I. tönyaq, qışlıq, şamal, tires II. tönyaqtağı, qışlıqtağı, şimaltağı
🌍 Gagauzça: poyraz
🌏 Saqalī: I. qotu II. qotugu
🌏 Dulgan-Hakalī: I. muora II. muora dieki
🌏 Tıvalap: I. soñgu çük II. soñgu, soñgu çüktün
🌏 Salırça: şimal, guniş
🌏 Xakastap: I. altınzarıx (altın-sarıx) II. altınzarxı
🌏 Altaylap: tündük
🌏 Şor: quzam
🌍 Urumça: arktos
🌍 Karajče: syrt, kyšlych, čafon
🌍 Qrımçahça: sırt
🌏 Soyot: artuu
🌏 Tofalap: I. qarañğaarı II. qarañğaarıkîî''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "seven" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "7" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yedi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "семь":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰘‎𐱅𐰃
🐺 Old Turkic (bef. 13th c.): yetti (yeti)
🇬🇧 English: seven
🇷🇺 Русский: семь (sem')
🇹🇷 Türkçe: yedi
🇦🇿 Türkcə: yeddi
🇹🇲 Türkmençe: ýedi
🇺🇿 Oʻzbekcha: yetti
🇰🇿 Qazaqşa: jeti
🇰🇬 Qırğızça: jeti
🌏 Uyghurche: yette 
🌍 Tatarça: cide
🌍 Başqortsa: yete
🌍 Çovaşla: ciçö
🌍 Qaraqalpaqsha: jeti
🌍 Qırımtatarca: yedi
🌍 Qumuqça: yetti
🌍 Qaraçay-Malqar: jeti
🌍 Noğayşa: yeti
🌏 Sıbırca: yete
🌍 Gagauzça: edi (еди)
🌏 Saqalī: sette
🌏 Dulgan-Hakalī: hette
🌏 Tıvalap: çedi
🌏 Salırça: yiti
🌏 Xakastap: çîti
🌏 Altaylap: ceti
🌏 Şor: çetti
🌍 Urumça:	yeddi (yedi)
🌍 Karajče: jedi
🌍 Qrımçahça: yedı
🌏 Soyot: çedi (cedi)
🌏 Tofalap: çedi''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "семя" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зернышко" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tohum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "семяна" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "seed" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "семена":
        bot.send_message(message.chat.id, '''🐺 Old Turkic: uruq
🇬🇧 English: seed
🇷🇺 Русский: семя, зёрнышко
🇹🇷 Türkçe: tohum
🇦🇿 Türkcə: toxum
🇹🇲 Türkmençe: tohum
🇺🇿 Oʻzbekcha: urugʻ, tuxum
🇰🇿 Qazaqşa: urıq, tuqım
🇰🇬 Qırğızça: uruq, ürön
    Uyghurche: uruq
    Tatarça:	orlıq, börtek
    Başqortsa: orloq, börtök
    Çovaşla: vorlox
    Qaraqalpaqsha: tuqım, urıq
    Qırımtatarca: urluq, tuhum
    Qumuqça: urluq
    Qaraçay-Malqar:	urluq, bürtük
    Noğayşa: urlıq
    Sıbırca: orloq, örän, yem
    Gagauzça: toom (toum)
    Saqalī: tuorāq, sieme
    Dulgan-Hakalī: tuorāq
    Tıvalap: ürezin, ürezi
    Salırça: urlux
    Xakastap: üren, ulğuruğ, urux
    Altaylap: üren
    Şor: üren
    Urumça: toxum, orlux, bürtük
    Karajče: urluch (urluk, urlyk)
    Qrımçahça: tuqum, urlıh
    Soyot: tarığ
    Tofalap: taraa, tarığ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "september" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "septembre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сентябрь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eylül":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: september
🇷🇺 Русский: сентябрь [sentyabr']
🇹🇷 Türkçe: eylül
🇦🇿 Türkcə: sentyabr, eylül
🇹🇲 Türkmençe: ruhnama
🇺🇿 Oʻzbekcha: sentabr, mezon
🇰🇿 Qazaqşa: qırküyek, mıyzam (mıyzan)
🇰🇬 Qırğızça: ayaq oona
    Uyghurche: mizan
    Tatarça: sintäber, ındır, äylül
    Başqortsa: harısay
    Çovaşla: avon
    Qaraqalpaqsha: sentyabr, miyzan
    Qırımtatarca: sentâbr, ceviz
    Qumuqça: sentyabr, qoçqar
    Qaraçay-Malqar: sentyabr, qırqawuz
    Noğayşa: sentyabr, qırqkiyik
    Sıbırca: sentyabr, misan, sarğaq
    Gagauzça: ceviz
    Saqalī: balağan ıya
    Dulgan-Hakalī: bulkāhın
    Tıvalap: tos
    Salırça: toxsıncı
    Xakastap: sentyabr
    Xakastap (Sağay): ürtün alçañ, xıra kîsçeñ
    Xakastap (Pîltir): ürtün
    Xakastap (Xaas): pözik
    Altaylap: sentyabr, sığın
    Şor: ürtün
    Urumça: septemvrioz
    Karajče: (they use Karaim calendar)
    Qrımçahça: sentyabr
    Soyot: sentyabr
    Tofalap: eyttiñ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "heart" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сердце" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yürek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kalp" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "❤️" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сердце":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): yüräk (cüräk)
🇬🇧 English: heart
🇷🇺 Русский: сердце [serdtse]
🇹🇷 Türkçe: yürek, kalp
🇦🇿 Türkcə: ürək, qəlb
🇹🇲 Türkmençe: ýürek
🇺🇿 Oʻzbekcha: yurak
🇰🇿 Qazaqşa: jürek
🇰🇬 Qırğızça: jürök
🌏 Uyghurche: yürek
🌍 Tatarça: yöräk
🌍 Başqortsa: yöräk
🌍 Çovaşla: çöre
🌍 Qaraqalpaqsha: júrek
🌍 Qırımtatarca: yürek
🌍 Qumuqça: yürek
🌍 Qaraçay-Malqar: jürek
🌍 Noğayşa: yürek
🌏 Sıbırca: yöräk
🌍 Gagauzça: üürek
🌏 Saqalī: süreq
🌏 Dulgan-Hakalī: hürek
🌏 Tıvalap: çürek
🌏 Salırça: yiräx (yirex, yirix)
🌏 Xakastap: çürek
🌏 Altaylap: cürek
🌏 Şor: çürek
🌍 Urumça: üräg (yürek)
🌍 Karajče: üriak (jirek, jürek)
🌍 Qrımçahça: yurek, qalb
🌏 Soyot: çüräk (cüräk)
🌏 Tofalap: çürek''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "голубой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "голубая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "голубое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "голубые" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "синий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "синяя" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "синее" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "синие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "небесный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "небесная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "небесное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "небесные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "blue" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mavi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gökrengi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gök rengi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "göy" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gök reng":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰚𐰇𐰚
🐺 Old Turkic: kök
🇬🇧 English: blue
🇷🇺 Русский: голубой, синий, небесный (-ая, -ое)
🇭🇺 Magyar: kék
🇲🇳 Mongol: khökh
🇹🇷 Türkçe: mavi, gök (rarely)
🇦🇿 Türkcə: göy, mavi (light blue)
🇹🇲 Türkmençe: gök
🇺🇿 Oʻzbekcha: koʻk
🇰🇿 Qazaqşa: kök
🇰🇬 Qırğızça: kök
    Uyghurche: kök
    Tatarça: kük
    Başqortsa: kük
    Çovaşla: kovak
    Qaraqalpaqsha: kók
    Qırımtatarca: kök, mavi
    Qumuqça: kök
    Qaraçay-Malqar:	kök
    Noğayşa: kök
    Sıbırca: kük
    Gagauzça: maavi, gök (rarely)
    Saqalī: küöq
    Dulgan-Hakalī: küök
    Tıvalap: kök
    Salırça: göx
    Xakastap: kök
    Altaylap: kök
    Şor: kök
    Urumça: kök (gög)
    Karajče: kiok
    Qrımçahça: kök
    Soyot: kök (gök)
    Tofalap: kök''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rock" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "скала" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "утес" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kaya":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰖𐰀
🐺 Old Turkic: qaya
🇬🇧 English: rock (geol.)
🇷🇺 Русский: скала, утёс
🇹🇷 Türkçe: kaya
🇦🇿 Türkcə: qaya, kəpəz (dialect)
🇹🇲 Türkmençe: gaýa
🇺🇿 Oʻzbekcha: qoya
🇰🇿 Qazaqşa: qıya, jartas
🇰🇬 Qırğızça: qıya, asqa
    Uyghurche: qiya, tash, qiya tash
    Tatarça: qıya
    Başqortsa: qaya
    Çovaşla: xısak, çul tu, çul xısak
    Qaraqalpaqsha: qıya
    Qırımtatarca: qaya
    Qumuqça: qaya
    Qaraçay-Malqar: qaya
    Noğayşa: qaya
    Sıbırca: qaya (qıya), taş
    Gagauzça: kaya, kepaz
    Saqalī: tās qaya
    Dulgan-Hakalī: tās, bosko tās
    Tıvalap: xaya
    Salırça: qaya
    Xakastap: xaya
    Altaylap: qaya
    Şor: qaya
    Urumça: xaya
    Karajče: kaja
    Qrımçahça: qaya
    Soyot: haya
    Tofalap: haya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sözlük" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lügât" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lügat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "словарь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "wordbook" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "словник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dictionary":
        bot.send_message(message.chat.id, '''🇬🇧 English: dictionary, wordbook
🇷🇺 Русский: словарь, словник (словник в значении "список слов" в большинство тюркских языков является переводов словосочетания "список слов", не требует специального слова)
🇹🇷 Türkçe: sözlük, lügât (archaism)
🇦🇿 Türkcə: lüğət, sözlük
🇹🇲 Türkmençe: sözlük, lugat (archaism), kamus (archaism)
🇺🇿 Oʻzbekcha: lugʻat, soʻzlik (archaism)
🇰🇿 Qazaqsha: sózdik, luǵat
🇰🇬 Qırğızça: sözdük
🌏 Uyghurche: lughet, sözlük
🌍 Tatarça: süzlek, löğät
🌍 Başqortsa: huðlek, löğät (archaism)
🌍 Çovaşla: somaxsar, somaxsen köneki, somaxlox (archaism)
🌍 Qaraqalpaqsha: sózlik
🌍 Qırımtatarca: luğat, sözlük, qamus (archaism)
🌍 Qumuqça: sözlük
🌍 Qaraçay-Malqar: sözlük, tılmaç kitab
🌍 Noğayşa: sözlik
🌏 Sıbırca: süslek
🌍 Gagauzça: sözlük, laflık
🌏 Saqalī: tıljıt
🌏 Dulgan-Hakalī: tıljıt
🌏 Tıvalap: söstük
🌏 Salırça: sözlük
🌏 Xakastap: söstik
🌏 Altaylap: sözlik
🌏 Şor: söstük
🌍 Urumça: sözler kitabı
🌍 Karajče: sioźliuk (sioźlik), sioźbitik
🌍 Qrımçahça: sözlık, luğat
🌏 Soyot: söstik
🌏 Tofalap: soottarı''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dog" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doggy" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bitch" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "собака" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пес" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кобель" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сука" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сучка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "köpek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "it" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "erkek köpek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kancık":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰃𐱃
🇬🇧 English: dog, bitch ♀
🇷🇺 Русский: собака, пёс ♂, кобель ♂, сука ♀
🇹🇷 Türkçe: köpek, it, erkek köpek ♂, kancık ♀
🇦🇿 Türkcə: it, köpək ♂, qancıq ♀
🇹🇲 Türkmençe: it, köpek ♂, ganjyk ♀
🇺🇿 Oʻzbekcha: it, kuchuk, ko'ppak ♂, qanjiq ♀
🇰🇿 Qazaqşa: iyt, töbet, arlan iyt ♂, qanşıq ♀
🇰🇬 Qırğızça: it, döböt ♂, qançıq ♀
🌏 Uyghurche: it
🌍 Tatarça:	et, ata et ♂, ana et ♀, änçek ♀
🌍 Başqortsa: et, arlan et ♂, käntäy ♀
🌍 Çovaşla: yıto, aca yıto ♂, yıto aci ♂, ama yıto ♀, yıto ami ♀
🌏 Qaraqalpaqsha: iyt, kópek ♂, qanshıq ♀
🌍 Qırımtatarca: it, köpek, erkek köpek ♂, qancıq ♀
🌍 Qumuqça: it, göbek, erkek it ♂, qançıq ♀
🌍 Qaraçay-Malqar: it, erkek it ♂, pariy ♂, gajı ♀, qançıq ♀
🌍 Noğayşa: iyt, ata iyt ♂, ana iyt ♀ 
🌏 Sıbırca: et, irkäk et ♂, qancıq ♀, üläkcen ♀
🌍 Gagauzça: köpek, it, turba ♂, kancık ♀
🌏 Saqalıı: ıt, atīr ıt ♂, tıhı ıt ♀
🌏 Dulğan-Hakalıı: ıt
🌏 Tıvalap: ıt, askır ıt ♂, kıs ıt ♀
🌏 Salırça: it
🌏 Xakastap: aday, irgek aday ♂, tizi aday ♀
🌏 Altay: iyt, erkek iyt ♂, tayğıl ♂, tiji iyt ♀
🌏 Şor:	aday
🌍 Urumça: it (yit), köpek, kancıx (xancıx, xançıx) ♀
🌍 Karajče:	it´ (it, ijt)
🌍 Qrımçahça: baraq, köpek
🌏 Soyot: ıt, er ıt ♂, epşi ıt ♀
🌏 Tofalap: ıt''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sun" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "the sun" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "solar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "солнце" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сонце" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "güneş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "☉":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): I. kün II. künäş, aditya, yaşıq
🇬🇧 English: I. sun II. The Sun, Solar (astr.) ☉
🇷🇺 Русский: I. солнце II. Солнце (звезда, астр.) ☉ [solntse]
🇹🇷 Türkçe: I. gün II. güneş
🇦🇿 Türkcə: I. gün II. günəş
🇹🇲 Türkmençe: I. güneş II. gün
🇺🇿 Oʻzbekcha: I. oftob, kun II. quyosh
🇰🇿 Qazaqşa: kün
🇰🇬 Qırğızça: kün
🌏 Uyghurche: quyash, aptap, kün
🌍 Tatarça: qoyaş, kön (archaism)
🌍 Başqortsa: qoyaş, kön
🌍 Çovaşla: xövel
🌍 Qaraqalpaqsha: quyas, kún
🌍 Qırımtatarca: I. kün II. küneş
🌍 Qumuqça: I. gün II. güneş
🌍 Qaraçay-Malqar: kün
🌍 Noğayşa: kün
🌏 Sıbırca: qoyaş, kön
🌍 Gagauzça:  I. gün II. güneş
🌏 Saqalī: kün
🌏 Dulgan-Hakalī: kün
🌏 Tıvalap: xün
🌏 Salırça: gün
🌏 Xakastap: kün
🌏 Altaylap: kün
🌏 Şor: kün, quyaş
🌍 Urumça: gün (kün), küneş
🌍 Karajče: kujaš (kujas), kiuń
🌍 Qrımçahça: küneş, şams
🌏 Soyot: kün (gün, hün)
🌏 Tofalap: hün (kün)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "salt" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "соль" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tuz":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): tuz
🇬🇧 English: salt
🇷🇺 Русский: соль [sol']
🇹🇷 Türkçe: tuz
🇦🇿 Türkcə: duz
🇹🇲 Türkmençe: duz
🇺🇿 Oʻzbekcha: tuz
🇰🇿 Qazaqşa: tuz
🇰🇬 Qırğızça: tuz
🌏 Uyghurche: tuz
🌍 Tatarça: toz
🌍 Başqortsa: toð
🌍 Çovaşla: tovar
🌍 Qaraqalpaqsha: duz
🌍 Qırımtatarca: tuz
🌍 Qumuqça: tuz
🌍 Qaraçay-Malqar: tuz
🌍 Noğayşa: tuz
🌏 Sıbırca: tos
🌍 Gagauzça: tuz
🌏 Saqalī: tūs
🌏 Dulgan-Hakalī: tūs
🌏 Tıvalap: dus
🌏 Salırça: duz
🌏 Xakastap: tus
🌏 Altaylap: tus
🌏 Şor: tus
🌍 Urumça: duz (tuz)
🌍 Karajče: tuz
🌍 Qrımçahça: tuz
🌏 Soyot: tus
🌏 Tofalap: tus''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "стамбул" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "станбул" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "стамбульский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "истанбул" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "истамбул" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "istanbul" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıstanbul" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "stambul" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "stanbul" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıstambul" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "istambul":
        bot.send_message(message.chat.id, '''🇬🇧 English: Istanbul
🇷🇺 Русский: Стамбул
🇹🇷 Türkçe: İstanbul
🇦🇿 Türkcə: İstanbul
🇹🇲 Türkmençe: Istanbul (Ystanbul)
🇺🇿 Oʻzbekcha: Istanbul (Istambul)
🇰🇿 Qazaqşa: Istanbul (Istambul)
🇰🇬 Qırğızça: İstanbul (Stambul)
    Uyghurche: Istanbul
    Tatarça: İstanbul
    Başqortsa: İstanbul
    Çovaşla: Stampol (İstanbul)
    Qaraqalpaqsha: Istanbul
    Qırımtatarca: İstanbul
    Qumuqça: İstanbul
    Qaraçay-Malqar: İstanbul
    Noğayşa: İstanbul (Stambul)
    Sıbırca: İstanbul
    Gagauzça: İstanbul
    Saqalī: İstanbul
    Dulgan-Hakalī: İstanbul
    Tıvalap: İstanbul
    Salırça: İstanbul
    Xakastap: İstanbul (Stambul)
    Altaylap: İstanbul (Stambul)
    Şor: İstanbul
    Urumça: İstanbul (İstanbol, Stambol, Stanbol)
    Karajče: İstanbul
    Qrımçahça: İstanbul
    Soyot: İstanbul
    Tofalap: İstanbul''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "el" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "эль" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "эл" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ulus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "улус" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ил":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰠, 𐰆𐰞𐰾
🐺 Old Turkic (bef. 13th c.): el, ulus (uluş)
🇬🇧 English: "el" or "ulus" (turkic society)
🇷🇺 Русский: "эль" (ил, ел, эл) или "улус" (тюркский социум, общество, люди, страна, народ, государство), также слово, которым обозначают свой традиционный ареал обитания
🇲🇳 Mongol: uls
🇹🇷 Türkçe: el (*anatomi "el" sonucu için "hand" yazın), ulus
🇦🇿 Türkcə: el
🇹🇲 Türkmençe: il
🇺🇿 Oʻzbekcha: el, ulus (archaism), el-ulus (archaism)
🇰🇿 Qazaqşa: el
🇰🇬 Qırğızça: el
🌏 Uyghurche: el
🌍 Tatarça: il
🌍 Başqortsa: il
🌍 Çovaşla: yal
🌍 Qaraqalpaqsha: el
🌍 Qırımtatarca: el
🌍 Qumuqça: el
🌍 Qaraçay-Malqar: el
🌍 Noğayşa: el
🌏 Sıbırca: il
🌍 Gagauzça: yer, ulus
🌏 Saqalī: sir, ulus
🌏 Dulgan-Hakalī: hir
🌏 Tıvalap: ulus
🌏 Salırça: yer, tifañ
🌏 Xakastap: îl
🌏 Altaylap: el
🌏 Şor: el
🌍 Urumça: el
🌍 Karajče: ėl´
🌍 Qrımçahça: el
🌏 Soyot: ulıs
🌏 Tofalap: ulus''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "there" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "там" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "orada" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "orası":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰦𐰀
🇬🇧 English: there (place)
🇷🇺 Русский: там [tam]
🇹🇷 Türkçe: orada, ora, orası
🇦🇿 Türkcə: orada, ora
🇹🇲 Türkmençe: ol ýerde, o taýda
🇺🇿 Oʻzbekcha: u yerda, u yoqda, u yonda
🇰🇿 Qazaqşa: onda, anda
🇰🇬 Qırğızça: tigi jaqta, tigi jerde, anda
    Uyghurche: unda, u yerde
    Tatarça: tegendä, anda, şul cirdä
    Başqortsa: tegendä, unda, şunda
    Çovaşla: unta, cavonta, lere
    Qaraqalpaqsha: onda, sonda, ol jerde, sol jerde
    Qırımtatarca: anda, o yerde
    Qumuqça: onda
    Qaraçay-Malqar:	anda, alayda
    Noğayşa: onda
    Sıbırca: anta, şanta
    Gagauzça: orada, orası
    Saqalıı: onno, antaq
    Dulğan-Hakalıı: onno (honno)
    Tıvalap: ında
    Salırça: anta (anda, ante), andacux, tu (tü, tǖ)
    Xakastap: anda
    Altay: anda (ondo)
    Şor: anda
    Urumça: orda, onda
    Karaj: anda (onda), anavda, ara (ari, ary)
    Qrımçahça: onda
    Soyot: ında, aa, deêde (teêde)
    Tofalap: ında, teêde''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "temperament" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хуй" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "xuy" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "huy" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mizaç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "темперамент":
        bot.send_message(message.chat.id, '''🇬🇧 English: temperament
🇷🇺 Русский: темперамент
🇹🇷 Türkçe: huy, mizaç
🇦🇿 Türkcə: xoy (xuy), məzac
🇹🇲 Türkmençe: hyjuw, ganygyzgynlyk
🇺🇿 Oʻzbekcha: mizoj
🇰🇿 Qazaqşa: qızıwqandılıq, minez
🇰🇬 Qırğızça: minez
    Uyghurche: xuy, müjez (mijez)
    Tatarça: qızuqanlılıq
    Başqortsa: därt, ğäyrät
    Çovaşla: yola
    Qaraqalpaqsha: minez, jedel, yosh, qızba
    Qırımtatarca: mizac
    Qumuqça: qılıq, bitim
    Qaraçay-Malqar: qılıq, jitilik, girtçilik
    Noğayşa: qılıq
    Sıbırca: qayrat
    Gagauzça: mizaç
    Saqalī: uoq, maygı
    Dulğan-Hakalī: maygı
    Tıvalap: kijiniñ büdüjü, çañ, aajı-çañ
    Salırça: micazi, açäx
    Xakastap: xılıx
    Altaylap: qılıq
    Şor: qılıq
    Urumça: tabiyet (tabyat)
    Karajče: kylyk (kylych)
    Qrımçahça: qılıq
    Soyot: qılıq, çañ
    Tofalap: qılıq''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tiger" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "leopard" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "леопард" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тигр" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kaplan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "leopar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pars":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰉𐰺𐰽 ,𐰉𐰺𐱁
🇬🇧 English: tiger, leopard
🇷🇺 Русский: тигр [tigr], леопард [leopard]
🇹🇷 Türkçe: kaplan, pars
🇦🇿 Türkcə: pələng, qaplan, bəbir
🇹🇲 Türkmençe: gaplaň, peleň, alajagaplaň, bars
🇺🇿 Oʻzbekcha: yo'lbars, qoplon
🇰🇿 Qazaqşa: jolbarıs, barıs, qabılan
🇰🇬 Qırğızça: jolbors, qabılan
    Uyghurche: yolvas, qaplan
    Tatarça: yulbarıs, qaplan
    Başqortsa: yulbarıþ, qaplan
    Çovaşla: tikor (tixor, tixxor, tıxor), ilparos
    Qaraqalpaqsha: jolbarıs, qablan
    Qırımtatarca: qaplan
    Qumuqça: qaplan
    Saqalıı: bābır
    Qaraçay-Malqar: qaplan
    Tıvalap: par
    Gagauzça: kaplan
    Noğayşa: yolbars, kaplan
    Sıbırca: ilbis, yulbarıs, qaplan
    Salırça: pascux
    Altay: bar
    Urumça: ğablan (xaplan), aslan-xaplan
    Karaj: bars (barst, pars)
    Qrımçahça: qaplan, pars
    Soyot: bar''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tılmaçı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tılmaç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "толмач" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dilmaç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tolmács" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tolmaç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tilmaç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "талмач" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "talmaç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tolmac" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tilmac" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dilmac" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dilmanc" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "interpreter" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tolmach":
        bot.send_message(message.chat.id, '''🐺 Old Turkic: tılmaçı
🇬🇧 English: interpreter
🇷🇺 Русский: толмач [tolmach]
🇭🇺 Magyar: tolmács
🇹🇷 Türkçe: dilmaç
🇦🇿 Türkcə: dilmanc
🇹🇲 Türkmençe: dilmaç
🇺🇿 Oʻzbekcha: tilmoch
🇰🇿 Qazaqşa: tilmaş
🇰🇬 Qırğızça: tilmeç
    Uyghurche: tilmach
    Tatarça: tılmaç
    Başqortsa: tılmas
    Çovaşla: tolmaç
    Qaraqalpaqsha: dilmash
    Qırımtatarca: tilmaç
    Qumuqça: tilmaç
    Qaraçay-Malqar: tılmaç
    Noğayşa: tılmaş
    Sıbırca: telmäc (tilmäc, tulmac)
    Gagauzça: talmaç
    Saqalī: tılbāsçıt, tılbas (archaism)
    Dulgan-Hakalī: tulmāsçıt
    Tıvalap: xelemeçi (xelmeeç)
    Salırça: dilmaç
    Xakastap: tilbestegci
    Altaylap: tilmeş
    Şor: ???
    Urumça: tilmaç
    Karajče: talmač (tolmač)
    Qrımçahça: tılmaç
    Soyot: tolmooçı (tolmoocı)
    Tofalap: tolmooçı''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "толсто" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "толстый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "толстая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "толстое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "толстые" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жирный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жирно" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жирная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жирное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жирные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "thick" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "упитанный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "упитанная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fatty" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oily" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kalın" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kalin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yoğun" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şişman" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tolbul" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "semiz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "semız" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yağlı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yağli" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yagli" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şişko":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰾. 𐰴𐰞𐰣 𐰾𐰾. 𐰾𐰢𐰃𐰔
🇬🇧 English: I. thick II. fat (adj.) III. fatty, oily
🇷🇺 Русский: I. толстый (-ая, -ое) II. толстый, жирный, упитанный (-ая, -ое) III. жирный (о продуктах)
🇹🇷 Türkçe: I. kalın, yoğun II. şişman, şişko, tombul, semiz III. yağlı
🇦🇿 Türkcə: I. qalın, yoğun II. gombul, kök, şişman, səmiz (dialect) III. yağlı, yağlaşov (yağlaşoy) (dialect)
🇹🇲 Türkmençe: I. galyň, ýogyn II. galyň, semiz, çişik III. ýagly
🇺🇿 Oʻzbekcha: I. qalin, yo'g'on II. semiz III. yog'li, seryog', sermoy
🇰🇿 Qazaqca: I. qalıŋ II. jıwan, semiz III. maylı, semiz
🇰🇬 Qırğızça: I. qalıñ II. joon, semiz, boluq III. mayluu
    Uyghurche: I. qelin, yoghan II. semiz III. yaghliq, mayliq
    Tatarça:	I. qalın II. yuan, simez III. maylı, simez
    Başqortsa: I. qalın, yıwan II. yıwan, himeð, kör, himergän III. maylı, himeð
    Çovaşla: I. xulon, küpçek (küpçem, küpşeke), parka II. samor, montor III. cullo
    Qaraqalpaqsha: I. qalıń, juwan II. juwan, semiz III. maylı, semiz
    Qırımtatarca: I. qalın II. şişman, semiz III. yağlı, semiz
    Qumuqça: I. qalın II. bazık, mazallı, semiz III. maylı, semiz
    Qaraçay-Malqar:	I. bazıq, qalın II. bazıq, semiz III. jawlu, semiz, qalın
    Noğayşa: I. qalın, dombay II. yuwan, tolı, dombay III. maylı, semiz
    Sıbırca: I. qalıñ, yowan II. tula, kör, sum, simiz (semiz) III. maylı, simiz (semiz)
    Gagauzça: I. kalın II. tuyan (tuuyan), semiz, şişikin (şişkin), şiman III. yaalı
    Saqalıı: I. qalıñ, suon II. suon, moju, emis III. emis, sıalāq
    Dulğan-Hakalıı: I. kalın II. huon, emis III. emis
    Tıvalap: I. çoon, kılın II. çoon, semis III. çaglıg, semis, üstüg
    Salırça: I. yoğan II. semus (simus) III. yağlı, semus (simus)
    Xakastap: I. xalın II. çoon, poğda III. çağlığ, sîmis
    Altay: I. qalıñ, coon II. coon, semis, tepçek III. semis, üstü
    Şor: I. qalın, çoon II. çoon, sebis III. semis (sebis)
    Urumça: I. ğalın (xalın) II. kök, şişman, semiz III. yağlı, maylı
    Karaj: I. kalyn II. bazych (bazyk), siemiź (semiz) III. javly (javlu), siemiź (semiz)
    Qrımçahça: I. qalın II. semız III. yağlı
    Soyot: I. hılın II. semîs III. çağlığ, üstiğ, dosalığ (tosalığ)
    Tofalap: I. hılı, II. semîs III. üstüğ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "slim" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тонкий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тонкая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тонкое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тонкие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ince" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ınce" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yufka" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тонко":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰖𐰆𐰖𐰴𐰀, 𐰘𐰨𐰏𐰀
🇬🇧 English: slim
🇷🇺 Русский: тонкий (-ая, -ое)
🇹🇷 Türkçe: ince, yufka
🇦🇿 Türkcə: nazik, incə, yuxa
🇹🇲 Türkmençe: inçe, näzik
🇺🇿 Oʻzbekcha: ingichka, yupqa, nozik
🇰🇿 Qazaqşa: jiŋişke, näzik, juqa
🇰🇬 Qırğızça: içke, juqa
    Uyghurche: inchike, yupqa
    Tatarça:	neçkä, näzek
    Başqortsa: näðek, yoqa
    Çovaşla: cüxe, cince
    Qaraqalpaqsha: jińishke, názik
    Qırımtatarca: ince, nazik, yufqa
    Qumuqça: inçe, nazik, yuqqa
    Qaraçay-Malqar:	iñçge (iñiçge), juqa, nazik
    Noğayşa: yinişke, nazik, yuqa
    Sıbırca: уeсkä (yiсkä), yoğa
    Gagauzça: incä, zarif, yufka (yıfka)
    Saqalıı: çarās, sinńiges
    Dulğan-Hakalıı: hinńiges (hinniges)
    Tıvalap: çiñge, çuga
    Salırça: yoxpa, nişke (neşki, leşki, läşki)
    Xakastap: çuğacax, çuğa, niske
    Altay: çiçke, cuqa
    Şor: çişke, çuğa
    Urumça: yuxa, xuba, ince
    Karajče: ińčkia (inckie, inčkie), indže, jufka
    Qrımşahça: ince, yufqa
    Soyot: çuğa (cuğa), cîñge
    Tofalap: çuğa, nîñge''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "that" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тот" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şu":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰆𐰞
🇬🇧 English: that (such)
🇷🇺 Русский: тот [tot]
🇹🇷 Türkçe: şu, о
🇦🇿 Türkcə: o
🇹🇲 Türkmençe: şu, şol
🇺🇿 Oʻzbekcha: shu, o'sha
🇰🇿 Qazaqşa: sol, anaw
🇰🇬 Qırğızça: oşol, tigi
    Uyghurche: u, avu, shu
    Tatarça: şul, tege
    Başqortsa: şul, tege
    Çovaşla: vol, cav (cavo), leş (leşö)
    Qaraqalpaqsha: sol, ana, ol
    Qırımtatarca: şu, о
    Qumuqça: şo, ol
    Qaraçay-Malqar:	ol (o)
    Noğayşa: sol, anaw, ol
    Sıbırca: şul (şu), tege
    Gagauzça: şu, o	
    Saqalī: ol, sol
    Dulğan-Hakalī: ol
    Tıvalap: ol
    Salırça: vu (u, o, ū), tūgu, tu (tü, tǖ)
    Xakastap: ol
    Altay: ol
    Şor: ol, tigi
    Urumça: o
    Karaj: ol, ošol (osol)
    Qrımçahça: o (ol), oşol
    Soyot: ol, deê (teê)
    Tofalap: ol, teê''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ot" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "grass" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "herb" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "трава" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "травка":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱃
🐺 Old Turkic (bef. 13th c.): ot
🇬🇧 English: grass, herb
🇷🇺 Русский: трава [trava]
🇹🇷 Türkçe: ot
🇦🇿 Türkcə: ot
🇹🇲 Türkmençe: ot
🇺🇿 Oʻzbekcha: oʻt, oʻlan
🇰🇿 Qazaqşa: ot, şöp
🇰🇬 Qırğızça: çöp, ot
🌏 Uyghurche: ot, ot-chöp, chöp
🌍 Tatarça: ülän
🌍 Başqortsa: ülän
🌍 Çovaşla: kurok
🌍 Qaraqalpaqsha: shóp
🌍 Qırımtatarca: ot
🌍 Qumuqça: ot
🌍 Qaraçay-Malqar: xans, kırdık, ot, otlaw, xane
🌍 Noğayşa: ölen
🌏 Sıbırca: ülän (üläñ, yülän, öylän)
🌍 Gagauzça: ot
🌏 Saqalī: ot
🌏 Dulgan-Hakalī: ot
🌏 Tıvalap: ot, sigen
🌏 Salırça: çöp
🌏 Xakastap: ot
🌏 Altaylap: ölön
🌏 Şor: öleñ, ot
🌍 Urumça: ot, ölet
🌍 Karajče: ot, kiogiot, čiop, ješillik
🌍 Qrımçahça: ot
🌏 Soyot: ot, kök (gök), sigen (sigän)
🌏 Tofalap: ot, kök, sigen''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "traktör" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "traktor" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tractor" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "трактор" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tiraxtur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "traxtır":
        bot.send_message(message.chat.id, '''🇬🇧 English: tractor
🇷🇺 Русский: трактор [traktor]
🇹🇷 Türkçe: traktör
🇦🇿 Türkcə: tiraxtur – South Azerbaijani Turkish + Derbend dialect
    official: traktor
    dialects: traxtır, traxdor, tıraxdır, traxdır
🇹🇲 Türkmençe: traktor, tyraktyr (dialect), dartar
🇺🇿 Oʻzbekcha: traktor, tiraqtir (dialect) 
🇰🇿 Qazaqşa: traktor, tıraqtır (tiräktir, traqtır, träktir) (dialect)
🇰🇬 Qırğızça: traktor
🌏 Uyghurche: traktor, tiraktor (dialect)
🌍 Tatarça: traktor, tıraxtır (dialect)
🌍 Başqortsa: traktor, tıraqtır (tıraqtor) (dialect)
🌍 Çovaşla: traktor
🌍 Qaraqalpaqsha: traktor
🌍 Qırımtatarca: traktor
🌍 Qumuqça: traktor, tıraqtir (taraqtir) (dialect)
🌍 Qaraçay-Malqar: traktor
🌍 Noğayşa: traktor
🌏 Sıbırca: traktor
🌍 Gagauzça: traktor
🌏 Saqalī: traktor, tıraqtır (dialect)
🌏 Dulgan-Hakalī: traktor
🌏 Tıvalap: traktor
🌏 Salırça: tolaci, cağcax (walking tractor)
🌏 Xakastap: traktor
🌏 Altaylap: traktor
🌏 Şor: traktor
🌍 Urumça: traktor
🌍 Karajče: traktor
🌍 Qrımçahça: traktor
🌏 Soyot: traktor
🌏 Tofalap: tıraqtır''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "traktör azerbaycan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tractor sazi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "traktor sazi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tiraxtur sazi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tiraxtur azerbaycan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tiraxtur azərbaycan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tiraxtur azerbaijan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "трактор сази" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tractor fc" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "traktor fc" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tiraxtur fc" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tiraxtur fk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tractor fk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "traktor fk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tractor club" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tractorclub" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "трактор азербайджан":
        bot.send_message(message.chat.id, '''🇬🇧 English: Tractor Azerbaijan
🇷🇺 Русский: Трактор Азербайджан
🇹🇷 Türkçe: Traktör Azerbaycan
🇦🇿 Türkcə: Tiraxtur Azərbaycan
🇹🇲 Türkmençe: Tyraktyr Azerbaýjan
🇺🇿 Oʻzbekcha: Tiraqtir Ozarbayjon
🇰🇿 Qazaqşa: Tıraqtır Äzirbayjan
🇰🇬 Qırğızça: Traktor Azerbayjan
🌏 Uyghurche: Tiraktor Ezerbeyjan
🌍 Tatarça: Tıraxtır Azärbaycan
🌍 Başqortsa: Tıraqtır Äzerbayjan
🌍 Çovaşla: Traktor Azerbayʤan
🌍 Qaraqalpaqsha: Traktor Ázerbayjan
🌍 Qırımtatarca: Traktor Azerbaycan
🌍 Qumuqça: Tıraqtir Azerbayjan
🌍 Qaraçay-Malqar: Traktor Azerbayjan
🌍 Noğayşa: Traktor Azerbaydjan
🌏 Sıbırca: Traktor Äzerbayjan
🌍 Gagauzça: Traktor Azerbaycan
🌏 Saqalī: Tıraqtır Azerbayjan
🌏 Dulgan-Hakalī: Traktor Azerbayjan
🌏 Tıvalap: Traktor Azerbaydjan
🌏 Salırça: Traxtor Azerbaycañ
🌏 Xakastap: Traktor Azerbaydjan
🌏 Altaylap: Traktor Azerbaydjan
🌏 Şor: Traktor Azerbaydjan
🌍 Urumça: Traktor Azırbacan
🌍 Karajče: Traktor Azierbajdžan
🌍 Qrımçahça: Traktor Azerbaycan
🌏 Soyot: Traktor Azerbayjan
🌏 Tofalap: Tıraqtır Azerbayjan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "three" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "три" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "3" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "üç":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰇𐰲 
🇬🇧 English: three
🇷🇺 Русский: три [tri]
🇹🇷 Türkçe: üç
🇦🇿 Türkcə: üç
🇹🇲 Türkmençe: üç
🇺🇿 Oʻzbekcha: uch
🇰🇿 Qazaqşa: üş
🇰🇬 Qırğızça: üç
    Uyghurche: üch
    Tatarça: öç
    Başqortsa: ös
    Çovaşla: vic, (vicö, viccö)
    Qaraqalpaqsha: u'sh
    Qırımtatarca: üç
    Qumuqça: üç
    Qaraçay-Malqar: üç
    Noğayşa: üş
    Sıbırca: öc
    Gagauzça: üç
    Saqalī: üs
    Tıvalap: üş
    Salırça: üş
    Xakastap: üs
    Altay: üç
    Şor: üş
    Dolgan: üs
    Urumça: üç
    Karaj: üč
    Qrımçahça: uç
    Soyot: üş
    Tofalap: üş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "turkey" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "türkiye" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "turkiye" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "turkıye" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "турция" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "туркия":
        bot.send_message(message.chat.id, '''🇬🇧 Note: In some/most languages "Türkiya" might be "Türkiyä". There is misunderstanding due to writing style in Cyrillic alphabet, because in Cyrillic script "ya" and "yä" are the same ("я").
🇷🇺 Примечание: В некоторых/многих языках слово "Türkiya" может быть заменено на "Türkiyä". Это недопонимание связано с тем, что в кириллическом алфавите этих языков используется буква "я", которая в латинице равна "ya" и "yä" одновременно.
🇹🇷 Not: Bazi/çok lehcede "Türkiya" kelimesi "Türkiyä" gibi yazılabilir, bu anlamsızlığa kirill alfabesi sebeptir. Çünkü kirill yazılışında "ya" ile "yä" sesleri aynı harfdır ("я").

🇬🇧 English: Turkey, Türkiye
🇷🇺 Русский: Турция
🇹🇷 Türkçe: Türkiye
🇦🇿 Türkcə: Türkiyə
🇹🇲 Türkmençe: Türkiýe
🇺🇿 Oʻzbekcha: Turkiya
🇰🇿 Qazaqşa: Türkiya
🇰🇬 Qırğızça: Türkiya
    Uyghurche: Türkiye
    Tatarça: Törkiä
    Başqortsa: Törkiä
    Çovaşla: Török cörö, Turtsi
    Qaraqalpaqsha: Túrkiya
    Qırımtatarca: Türkiye
    Qumuqça: Türkiya
    Qaraçay-Malqar: Türk
    Noğayşa: Türkiya
    Sıbırca: Törkiyä
    Gagauzça: Türkiyä
    Saqalī: Türkiye (Türküye)
    Dulgan-Hakalī: Türkiye (Türküye)
    Tıvalap: Türkiye
    Salırça: Türkiye
    Xakastap: Türkiya (Turkiya)
    Altay: ???
    Şor: ???
    Urumça: Türkiya
    Karajče: Turkija
    Qrımçahça: Türkiya
    Soyot: ???
    Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ты" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "you" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sen":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰾𐰤 
🇬🇧 English: you (singular) (write "siz" for plural)
🇷🇺 Русский: ты [ty]
🇹🇷 Türkçe: sen
🇦🇿 Türkcə: sən
🇹🇲 Türkmençe: sen
🇺🇿 Oʻzbekcha: sen
🇰🇿 Qazaqşa: sen
🇰🇬 Qırğızça: sen
    Uyghurche: sen
    Tatarça: sin
    Başqortsa: hin
    Çovaşla: esö
    Qaraqalpaqsha: sen
    Qırımtatarca: sen
    Qumuqça: sen
    Qaraçay-Malqar: sen
    Noğayşa: sen
    Sıbırca: sin (sen)
    Gagauzça: sän
    Saqalī: en
    Tıvalap: sen
    Salırça: sän (sen)
    Xakastap: sin
    Altay: sen
    Şor: sen
    Dolgan: en
    Urumça: sän (sen)
    Karaj: sień
    Qrımçahça: sen
    Soyot: sen
    Tofalap: sen''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тяжелый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тяжелая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тяжелое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тяжелые" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ağır" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ağir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "heavy":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰍𐰃𐰺
🇬🇧 English: heavy
🇷🇺 Русский: тяжелый (-ая, -ое)
🇹🇷 Türkçe: ağır
🇦🇿 Türkcə: ağır
🇹🇲 Türkmençe: agyr
🇺🇿 Oʻzbekcha: ogʻir
🇰🇿 Qazaqşa: awır
🇰🇬 Qırğızça: oor
    Uyghurche: eghir
    Tatarça: awır
    Başqortsa: awır
    Çovaşla: yıvor
    Qaraqalpaqsha: awır
    Qırımtatarca: ağır
    Qumuqça: awur
    Qaraçay-Malqar:	awur
    Noğayşa: awır
    Sıbırca: awır (awur, äwür)
    Gagauzça: aar
    Saqalī: ıar
    Dulğan-Hakalī: ıar
    Tıvalap: aar
    Salırça: āğırcux, ağır
    Xakastap: aar
    Altay: uur
    Şor: aar
    Urumça: ağır (avur)
    Karaj: avur (ahyr)
    Qrımçahça: ağır
    Soyot: aar
    Tofalap: aar''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "у нас" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "we have" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "with us" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bizde" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пизда":
        bot.send_message(message.chat.id, '''🇬🇧 English: we have, with us
🇷🇺 Русский: у нас [u nas]
🇹🇷 Türkçe: bizde
🇦🇿 Türkcə: bizdə
🇹🇲 Türkmençe: bizde
🇺🇿 Oʻzbekcha: bizda
🇰🇿 Qazaqşa: bizde
🇰🇬 Qırğızça: bizde
    Uyghurche: bizde
    Tatarça: bezdä
    Başqortsa: beððä
    Çovaşla: epirte
    Qaraqalpaqsha: bizde
    Qırımtatarca: bizde
    Qumuqça: bizde
    Qaraçay-Malqar: bizde
    Noğayşa: bizde
    Sıbırca: pestä
    Gagauzça: bizde
    Saqalıı: bihigiga
    Hakalıı (Dulgan):	bihigiga
    Tıvalap: biste
    Salırça: piserde
    Xakastap: piste
    Altay: biste
    Şor: piste
    Urumça: bizde
    Karaj: biźdie
    Qrımçahça: bızde
    Soyot: bîstê
    Tofalap: bîstê''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "narrow" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "узкий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "узкая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "узский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "узкое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "узкие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тесный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "узко" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тесно" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тесные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dar":
        bot.send_message(message.chat.id, '''🇬🇧 English: narrow
🇷🇺 Русский: узкий, тесный (-ая, -ое)
🇹🇷 Türkçe: dar
🇦🇿 Türkcə: dar
🇹🇲 Türkmençe: dar
🇺🇿 Oʻzbekcha: tor
🇰🇿 Qazaqşa: tar
🇰🇬 Qırğızça: tar
    Uyghurche: tar
    Tatarça: tar
    Başqortsa: tar
    Çovaşla: tovor, ansor
    Qaraqalpaqsha: tar
    Qırımtatarca: tar
    Qumuqça: tar
    Qaraçay-Malqar:	tar
    Noğayşa: tar
    Sıbırca: tar
    Gagauzça: dar
    Saqalī: kıarağas, sinńiges
    Dulğan-Hakalī: kıaragas
    Tıvalap: tar, kızıı
    Salırça: tar
    Xakastap: tar, niske
    Altay: tar, qızıq
    Şor: tar
    Urumça: dar (tar), sıxıx
    Karajče: tar, kysyk (kysych)
    Qrımçahça: tar
    Soyot: tar
    Tofalap: tar, nîñge''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "salyangoz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gastropoda" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "snail" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "улитка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "улиточный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "улиточка":
        bot.send_message(message.chat.id, '''🇬🇧 English: snail, gastropoda
🇷🇺 Русский: улитка [ulitka]
🇹🇷 Türkçe: salyangoz
🇦🇿 Türkcə: ilbiz, şeytan (dialect), babaqulu (dialect), xaxayək (dialect), xəxəy (dialect)
🇹🇲 Türkmençe: balykgulak
🇺🇿 Oʻzbekcha: shilliq
🇰🇿 Qazaqşa: ulıw
🇰🇬 Qırğızça: ülül, qoçqor müyüz
🌏 Uyghurche: qulule, qochqar müñüz, muzaybişi
🌍 Tatarça: äkäm-tökäm, quçqar
🌍 Başqortsa: qusqar
🌍 Çovaşla: şuy, şuyttan moyraki, suyttan-xuran
🌍 Qaraqalpaqsha: suw ögizi
🌍 Qırımtatarca: çıqçıqbalaban
🌍 Qumuqça: xurtuya
🌍 Qaraçay-Malqar: tekelemüyüz
🌍 Noğayşa: ıluw
🌏 Sıbırca: äkäk-tökäm, qucqar
🌍 Gagauzça: sülük, melk
🌏 Saqalī: qaba, çoqu qāta
🌏 Dulgan-Hakalī: çoku kāta
🌏 Tıvalap: xap-balık
🌏 Salırça: puzuvaş, mogumo
🌏 Xakastap: ???
🌏 Altaylap: cılan-castıq
🌏 Şor: ???
🌍 Urumça: çıxçıxbalaban, sümükli böcük
🌍 Karajče: siliegejli kurt, tyrtyr, baha
🌍 Qrımçahça: tırtır
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ухо" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уши" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ear" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kulak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "an ear":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰸𐰆𐰞𐰴
🐺 Old Turkic: qulaq (qulğaq, qulxaq, qulqaq)
🇬🇧 English: ear
🇷🇺 Русский: ухо [ukho]
🇹🇷 Türkçe: kulak
🇦🇿 Türkcə: qulaq
🇹🇲 Türkmençe: gulak
🇺🇿 Oʻzbekcha: quloq
🇰🇿 Qazaqşa: qulaq
🇰🇬 Qırğızça: qulaq
    Uyghurche: qulaq
    Tatarça: qolaq
    Başqortsa: qolaq
    Çovaşla: xolxa
    Qaraqalpaqsha: qulaq
    Qırımtatarca: qulaq
    Qumuqça: qulaq
    Qaraçay-Malqar:	qulaq
    Noğayşa: qulaq
    Sıbırca: qolaq
    Gagauzça: kulak
    Saqalī: kulgāq
    Dulgan-Hakalī: kulgāk
    Tıvalap: kulak
    Salırça: qulax (kulax), kum
    Xakastap: xulax
    Altaylap: qulaq
    Şor: qulaq
    Urumça: xulax (ğulax, ğulağ)
    Karajče: kulach (kulak)
    Qrımçahça: qulah
    Soyot: qulaq
    Tofalap: qulaq''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "february" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "февраль" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "februar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şubat":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: february
🇷🇺 Русский: февраль [fevral']
🇹🇷 Türkçe: şubat
🇦🇿 Türkcə: fevral, şubat (şübat)
🇹🇲 Türkmençe: baýdak
🇺🇿 Oʻzbekcha: fevral, hut
🇰🇿 Qazaqşa: aqpan, qut
🇰🇬 Qırğızça: birdin ayı
    Uyghurche: hud
    Tatarça: fibral, aqman, şöbat
    Başqortsa: şaqay
    Çovaşla: naros
    Qaraqalpaqsha: fevral, hut
    Qırımtatarca: fevral, kiçik ay
    Qumuqça: fevral, çille
    Qaraçay-Malqar: fevral, bayrım
    Noğayşa: fevral, uwıt
    Sıbırca: fevral, qot, köcögän
    Gagauzça: gücük
    Saqalī: olunńu
    Dulğan-Hakalī: üöles
    Tıvalap: iyi
    Salırça: ikinci
    Xakastap: fevral
    Xakastap (Sağay): azığ
    Xakastap (Pîltir): azığ
    Xakastap (Xaas): pözig
    Altaylap: fevral, qoçqor
    Şor: azığ
    Urumça: fevrar
    Karajče: (they use Karaim calendar)
    Qrımçahça: fevral
    Soyot: fevral
    Tofalap: kuruğ hovuğ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "федор" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "федя" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "theodore" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "theodor" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ted" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "teddy" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "teodor" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "todur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пидр" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tevazirus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пидор":
        bot.send_message(message.chat.id, '''🇬🇧 English: Theodore, Ted, Teddy
🇷🇺 Русский: Фёдор, Федя
🇹🇷 Türkçe: Tevazirus
🇰🇿 Qazaqşa: Şodır
🌍 Çovaşla: Xüetör (Xövetör, Xöveyuk, Öveyuk)
🌍 Qaraçay-Malqar: Totur
🌍 Gagauzça: Todur
🌏 Saqalī: Süöder
🌏 Dulgan-Hakalī: Pēder
🌏 Xakastap: Pidor
🌏 Şor: Pödir
🌍 Urumça: Todor''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fruct" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "meyve" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фрукт" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "плод" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fruit" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fruits":
        bot.send_message(message.chat.id, '''🇬🇧 English: fruit
🇷🇺 Русский: фрукт [frukt], плод [plod]
🇲🇳 Mongol: jims
🇹🇷 Türkçe: yemiş, meyve
🇦🇿 Türkcə: meyvə, yemiş (dialect, meaning may vary, "muskmelon" in standart language)
🇹🇲 Türkmençe: iýmiş, miwe
🇺🇿 Oʻzbekcha: meva
🇰🇿 Qazaqşa: jemis
🇰🇬 Qırğızça: jemiş
    Uyghurche: méwe
    Tatarça: cimeş
    Başqortsa: yemeş
    Çovaşla: cimöc
    Qaraqalpaqsha: jemis, miywe
    Qırımtatarca: meyva, yemiş
    Qumuqça: yemiş
    Qaraçay-Malqar:	köget, jemiş
    Noğayşa: yemis
    Sıbırca: yemeş
    Gagauzça: meyva
    Saqalī: burūkta (frukta), oton (soft fruit)
    Dulğan-Hakalī: hugun (soft fruit)
    Tıvalap: çimis
    Salırça: yimiş, armut-irıx
    Xakastap: frukt, nîmîs
    Altaylap: ciilek, frukta
    Şor: ezre
    Urumça: meyvä (meyva, meva), yemiş
    Karajče: jemiš (jemis)
    Qrımçahça: yemış, meyva
    Soyot: hat (soft fruit)
    Tofalap: qat (soft fruit)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "химия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chemistry" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kimya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kimiya":
        bot.send_message(message.chat.id, '''🇬🇧 English: chemistry
🇷🇺 Русский: химия [khimiya]
🇹🇷 Türkçe: kimya
🇦🇿 Türkcə: kimya
🇹🇲 Türkmençe: himiýa, kimýä (archaism)
🇺🇿 Oʻzbekcha: kimyo, ximiya
🇰🇿 Qazaqşa: himiya, kiymiye (archaism)
🇰🇬 Qırğızça: ximiya
    Uyghurche: ximiye
    Tatarça: ximiä, kimiä (kimia) (archaism)
    Başqortsa: ximiya, ximeyä (archaism)
    Çovaşla: ximi
    Qaraqalpaqsha: ximiya
    Qırımtatarca: kimya, himiya
    Qumuqça: ximiya
    Qaraçay-Malqar: ximiya
    Noğayşa: ximiya
    Sıbırca: ximiya
    Gagauzça: kimya
    Saqalī: qimiya
    Dulgan-Hakalī: ???
    Tıvalap: ???
    Salırça: xuaşye
    Xakastap: ???
    Altaylap: ???
    Şor: ???
    Urumça: ???
    Karajče: chimija
    Qrımçahça: ???
    Soyot: ???
    Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "good" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iyi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yahşi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yahşı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хороший" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хорошая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хорошее" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хорошие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хорошо":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰓𐰏𐰇
🐺 Old Turkic (bef. 13th c.): edgü, kuşal, nik
🇬🇧 English: good
🇷🇺 Русский: хороший (-ая, -ое)
🇹🇷 Türkçe: iyi
🇦🇿 Türkcə: yaxşı
🇹🇲 Türkmençe: ýagşy
🇺🇿 Oʻzbekcha: yaxshi, ezgu
🇰🇿 Qazaqşa:	jaqsı, iygi
🇰🇬 Qırğızça: jaqşı
🌏 Uyghurche: yakhshi
🌍 Tatarça:	yaxşı
🌍 Başqortsa: yaqşı
🌍 Çovaşla: layox, avan, yuroxlo
🌍 Qaraqalpaqsha: jaqsı
🌍 Qırımtatarca: yahşı, eyi
🌍 Qumuqça: yaxşı
🌍 Qaraçay-Malqar: aşxı, igi
🌍 Noğayşa: yaxşı, iygi
🌏 Sıbırca: yaqşı
🌍 Gagauzça: iyi (iy), islää
🌏 Saqalī: ütüö, üçügey
🌏 Dulgan-Hakalī: üçügey
🌏 Tıvalap: eki
🌏 Salırça: yaxşi
🌏 Xakastap: çaxsı
🌏 Altaylap: caqşı
🌏 Şor: çaqşı
🌍 Urumça: yaxşı, iyi (ey, eyi)
🌍 Karajče: jachšy, iji (ėgi, ėji)
🌍 Qrımçahça: yaxşı, eyı
🌏 Soyot: ekki
🌏 Tofalap: ekki, bert''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "christian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "христианин" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "христианский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "христиан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "християнин" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "христианка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hristiyan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "isevi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nasrani":
        bot.send_message(message.chat.id, '''🇬🇧 English: christian
🇷🇺 Русский: христианин [khristianin]
🇹🇷 Türkçe: hristiyan, isevi, nasrani
🇦🇿 Türkcə: xaçpərəst, isəvi, nəsrani, məsihi, xristian
🇹🇲 Türkmençe: haçparaz, hristian, nasary {arch.}
🇺🇿 Oʻzbekcha: xristian, masihiy, masihchi
🇰🇿 Qazaqşa: kiresşi, mäsihşi, hristiyan
🇰🇬 Qırğızça: maşayaqçı
    Uyghurche: mesihiy, mesihchi
    Tatarça: mäsixçe, xristian
    Başqortsa: mäsixse, xristian
    Çovaşla: xristian
    Qaraqalpaqsha: másixshi‎, xristian
    Qırımtatarca: mesihiy, hristian
    Qumuqça: xaçperes, xristian
    Qaraçay-Malqar: xristianlı
    Noğayşa: şoqınğan, xristian
    Sıbırca: mäsixi, cuğınqan
    Gagauzça: ristian (hristian)
    Saqalī: qristian
    Tıvalap: xristian
    Xakastap: xrîstîan
    Altay: krestü kiji
    Şor: xristian
    Dolgan: xristian
    Urumça: xristiyan, xristianos
    Karaj: christian
    Qrımçahça: hristian
    Soyot: xrîstîan
    Tofalap: xrîstîan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "flower" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "цветы" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "цветок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "цветки" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çiçek":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): çeçäk, qua (xua)
🇬🇧 English: flower
🇷🇺 Русский: цветок, цветки
🇲🇳 Mongol: tsetseg
🇹🇷 Türkçe: çiçek
🇦🇿 Türkcə: çiçək, gül
🇹🇲 Türkmençe: gül
🇺🇿 Oʻzbekcha: gul, chechak
🇰🇿 Qazaqşa: gül, şeşek
🇰🇬 Qırğızça: gül
    Uyghurche: gül, chéchek
    Tatarça: çäçäk, göl
    Başqortsa: säskä, göl
    Çovaşla: çeçek, cecke
    Qaraqalpaqsha: gúl
    Qırımtatarca: çiçek (çeçek)
    Qumuqça: çeçek, gül
    Qaraçay-Malqar:	çiçek, gül, gokka xans
    Noğayşa: şeşekey
    Sıbırca: cicäk, köl, cicegäy
    Gagauzça: çiçek
    Saqalī: çeçik, sibekki (cvetki)
    Dulgan-Hakalī: ot
    Tıvalap: çeçek
    Salırça: çiçex (çiçix), xua
    Xakastap: çaxayax, porço
    Altaylap: çeçek
    Şor: çaqkiyek
    Urumça: çiçäk (çiçek), gül
    Karajče: čiečiak (cieciek, čiček)
    Qrımçahça: çıçek
    Soyot: çeçäk (çeçek)
    Tofalap: aqqaş (aqaş)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "человек" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "human" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "insan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kişi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ademoğlu":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰚𐰃𐰾𐰃 (𐰚𐰃𐱁𐰃)
🇬🇧 English: human
🇷🇺 Русский: человек [chelovek]
🇹🇷 Türkçe: insan, kişi
🇦🇿 Türkcə: insan, adam, Adəm oğlu (religious)
🇹🇲 Türkmençe: ynsan, adam, kişi
🇺🇿 Oʻzbekcha: kishi, odam, inson
🇰🇿 Qazaqşa: adam, kisi, ınsan (religious)
🇰🇬 Qırğızça: kişi, adam, ınsan
    Uyghurche: insan, kishi, adem
    Tatarça: keşe, adäm, insan
    Başqortsa: keşe, äðäm, insan
    Çovaşla: cın, etem
    Qaraqalpaqsha: kisi, adam, insan
    Qırımtatarca: insan, adam, kişi, Adem evlâdı (religious)
    Qumuqça: adam, gişi, insan
    Qaraçay-Malqar:	adam, kişi, insan
    Noğayşa: ädem, kisi, ınsan
    Sıbırca: keşe (kişi), ätäm
    Gagauzça: insan, kişi, insanoolu (religious)
    Saqalī: kihi
    Dulğan-Hakalī: kihi
    Tıvalap: kiji
    Salırça: kişi (keşe), atam, kişicux
    Xakastap: kizi
    Altay: kiji
    Şor: kiji
    Urumça: insan, adam, kişi
    Karajče: kiši (kisi), adam, insan, adam ohlu
    Qrımçahça: insan, adam, kışı
    Soyot: kîşî (kîhî)
    Tofalap: kîşî''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "worm" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "червь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "червяк" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurt" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "solucan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "червячек":
        bot.send_message(message.chat.id, '''🇬🇧 English: worm
🇷🇺 Русский: червь [cherv'], червяк [chervyak]
🇹🇷 Türkçe: kurt, solucan
🇦🇿 Türkcə: qurd, soxulcan, sazan (dialect)
🇹🇲 Türkmençe: gurt, gurçuk
🇺🇿 Oʻzbekcha: qurt, chuvalchang
🇰🇿 Qazaqşa: qurt, şubalşaŋ
🇰🇬 Qırğızça: qurt
    Uyghurche: qurt (qurut)
    Tatarça:	qort, sualçan (suwalçan)
    Başqortsa: qort, seläwsen
    Çovaşla: xurt, oman
    Qaraqalpaqsha: qurt
    Qırımtatarca: qurt, sıvalçan (suvalçan)
    Qumuqça: xurt
    Qaraçay-Malqar:	qurt
    Noğayşa: qurt
    Sıbırca: qort, uwulsan
    Gagauzça: kurt, solcan (solcaan, solucan)
    Saqalī: çierbe, üön
    Dulğan-Hakalī: üön
    Tıvalap: kurt, şıylaşkın
    Salırça: sugulcıñ
    Xakastap: xurt
    Altaylap: qurt, çoyloşqon
    Şor: qurt, şoşqan
    Urumça: ğurt (xurt), suvalçan (sıvalçan)
    Karajče: kurt
    Qrımçahça: qurt
    Soyot: qurt, şoylaşqan
    Tofalap: qurt''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "black" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kara" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "siyah" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "черный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "черная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "черные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "черное":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰺𐰀 
🐺 Old Turkic: qara
🇬🇧 English: black
🇷🇺 Русский: чёрный (-ая, -ое)
🇯🇵 Nihongo: kuro
🇲🇳 Mongol: khara (khar)
🇹🇷 Türkçe: kara, siyah
🇦🇿 Türkcə: qara
🇹🇲 Türkmençe: gara
🇺🇿 Oʻzbekcha: qora
🇰🇿 Qazaqşa: qara
🇰🇬 Qırğızça: qara
    Uyghurche: qara
    Tatarça: qara
    Başqortsa: qara
    Çovaşla: xura
    Qaraqalpaqsha: qara
    Qırımtatarca: qara
    Qumuqça: qara
    Qaraçay-Malqar: qara
    Noğayşa: qara
    Sıbırca: qara
    Gagauzça: kara
    Saqalī: qara
    Dulgan-Hakalī: kara
    Tıvalap: kara
    Salırça: qara
    Xakastap: xara
    Altaylap: qara
    Şor: qara
    Urumça: ğara (kara, xara)
    Karajče: kara
    Qrımçahça: qara
    Soyot: qara
    Tofalap: qara''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "four" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "4" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "четыре" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dört" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dörd":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱅𐰇𐰼𐱅 
🇬🇧 English: four
🇷🇺 Русский: четыре [chetyre]
🇹🇷 Türkçe: dört
🇦🇿 Türkcə: dörd
🇹🇲 Türkmençe: dört
🇺🇿 Oʻzbekcha: toʻrt
🇰🇿 Qazaqşa: tört
🇰🇬 Qırğızça: tört
    Uyghurche: tört
    Tatarça: dürt
    Başqortsa: dürt
    Çovaşla: tovat (tovato, tovatto)
    Qaraqalpaqsha: to'rt
    Qırımtatarca: dört
    Qumuqça: dört
    Qaraçay-Malqar: tört
    Noğayşa: dört
    Sıbırca: dürt
    Gagauzça: dört
    Saqalī: tüört
    Tıvalap: dört
    Salırça: t'öt
    Xakastap: tört
    Altay: tört
    Şor: tört
    Dolgan: tüört
    Urumça: dört (dörd)
    Karaj: diort’
    Qrımçahça: dört
    Soyot: dört''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "что" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "what" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ne" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "туох":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰤𐰀, 𐰭𐰭
🇬🇧 English: what
🇷🇺 Русский: что (местоимение)
🇹🇷 Türkçe: ne
🇦🇿 Türkcə: nə
🇹🇲 Türkmençe: näme
🇺🇿 Oʻzbekcha: nima, na
🇰🇿 Qazaqşa: ne
🇰🇬 Qırğızça: emne
    Uyghurche: néme
    Tatarça: ni, närsä
    Başqortsa: ni, nimä
    Çovaşla: mön
    Qaraqalpaqsha: ne
    Qırımtatarca: ne
    Qumuqça: ne
    Qaraçay-Malqar:	ne
    Noğayşa: ne
    Sıbırca: ni, nimä (nämä)
    Gagauzça: ne
    Saqalī: tuoq
    Dulgan-Hakalī: tuok
    Tıvalap: çüü
    Salırça: nä (ne), neñ (nañ, niñ)
    Xakastap: nîme
    Altay: ne, neme
    Şor: noo
    Urumça: nä (ne, ni, nı)
    Karaj: nie (ne)
    Qrımçahça: ne
    Soyot: çü (cü)
    Tofalap: çü''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "altı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "alti" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "six" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "6" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шесть":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰞𐱃𐰃
🐺 Old Turkic (bef. 13th c.): altı
🇬🇧 English: six
🇷🇺 Русский: шесть [shest']
🇹🇷 Türkçe: altı
🇦🇿 Türkcə: altı
🇹🇲 Türkmençe: alty
🇺🇿 Oʻzbekcha: olti
🇰🇿 Qazaqşa: altı
🇰🇬 Qırğızça: altı
🌏 Uyghurche: alte
🌍 Tatarça: altı
🌍 Başqortsa: altı
🌍 Çovaşla: ulto (ultto)
🌍 Qaraqalpaqsha: altı
🌍 Qırımtatarca: altı
🌍 Qumuqça: altı
🌍 Qaraçay-Malqar: altı
🌍 Noğayşa: altı
🌏 Sıbırca: altı
🌍 Gagauzça: altı
🌏 Saqalī: alta
🌏 Dulgan-Hakalī: alta
🌏 Tıvalap: aldı
🌏 Salırça: altı
🌏 Xakastap: altı
🌏 Altaylap: altı (alçı)
🌏 Şor: altı
🌍 Urumça: altı
🌍 Karajče: alty
🌍 Qrımçahça: altı
🌏 Soyot: altı
🌏 Tofalap: altı''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "wide" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "broad" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "широкий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "широкая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "широкое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "широкие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "enli" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "geniş":
        bot.send_message(message.chat.id, '''🇬🇧 English: wide, broad
🇷🇺 Русский: широкий (-ая, -ое)
🇹🇷 Türkçe: geniş, enli
🇦🇿 Türkcə: gen, geniş, enli
🇹🇲 Türkmençe: giň, giňiş, inli
🇺🇿 Oʻzbekcha: keng, enlik, serbar
🇰🇿 Qazaqşa: keŋ, jalpaq
🇰🇬 Qırğızça: keñ, endüü, jazı
    Uyghurche: keng, azade
    Tatarça: kiñ, iñle
    Başqortsa: kiñ, iñle, yaþı
    Çovaşla: anlo, sarlaka
    Qaraqalpaqsha: keń, enli
    Qırımtatarca: keñ, keniş
    Qumuqça: geñ, enli
    Qaraçay-Malqar:	keñ, erkin
    Noğayşa: keñ, enli
    Sıbırca: käñ (kiñ), yalbaq, yalbırsaq, yazı
    Gagauzça: geniş
    Saqalī: kieñ, ketit
    Dulğan-Hakalī: ketit
    Tıvalap: delgem, algıg
    Salırça: ???
    Xakastap: allığ, çalbax
    Altay: keñ, calbaq, elbek
    Şor: keñ, çalbaq, ennig
    Urumça: enni (eñli, yeñli), keñ
    Karaj: kień (ken), avlach (avlak), keńiš
    Qrımçahça: keñ
    Soyot: eńgiri, alhığ (alhuğ), örgän
    Tofalap: eńgiri, alhığ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "школа" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "school" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "okul" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mektep" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mekteb" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мактаб":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): nikay (religious)
🇬🇧 English: school
🇷🇺 Русский: школа [shkola]
🇹🇷 Türkçe: okul (*?), mektep (archaism)
🇦🇿 Türkcə: məktəb (North Azerbaijani), mədrəsə (South Azerbaijani)
🇹🇲 Türkmençe: mekdep
🇺🇿 Oʻzbekcha: maktab
🇰🇿 Qazaqşa: mektep
🇰🇬 Qırğızça: mektep
🌏 Uyghurche: mektep
🌍 Tatarça: mäktäp
🌍 Başqortsa: mäktäp
🌍 Çovaşla: şkul
🌍 Qaraqalpaqsha: mektep
🌍 Qırımtatarca: mektep
🌍 Qumuqça: maktap
🌍 Qaraçay-Malqar: şkol
🌍 Noğayşa: mektep
🌏 Sıbırca: mäktäp
🌍 Gagauzça: şkola, okul
🌏 Saqalī: oskuola
🌏 Dulgan-Hakalī: oskuola (şkola)
🌏 Tıvalap: şkola
🌏 Salırça: mextabus, şüeşo (şyeşo, şöşü)
🌏 Xakastap: şkola
🌏 Altaylap: şqol
🌏 Şor: şqol
🌍 Urumça: sxolios (şkola, skolâ, skolios, sxolio)
🌍 Karajče: üriatiuv üviu
🌍 Qrımçahça: mekteb
🌏 Soyot: ışqool
🌏 Tofalap: ööredir öğ, ışqool
    * 🇫🇷 Français: école''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "these" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "this" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "этот" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "эта" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "эти":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰉𐰆
🇬🇧 English: this, these
🇷🇺 Русский: этот, эта, эти
🇹🇷 Türkçe: bu
🇦🇿 Türkcə: bu
🇹🇲 Türkmençe: bu
🇺🇿 Oʻzbekcha: bu
🇰🇿 Qazaqşa: bul (bu)
🇰🇬 Qırğızça: bu (bul)
    Uyghurche: bu
    Tatarça: bu
    Başqortsa: bıl
    Çovaşla: ku
    Qaraqalpaqsha: bul
    Qırımtatarca: bu
    Qumuqça: bu
    Qaraçay-Malqar:	bu
    Noğayşa: bu
    Sıbırca: pı (bu, po, pö, bo, bö)
    Gagauzça: bu
    Saqalī: bu
    Hakalī (Dulgan): bu
    Tıvalap:	bo
    Salırça: pu (bu, po, mo)
    Xakastap: pu
    Altay: bu
    Şor: po
    Urumça: bu
    Karaj: bu
    Qrımçahça: bu
    Soyot: bo
    Tofalap: bo''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "i" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "I" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "я" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ben":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰢𐰤 
🇬🇧 English: I
🇷🇺 Русский: я [ya]
🇹🇷 Türkçe: ben
🇦🇿 Türkcə: mən
🇹🇲 Türkmençe: men
🇺🇿 Oʻzbekcha: men
🇰🇿 Qazaqşa: men
🇰🇬 Qırğızça: men
    Uyghurche: men
    Tatarça: min
    Başqortsa: min
    Çovaşla: epö
    Qaraqalpaqsha: men
    Qırımtatarca: men
    Qumuqça: men
    Qaraçay-Malqar: men
    Noğayşa: men
    Sıbırca: min (ben, män)
    Gagauzça: bän
    Saqalī: min
    Tıvalap: men
    Salırça: män (men)
    Xakastap: min
    Altay: men
    Şor: men
    Dolgan: min
    Urumça: bän (men)
    Karaj: mień
    Qrımçahça: men
    Soyot: men
    Tofalap: men''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "apple" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "яблоко" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "alma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "elma":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): alma, alımla
🇬🇧 English: apple
🇷🇺 Русский: яблоко [yabloko]
🇭🇺 Magyar: alma
🇲🇳 Mongol: alim (alima)
🇹🇷 Türkçe: elma
🇦🇿 Türkcə: alma
🇹🇲 Türkmençe: alma
🇺🇿 Oʻzbekcha: olma
🇰🇿 Qazaqşa: alma
🇰🇬 Qırğızça: alma
🌏 Uyghurche: alma
🌍 Tatarça: alma
🌍 Başqortsa: alma
🌍 Çovaşla: ulma, panulmi
🌍 Qaraqalpaqsha: alma
🌍 Qırımtatarca: alma
🌍 Qumuqça: alma
🌍 Qaraçay-Malqar: alma
🌍 Noğayşa: alma
🌏 Sıbırca: alma
🌍 Gagauzça: alma
🌏 Saqalī: jābılaka (yabloko)
🌏 Dulgan-Hakalī: yabloko
🌏 Tıvalap: yablok (yabloko)
🌏 Salırça: alima
🌏 Xakastap: yabloko
🌏 Altaylap: yablok, alma (archaism)
🌏 Şor: yabloko
🌍 Urumça: alma
🌍 Karajče: alma
🌍 Qrımçahça: alma
🌏 Soyot: yabloko
🌏 Tofalap: yabloga''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lamb" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ягненок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kuzu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "барашек" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "барашка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "детеныш барана" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "детеныш овцы" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ягнец":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): qozı, baqlan qozı (fat livestock lamb), toqlı (0,5 y.o.), sögüş (meat)
🇬🇧 English: lamb
🇷🇺 Русский: ягнёнок [yagnyonok]
🇯🇵 Nihongo: kohitsuji
🇹🇷 Türkçe: kuzu
🇦🇿 Türkcə: quzu
🇹🇲 Türkmençe: guzy
🇺🇿 Oʻzbekcha: qoʻzi
🇰🇿 Qazaqşa: qozı, qoşaqan
🇰🇬 Qırğızça: qozu
🌏 Uyghurche: qoza, paqlan
🌍 Tatarça: quzı, bäti, bärän
🌍 Başqortsa: quðı, harıq bäräse, tuqtı
🌍 Çovaşla: pütek, poran (puran, puram, poram)
🌍 Qaraqalpaqsha: qozı
🌍 Qırımtatarca: qozu, canay (dial.), qocanay (dial.)
🌍 Qumuqça: qozu
🌍 Qaraçay-Malqar: qozu
🌍 Noğayşa: qozı
🌏 Sıbırca: qusı, quy pala
🌍 Gagauzça: kuzu
🌏 Saqalī: barān oğoto
🌏 Dulgan-Hakalī: barān ogoto
🌏 Tıvalap: xuragan*
🌏 Salırça: qozı (quzı, gozi)
🌏 Xakastap: xuçacax, xurağan*
🌏 Altaylap: quraan*
🌏 Şor: qurağan* (1 y.o.), tölege (2 y.o.)
🌍 Urumça: xuzu (ğuzi, xozu), xozu bala
🌍 Karajče: kozu, jaš koj
🌍 Qrımçahça: qozu
🌏 Soyot: hurağan*, tölik (1 y.o.)
🌏 Tofalap: hoy oğlu, hurağan* (1 y.o.)
    * 🇲🇳 Mongol: khurga''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "язык" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "language" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tongue" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lang":
        bot.send_message(message.chat.id, '''🇬🇧 English: I. language II. tongue
🇷🇺 Русский: язык [yazyk]
🇹🇷 Türkçe: dil
🇦🇿 Türkcə: dil
🇹🇲 Türkmençe: dil
🇺🇿 Oʻzbekcha: til
🇰🇿 Qazaqşa: til
🇰🇬 Qırğızça: til
    Uyghurche: til
    Tatarça: tel
    Başqortsa: tel
    Çovaşla: çölxe
    Qaraqalpaqsha: til
    Qırımtatarca: til
    Qumuqça: til
    Qaraçay-Malqar: til
    Noğayşa: til
    Sıbırca: tel (til)
    Gagauzça: dil
    Saqalī: tıl
    Dulğan-Hakalī: I. haña II. tıl
    Tıvalap: dıl
    Salırça: til (dil)
    Xakastap: til
    Altay: til
    Şor:	til
    Urumça: dil (til)
    Karajče: til´ (til)
    Qrımçahça: tıl
    Soyot: dıl (tıl)
    Tofalap: dıl (tıl)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "egg" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eggs" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "яйцо" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "яицо" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yumurta":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): yumurtğa (yumurqa)
🇬🇧 English: egg
🇷🇺 Русский: яйцо [yaytso]
🇹🇷 Türkçe: yumurta
🇦🇿 Türkcə: yumurta
🇹🇲 Türkmençe: ýumurtga
🇺🇿 Oʻzbekcha: tuxum, yumurtqa
🇰🇿 Qazaqşa: jumırtqa
🇰🇬 Qırğızça: jumurtqa
🌏 Uyghurche: tukhum
🌍 Tatarça: yomırqa
🌍 Başqortsa: yomortqa
🌍 Çovaşla: comarta
🌍 Qaraqalpaqsha: máyek
🌍 Qırımtatarca: yımırta
🌍 Qumuqça: yımırtqa
🌍 Qaraçay-Malqar: jumurtxa, gakkı
🌍 Noğayşa: yumırtqa
🌏 Sıbırca: yomortqa (yomırtqa)
🌍 Gagauzça: yımırta
🌏 Saqalī: sımīt
🌏 Dulgan-Hakalī: hımīt
🌏 Tıvalap: çumurga (çuurga)
🌏 Salırça: yumurta (yomurta, yumotor)
🌏 Xakastap: nımırxa
🌏 Altaylap: cımırtqa
🌏 Şor: nıbırtqa
🌍 Urumça: yumurta (yemırta)
🌍 Karajče: jumurtcha (jumurta, jymyrta)
🌍 Qrımçahça: yımırta
🌏 Soyot: çuurha (cuurha)
🌏 Tofalap: nümurha''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "january" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "januar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "январь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ocak ayı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ocak":
        bot.send_message(message.chat.id, '''🇬🇧 First written actual word (now in use), then historical (archaism). Before Russian invasion most of Turkic people used Hijri calendar, thats why they don't have words for Gregorian months and use Russian loanwords. 
🇷🇺 Сначала написан ныне используемый, затем исторический (устаревший). До российского нашествия, большинство тюркских народов использовали календарь по Хиджре, поэтому названия различаются, а многие используют заимствования из русского для обозначения Григорианских месяцев.
🇹🇷 Önce şimdi kullanımda olan kelime yazılmış, sonra tarihi (eskimiş), şimdi türk milletlerin coğu Miladi ayları için rusçadan alınma sözler kullanır, çünkü önce Hicri takvimi kullanırdı.

🇬🇧 English: january
🇷🇺 Русский: январь [yanvar']
🇹🇷 Türkçe: ocak
🇦🇿 Türkcə: yanvar, qanuni-sani
🇹🇲 Türkmençe: türkmenbaşy
🇺🇿 Oʻzbekcha: yanvar, dalv
🇰🇿 Qazaqşa: qaŋtar, däliw
🇰🇬 Qırğızça: üçtün ayı
    Uyghurche: qehritan
    Tatarça: ğıynwar, qırlaç
    Başqortsa: hıwığay
    Çovaşla: korlaç
    Qaraqalpaqsha: yanvar, dáliw
    Qırımtatarca: yanvar, qara qış
    Qumuqça: yanvar, ayuwyatğan
    Qaraçay-Malqar: yanvar, başil
    Noğayşa: yanvar, qañtar (qañıtar)
    Sıbırca: yanvar, tälew, yel (yil)
    Gagauzça: büük
    Saqalī: toqsunńu
    Dulğan-Hakalī: kün taksar
    Tıvalap: bir
    Salırça: pirinci
    Xakastap: yanvar
    Xakastap (Sağay): çîl
    Xakastap (Pîltir): kürgen
    Xakastap (Xaas): kürgen
    Altaylap: yanvar, çağan
    Şor: çel
    Urumça: yinar
    Karajče: (they use Karaim calendar)
    Qrımçahça: yanvar
    Soyot: yanvar
    Tofalap: aq''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "japanese" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "японец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "японка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "японский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "japon":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): cabarqalı
🇬🇧 English: japanese
🇷🇺 Русский: японец, японка, японский (-ая, -ое)
🇹🇷 Türkçe: japon
🇦🇿 Türkcə: yapon, japoni (archaism), japonlu (archaism)
🇹🇲 Türkmençe: ýapon
🇺🇿 Oʻzbekcha: yapon
🇰🇿 Qazaqşa: japon
🇰🇬 Qırğızça: japon (yapon)
🌏 Uyghurche: yapon
🌍 Tatarça: yapun
🌍 Başqortsa: yapon
🌍 Çovaşla: yappun (yappon, yapon)
🌍 Qaraqalpaqsha: yapon
🌍 Qırımtatarca: yapon
🌍 Qumuqça: yaponlu, yapon
🌍 Qaraçay-Malqar: yaponlu
🌍 Noğayşa: yapon
🌏 Sıbırca: yamar, nippon
🌍 Gagauzça: yapon
🌏 Saqalī: joppuon
🌏 Dulgan-Hakalī: joppuon
🌏 Tıvalap: yapon
🌏 Salırça: ribun, ribun kişi
🌏 Xakastap: yapon
🌏 Altaylap: yapon
🌏 Şor: yapon
🌍 Urumça: yapon
🌍 Karajče: japon
🌍 Qrımçahça: yapon (japon)
🌏 Soyot: yapon
🌏 Tofalap: yapon''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "japan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nippon" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "япония" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nihon" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ruğan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "japonya":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): Cabarqa (جَابَرْقَا)
🇬🇧 English: Japan
🇷🇺 Русский: Япония [Yaponiya]
🇯🇵 Nihongo: 日本 [Nippon, Nihon]
🇹🇷 Türkçe: Japonya, Ruğan (archaism, Ottoman Turkish)
🇦🇿 Türkcə: Yaponiya, Japon (archaism), Məmləkəti Japon (archaism)
🇹🇲 Türkmençe: Ýaponiýa
🇺🇿 Oʻzbekcha: Yaponiya
🇰🇿 Qazaqşa: Japoniya
🇰🇬 Qırğızça: Japoniya (Yaponiya)
🌏 Uyghurche: Yaponiye
🌍 Tatarça: Yapunstan, Yapuniä
🌍 Başqortsa: Yaponiya
🌍 Çovaşla: Yaponi
🌍 Qaraqalpaqsha: Yaponiya
🌍 Qırımtatarca: Yaponiya
🌍 Qumuqça: Yaponiya, Yapon (archaism)
🌍 Qaraçay-Malqar: Yapon
🌍 Noğayşa: Yaponiya
🌏 Sıbırca: Yamar il, Nippon el
🌍 Gagauzça: Yaponiya
🌏 Saqalī: Joppuon
🌏 Dulgan-Hakalī: Joppuon
🌏 Tıvalap: Yaponiya
🌏 Salırça: Ribun
🌏 Xakastap: Yaponîya
🌏 Altaylap: Yaponiya
🌏 Şor: Yaponiya
🌍 Urumça: Yaponiya
🌍 Karajče: Japonija
🌍 Qrımçahça: Yaponiya (Japonya)
🌏 Soyot: Yapon, Yaponîya
🌏 Tofalap: Yaponîya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "интернет" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "internet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ınternet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genel ağ" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genelağ" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "всемирная сеть":
        bot.send_message(message.chat.id, '''🇬🇧 English: internet
🇷🇺 Русский: интернет [internet], всемирная сеть [vsemirnaya set']
🇹🇷 Türkçe: internet [ˈintæɾnet], genel ağ
🇦🇿 Türkcə: internet
🇹🇲 Türkmençe: internet
🇺🇿 Oʻzbekcha: internet
🇰🇿 Qazaqşa: ğalamtor, internet
🇰🇬 Qırğızça: internet
🌏 Uyghurche: tor, intérnét
🌍 Tatarça: internet, bötendönyä çeltäre
🌍 Başqortsa: internet, donya seltäre
🌍 Çovaşla: internet, pur tönçe ereşö
🌍 Qaraqalpaqsha: internet
🌍 Qırımtatarca: internet
🌍 Qumuqça: internet
🌍 Qaraçay-Malqar: internet
🌍 Noğayşa: internet
🌏 Sıbırca: internet
🌍 Gagauzça: internet
🌏 Saqalī: interiniet
🌏 Dulgan-Hakalī: interiniet
🌏 Tıvalap: internet
🌏 Salırça: dor
🌏 Xakastap: înternet
🌏 Altaylap: internet
🌏 Şor: internet
🌍 Urumça: internet
🌍 Karajče: internet
🌍 Qrımçahça: internet
🌏 Soyot: înternêt
🌏 Tofalap: înternêt''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "история" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "history" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tarih" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hystory" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "histori" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tarıh":
        bot.send_message(message.chat.id, '''🇬🇧 English: history
🇷🇺 Русский: история [istoriya]
🇹🇷 Türkçe: tarih
🇦🇿 Türkcə: tarix
🇹🇲 Türkmençe: taryh
🇺🇿 Oʻzbekcha: tarix
🇰🇿 Qazaqşa: tarıyh, tawarıh {archaism}
🇰🇬 Qırğızça: tarıx
🌏 Uyghurche: tarix
🌍 Tatarça: tarix
🌍 Başqortsa: tarix
🌍 Çovaşla: istori
🌍 Qaraqalpaqsha: tariyx
🌍 Qırımtatarca: tarih
🌍 Qumuqça: tarix
🌍 Qaraçay-Malqar: tarix
🌍 Noğayşa: tarıx
🌏 Sıbırca: tariq
🌍 Gagauzça: tarih
🌏 Saqalī: ostuoruya
🌏 Dulgan-Hakalī: istoriya
🌏 Tıvalap: töögü
🌏 Salırça: lïşi
🌏 Xakastap: tarxın
🌏 Altaylap: istoriya
🌏 Şor: istoriya
🌍 Urumça: istoria
🌍 Karajče: istorija
🌍 Qrımçahça: tarih
🌏 Soyot: îstorîya
🌏 Tofalap: îstorîya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cake" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кекс" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "keks" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кек":
        bot.send_message(message.chat.id, '''🇬🇧 English: cake
🇷🇺 Русский: кекс [keks]
🇹🇷 Türkçe: kek
🇦🇿 Türkcə: keks
🇹🇲 Türkmençe: keks
🇺🇿 Oʻzbekcha: keks
🇰🇿 Qazaqşa: keks
🇰🇬 Qırğızça: keks
🌏 Uyghurche: keks
🌍 Tatarça: keks [kekes]
🌍 Başqortsa: keks [kekes]
🌍 Çovaşla: keks
🌍 Qaraqalpaqsha: keks
🌍 Qırımtatarca: keks
🌍 Qumuqça: keks
🌍 Qaraçay-Malqar: keks
🌍 Noğayşa: keks
🌏 Sıbırca: keks [kekes]
🌍 Gagauzça: keks
🌏 Saqalī: keks
🌏 Dulgan-Hakalī: keks
🌏 Tıvalap: keks
🌏 Salırça: dango
🌏 Xakastap: keks
🌏 Altaylap: keks
🌏 Şor: keks
🌍 Urumça: keks
🌍 Karajče: keks
🌍 Qrımçahça: keks
🌏 Soyot: keks
🌏 Tofalap: keks''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sea" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "море" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "deniz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "морской":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱃𐰞𐰆𐰖‎
🐺 Old Turkic (bef. 13th c.): teŋiz (deŋiz), taluy (talay), sundırı (sundurı)
🇬🇧 English: sea
🇷🇺 Русский: море [more]
🇲🇳 Mongol: tengis
🇹🇷 Türkçe: deniz
🇦🇿 Türkcə: dəniz
🇹🇲 Türkmençe: deňiz
🇺🇿 Oʻzbekcha: dengiz
🇰🇿 Qazaqşa: teŋiz
🇰🇬 Qırğızça: deŋiz
🌏 Uyghurche: dengiz
🌍 Tatarça: diñgez
🌍 Başqortsa: diñgeð
🌍 Çovaşla: tinös
🌍 Qaraqalpaqsha: teńiz
🌍 Qırımtatarca: deñiz
🌍 Qumuqça: deñiz
🌍 Qaraçay-Malqar: teñiz
🌍 Noğayşa: teñiz
🌏 Sıbırca: tiñges
🌍 Gagauzça: deniz
🌏 Saqalī: muora, bayğal
🌏 Dulgan-Hakalī: baygal, muora
🌏 Tıvalap: dalay (talay)
🌏 Salırça: deñiz
🌏 Xakastap: talay
🌏 Altaylap: talay
🌏 Şor: talay
🌍 Urumça: dängiz (deniz)
🌍 Karajče: tieńgiź (deńiź, deniz, teniz)
🌍 Qrımçahça: dengız
🌏 Soyot: dalay, deñgîs
🌏 Tofalap: dalay''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "city" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "город" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şehir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "городок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "town" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kent":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): balıq (baluq), känt (känd, ken), şähir, qala, toy
🇬🇧 English: I. city II. town
🇷🇺 Русский: I. город [gorod] II. городок, малый город
🇹🇷 Türkçe: I. şehir II. kent
🇦🇿 Türkcə: şəhər
🇹🇲 Türkmençe: şäher
🇺🇿 Oʻzbekcha: shahar
🇰🇿 Qazaqşa: qala, şahar
🇰🇬 Qırğızça: şaar
🌏 Uyghurche: sheher
🌍 Tatarça: şähär, qala
🌍 Başqortsa: qala
🌍 Çovaşla: xula
🌍 Qaraqalpaqsha: qala
🌍 Qırımtatarca: şeer
🌍 Qumuqça: şahar
🌍 Qaraçay-Malqar: şahar
🌍 Noğayşa: qala
🌏 Sıbırca: tora, qala
🌍 Gagauzça: kent, kasaba, şehir (bigger than kasaba)
🌏 Saqalī: kuorat
🌏 Dulgan-Hakalī: guorat
🌏 Tıvalap: xooray
🌏 Salırça: şexir, qın (cıñ), keyşañ
🌏 Xakastap: gorod, saar (acrhaism), xorım (archaism)
🌏 Altaylap: tura
🌏 Şor: tura
🌍 Urumça: şäär (şeyir, şer, şeyer, şeer)
🌍 Karajče: šahar (šeher, sahar, šachar)
🌍 Qrımçahça: şeer
🌏 Soyot: gorod
🌏 Tofalap: qoorıt (goorıt)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doll" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кукла" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kukla" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oyuncak bebek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "puppet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "a doll":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): quðurçuq
🇬🇧 English: doll
🇷🇺 Русский: кукла [kukla]
🇹🇷 Türkçe: bebek (oyuncak bebek), kukla
🇦🇿 Türkcə: kukla, gəlincik (usually female doll), gəlin (usually female doll), digin (archaism), müqəvva (archaism), qolçax (qolcaq) (dialect), bəbə (dialect), şonqubəbə (dialect), ələmxortdadi (dialect)
🇹🇲 Türkmençe: gurjak, oýnatgy aýal (only female doll)
🇺🇿 Oʻzbekcha: qo'g'irchok
🇰🇿 Qazaqşa: quwırşaq
🇰🇬 Qırğızça: quurçaq
🌏 Uyghurche: qurchaq
🌍 Tatarça: qurçaq
🌍 Başqortsa: qursaq
🌍 Çovaşla: pukane
🌍 Qaraqalpaqsha: quwırshaq
🌍 Qırımtatarca: qoqla
🌍 Qumuqça: qurçaq
🌍 Qaraçay-Malqar: ginji
🌍 Noğayşa: quwırşaq
🌏 Sıbırca: qurcaq
🌍 Gagauzça: kukla
🌏 Saqalī: kūkula, kokūkka
🌏 Dulgan-Hakalī: kūkla
🌏 Tıvalap: kukla, oynaar-kıs (female doll)
🌏 Salırça: vava
🌏 Xakastap: köklö, axpıyax
🌏 Altaylap: naaday, buubay, küükle
🌏 Şor: qızıraq
🌍 Urumça: xoxla
🌍 Karajče: bebek
🌍 Qrımçahça: qoqla, bebey, babiy
🌏 Soyot: oynaar urığ
🌏 Tofalap: oynaar uruğ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kazak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qazaq" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "казах" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kazakh" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "казашка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "казахский":
        bot.send_message(message.chat.id, '''🇬🇧 English: kazakh
🇷🇺 Русский: казах [kazakh]
🇹🇷 Türkçe: kazak
🇦🇿 Türkcə: qazax
🇹🇲 Türkmençe: gazak
🇺🇿 Oʻzbekcha: qozoq
🇰🇿 Qazaqşa: qazaq
🇰🇬 Qırğızça: qazaq
    Uyghurche: qazaq
    Tatarça: qazaq
    Başqortsa: qazaq
    Çovaşla: kazax, xozax {archasm}, nogay {archaism}
    Qaraqalpaqsha: qazaq
    Qırımtatarca: qazah
    Qumuqça: qazax
    Qaraçay-Malqar: qazah
    Noğayşa: qazax
    Sıbırca: qasaq
    Gagauzça: kazak
    Saqalī: kazaq
    Dulgan-Hakalī: kazak
    Tıvalap: kazax
    Salırça: qazak (xasa)
    Xakastap: xazax
    Altaylap: qazax
    Şor: kazax
    Urumça: xazax
    Karajče: kazak
    Qrımçahça: qazah
    Soyot: kazax
    Tofalap: kazax''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "russian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "русский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "руский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "русская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "руская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "русское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "руское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "русские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "руские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "в жопе узкий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "урус" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "русня" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "русич" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рузке" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "руске" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sarıkulak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sarı kulak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "руски" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pycku" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ruski" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "urus":
        bot.send_message(message.chat.id, '''🐺 Old Turkic: mosqovlu
🇬🇧 English: russian
🇷🇺 Русский: русский (-ая, -ое), урус (ethnophaulism), русня (ethnophaulism), рузке (ethnophaulism)
🇹🇷 Türkçe: rus, nataşa (female, ethnophaulism)
🇦🇿 Türkcə: rus, urus (dialect), sarıqulax (sarıqulaq) (dialect, ethnophaulism), nataşa (female, ethnophaulism)
🇹🇲 Türkmençe: rus, orys (archaism)
🇺🇿 Oʻzbekcha: rus, oʻrus (archaism)
🇰🇿 Qazaqşa: orıs, aqqulaq (ethnophaulism)
🇰🇬 Qırğızça: orus
    Uyghurche: rus
    Tatarça: urıs, marca (female)
    Başqortsa: urıþ
    Çovaşla: vıros
    Qaraqalpaqsha: rus
    Qırımtatarca: rus, urus
    Qumuqça: orus, rus
    Qaraçay-Malqar: oruslu
    Noğayşa: orıs
    Sıbırca: urıs
    Gagauzça: rus
    Saqalī: nūçça
    Hakalī (Dulgan): nūçça
    Tıvalap: orus
    Salırça: rus, ıluosi
    Xakastap: orıs
    Altay: orus, onor (archaism)
    Şor: qazaq
    Urumça: urus, xazax, maskal (moskov, moskol, moskal)
    Karaj: javan, orus (urus)
    Qrımçahça: urus
    Soyot: orıs
    Tofalap: orus (orıs)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "türk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "türük" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "turk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "turkish" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "turkic" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "турок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "турчанка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюрк" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюрок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "турк" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюрчанка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюркский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюркское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюркские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюркская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "турецкий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "турецкое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "турецкая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "турецкие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюрки" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "турки" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "turkısh" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "turkıc":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱅𐰇𐰼𐰜 (𐱅𐰇𐰼𐰛)
🐺 Old Turkic (bef. 13th c.): türk (türük)
🇬🇧 English: I. turk, turkish II. turk, turkic
🇷🇺 Русский: I. турок [turok], турчанка (female), турецкий (-ая, -ое) II. тюрк [tyurk], тюркский (-ая, -ое)
🇹🇷 Türkçe: türk
🇦🇿 Türkcə: türk
🇹🇲 Türkmençe: türk, türki (adj.)
🇺🇿 Oʻzbekcha: turk, turkiy (adj.)
🇰🇿 Qazaqşa: I. türik II. türki
🇰🇬 Qırğızça: türk
🌏 Uyghurche: türk
🌍 Tatarça: I. törek II. törki
🌍 Başqortsa: I. török II. törki
🌍 Çovaşla: török
🌍 Qaraqalpaqsha: túrk
🌍 Qırımtatarca: türk
🌍 Qumuqça: türk
🌍 Qaraçay-Malqar: I. türklü II. türk
🌍 Noğayşa: türk
🌏 Sıbırca: I. török II. törkiy
🌍 Gagauzça: türk
🌏 Saqalī: tǖrk (tǖr, türk, turak)
🌏 Dulgan-Hakalī: türk
🌏 Tıvalap: I. turk II. türk
🌏 Salırça: türk
🌏 Xakastap: I. turk II. türk
🌏 Altay: türk
🌏 Şor: türk
🌍 Urumça: türk
🌍 Karajče: tiurk
🌍 Qrımçahça: türk
🌏 Soyot: türk
🌏 Tofalap: türk''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "listen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "слушай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "послушай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "выслушай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dinle" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "слушать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "послушать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "выслушать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dinlemek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to listen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kulak asmak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kulak as":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): tıŋla, eşitgil, eşid (eşit), qulaq tut
🇬🇧 English: listen
🇷🇺 Русский: слушай, послушай
🇹🇷 Türkçe: dinle, kulak as
🇦🇿 Türkcə: dinlə, qulaq as
🇹🇲 Türkmençe: diňle
🇺🇿 Oʻzbekcha: tingla, quloq sol
🇰🇿 Qazaqşa: tıŋda
🇰🇬 Qırğızça: tıŋşo
🌏 Uyghurche: tingshi
🌍 Tatarça: tıñla
🌍 Başqortsa: tıñla
🌍 Çovaşla: tonla, itle
🌍 Qaraqalpaqsha: tıńla, qulaq sal
🌍 Qırımtatarca: diñle
🌍 Qumuqça: tıñla
🌍 Qaraçay-Malqar: tınğıla
🌍 Noğayşa: tıñla
🌏 Sıbırca: tıñna
🌍 Gagauzça: dinle, sesle
🌏 Saqalī: ihit
🌏 Dulgan-Hakalī: ihit
🌏 Tıvalap: dıñna
🌏 Salırça: diñnä, añna
🌏 Xakastap: tıñni, is
🌏 Altaylap: uq
🌏 Şor: uq
🌍 Urumça: dinne
🌍 Karajče: tynla, kajyrhyn ėšitiuviujńiu
🌍 Qrımçahça: dıñle
🌏 Soyot: dıñna (tıñna)
🌏 Tofalap: dıñna (tıñna)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "white" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "beyaz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "белый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "белая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "белое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "белые":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴 (𐰀𐰴), 𐰘𐰇𐰼𐰇𐰭
🐺 Old Turkic: aq, yürüŋ (ürüŋ, örün)
🇬🇧 English: white
🇷🇺 Русский: белый (-ая, -ое)
🇹🇷 Türkçe: beyaz, ak
🇦🇿 Türkcə: ağ, bəyaz
🇹🇲 Türkmençe: ak
🇺🇿 Oʻzbekcha: oq
🇰🇿 Qazaqşa: aq
🇰🇬 Qırğızça: aq
    Uyghurche: aq
    Tatarça:	aq
    Başqortsa: aq
    Çovaşla: şuro (şor, şur), ux (dialect)
    Qaraqalpaqsha: aq
    Qırımtatarca: aq, beyaz
    Qumuqça: aq
    Qaraçay-Malqar:	aq
    Noğayşa: aq
    Sıbırca: aq
    Gagauzça: ak, biyaz
    Saqalī: ürüñ, mañan
    Dulgan-Hakalī: çēlkē
    Tıvalap: ak
    Salırça: ax
    Xakastap: ax
    Altaylap: aq
    Şor: aq
    Urumça: ax (ağ), biyaz (beyaz, byaz)
    Karajče: ach (ak), bijaz
    Qrımçahça: ah, byaz
    Soyot: aq
    Tofalap: aq''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kızıl" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kırmızı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "al" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kizil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kirmizi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "red" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "scarlet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "красный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "красная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "красное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "алый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "алая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "алое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "красные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "алые":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): qızıl, al, yepin (yepkil, yepkin, yepün)
🇬🇧 English: red, scarlet
🇷🇺 Русский: красный (-ая, -ое), алый (-ая, -ое)
🇹🇷 Türkçe: kızıl, kırmızı, al
🇦🇿 Türkcə: qırmızı, al, qızıl
🇹🇲 Türkmençe: gyzyl, al, gyrmyzy
🇺🇿 Oʻzbekcha: qizil, qirmizi, alvon
🇰🇿 Qazaqşa: qızıl, qırmızı, alqızıl
🇰🇬 Qırğızça: qızıl
🌏 Uyghurche: qizil
🌍 Tatarça: qızıl, al
🌍 Başqortsa: qıðıl, al
🌍 Çovaşla: xörlö, xöm (xömlö)
🌍 Qaraqalpaqsha: qızıl
🌍 Qırımtatarca: qırmızı, qızıl, al
🌍 Qumuqça: qızıl, al, qırmızı
🌍 Qaraçay-Malqar: qızıl
🌍 Noğayşa:	qızıl, al
🌏 Sıbırca: qısıl, al
🌍 Gagauzça: kırmızı, al
🌏 Saqalī: kıhıl
🌏 Dulgan-Hakalī: kıtarkay, kıhıl
🌏 Tıvalap: kızıl
🌏 Salırça: qızıl
🌏 Xakastap: xızıl
🌏 Altaylap: qızıl
🌏 Şor: qızıl
🌍 Urumça: xızıl, ğırmızı (xırmızı), al (eal, eval)
🌍 Karajče: kyzyl, kyrmyzy, al
🌍 Qrımçahça: qırmızı, al
🌏 Soyot: qızıl
🌏 Tofalap: qızıl''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "green" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yeşil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зеленый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зеленая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зеленое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зеленые" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yeşıl":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): yaşıl, kök (blue, green, turquoise, gray, glaucous, violet)
🇬🇧 English: green
🇷🇺 Русский: зелёный (-ая, -ое)
🇹🇷 Türkçe: yeşil
🇦🇿 Türkcə: yaşıl, göy (blue, green, turquoise, glaucous, violet)
🇹🇲 Türkmençe: ýaşyl
🇺🇿 Oʻzbekcha: yashil
🇰🇿 Qazaqşa: jasıl, kök (blue, green, turquoise, glaucous)
🇰🇬 Qırğızça: jaşıl
🌏 Uyghurche: yeshil
🌍 Tatarça: yäşel
🌍 Başqortsa: yäşel
🌍 Çovaşla: yeşöl (ешĕл), simös
🌍 Qaraqalpaqsha: jasıl
🌍 Qırımtatarca: yeşil
🌍 Qumuqça: yaşıl, gök (blue, green, turquoise)
🌍 Qaraçay-Malqar: jaşıl
🌍 Noğayşa: yasıl
🌏 Sıbırca: yäşel
🌍 Gagauzça: eşil (ешил)
🌏 Saqalī: küöq (green, blue)
🌏 Dulgan-Hakalī: küök (green, blue)
🌏 Tıvalap: nogaan, kök (blue, green, turquoise, glaucous, violet)
🌏 Salırça: yaşil
🌏 Xakastap: ot kök, noğan, çazıl (archaism)
🌏 Altaylap: cajıl
🌏 Şor: çajıl
🌍 Urumça: yeşil (eşil), gög (blue, green, turquoise, glaucous, violet)
🌍 Karajče: ješil´ (isil)
🌍 Qrımçahça: yeşıl
🌏 Soyot: gök (kök) (green, blue)
🌏 Tofalap: suğ-kök, kök (green, blue)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yellow" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sarı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "желтый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "желтая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "желтое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "желтые" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жолтый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жолтая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жолтое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жолтые":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰽𐰺𐰍
🐺 Old Turkic (bef. 13th c.): sarığ, eträk
🇬🇧 English: yellow
🇷🇺 Русский: жёлтый (-ая, -ое) [zheltyy]
🇭🇺 Magyar: sárga
🇹🇷 Türkçe: sarı
🇦🇿 Türkcə: sarı
🇹🇲 Türkmençe: sary
🇺🇿 Oʻzbekcha: sariq
🇰🇿 Qazaqşa: sarı
🇰🇬 Qırğızça: sarı
🌏 Uyghurche: sériq
🌍 Tatarça: sarı
🌍 Başqortsa: harı
🌍 Çovaşla: saro
🌍 Qaraqalpaqsha: sarı
🌍 Qırımtatarca: sarı
🌍 Qumuqça: sarı
🌍 Qaraçay-Malqar: sarı
🌍 Noğayşa: sarı
🌏 Sıbırca: sarı
🌍 Gagauzça: sarı
🌏 Saqalī: arağas, saharqay, sarık
🌏 Dulgan-Hakalī: hahıl
🌏 Tıvalap: sarıg
🌏 Salırça: sarı
🌏 Xakastap: sarığ
🌏 Altaylap: sarı
🌏 Şor: sarığ
🌍 Urumça: sarı
🌍 Karajče: sary
🌍 Qrımçahça: sarı
🌏 Soyot: sarığ
🌏 Tofalap: sarığ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "makine" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "machine" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "машина" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "машына" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "maşın" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mechanical device" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "maşin":
        bot.send_message(message.chat.id, '''🇬🇧 English: machine
🇷🇺 Русский: машина (в широком смысле, для значения "автомобиль" введите "автомобиль") [mashyna]
🇹🇷 Türkçe: makine
🇦🇿 Türkcə: maşın
🇹🇲 Türkmençe: maşyn
🇺🇿 Oʻzbekcha: mashina, makina (archaism)
🇰🇿 Qazaqşa: mäşiyne (maşıyna, maşina)
🇰🇬 Qırğızça: maşına
🌏 Uyghurche: mashina
🌍 Tatarça: maşına
🌍 Başqortsa: maşına
🌍 Çovaşla: maşşina (maşına)
🌍 Qaraqalpaqsha: mashına
🌍 Qırımtatarca: maşna, makina (archaism)
🌍 Qumuqça: maşın
🌍 Qaraçay-Malqar: maşına
🌍 Noğayşa: mäşin
🌏 Sıbırca: maşına (maşinä)
🌍 Gagauzça: maşına
🌏 Saqalī: massīna
🌏 Dulgan-Hakalī: massīna
🌏 Tıvalap: maşina (maşına)
🌏 Salırça: ci
🌏 Xakastap: maşına
🌏 Altaylap: maşına
🌏 Şor: maşına
🌍 Urumça: maşına (marışna, marşın, marşına)
🌍 Karajče: mašina (mašyna)
🌍 Qrımçahça: maşına
🌏 Soyot: maşîîn (maşıına, mahîîna)
🌏 Tofalap: maşîîn''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "экономия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "saving" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tasarruf" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kanâat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kanaat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "расчетливость" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "экономность" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бережливость":
        bot.send_message(message.chat.id, '''🇬🇧 English: saving
🇷🇺 Русский: экономия [ekonomiya]
🇹🇷 Türkçe: tasarruf, kanâat
🇦🇿 Türkcə: qənaət, qənaətçilik, təsərrüf, isrif (isrip) (dialect), madar (dialect), sülf (dialect)
🇹🇲 Türkmençe: tygşytlylyk, saklyk
🇺🇿 Oʻzbekcha: tejam, tejamkorlik
🇰🇿 Qazaqşa: ünem, ünemdew
🇰🇬 Qırğızça: ünömdöö, ünömdüülü
🌏 Uyghurche: téjem
🌍 Tatarça: saqlıq, saqçıllıq, xästärlek
🌍 Başqortsa: haqlıq, haqlaw, bäräkätlelek, haqsıllıq
🌍 Çovaşla: pereket, pereketlöx, tirpeylöx
🌍 Qaraqalpaqsha: ünemlew
🌍 Qırımtatarca: tasarruf, tutumlu qullanma, bilip çevirme
🌍 Qumuqça: ayap tutuw, ayap xarjlaw
🌍 Qaraçay-Malqar: ayaw, ayawlu etiw, ayab qaldırıw, ayab joyuw, zırafsız joyuw
🌍 Noğayşa: saq tutuwşılıq
🌏 Sıbırca: (aqcanı) yuqqa tustırmaw, (aqcanı) pelep oşlanıw, tötökläw
🌍 Gagauzça: kanaat (kanayat)
🌏 Saqalī: kemçilēhin
🌏 Dulgan-Hakalī: ekonomiya
🌏 Tıvalap: kam, kamnalga
🌏 Salırça: taca
🌏 Xakastap: üzürles
🌏 Altaylap: çeber qorodor(ı), çeberleer(i)
🌏 Şor: ekonomiya
🌍 Urumça: tutumlu xullanma
🌍 Karajče: kanaat
🌍 Qrımçahça: sarflıh
🌏 Soyot: ekonomîya
🌏 Tofalap: ekonomîya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rain" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дождь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yağmur":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): yağmur (yamğur)
🇬🇧 English: rain
🇷🇺 Русский: дождь [dozhd']
🇹🇷 Türkçe: yağmur
🇦🇿 Türkcə: yağış, yağmur, yağannıx (yağanlıq) (dialect), gülül {dial., rain with big drops}, gürşat {dial., heavy rain}, hır {dial., small rain}, qarapüsəh (qarapüsək) {dial., small rain}, qarayarpax (qarayarpaq) {dial., rain with big drops}, püsəh (püsək) {dial. small rain}
🇹🇲 Türkmençe: ýagyş, ýagmyr
🇺🇿 Oʻzbekcha: yomgʻir
🇰🇿 Qazaqşa: jaŋbır, jawın
🇰🇬 Qırğızça: jamğır, jaan {heavy rain}
🌏 Uyghurche: yamghur
🌍 Tatarça: yañğır
🌍 Başqortsa: yamğır
🌍 Çovaşla: cumor
🌍 Qaraqalpaqsha: jamǵır, jawın
🌍 Qırımtatarca: yağmur, cavun {dial.}
🌍 Qumuqça: yañgur, yawun
🌍 Qaraçay-Malqar: jañgur, jawun
🌍 Noğayşa: yamğır
🌏 Sıbırca: yañqır, yawın
🌍 Gagauzça: yaamur
🌏 Saqalī: ardaq, samīr
🌏 Dulgan-Hakalī: hamīr
🌏 Tıvalap: ças, çaaşkın
🌏 Salırça: yağmur
🌏 Xakastap: nañmır
🌏 Altaylap: cañmır, caaş
🌏 Şor: nağbur
🌍 Urumça: yağış, yağmur, yavun, sağanax
🌍 Karajče: jamhur (jahmur, janhur)
🌍 Qrımçahça: yağmur (yañğur)
🌏 Soyot: ças
🌏 Tofalap: ösken, upqan {heavy rain}, ças {heavy rain}''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bunker" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бункер" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "подземное укрытие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sığınak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "siğinak":
        bot.send_message(message.chat.id, '''🇬🇧 English: bunker
🇷🇺 Русский: бункер [bunker] (подземное укрытие)
🇹🇷 Türkçe: sığınak
🇦🇿 Türkcə: sığınaq (sığınacaq)
🇹🇲 Türkmençe: bunker
🇺🇿 Oʻzbekcha: bunker
🇰🇿 Qazaqşa: bunker
🇰🇬 Qırğızça: bunker
🌏 Uyghurche: bunkér
🌍 Tatarça: bunker
🌍 Başqortsa: bunker
🌍 Çovaşla: punkkör (bunker)
🌍 Qaraqalpaqsha: bunker
🌍 Qırımtatarca: sığınaq (sığanaq)
🌍 Qumuqça: bunker
🌍 Qaraçay-Malqar: bunker
🌍 Noğayşa: bunker
🌏 Sıbırca: bunker
🌍 Gagauzça: mazgal
🌏 Saqalī: būñkar (bunker)
🌏 Dulgan-Hakalī: bunker
🌏 Tıvalap: bunker
🌏 Salırça: dibu
🌏 Xakastap: bunker
🌏 Altaylap: bunker
🌏 Şor: bunker
🌍 Urumça: bunker
🌍 Karajče: syhynč, saklanmach, syjynč
🌍 Qrımçahça: bunker
🌏 Soyot: bunker
🌏 Tofalap: bunker''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bride" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "daughter-in-law" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "daughterinlaw" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "daughter in law" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "невеста" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gelin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "невестка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "новобрачная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сноха":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): kelin, keliŋün (kelin yegün)
🇬🇧 English: I. bride II. daughter-in-law
🇷🇺 Русский: I. невеста [nevesta] II. невестка [nevestka]
🇹🇷 Türkçe: gelin
🇦🇿 Türkcə: gəlin
🇹🇲 Türkmençe: gelneje, gelin
🇺🇿 Oʻzbekcha: kelin
🇰🇿 Qazaqşa: kelin
🇰🇬 Qırğızça: kelin
🌏 Uyghurche: kélin
🌍 Tatarça: kilen
🌍 Başqortsa: kilen
🌍 Çovaşla: kin
🌍 Qaraqalpaqsha: kelin
🌍 Qırımtatarca: kelin
🌍 Qumuqça: gelin
🌍 Qaraçay-Malqar: kelin
🌍 Noğayşa: kelin, kelinşek
🌏 Sıbırca: kilen, kilencäk
🌍 Gagauzça: gelin
🌏 Saqalī: kiyït
🌏 Dulgan-Hakalī: kinït
🌏 Tıvalap: kelin
🌏 Salırça: yeñkinagu, agu
🌏 Xakastap: kîlin
🌏 Altaylap: kelin, keldi
🌏 Şor: kelin, negeeçi
🌍 Urumça: gälin (kelin)
🌍 Karajče: kieliń (kelin, kielin)
🌍 Qrımçahça: kelın
🌏 Soyot: helîn
🌏 Tofalap: helîn''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eid-ul-azha" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eid ul azha" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eidulazha" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eid al-adha" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eid al adha" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eidaladha" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eid-al-adha" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курбан-байрам" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курбан байрам" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курбанбайрам" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurban bayramı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurban bayrami" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurban-bayram" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eid qurban" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ид аль адха" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "festival of the sacrifice" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "праздник жертвоприношения" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurban bayram":
        bot.send_message(message.chat.id, '''🇬🇧 English: Eid al-Adha (Eid-ul-Azha)
🇷🇺 Русский: Курбан-байрам [Kurban-bayram]
🇹🇷 Türkçe: Kurban Bayramı
🇦🇿 Türkcə: Qurban bayramı
🇹🇲 Türkmençe: Gurban baýramy
🇺🇿 Oʻzbekcha: Qurbon hayiti
🇰🇿 Qazaqşa: Qurban ayt
🇰🇬 Qırğızça: Qurman Ayt
🌏 Uyghurche: Qurvan héyt
🌍 Tatarça: Qorban bäyräme, Qorban ğayıtı
🌍 Başqortsa: Qorban bayramı
🌍 Çovaşla: Xorpan payranö
🌍 Qaraqalpaqsha: Qurban bayramı
🌍 Qırımtatarca: Qurban bayramı
🌍 Qumuqça: Qurban bayram
🌍 Qaraçay-Malqar: Qurman bayram
🌍 Noğayşa: Qurman bayram
🌏 Sıbırca: Qorman payramı
🌍 Gagauzça: Kurban bayramı (Kurban yortusu)
🌏 Saqalī: Kurban-bayram
🌏 Dulgan-Hakalī: Kurban-bayram
🌏 Tıvalap: Kurban-bayram
🌏 Salırça: Qurban ayit
🌏 Xakastap: Kurban-bayram
🌏 Altaylap: Kurban-bayram
🌏 Şor: Kurban-bayram
🌍 Urumça: Xurban bayramı
🌍 Karajče: Kurban bajramy
🌍 Qrımçahça: Qurban bayramı
🌏 Soyot: Kurban-bayram
🌏 Tofalap: Kurban-bayram''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "öz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "özü" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kendi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "own" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "itself" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "himself" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "herself" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "свой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "собственный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "само" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сам" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сама" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "своя" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "свое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "свои" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "собственная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "собственное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "собственные":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): I. öz II. özü, öz kentü (öz kendü)
🇬🇧 English: I. own II. itself, himself, herself
🇷🇺 Русский: I. свой, собственный II. само, сам, сама
🇹🇷 Türkçe: I. kendi, öz II. özü, kendi
🇦🇿 Türkcə: I. öz II. özü
🇹🇲 Türkmençe: I. öz II. özi
🇺🇿 Oʻzbekcha: I. oʻz II. oʻzi
🇰🇿 Qazaqşa: I. öz II. özi
🇰🇬 Qırğızça: I. öz II. özü
🌏 Uyghurche: I. öz II. özi
🌍 Tatarça: I. üz II. üze
🌍 Başqortsa: I. üð II. üðe
🌍 Çovaşla: xam (my), xu (your), xay (its, his, her)
🌍 Qaraqalpaqsha: I. öz II. özi
🌍 Qırımtatarca: I. öz, kendi (dialect) II. özü, kendi (dialect)
🌍 Qumuqça: I. öz II. özü
🌍 Qaraçay-Malqar: kesi (+affix)
🌍 Noğayşa: I. öz II. özi
🌏 Sıbırca: üs
🌍 Gagauzça: I. kendi, öz II. özü, kendi
🌏 Saqalī: beye
🌏 Dulgan-Hakalī: beye
🌏 Tıvalap: I. bot II. bodu
🌏 Salırça: I. i (iz, öz) II. izi
🌏 Xakastap: I. pos II. pozı
🌏 Altaylap: I. boyınıñ II. boyı
🌏 Şor: I. pos II. pozu
🌍 Urumça: I. öz II. özü
🌍 Karajče: I. öź II. öźiu
🌍 Qrımçahça: I. gendı, öz II. özı, gendı
🌏 Soyot: I. bodınıñ (bodnıñ) II. bodı
🌏 Tofalap: I. bodunuñ II. bodu''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лэптоп" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ноутбук" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "noutbuk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "leptop" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "laptop" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dizüstü bilgisayar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "notebook computer" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dizüstü":
        bot.send_message(message.chat.id, '''🇬🇧 English: laptop, ((notebook) (computer))
🇷🇺 Русский: ноутбук [noutbuk], лэптоп [leptop]
🇹🇷 Türkçe: ((dizüstü) (bilgisayar)), laptop
🇦🇿 Türkcə: ((dizüstü) (bilgisayar)), noutbuk, dizüstü kompüter
🇹🇲 Türkmençe: noutbuk
🇺🇿 Oʻzbekcha: laptop, noutbuk
🇰🇿 Qazaqşa: noutbuk, laptop
🇰🇬 Qırğızça: noutbuk, çaqan kompyuter
🌏 Uyghurche: ((éteküsti) (kompyutér))
🌍 Tatarça: noutbuk, laptop, portativ kompyuter
🌍 Başqortsa: noutbuk
🌍 Çovaşla: noutbuk, leptop
🌍 Qaraqalpaqsha: noutbuk
🌍 Qırımtatarca: tizüstü, noutbuk
🌍 Qumuqça: noutbuk
🌍 Qaraçay-Malqar: noutbuk
🌍 Noğayşa: noutbuk
🌏 Sıbırca: noutbuk
🌍 Gagauzça: noutbuk
🌏 Saqalī: noutbuk
🌏 Dulgan-Hakalī: noutbuk
🌏 Tıvalap: noutbuk
🌏 Salırça: el diennao
🌏 Xakastap: noutbuk
🌏 Altaylap: noutbuk
🌏 Şor: noutbuk
🌍 Urumça: noutbuk
🌍 Karajče: laptop
🌍 Qrımçahça: noutbuk
🌏 Soyot: noutbuk
🌏 Tofalap: noutbuk''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "twenty" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "20" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "двадцать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yirmi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iyirmi":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰘𐰃𐰏𐰼𐰢𐰃 
🐺 Old Turkic (bef. 13th c.): yegirmi
🇬🇧 English: twenty
🇷🇺 Русский: двадцать [dvadtsat']
🇹🇷 Türkçe: yirmi
🇦🇿 Türkcə: iyirmi
🇹🇲 Türkmençe: ýigrimi
🇺🇿 Oʻzbekcha: yigirma
🇰🇿 Qazaqşa: jıyırma
🇰🇬 Qırğızça: jıyırma
🌏 Uyghurche: yigrime
🌍 Tatarça: yegerme
🌍 Başqortsa: yegerme
🌍 Çovaşla: ciröm
🌍 Qaraqalpaqsha: jigirma
🌍 Qırımtatarca: yigirmi
🌍 Qumuqça: yigirma
🌍 Qaraçay-Malqar: jıyırma
🌍 Noğayşa: yırma
🌏 Sıbırca: yegermä
🌍 Gagauzça: irmi
🌏 Saqalī: sǖrbe
🌏 Dulgan-Hakalī: hǖrbe
🌏 Tıvalap: çeerbi
🌏 Salırça: yiğirmi
🌏 Xakastap: çîbirge
🌏 Altaylap: cirme
🌏 Şor: çegirbe
🌍 Urumça: igirmi (girim, yirmi, yigirmi)
🌍 Karajče: jigirmi (igirme, egirme)
🌍 Qrımçahça: yıgırım (yıgrım)
🌏 Soyot: çêêrbî (çêêrvî)
🌏 Tofalap: îhön''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eight" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "8" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восемь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sekiz":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰾‎𐰚𐰔
🐺 Old Turkic (bef. 13th c.): sekkiz (sekiz)
🇬🇧 English: eight
🇷🇺 Русский: восемь [vosem']
🇹🇷 Türkçe: sekiz
🇦🇿 Türkcə: səkkiz
🇹🇲 Türkmençe: sekiz
🇺🇿 Oʻzbekcha: sakkiz
🇰🇿 Qazaqşa: segiz
🇰🇬 Qırğızça: segiz
🌏 Uyghurche: sekkiz
🌍 Tatarça: sigez
🌍 Başqortsa: higeð
🌍 Çovaşla: sakkor
🌍 Qaraqalpaqsha: segiz
🌍 Qırımtatarca: sekiz
🌍 Qumuqça: segiz
🌍 Qaraçay-Malqar: segiz
🌍 Noğayşa: segiz
🌏 Sıbırca: siges
🌍 Gagauzça: sekiz
🌏 Saqalī: ağıs
🌏 Dulgan-Hakalī: agıs
🌏 Tıvalap: ses
🌏 Salırça: sekkis
🌏 Xakastap: sîgis
🌏 Altaylap: segis
🌏 Şor: segis
🌍 Urumça: säkkiz (sekiz)
🌍 Karajče: segiź (sekiz)
🌍 Qrımçahça: sekız
🌏 Soyot: ses
🌏 Tofalap: sehes''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "латвия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "latvia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "letonya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "letoniya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "latviya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "latvija":
        bot.send_message(message.chat.id, '''🇬🇧 English: Latvia
🇷🇺 Русский: Латвия [Latviya]
🇹🇷 Türkçe: Letonya
🇦🇿 Türkcə: Latviya, Letoniya (archaism)
🇹🇲 Türkmençe: Latwiýa
🇺🇿 Oʻzbekcha: Latviya
🇰🇿 Qazaqşa: Latviya (Latwıya)
🇰🇬 Qırğızça: Latviya
🌏 Uyghurche: Latviye
🌍 Tatarça: Latviä, Letoniä
🌍 Başqortsa: Latviya/Latviä (Латвия)
🌍 Çovaşla: Latvi
🌍 Qaraqalpaqsha: Latviya
🌍 Qırımtatarca: Latviya
🌍 Qumuqça: Latviya
🌍 Qaraçay-Malqar: Latviya
🌍 Noğayşa: Latviya
🌏 Sıbırca: Latviä
🌍 Gagauzça: Latviya
🌏 Saqalī: Latviya
🌏 Dulgan-Hakalī: Latviya
🌏 Tıvalap: Latviya
🌏 Salırça: Latuveya, Letoniya
🌏 Xakastap: Latvîya
🌏 Altaylap: Latviya
🌏 Şor: Latviya
🌍 Urumça: Latviya
🌍 Karajče: Latvija
🌍 Qrımçahça: Letonya
🌏 Soyot: Latvîya
🌏 Tofalap: Latvîya
In Latvian: Latvija''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nine" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "9" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "девять" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dokuz":
        bot.send_message(message.chat.id, '''🐺𐰚𐰇𐰚𐱅𐰇𐰼𐰜: ‎𐱃𐰆𐰴𐰔
🐺 Old Turkic (bef. 13th c.): toquz
🇬🇧 English: nine
🇷🇺 Русский: девять [devyat']
🇹🇷 Türkçe: dokuz
🇦🇿 Türkcə: doqquz
🇹🇲 Türkmençe: dokuz
🇺🇿 Oʻzbekcha: toʻqqiz
🇰🇿 Qazaqşa: toğız
🇰🇬 Qırğızça: toğuz
🌏 Uyghurche: toqquz
🌍 Tatarça: tuğız
🌍 Başqortsa: tuğıð
🌍 Çovaşla: toxor
🌍 Qaraqalpaqsha: toǵız
🌍 Qırımtatarca: doquz
🌍 Qumuqça: toğuz
🌍 Qaraçay-Malqar: toğuz
🌍 Noğayşa: toğız
🌏 Sıbırca: tuğıs
🌍 Gagauzça: dokuz
🌏 Saqalī: toğus
🌏 Dulgan-Hakalī: togus
🌏 Tıvalap: tos
🌏 Salırça: doqus (toqos)
🌏 Xakastap: toğıs
🌏 Altaylap: toğus
🌏 Şor: toğus
🌍 Urumça: doxkuz (doxuz)
🌍 Karajče: tohuz
🌍 Qrımçahça: doqız
🌏 Soyot: tos
🌏 Tofalap: tohos''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "beard" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "борода" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sakal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бородка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "растительность на лице" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "расстительность на лице":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): saqal
🇬🇧 English: beard
🇷🇺 Русский: борода [boroda]
🇭🇺 Magyar: szakáll
🇲🇳 Mongol: sakhal
🇹🇷 Türkçe: sakal
🇦🇿 Türkcə: saqqal
🇹🇲 Türkmençe: sakgal
🇺🇿 Oʻzbekcha: soqol
🇰🇿 Qazaqşa: saqal
🇰🇬 Qırğızça: saqal
🌏 Uyghurche: saqal
🌍 Tatarça: saqal
🌍 Başqortsa: haqal
🌍 Çovaşla: suxal
🌍 Qaraqalpaqsha: saqal
🌍 Qırımtatarca: saqal
🌍 Qumuqça: saqal
🌍 Qaraçay-Malqar: saqal
🌍 Noğayşa: saqal
🌏 Sıbırca: sağal
🌍 Gagauzça: sakal
🌏 Saqalī: señiye bıtıga, bıtık (+ mustache)
🌏 Dulgan-Hakalī: bıtık (+ mustache)
🌏 Tıvalap: segel salı, sal (+ mustache)
🌏 Salırça: sağal
🌏 Xakastap: sağal
🌏 Altaylap: sağal
🌏 Şor: eek sağalı, sağal (+ mustache)
🌍 Urumça: saxkhal (saxal)
🌍 Karajče: sakal (sahal)
🌍 Qrımçahça: saqal
🌏 Soyot: sal
🌏 Tofalap: sahal (+ mustache)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çiŋğis qağan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genghis khan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genghiskhan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genghis-khan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genghis khaan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genghiskhaan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genghis-khaan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чингисхан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чингис хан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чингизхан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чингиз хан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chinggis khaan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chinggis-khaan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chinggis khan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chinggiskhaan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chinggis-khan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chinggiskhan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cengizhan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cengiz-han" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cengız han" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cengiz han":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): Çiŋğis Qağan
🇬🇧 English: Genghis Khan
🇷🇺 Русский: Чингисхан [Chingiskhan]
🇲🇳 Mongol: Chinggis Khaan
🇹🇷 Türkçe: Cengiz Han
🇦🇿 Türkcə: Çingiz Xan
🇹🇲 Türkmençe: Çingiz Han
🇺🇿 Oʻzbekcha: Chingizxon
🇰🇿 Qazaqşa: Şıŋğıs Han
🇰🇬 Qırğızça: Çıŋğız Xan
🌏 Uyghurche: Chinggizxan
🌍 Tatarça: Çıñğızxan
🌍 Başqortsa: Sıñğıðxan
🌍 Çovaşla: Çingisxan
🌍 Qaraqalpaqsha: Shıńǵıs Xan
🌍 Qırımtatarca: Cengiz Han
🌍 Qumuqça: Çingiz Xan
🌍 Qaraçay-Malqar: Çingiz Xan
🌍 Noğayşa: Şıñğız Xan
🌏 Sıbırca: Ciñkes Qan (Cımğıs-qan)
🌍 Gagauzça: Cengiz Han
🌏 Saqalī: Çıñıs Qān
🌏 Dulgan-Hakalī: Çıñıs Kān
🌏 Tıvalap: Çiñgis-xaan
🌏 Salırça: Çiñgiz Xan (Çeñcisı Xan)
🌏 Xakastap: Çîngîsxan
🌏 Altaylap: Çingisxan
🌏 Şor: Çingisxan
🌍 Urumça: Çingiz Xan
🌍 Karajče: Čingischan
🌍 Qrımçahça: Cengız Han
🌏 Soyot: Çîngîs Haan
🌏 Tofalap: Çîngîs Haan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "плов" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pilaf" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pilau" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pilav" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пилав" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "plov":
        bot.send_message(message.chat.id, '''🇬🇧 English: pilaf (pilau)
🇷🇺 Русский: плов [plov], пилав [pilav] (archaism)
🇹🇷 Türkçe: pilav
🇦🇿 Türkcə: aş, plov, pilav (dialect), plo (pılo) (dialect)
🇹🇲 Türkmençe: palaw
🇺🇿 Oʻzbekcha: osh, palov
🇰🇿 Qazaqşa: palaw
🇰🇬 Qırğızça: paloo, aş
🌏 Uyghurche: polu (polo), aş
🌍 Tatarça: pılaw
🌍 Başqortsa: bılaw
🌍 Çovaşla: plov
🌍 Qaraqalpaqsha: palaw
🌍 Qırımtatarca: pilâv
🌍 Qumuqça: pilaw
🌍 Qaraçay-Malqar: plow
🌍 Noğayşa: pılaw
🌏 Sıbırca: pılaw
🌍 Gagauzça: pilaf (pilav)
🌏 Saqalī: plov
🌏 Dulgan-Hakalī: plov
🌏 Tıvalap: plov
🌏 Salırça: aş
🌏 Xakastap: plov
🌏 Altaylap: plov
🌏 Şor: plov
🌍 Urumça: pilaf (piläv, pulov, pılav)
🌍 Karajče: pilav
🌍 Qrımçahça: pilav
🌏 Soyot: plov
🌏 Tofalap: plov''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "planet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "planeta" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "планета" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gezegen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "seyyare":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): garx (grax)
🇬🇧 English: planet
🇷🇺 Русский: планета [planeta]
🇹🇷 Türkçe: gezegen, seyyare
🇦🇿 Türkcə: səyyarə, planet, gəzəyən (rarely, purism)
🇹🇲 Türkmençe: saýýar, planeta, asman gewresi, pylanet (archaism)
🇺🇿 Oʻzbekcha: sayyora
🇰🇿 Qazaqşa: ğalamşar, planeta
🇰🇬 Qırğızça: planeta
🌏 Uyghurche: planét, seyyare
🌍 Tatarça: planeta
🌍 Başqortsa: planeta
🌍 Çovaşla: planeta
🌍 Qaraqalpaqsha: planeta
🌍 Qırımtatarca: seyyare
🌍 Qumuqça: planet (planeta)
🌍 Qaraçay-Malqar: planeta
🌍 Noğayşa: planeta
🌏 Sıbırca: planeta
🌍 Gagauzça: planeta
🌏 Saqalī: planeta
🌏 Dulgan-Hakalī: planeta
🌏 Tıvalap: planeta
🌏 Salırça: şiñşiñ
🌏 Xakastap: planeta
🌏 Altaylap: planeta
🌏 Şor: planeta
🌍 Urumça: planet (planeta)
🌍 Karajče: planeta
🌍 Qrımçahça: planeta
🌏 Soyot: garag, planeta
🌏 Tofalap: planeta''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ben seni seviyorum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "я тебя люблю" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "i love you" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iloveyou" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ı love u" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "i love u" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıloveu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "я тебя люблю" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "seni seviyorum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "seviyorum seni" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iloveu":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): men seni sevärmen
🇬🇧 English: I love you
🇷🇺 Русский: я тебя люблю
🇹🇷 Türkçe: ben seni seviyorum
🇦🇿 Türkcə: mən səni sevirəm (to partner), mən səni çox istəyirəm (to family member, friend, relative, comrade etc)
🇹🇲 Türkmençe: men seni söýýärin
🇺🇿 Oʻzbekcha: men seni sevaman
🇰🇿 Qazaqşa: men seni süyemin, men seni jaqsı köremin
🇰🇬 Qırğızça: men seni süyöm
🌏 Uyghurche: men seni söyümen, men seni yaxshi körümen
🌍 Tatarça: min sine yaratam
🌍 Başqortsa: min hine yaratam
🌍 Çovaşla: epö sana yuratatop
🌍 Qaraqalpaqsha: men seni súyemen, men seni jaqsı kóremen
🌍 Qırımtatarca: men seni sevem
🌍 Qumuqça: men seni süyemen
🌍 Qaraçay-Malqar: men seni süyeme
🌍 Noğayşa: men seni süyemen
🌏 Sıbırca: min sine söyämen, min sine yaratam
🌍 Gagauzça: bän seni severim
🌏 Saqalī: min eyigin taptībın
🌏 Dolgan-Hakalī: min enigin bagarabın
🌏 Tıvalap: men señee ınak tur-men
🌏 Salırça: män sini söyür
🌏 Xakastap: min sin xınara, min sağaa xınçam
🌏 Altay: men seni süüp turar
🌏 Şor: men sağa kölençam
🌍 Urumça: bän säni severim
🌍 Karajče: mień sieńi siuviam
🌍 Qrımçahça: men senı süvem
🌏 Soyot: men sîîğä ınaq tur-men
🌏 Tofalap: men seni ekkisinêr men''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "10" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "on" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "десять" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ten":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰆𐰣
🐺 Old Turkic (bef. 13th c.): on
🇬🇧 English: ten
🇷🇺 Русский: десять [desyat']
🇹🇷 Türkçe: on
🇦🇿 Türkcə: on
🇹🇲 Türkmençe: on
🇺🇿 Oʻzbekcha: o‘n
🇰🇿 Qazaqşa: on
🇰🇬 Qırğızça: on
🌏 Uyghurche: on
🌍 Tatarça: un
🌍 Başqortsa: un
🌍 Çovaşla: vun
🌍 Qaraqalpaqsha: on
🌍 Qırımtatarca: on
🌍 Qumuqça: on
🌍 Qaraçay-Malqar: on
🌍 Noğayşa: on
🌏 Sıbırca: un
🌍 Gagauzça: on
🌏 Saqalī: uon
🌏 Dulgan-Hakalī: uon
🌏 Tıvalap: on
🌏 Salırça: on
🌏 Xakastap: on
🌏 Altaylap: on
🌏 Şor: on
🌍 Urumça: on
🌍 Karajče: on
🌍 Qrımçahça: on
🌏 Soyot: on
🌏 Tofalap: on''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eleven" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "одиннадцать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "одинадцать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "11" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "on bir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "onbir":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰋𐰃𐰼 : 𐰘𐰃𐰏𐰼𐰢𐰃
🐺 Old Turkic (bef. 13th c.): bir yegirmi (1 + 20)
🇬🇧 English: eleven
🇷🇺 Русский: одиннадцать [odinnadtsat']
🇹🇷 Türkçe: on bir (10 + 1)
🇦🇿 Türkcə: on bir
🇹🇲 Türkmençe: on bir
🇺🇿 Oʻzbekcha: o‘n bir
🇰🇿 Qazaqşa: on bir
🇰🇬 Qırğızça: on bir
🌏 Uyghurche: on bir
🌍 Tatarça: unber
🌍 Başqortsa: un ber
🌍 Çovaşla: vunpör
🌍 Qaraqalpaqsha: on bir
🌍 Qırımtatarca: on bir
🌍 Qumuqça: on bir
🌍 Qaraçay-Malqar: on bir
🌍 Noğayşa: on bir
🌏 Sıbırca: unper
🌍 Gagauzça: on bir
🌏 Saqalī: uon bïr
🌏 Dulgan-Hakalī: uon bïr
🌏 Tıvalap: on bir
🌏 Salırça: on bir
🌏 Xakastap: on pir
🌏 Altaylap: on bir
🌏 Şor: on pir
🌍 Urumça: on bir
🌍 Karajče: on bir
🌍 Qrımçahça: on bır
🌏 Soyot: on bir
🌏 Tofalap: on bir''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "twelve" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tvelve" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "двенадцать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "двеннадцать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "on iki" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "on ıkı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "12" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oniki":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰚𐰃 : 𐰘𐰃𐰏𐰼𐰢𐰃
🐺 Old Turkic (bef. 13th c.): eki yegirmi
🇬🇧 English: twelve
🇷🇺 Русский: двенадцать [dvenadtsat']
🇹🇷 Türkçe: on iki
🇦🇿 Türkcə: on iki
🇹🇲 Türkmençe: on iki
🇺🇿 Oʻzbekcha: o‘n ikki
🇰🇿 Qazaqşa: on eki
🇰🇬 Qırğızça: on eki
🌏 Uyghurche: on ikki
🌍 Tatarça: unike
🌍 Başqortsa: un ike
🌍 Çovaşla: vunikkö
🌍 Qaraqalpaqsha: on eki
🌍 Qırımtatarca: on eki
🌍 Qumuqça: on eki
🌍 Qaraçay-Malqar: on eki
🌍 Noğayşa: on eki
🌏 Sıbırca: unikä
🌍 Gagauzça: on iki
🌏 Saqalī: uon ikki
🌏 Dulgan-Hakalī: uon ikki
🌏 Tıvalap: on iyi
🌏 Salırça: on iki
🌏 Xakastap: on iki
🌏 Altaylap: on eki
🌏 Şor: on iygi
🌍 Urumça: on iki
🌍 Karajče: on ėki
🌍 Qrımçahça: on ekı
🌏 Soyot: on îhî
🌏 Tofalap: on îhî''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "люблю" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "i love" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ı love" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "seviyorum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "я люблю" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ben seviyorum":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): sevärmen
🇬🇧 English: I love
🇷🇺 Русский: люблю
🇹🇷 Türkçe: seviyorum
🇦🇿 Türkcə: sevirəm (to partner), çox istəyirəm (to family member, friend, relative, comrade etc)
🇹🇲 Türkmençe: söýýärin
🇺🇿 Oʻzbekcha: sevaman
🇰🇿 Qazaqşa: süyemin, jaqsı köremin
🇰🇬 Qırğızça: süyöm
🌏 Uyghurche: söyümen, yaxshi körümen
🌍 Tatarça: yaratam
🌍 Başqortsa: yaratam
🌍 Çovaşla: yuratatop
🌍 Qaraqalpaqsha: súyemen, jaqsı kóremen
🌍 Qırımtatarca: sevem
🌍 Qumuqça: süyemen
🌍 Qaraçay-Malqar: süyeme
🌍 Noğayşa: süyemen
🌏 Sıbırca: söyämen, yaratam
🌍 Gagauzça: severim
🌏 Saqalī: taptībın
🌏 Dolgan-Hakalī: bagarabın
🌏 Tıvalap: ınak tur-men
🌏 Salırça: män söyür
🌏 Xakastap: min xınara, xınçam
🌏 Altay: men süüp turar
🌏 Şor: kölençam
🌍 Urumça: severim
🌍 Karajče: siuviam
🌍 Qrımçahça: süvem
🌏 Soyot: ınaq tur-men
🌏 Tofalap: ekkisinêr men''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "discrimination" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ayrımcılık" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ayrimcilik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дискриминация" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ущемление" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ущемление прав":
        bot.send_message(message.chat.id, '''🇬🇧 English: discrimination
🇷🇺 Русский: дискриминация [diskriminatsiya]
🇹🇷 Türkçe: ayrımcılık
🇦🇿 Türkcə: ayrı-seçkilik
🇹🇲 Türkmençe: diskriminasiýa, hukuklary kemsitme
🇺🇿 Oʻzbekcha: diskriminatsiya, kamsitish
🇰🇿 Qazaqşa: diskriminasıya, kemsitiwşilik
🇰🇬 Qırğızça: diskriminatsiya, kemsintüü
🌏 Uyghurche: ayrimichiliq, kemsitish
🌍 Tatarça: diskriminatsiä
🌍 Başqortsa: diskriminatsiya, xoquq qısıw
🌍 Çovaşla: diskriminatsi
🌍 Qaraqalpaqsha: diskriminatsiya
🌍 Qırımtatarca: ayırım
🌍 Qumuqça: diskriminatsiya
🌍 Qaraçay-Malqar: diskriminatsiya, ayırıw
🌍 Noğayşa: diskriminatsiya
🌏 Sıbırca: diskriminaciä
🌍 Gagauzça: diskriminatsiya, ayrımcılık
🌏 Saqalī: diskriminaciya
🌏 Dulgan-Hakalī: diskriminaciya
🌏 Tıvalap: diskriminatsiya, ılgaarı
🌏 Salırça: arlaşdurma
🌏 Xakastap: dîskrîmînatsiya
🌏 Altaylap: diskriminatsiya
🌏 Şor: diskriminatsiya
🌍 Urumça: diskriminatsiya, ayrımcılıq
🌍 Karajče: diskriminacija, ajyrym
🌍 Qrımçahça: diskriminatsiya, ayırım
🌏 Soyot: dîskrîmînatsiya
🌏 Tofalap: dîskrîmînatsiya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кис-кис" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кис-кис-кис" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кискис" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кис кис" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кис кис кис" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кискискис" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kitty kitty" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kitty-kitty" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kitty kitty kitty" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kitty-kitty-kitty" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chh-chh" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chh-chh-chh" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chh chh chh" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chh chh" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pisipisi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pisi-pisi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кс-кс" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кыс-кыс" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кыс-кыс-кыс" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pisi pisi":
        bot.send_message(message.chat.id, '''🇬🇧 English: kitty kitty, chh-chh-chh
🇷🇺 Русский: кис-кис [kis-kis] (кыс-кыс) [kys-kys]
🇹🇷 Türkçe: pisi pisi
🇦🇿 Türkcə: piş-piş
🇹🇲 Türkmençe: piş-piş
🇺🇿 Oʻzbekcha: pish-pish
🇰🇿 Qazaqşa: pis-pis
🇰🇬 Qırğızça: mıy-mıy
🌏 Uyghurche: pish-pish
🌍 Tatarça: pes-pes
🌍 Başqortsa: bes-bes
🌍 Çovaşla: pöc-pöc
🌍 Qaraqalpaqsha: pısh-pısh
🌍 Qırımtatarca: pis-pis
🌍 Qumuqça: bişew-bişew
🌍 Qaraçay-Malqar: kişiw-kişiw
🌍 Noğayşa: piş-piş
🌏 Sıbırca: pes-pes
🌍 Gagauzça: pisi-pisi
🌏 Saqalī: kıs-kıs
🌏 Dulgan-Hakalī: kıs-kıs
🌏 Tıvalap: kıs-kıs
🌏 Salırça: mi-mi-mi
🌏 Xakastap: kis-kis
🌏 Altaylap: qıs-qıs
🌏 Şor: qıs-qıs
🌍 Urumça: pis-pis
🌍 Karajče: pis-pis
🌍 Qrımçahça: pis-pis
🌏 Soyot: qıs-qıs
🌏 Tofalap: qıs-qıs''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "now" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сейчас" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şimdi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şu an" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şuan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "в данный момент":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰢𐱃𐰃 
🐺 Old Turkic (bef. 13th c.): emdi (amtı, emti), bu ödtä, bu sa'at
🇬🇧 English: now
🇷🇺 Русский: сейчас [seychas]
🇹🇷 Türkçe: şimdi, şu an
🇦🇿 Türkcə: indi, bu saat (psat - dial.), hal-hazırda
🇹🇲 Türkmençe: häzir, şindi (indi), şu wagt 
🇺🇿 Oʻzbekcha: hozir, endi
🇰🇿 Qazaqşa: qazir (käzir, qazır)
🇰🇬 Qırğızça: azır
🌏 Uyghurche: hazir, emdi
🌍 Tatarça: xäzer, äle, inde
🌍 Başqortsa: xäðer, äle, oşo mäldä
🌍 Çovaşla: köc, xalö (xalex, xal), çasax
🌍 Qaraqalpaqsha: házir
🌍 Qırımtatarca: şimdi, şimdiçik
🌍 Qumuqça: hali, bussahat
🌍 Qaraçay-Malqar: busağatda
🌍 Noğayşa: ali, söli, azir, bu saat
🌏 Sıbırca: qäser
🌍 Gagauzça: şindi
🌏 Saqalī: biligin, sibiligin
🌏 Dulgan-Hakalī: anı
🌏 Tıvalap: am, doraan
🌏 Salırça: inci, pöxte (pöxtä, pu vaxtte), çuxur (çoxur)
🌏 Xakastap: am, amdı, sağam
🌏 Altaylap: em tura, emdi
🌏 Şor: am
🌍 Urumça: şindi, endi (imdi)
🌍 Karajče: endi, hali (halie), halieginia (haligine)
🌍 Qrımçahça: şındı, endı
🌏 Soyot: am, amdı
🌏 Tofalap: am, amdı''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "öyle" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "böyle" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "such" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "so" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "так" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "такой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "такая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "такое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "такие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şöyle":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): antağ (antaq), mundağ (muntağ), osuğluğ
🇬🇧 English: so, such
🇷🇺 Русский: так, такое (-ая, -ое, -ие)
🇹🇷 Türkçe: öyle, şöyle, böyle
🇦🇿 Türkcə: elə, belə, öylə (archaism), böylə (archaism)
🇹🇲 Türkmençe: şeýle, beýle
🇺🇿 Oʻzbekcha: shunday, bunday
🇰🇿 Qazaqşa: munday, onday, sonday, osınday
🇰🇬 Qırğızça: mınday, uşunday, oşondoy
🌏 Uyghurche: shundaq, bundaq
🌍 Tatarça: andıy, mondıy
🌍 Başqortsa: şulay, ulay, şunday, bınday, oşonday
🌍 Çovaşla: capla, apla, cakon pek, cavon pek, cav teri
🌍 Qaraqalpaqsha: solay, sonday, bunday, bılay, olay
🌍 Qırımtatarca: öyle, şöyle, böyle
🌍 Qumuqça: şolay, olay, bulay
🌍 Qaraçay-Malqar: allay, alay
🌍 Noğayşa: solay, sonday, sosınday
🌏 Sıbırca: alay, şalay, pılay
🌍 Gagauzça: ölä, bölä
🌏 Saqalī: mannık, itinnik, onnuk
🌏 Dulgan-Hakalī: beyelēk, itinnik, onnuk
🌏 Tıvalap: ındıg, mındıg
🌏 Salırça: eliği, beliği
🌏 Xakastap: andağ, mındağ
🌏 Altaylap: andıy, mındıy
🌏 Şor: endig (far), andığ (far), mindig (near), mındığ (near)
🌍 Urumça: bele (böyle), bulay (bılay), alay
🌍 Karajče: alej, bulej, bundi
🌍 Qrımçahça: ole, bole (boyle), bulay
🌏 Soyot: ındığ, mındığ
🌏 Tofalap: ındığ, mındığ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "суннит" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sunnit" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sunni" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sunni muslim" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sunnite" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sünni" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sünnü" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "суннитский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "суннитские":
        bot.send_message(message.chat.id, '''🇬🇧 English: Sunni, Sunnite, Sunni Muslim
🇷🇺 Русский: суннит [sunnit]
🇹🇷 Türkçe: Sünni
🇦🇿 Türkcə: Sünni, Sünnü (dial.)
🇹🇲 Türkmençe: sünni
🇺🇿 Oʻzbekcha: sunniy
🇰🇿 Qazaqşa: sünniyt
🇰🇬 Qırğızça: sunnit
🌏 Uyghurche: Sunni
🌍 Tatarça: Sönni
🌍 Başqortsa: Sönni
🌍 Çovaşla: sunnit
🌍 Qaraqalpaqsha: sunnit
🌍 Qırımtatarca: sünniy
🌍 Qumuqça: Sünni
🌍 Qaraçay-Malqar: sunnit
🌍 Noğayşa: Sünni
🌏 Sıbırca: Sönni
🌍 Gagauzça: Sünni
🌏 Saqalī: Sunnahıt
🌏 Dulgan-Hakalī: Sunnahıt
🌏 Tıvalap: sunnit
🌏 Salırça: Sunni
🌏 Xakastap: sunnît
🌏 Altaylap: sunnit
🌏 Şor: sunnit
🌍 Urumça: Sünni, sunites
🌍 Karajče: siunnij
🌍 Qrımçahça: sünniy
🌏 Soyot: sunnît
🌏 Tofalap: sunnît''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "суннизм" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sunnizm" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sunnism" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sunni islam" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sunnı ıslam" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sünnilik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ehli sünnet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ehl-i sünnet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sünnılık":
        bot.send_message(message.chat.id, '''🇬🇧 English: Sunni, Sunni Islam, Sunnism
🇷🇺 Русский: суннизм [sunnizm]
🇹🇷 Türkçe: Sünnilik, Ehl-i Sünnet
🇦🇿 Türkcə: Sünnilik, Sünnülük (dial.), Əhli Sünnə
🇹🇲 Türkmençe: sünnilik
🇺🇿 Oʻzbekcha: sunniylik, Ahl as-Sunna val-Jamoa
🇰🇿 Qazaqşa: sünniyzm, Ähl äs-Sunna wäl-Jamagat
🇰🇬 Qırğızça: sunnizm
🌏 Uyghurche: Sunnilik
🌍 Tatarça: Sönniçelek
🌍 Başqortsa: Sönnilek
🌍 Çovaşla: sunnizm
🌍 Qaraqalpaqsha: sunnizm
🌍 Qırımtatarca: sünniylik
🌍 Qumuqça: Sünnilik
🌍 Qaraçay-Malqar: sunnizm
🌍 Noğayşa: Sünnilik
🌏 Sıbırca: Sönnilek
🌍 Gagauzça: Sünnilik
🌏 Saqalī: sunnizm
🌏 Dulgan-Hakalī: sunnizm
🌏 Tıvalap: sunnizm
🌏 Salırça: Sunnilik
🌏 Xakastap: sunnîzm
🌏 Altaylap: sunnizm
🌏 Şor: sunnizm
🌍 Urumça: sunizmoz
🌍 Karajče: siunnijlik
🌍 Qrımçahça: sünniylik
🌏 Soyot: sunnîzm
🌏 Tofalap: sunnîzm''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шиит" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shiit" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şii" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şıı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "alevi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "alevı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şie" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shii" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shia muslim" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shi'ite" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шиитская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шиитские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shiites":
        bot.send_message(message.chat.id, '''🇬🇧 English: Shia, Shia Muslim, Shi'ite
🇷🇺 Русский: шиит [shiit]
🇹🇷 Türkçe: Şii, Alevi
🇦🇿 Türkcə: Şiə
🇹🇲 Türkmençe: şaýy
🇺🇿 Oʻzbekcha: shia
🇰🇿 Qazaqşa: şıyğa, şiit
🇰🇬 Qırğızça: şiit
🌏 Uyghurche: Shiye
🌍 Tatarça: şığıy
🌍 Başqortsa: şığıy
🌍 Çovaşla: şiit
🌍 Qaraqalpaqsha: shiit
🌍 Qırımtatarca: şiiy
🌍 Qumuqça: şiyit
🌍 Qaraçay-Malqar: şeyit
🌍 Noğayşa: şeyit
🌏 Sıbırca: şığıy
🌍 Gagauzça: şii
🌏 Saqalī: Şia
🌏 Dulgan-Hakalī: Şia
🌏 Tıvalap: şiit
🌏 Salırça: şiye
🌏 Xakastap: şîît
🌏 Altaylap: şiit
🌏 Şor: şiit
🌍 Urumça: xızılbaş
🌍 Karajče: šiij
🌍 Qrımçahça: şiiy
🌏 Soyot: şîît
🌏 Tofalap: şîît''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шиизм" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шиитство" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shia islam" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "alevilik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şiilik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şıılık" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shiizm":
        bot.send_message(message.chat.id, '''🇬🇧 English: Shia Islam, Shia
🇷🇺 Русский: шиизм [shiizm]
🇹🇷 Türkçe: Şiilik, Alevilik
🇦🇿 Türkcə: Şiəlik
🇹🇲 Türkmençe: şaýylyk
🇺🇿 Oʻzbekcha: shialik
🇰🇿 Qazaqşa: şıyğalıq, şiizm
🇰🇬 Qırğızça: şiizm
🌏 Uyghurche: Shiyelik
🌍 Tatarça: şığıyçılıq, şığıylek
🌍 Başqortsa: şığıylıq
🌍 Çovaşla: şiizm
🌍 Qaraqalpaqsha: shiizm
🌍 Qırımtatarca: şiiylik
🌍 Qumuqça: şiyitlik
🌍 Qaraçay-Malqar: şiizm
🌍 Noğayşa: şeyitlik
🌏 Sıbırca: şığıylıq
🌍 Gagauzça: şiilik
🌏 Saqalī: şiizm
🌏 Dulgan-Hakalī: şiizm
🌏 Tıvalap: şiizm
🌏 Salırça: şiyepay
🌏 Xakastap: şîîzm
🌏 Altaylap: şiizm
🌏 Şor: şiizm
🌍 Urumça: xızılbaşçılıq
🌍 Karajče: šiijlik
🌍 Qrımçahça: şiiylik
🌏 Soyot: şîîzm
🌏 Tofalap: şîîzm''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "математика" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "matematika" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "matematik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mathematics" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "maths" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "riyaziye" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "матика" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "матиматика" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "математека" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "riyaziyet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "math":
        bot.send_message(message.chat.id, '''🇬🇧 English: mathematics
🇷🇺 Русский: математика [matematika]
🇹🇷 Türkçe: matematik, riyaziye (Ottoman Turkish)
🇦🇿 Türkcə: riyaziyyat
🇹🇲 Türkmençe: matematika, ryýazýat (archaism)
🇺🇿 Oʻzbekcha: matematika, riyoziyot (archaism)
🇰🇿 Qazaqşa: matematika, qıysap ğılımı (hisap ilmi) (archaism)
🇰🇬 Qırğızça: matematika
🌏 Uyghurche: matématika
🌍 Tatarça: riyaziyat, matematika
🌍 Başqortsa: matematika
🌍 Çovaşla: mattemattiko
🌍 Qaraqalpaqsha: matematika
🌍 Qırımtatarca: riyaziyat
🌍 Qumuqça: riyaziyat
🌍 Qaraçay-Malqar: matematika
🌍 Noğayşa: matematika, esap
🌏 Sıbırca: matematika, isäp ilmi (archaism)
🌍 Gagauzça: matematik
🌏 Saqalī: matematika
🌏 Dulgan-Hakalī: matematika
🌏 Tıvalap: matematika, san ertemi
🌏 Salırça: şuşye
🌏 Xakastap: matematîka
🌏 Altaylap: matematika
🌏 Şor: matematika, too
🌍 Urumça: matematika
🌍 Karajče: matematika
🌍 Qrımçahça: riyaziyat
🌏 Soyot: matematîka
🌏 Tofalap: matematîka''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "современный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "современый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "современная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "современное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "современные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "современник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "современик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "modern" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çağdaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "contemporary" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "contenporary" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "современно" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "нынешний" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "нынешняя" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "нынешнее" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "нынешние" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "теперешний" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "современница" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "coeval" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "zamandaş":
        bot.send_message(message.chat.id, '''🇬🇧 English: I. contemporary, coeval II. modern
🇷🇺 Русский: современный [sovremenny] (-ая, -ое), современник [sovremennik] (I)
🐺 Old Turkic (bef. 13th c.): yügärüki (II), közünür (II), amtı (II), amtıqı (II)
🇹🇷 Türkçe: çağdaş, modern (II)
🇦🇿 Türkcə: çağdaş, müasir, həməsr (I), indiki (II), hazırkı (II)
🇹🇲 Türkmençe: döwrebap, zamandaş (I), asyrdaş (I), döwürdeş (I), häzirki (II)
🇺🇿 Oʻzbekcha: zamonaviy, zamondosh (I), hozirgi (II)
🇰🇿 Qazaqşa: zamanawıy, zamandas (I), tustas (I), qazirgi (II)
🇰🇬 Qırğızça: zamanbap, zamandaş (I), azırqıça (II)
🌏 Uyghurche: chaghdash, zamaniwiy, zamandash (I), hazirqi (II)
🌍 Tatarça: zamandaş (I), xäzerge (II)
🌍 Başqortsa: zamandaş (I), xäðerge (II), möhim (II)
🌍 Çovaşla: xalxi
🌍 Qaraqalpaqsha: zamanlas (I), dáwirles (I), házirgi (II),  házirgi zaman (II)
🌍 Qırımtatarca: zemaneviy, zamandaş (I), şimdiki (II)
🌍 Qumuqça: zamandaş (I), haligi (II)
🌍 Qaraçay-Malqar: zamanında jaşağan (I), zamanındağı (I), busağatdağı (II)
🌍 Noğayşa: zamandas (I), äligi (II), sölegi (II), bu zamanğı (II)
🌏 Sıbırca: samantaş (I), qäserge (II)
🌍 Gagauzça: zamandaş (I), modern (II)
🌏 Saqalī: bïr kemnēq (I), biliññi (II), anıgı (II)
🌏 Dulgan-Hakalī: bïr kemnēk (I), biliññi (II), anıgı (II)
🌏 Tıvalap: çañgıs üe (I), ol üe (I), amgı üe (II), bo üe (II)
🌏 Salırça: zamandaş (I), çuxurğı (II)
🌏 Xakastap: pir tustağı (I), amğı (II), amdığı (II)
🌏 Altaylap: bir öydögi (I), emdigi (II)
🌏 Şor: pir tuştağı (I), amdığı (II)
🌍 Urumça: zamandaş (I), bu zamanlı (II), şindiki (II)
🌍 Karajče: zamandaš (I), birzamanly (I), biugiungiu (bugiunky) (II), zemane (II)
🌍 Qrımçahça: zamandaş (I), zemane (II)
🌏 Soyot: bir öy hiräsindegi (I), amğı (II)
🌏 Tofalap: bir şağdağı (I), amğıı (II)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "capital" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "capital city" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "столица" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "payitaht" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "paytaht" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "başkent" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "столичная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "столичный":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): balıq, ordu, örgün (throne), toy (residence, general headquarters)
🇬🇧 English: capital (capital city)
🇷🇺 Русский: столица [stolitsa]
🇹🇷 Türkçe: başkent, payitaht (ottoman turk.)
🇦🇿 Türkcə: paytaxt, baş şəhər, mərkəz
🇹🇲 Türkmençe: paýtagt, merkez, merkezi şäher
🇺🇿 Oʻzbekcha: poytaxt
🇰🇿 Qazaqşa: astana, elorda
🇰🇬 Qırğızça: borbor, ordoşaar, başqalaa
🌏 Uyghurche: paytexit (paytext), bash kent, merkez
🌍 Tatarça: başqala, paytäxet, baş şähär, märkäz
🌍 Başqortsa: baş qala (başqala)
🌍 Çovaşla: töp xula, aslo xula, patşa xoli
🌍 Qaraqalpaqsha: paytaxt, oray, bas qala
🌍 Qırımtatarca: paytaht, baş şeer
🌍 Qumuqça: taxşahar (tax şahar)
🌍 Qaraçay-Malqar: orta şahar, ara şahar
🌍 Noğayşa: bas qala
🌏 Sıbırca: paş tora
🌍 Gagauzça: baş kent, baş kasaba
🌏 Saqalī: turū sir, kïn
🌏 Dulgan-Hakalī: turū hir, kïn
🌏 Tıvalap: nayısılal, töp xooray
🌏 Salırça: paytagt
🌏 Xakastap: stolîtsa
🌏 Altaylap: stolitsa, qaan tergezi (archaism)
🌏 Şor: öön tura
🌍 Urumça: axdivan şeeri, paduşanın şeeri
🌍 Karajče: bij sahar (bij-šahar), bas sahar (baš šeher), saraj šahary
🌍 Qrımçahça: paytaht, baş şeer
🌏 Soyot: ulığ-cer
🌏 Tofalap: uluğ-cer''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ve" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "and" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "и":
        bot.send_message(message.chat.id, '''🇬🇧 See also "with", because in Turkic languages "with" is often used than "and" (For example, "cat and dog" literally will be "cat with dog")
🇷🇺 Посмотрите также союз "с", поскольку в тюркских языках часто используется этот союз чем "и" (Напр. "кот и собака" дословно будет "кот с собакой")

🇬🇧 English: and
🇷🇺 Русский: и [i]
🇹🇷 Türkçe: ve
🇦🇿 Türkcə: və
🇹🇲 Türkmençe: we
🇺🇿 Oʻzbekcha: va
🇰🇿 Qazaqşa: jäne
🇰🇬 Qırğızça: jana
🌏 Uyghurche: we
🌍 Tatarça: wä, häm
🌍 Başqortsa: häm
🌍 Çovaşla: ta/te, tata
🌍 Qaraqalpaqsha: jáne
🌍 Qırımtatarca: ve
🌍 Qumuqça: wa
🌍 Qaraçay-Malqar: em
🌍 Noğayşa: em
🌏 Sıbırca: äm
🌍 Gagauzça: hem
🌏 Saqalī: uonna
🌏 Dulgan-Hakalī: onton, onuga
🌏 Tıvalap: baza
🌏 Salırça: ve
🌏 Xakastap: paza
🌏 Altaylap: baza la
🌏 Şor: pazoq
🌍 Urumça: ve
🌍 Karajče: hiem, da
🌍 Qrımçahça: ve, em, em de
🌏 Soyot: bısa (bısaaq)
🌏 Tofalap: bısaa''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "with" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "с" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ile" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıle" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "билан":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰋𐰃𐰼𐰠𐰀
🐺 Old Turkic (bef. 13th c.): birlä (bilä)
🇬🇧 English: with
🇷🇺 Русский: с [s] (с кем-либо, с чем-либо)
🇹🇷 Türkçe: ile (-la/-le)
🇦🇿 Türkcə: ilə (-la/-lə) (north azerb.), inən (-nan/-nən) (south azerb.)
🇹🇲 Türkmençe: bilen
🇺🇿 Oʻzbekcha: bilan
🇰🇿 Qazaqşa: menen (-men/-ben/-pen)
🇰🇬 Qırğızça: menen
🌏 Uyghurche: bilen
🌍 Tatarça: belän
🌍 Başqortsa: menän
🌍 Çovaşla: -pa/-pe, -lo/-lö
🌍 Qaraqalpaqsha: menen/benen/penen
🌍 Qırımtatarca: ile, -nen
🌍 Qumuqça: bulan
🌍 Qaraçay-Malqar: bla
🌍 Noğayşa: -man/-men/-pan/-pen
🌏 Sıbırca: pelän, -man/-män
🌍 Gagauzça: bilä, -nan/-nen
🌏 Saqalī: kıtta, -nīn/-nan/-lāq
🌏 Dulgan-Hakalī: gıtta (kıtta), -nīn/-nan/-lāk
🌏 Tıvalap: bile
🌏 Salırça: bilen
🌏 Xakastap: -nañ/-neñ/-tañ/-teñ/-dañ/-deñ
🌏 Altaylap: -la/-le/-lo/-lö
🌏 Şor: pazoq, qapşıra
🌍 Urumça: -nan/-nän
🌍 Karajče: iliań (beliań, bilen, byla, bilien, bile)
🌍 Qrımçahça: ilen, -nen
🌏 Soyot: bile (bilä, ble, blä) / bıla (bla)
🌏 Tofalap: bile (ble) / bıla (bla)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "exception" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "исключение" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "istisna":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): qalı
🇬🇧 English: exception
🇷🇺 Русский: исключение (из правил) [isklyucheniye]
🇹🇷 Türkçe: istisna
🇦🇿 Türkcə: istisna
🇹🇲 Türkmençe: kadadan çykma
🇺🇿 Oʻzbekcha: istisno
🇰🇿 Qazaqşa: erekşelik, birıŋğay jağday, tısqarılıq, erejeden tıs
🇰🇬 Qırğızça: erejeden tışqarı, özgöçö
🌏 Uyghurche: istisna
🌍 Tatarça: çığarma, çitläşü
🌍 Başqortsa: ayırma, sitläşew, ayırımlıq, taşlama
🌍 Çovaşla: normoran poronsa, uroxla pulma pultarni, pravilona poxonmanni
🌍 Qaraqalpaqsha: ayrıqshalıq, erekshelik, ayırım
🌍 Qırımtatarca: istisna
🌍 Qumuqça: qaydadan tayışıw
🌍 Qaraçay-Malqar: jangız, ayırıb
🌍 Noğayşa: ayırmalıq, basqalıq
🌏 Sıbırca: cığarma
🌍 Gagauzça: kuralların dışlaması
🌏 Saqalī: tuorāhın, qālī, kehï
🌏 Dulgan-Hakalī: tuorāhın, kālī, kehï
🌏 Tıvalap: onzagay tavarılga, tuskay tavarılga, ündüreri
🌏 Salırça: istisna, rivey (livay)
🌏 Xakastap: ~ pasxazı
🌏 Altaylap: ~ başqazı
🌏 Şor: ~ paşqazı
🌍 Urumça: istisna
🌍 Karajče: ~ hajrysy
🌍 Qrımçahça: istisna
🌏 Soyot: ~ başqası
🌏 Tofalap: ~ başqası''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bee" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "arı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пчелы" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пчела" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пчелка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "honeybee" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "honey bee" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bal arısı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "apis" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "anthophila" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ari":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): arı
🇬🇧 English: bee, apis, honeybee
🇷🇺 Русский: пчела [pchela]
🇹🇷 Türkçe: arı, bal arısı
🇦🇿 Türkcə: arı
🇹🇲 Türkmençe: ary
🇺🇿 Oʻzbekcha: asalari, bolari
🇰🇿 Qazaqşa: ara, bal ara (balara), jabayı ara
🇰🇬 Qırğızça: aarı
🌏 Uyghurche: hesel herisi
🌍 Tatarça: bal qortı, umarta qortı
🌍 Başqortsa: bal qorto, umarta qorto, iñgej
🌍 Çovaşla: pıl xurçö, völle xurçö
🌍 Qaraqalpaqsha: hárre, pal hárresi
🌍 Qırımtatarca: balqurt, arı (archaism)
🌍 Qumuqça: balcibin
🌍 Qaraçay-Malqar: bal çibin
🌍 Noğayşa: bal şıbın
🌏 Sıbırca: arı, palbaqtı (balbaqsı), balğurt, cağawın, palcağawın
🌍 Gagauzça: kuvan, arı
🌏 Saqalī: müöttēq ıñırıa, müöttēq tigēyi, iñrae (archaism)
🌏 Dulgan-Hakalī: ıñırıa
🌏 Tıvalap: arı
🌏 Salırça: pal çüyin (balcuyin)
🌏 Xakastap: aar
🌏 Altaylap: adaru
🌏 Şor: aarı
🌍 Urumça: petäk, balxurt, balxurtçibin, balçibin
🌍 Karajče: balkurt (bal kurty), balcibin, čiuliu (čulu)
🌍 Qrımçahça: balqurt çıbını
🌏 Soyot: arı
🌏 Tofalap: arı''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yaddaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bellek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hafıza" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hafiza" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hatır" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hatir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hatıra" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hatira" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "memori" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "memory" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "память" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "воспоминание" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "реминисценция" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "memorı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "recollection" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "reminiscence":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): yad, zikr (zikir)
🇬🇧 English: memory, reminiscence (II), recollection (II)
🇷🇺 Русский: память, воспоминание (II)
🇹🇷 Türkçe: bellek, hafıza, hatır
🇦🇿 Türkcə: yaddaş, hafizə, yad, zehin, zənn, huş (III)
🇹🇲 Türkmençe: ýat, ýatlama, huş (III)
🇺🇿 Oʻzbekcha: xotira (xotir), yod, es
🇰🇿 Qazaqşa: es, jad, estelik (II)
🇰🇬 Qırğızça: es
🌏 Uyghurche: es, xatire, eslime, yad
🌍 Tatarça: xäter (xatirä), zihen, is
🌍 Başqortsa: xäter (xätirä), zihen, iþ (III)
🌍 Çovaşla: as, asonu, as-pil, asomlox (II)
🌍 Qaraqalpaqsha: yad, es, huş (III)
🌍 Qırımtatarca: afıza, zein, yad, hatıra (II), es (us) (III)
🌍 Qumuqça: es, esdelik (II)
🌍 Qaraçay-Malqar: es, esdegi (II), esde qalğan zat (II)
🌍 Noğayşa: es, estelik (II)
🌏 Sıbırca: is, qäter (II), istälek (II)
🌍 Gagauzça: bellek, anıt, anı (II)
🌏 Saqalī: öy, öygö tutū, keries (II), aqtī (II)
🌏 Dulgan-Hakalī: öy
🌏 Tıvalap: çüve utpazı, ugaan, saktıışkın (II), turaskaal (II)
🌏 Salırça: yad, sahış (reminiscence of bride)
🌏 Xakastap: sağıs, sağısxa kîrgeni (II)
🌏 Altaylap: ezem, es (III)
🌏 Şor: es, pögünüş (II)
🌍 Urumça: es, sağınç, xatır (atır, xatir) (II), mnimosinos (mnimosino) (II)
🌍 Karajče: ėś, sahynč (sahyš), chatyr (II)
🌍 Qrımçahça: es, xatır
🌏 Soyot: sağış, saqtıışqın (II)
🌏 Tofalap: sağış, saqtıışqın (II), medää (III)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dress" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gown" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "elbise" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kadın elbisesi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kadin elbisesi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "платье" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "женское платье" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "women's dress" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "womens dress" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "women dress" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "woman's dress" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "womans dress" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "платьице" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "платишко" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "woman dress":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): ton
🇬🇧 English: dress (women's dress), gown
🇷🇺 Русский: платье [plat'ye] (женское платье)
🇹🇷 Türkçe: elbise (kadın elbisesi)
🇦🇿 Türkcə: don
🇹🇲 Türkmençe: köýnek (+ shirt)
🇺🇿 Oʻzbekcha: koʻylak (+ shirt)
🇰🇿 Qazaqşa: köylek (+ shirt)
🇰🇬 Qırğızça: köynök (+ shirt)
🌏 Uyghurche: uzun köynek, xotun elbisesi
🌍 Tatarça: külmäk (+ shirt)
🌍 Başqortsa: küldäk (+ shirt)
🌍 Çovaşla: platye, köpe (+ shirt), xörarom tavraşö
🌍 Qaraqalpaqsha: kóylek (+ shirt)
🌍 Qırımtatarca: anter
🌍 Qumuqça: opuraq
🌍 Qaraçay: çepken
🌍 Malqar: jıyrıq
🌍 Noğayşa: şıba
🌏 Sıbırca: köyläk (göynäk) (+ shirt)
🌍 Gagauzça: fistan
🌏 Saqalī: bılāççıya
🌏 Dulgan-Hakalī: platye, urbākı (+ shirt)
🌏 Tıvalap: platye
🌏 Salırça: poyqarax (peqarax, poykırıx), xantar (xanter, xantär) (+ shirt)
🌏 Xakastap: platye, kögenek (+ shirt)
🌏 Altaylap: platye
🌏 Şor: könek (+ shirt)
🌍 Urumça: kaba (gaba), fistan, urba (ruba, urbaşka) (+ shirt)
🌍 Karajče: uprak (uprach), urba
🌍 Qrımçahça: fstan
🌏 Soyot: platye, çamça (+ shirt)
🌏 Tofalap: platye, ırmaaqı (+ shirt)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рубашка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рубаха" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shirt" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сорочка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сорошка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gömlek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "schirt" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gölmek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rubashka":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): köŋläk
🇬🇧 English: shirt
🇷🇺 Русский: рубашка [rubashka]
🇹🇷 Türkçe: gömlek
🇦🇿 Türkcə: köynək
🇹🇲 Türkmençe: köýnek
🇺🇿 Oʻzbekcha: koʻylak
🇰🇿 Qazaqşa: jeyde, köylek (erler köylegi)
🇰🇬 Qırğızça: köynök
🌏 Uyghurche: köynek
🌍 Tatarça: külmäk
🌍 Başqortsa: küldäk
🌍 Çovaşla: köpe
🌍 Qaraqalpaqsha: kóylek
🌍 Qırımtatarca: kölmek
🌍 Qumuqça: gölek
🌍 Qaraçay-Malqar: kölek
🌍 Noğayşa: köylek
🌏 Sıbırca: köyläk (göynäk)
🌍 Gagauzça: gölmek, flani
🌏 Saqalī: ırbāqı
🌏 Dulgan-Hakalī: urbākı
🌏 Tıvalap: xöyleñ
🌏 Salırça: xantar (xanter, xantär), çämcä (çamca)
🌏 Xakastap: kögenek
🌏 Altaylap: künek, çamça
🌏 Şor: könek
🌍 Urumça: kölek, urba (ruba, urbaşka)
🌍 Karajče: kelmek (kiolmiak)
🌍 Qrımçahça: kolmek
🌏 Soyot: çamça, urmaaxı
🌏 Tofalap: ırmaaqı (ırmaaqqı)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "buz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "льдина" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лед" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ледышка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ice" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "muz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ледок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıce" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "frozen water":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): buz (muz)
🇬🇧 English: ice
🇷🇺 Русский: лёд [lyod]
🇹🇷 Türkçe: buz
🇦🇿 Türkcə: buz
🇹🇲 Türkmençe: buz
🇺🇿 Oʻzbekcha: muz
🇰🇿 Qazaqşa: muz
🇰🇬 Qırğızça: muz
🌏 Uyghurche: muz
🌍 Tatarça: boz
🌍 Başqortsa: boð
🌍 Çovaşla: por
🌍 Qaraqalpaqsha: muz
🌍 Qırımtatarca: buz
🌍 Qumuqça:	buz
🌍 Qaraçay-Malqar: buz
🌍 Noğayşa: buz
🌏 Sıbırca:	pos
🌍 Gagauzça: buz
🌏 Saqalī: mūs
🌏 Dulgan-Hakalī: būs
🌏 Tıvalap: doş
🌏 Salırça: muz
🌏 Xakastap: pus
🌏 Altaylap: toş, bus (pus, mus)
🌏 Şor: mus
🌍 Urumça: buz
🌍 Karajče: buz
🌍 Qrımçahça: buz
🌏 Soyot: toş
🌏 Tofalap: toş''', reply_markup=markup_menu)

    elif message.text.lower() == "большой брат" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "старший брат" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "болшой брат" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "büyük birader" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "büyuk bırader" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "büyük bırader" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "big bro" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "big brother" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "older brother" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "old brother" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bıg brother":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): aqa, eçi
🇬🇧 English: big brother, older brother
🇷🇺 Русский: большой брат, старший брат 
🇹🇷 Türkçe: büyük birader, ağabey, abi
🇦🇿 Türkcə: böyük qardaş, ağa (dialect), ağadadaş (dialect), dadaş (dialect), qağa (dialect)
🇹🇲 Türkmençe: uly gardaş, aga
🇺🇿 Oʻzbekcha: katta aka, aka
🇰🇿 Qazaqşa: ülken ağa, ağa
🇰🇬 Qırğızça: uluu ağa, ağa
🌏 Uyghurche: büyük brader, aka
🌍 Tatarça: zur abıy, abıy (abzıy)
🌍 Başqortsa: ður ağay, ağay
🌍 Çovaşla: pısok piççe, piççe
🌍 Qaraqalpaqsha: úlken aǵa, aǵa
🌍 Qırımtatarca: büyük ağa, ağa
🌍 Qumuqça: ullu qardaş, ağa
🌍 Qaraçay-Malqar: ullu qarındaş (~ qarnaş), tamada qarındaş (~ qarnaş), abadan qarındaş (~ qarnaş)
🌍 Noğayşa: üyken qardaş, ağa
🌏 Sıbırca: ollo äkä (~ ağa, ~ aqa)
🌍 Gagauzça: büük kardaş, batü
🌏 Saqalī: ulaqan ubay
🌏 Dulgan-Hakalī: ulakan ubay
🌏 Tıvalap: ulug akıy
🌏 Salırça: ullı kaka (~ kaga)
🌏 Xakastap: uluğ xarındas, abaa
🌏 Altaylap: caan qarındaş (coon ~), aqa
🌏 Şor: uluğ aça, aça
🌍 Urumça: beyük ğardaş (büyük ~), ağa
🌍 Karajče: bijik karyndaš (~ kardaš), aka
🌍 Qrımçahça: buyuk aqay (~ ağa)
🌏 Soyot: ulığ haqı, haqı
🌏 Tofalap: uluğ aha, aha''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "любовь" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лаффки" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "love" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "любов" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "любовный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "luv" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sevgi" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sevda" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fondness" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "aşk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "влюбленность" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mehr" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "muhabbet":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): sevig, sevmäk, sevüglük, vudd, amranmaq
🇬🇧 English: love
🇷🇺 Русский: любовь [lyubov']
🇭🇺 Magyar: szeretet
🇹🇷 Türkçe: sevgi, aşk, muhabbet, sevda
🇦🇿 Türkcə: sevgi, eşq, məhəbbət, sevda, mehr
🇹🇲 Türkmençe: söýgi, yşk, muhabbet, mähir
🇺🇿 Oʻzbekcha: sevgi, ishq, muhabbat, mehr, sevish
🇰🇿 Qazaqşa: mahabbat, süyispenşilik
🇰🇬 Qırğızça: mahabbat, süyüü, aşıqtıq
🌏 Uyghurche: söygü, söyüsh, küyünüsh
🌍 Tatarça: mähäbbät, yaratu, söyü, ğıyşıq
🌍 Başqortsa: mähäbbät, yaratıw, höyöw, ğişıq
🌍 Çovaşla: yuratu, yuratni, savni, savoşu
🌍 Qaraqalpaqsha: muhabbat, súyiw, súyiwshilik, súygenlik, ashıqlıq
🌍 Qırımtatarca: sevgi, aşq, muabbet, sevda
🌍 Qumuqça:	süyüw, süyüm, muhabbat, ğaşıqlıq
🌍 Qaraçay-Malqar: süyüw, süymeklik
🌍 Noğayşa: süyüw, süyisüw, yaratuw
🌏 Sıbırca:	söyöw, söygö, yaratıw
🌍 Gagauzça: sevgi, aşk, seviş, sevim, sevda
🌏 Saqalī: taptal, taptīr
🌏 Dulgan-Hakalī: baga
🌏 Tıvalap: ınakşıl, ınak boluru, ınak (archaism)
🌏 Salırça: söyüş, havan
🌏 Xakastap: köölenis, xınıs, kööl
🌏 Altaylap: süüş, süügen
🌏 Şor: köleniş
🌍 Urumça: sevgi, eşx (eşk, ışx), muabet (muhabbet, mabet), maabetlik, sevda, sevdalıx, seviş (süyüş), sevim, süyümlük
🌍 Karajče: siuviarlik (siverlik), zevda, zevdalyk, sivim, sivmek
🌍 Qrımçahça: süverlık, eşq, sevda, sevdalıh
🌏 Soyot: ınaqşıl
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "axe" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ax" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "топор" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "balta" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "секира" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "топорный":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): baltu (baldu)
🇬🇧 English: axe
🇷🇺 Русский: топор [topor], секира [sekira]
🇭🇺 Magyar: balta
🇲🇳 Mongol: balta (balt), sükhe (sükh)
🇹🇷 Türkçe: balta
🇦🇿 Türkcə: balta
🇹🇲 Türkmençe: palta
🇺🇿 Oʻzbekcha: bolta
🇰🇿 Qazaqşa: balta
🇰🇬 Qırğızça: balta
🌏 Uyghurche: palta
🌍 Tatarça: balta
🌍 Başqortsa: balta
🌍 Çovaşla: purto
🌍 Qaraqalpaqsha: balta
🌍 Qırımtatarca: balta
🌍 Qumuqça:	balta
🌍 Qaraçay-Malqar: balta
🌍 Noğayşa: balta
🌏 Sıbırca:	palta
🌍 Gagauzça: balta
🌏 Saqalī: süge
🌏 Dulgan-Hakalī: hüge
🌏 Tıvalap: baldı, süge
🌏 Salırça: palda (palto)
🌏 Xakastap: paltı (maltı)
🌏 Altaylap: malta
🌏 Şor: malta
🌍 Urumça: balta
🌍 Karajče: balta (bolta), keskič
🌍 Qrımçahça: balta
🌏 Soyot: sügä
🌏 Tofalap: süge''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "коздима" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kojima" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hideo kojima" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хидэо кодзима" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хидео кодзима" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "deha" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kajima" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hideo kajima" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хидэо кадзима" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хидео кадзима" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кадзима" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гений" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genius" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "homo ingeniosus" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dahi" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гениальный":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): irşi täŋri
🇬🇧 English: genius
🇷🇺 Русский: гений [geniy]
🇹🇷 Türkçe: deha, dahi
🇦🇿 Türkcə: dahi
🇹🇲 Türkmençe: uly alym, uçursyz zehin, dahy (archaism)
🇺🇿 Oʻzbekcha: daho, dohiy
🇰🇿 Qazaqşa: danışpan, kemeŋger
🇰🇬 Qırğızça: oluya, geniy
🌏 Uyghurche: dahiy
🌍 Tatarça: dahi
🌍 Başqortsa: dahi
🌍 Çovaşla: geni
🌍 Qaraqalpaqsha: danıshpan
🌍 Qırımtatarca: dea, kemalatlı (archaism)
🌍 Qumuqça:	ullu pahmulu (~ adam)
🌍 Qaraçay-Malqar: ullu pahmulu (~ adam)
🌍 Noğayşa: geniy
🌏 Sıbırca:	dahiy
🌍 Gagauzça: dahi, geniy
🌏 Saqalī: geniy
🌏 Dulgan-Hakalī: geniy
🌏 Tıvalap: şılgarañgay ugaannıg (~ kiji)
🌏 Salırça: cin, tiensay
🌏 Xakastap: geniy
🌏 Altaylap: oyğor (~ kiji)
🌏 Şor: geniy
🌍 Urumça: dahi, idiofiya
🌍 Karajče: dahi
🌍 Qrımçahça: dea
🌏 Soyot: geniy
🌏 Tofalap: geniy''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "arpa" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ячмень" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ячмен" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ячменный" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "barley":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): arpa
🇬🇧 English: barley
🇷🇺 Русский: ячмень [yachmien]
🇭🇺 Magyar: árpa
🇲🇳 Mongol: arbay (arvay)
🇹🇷 Türkçe: arpa
🇦🇿 Türkcə: arpa
🇹🇲 Türkmençe: arpa
🇺🇿 Oʻzbekcha: arpa
🇰🇿 Qazaqşa: arpa
🇰🇬 Qırğızça: arpa
🌏 Uyghurche: arpa
🌍 Tatarça: arpa
🌍 Başqortsa: arpa
🌍 Çovaşla: urpa
🌍 Qaraqalpaqsha: arpa
🌍 Qırımtatarca: arpa
🌍 Qumuqça:	arpa
🌍 Qaraçay-Malqar: arpa
🌍 Noğayşa: arpa
🌏 Sıbırca:	arpa, aşlıq
🌍 Gagauzça: arpa
🌏 Saqalī: neçimien
🌏 Dulgan-Hakalī: yaçmien
🌏 Tıvalap: arbay
🌏 Salırça: arfa (arepa, afra)
🌏 Xakastap: arba, köçe
🌏 Altaylap: arba
🌏 Şor: aş
🌍 Urumça: arpa
🌍 Karajče: arpa
🌍 Qrımçahça: arpa
🌏 Soyot: arbay
🌏 Tofalap: yaçmen''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гость" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "konuk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гостевой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гостья" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "konak" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "musafir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mihman" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "misafir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "the guest" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "конах" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "къонах" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кхонах" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "guest":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): qonuq, küdän (küdün, küðän), uma (wayfarer)
🇬🇧 English: guest
🇷🇺 Русский: гость [gost']
🇹🇷 Türkçe: misafir, konuk, mihman
🇦🇿 Türkcə: qonaq, mehman, müsafir (wayfarer)
🇹🇲 Türkmençe: myhman, gonak, mysapyr (wayfarer)
🇺🇿 Oʻzbekcha: mehmon, qoʻnoq, musofir (wayfarer)
🇰🇿 Qazaqşa: qonaq, meyman, müsäpir (wayfarer)
🇰🇬 Qırğızça: qonoq, meyman
🌏 Uyghurche: méhman, qonaq, musapir (wayfarer)
🌍 Tatarça: qunaq, mihman, mosafir (wayfarer)
🌍 Başqortsa: qunaq, mihman, mosafir (wayfarer)
🌍 Çovaşla: xona
🌍 Qaraqalpaqsha: qonaq, miyman, músápir (wayfarer)
🌍 Qırımtatarca: musafir, qonaq
🌍 Qumuqça:	qonaq
🌍 Qaraçay-Malqar: qonaq, musafir (wayfarer)
🌍 Noğayşa: qonaq
🌏 Sıbırca:	qunaq, mosabir (wayfarer), aljı (archaism)
🌍 Gagauzça: konuk, mihman, musaafir, konak (+ wayfarer's place of abode)
🌏 Saqalī: ıaljıt, qonoho (guest who will spend the night)
🌏 Dulgan-Hakalī: ıaljıt
🌏 Tıvalap: aalçı
🌏 Salırça: qonax
🌏 Xakastap: aalcı
🌏 Altaylap: ayılçı
🌏 Şor: aymaqçı
🌍 Urumça: müsävir (misefir, misafir, mısafır), xonax
🌍 Karajče: konach (konak), musafir (musefir, miusefir, mysefir)
🌍 Qrımçahça: qonaq, mısafır
🌏 Soyot: aalcı
🌏 Tofalap: aalcı''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "китай" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "китайский" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "китайская" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "китайское" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "китайские" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chine" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "china" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kitay" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qin" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çin" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "поднебесная" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кнр" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "zhōngguó" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "zhongguo" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tianxia" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "prc":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): Xıtay, Tavğaç, Çin, Çin-ü Maçin, Maxaçinadiş
🇬🇧 English: China, Cathay (archaism)
🇷🇺 Русский: Китай [Kitay]
🇹🇷 Türkçe: Çin, Sin (Ottoman Turk.), Maçin (Ottoman Turk.)
🇦🇿 Türkcə: Çin, Kitay (in sovyet Azerbaijan), Xita (خطا) (archaism)
🇹🇲 Türkmençe: Hytaý, Çyn ülkesi (archaism)
🇺🇿 Oʻzbekcha: Xitoy, Chin (archaism)
🇰🇿 Qazaqşa: Qıtay
🇰🇬 Qırğızça: Qıtay, Juñgo (dialect)
🌏 Uyghurche: Chine, Junggo, Kidat (acrhaism)
🌍 Tatarça: Qıtay, Çin
🌍 Başqortsa: Qıtay
🌍 Çovaşla: Kittay
🌍 Qaraqalpaqsha: Qıtay
🌍 Qırımtatarca: Çin, Qıtay
🌍 Qumuqça:	Çin, Qıtay
🌍 Qaraçay-Malqar: Qıtay
🌍 Noğayşa: Qıtay
🌏 Sıbırca:	Qıtay, Cın
🌍 Gagauzça: Kitay, Çin
🌏 Saqalī: Kıtay
🌏 Dulgan-Hakalī: Kıtay
🌏 Tıvalap: Kıdat
🌏 Salırça: Suyni, Hatı (Xadi, Xaçi), Cuñgo
🌏 Xakastap: Xıdat
🌏 Altaylap: Qıdat
🌏 Şor: Qıdat
🌍 Urumça: Xina, Çin
🌍 Karajče: China, Čin
🌍 Qrımçahça: Çin
🌏 Soyot: Qıtat
🌏 Tofalap: Qıtat
in Chinese: Zhōngguó''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "китаец" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "китаянка" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "китайцы" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chinese" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chinase" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kitaylı" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qinese" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çinli" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ching chong" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ching-chong" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chingchong" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çin çon" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chinee" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chink" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "китаеза" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чингчонг" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çinçon":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): xıtay, tabğaç (tavğaç), çınlığ, çini
🇬🇧 English: Chinese
🇷🇺 Русский: китаец [китаец]
🇹🇷 Türkçe: Çinli
🇦🇿 Türkcə: çinli, kitay (in sovyet Azerbaijan)
🇹🇲 Türkmençe: hytaý, hytaýly
🇺🇿 Oʻzbekcha: xitoy, chinli (archaism)
🇰🇿 Qazaqşa: qıtay
🇰🇬 Qırğızça: qıtay
🌏 Uyghurche: xenzu, jongguluq, Kidat kişi (acrhaism)
🌍 Tatarça: qıtay
🌍 Başqortsa: qıtay
🌍 Çovaşla: kittay
🌍 Qaraqalpaqsha: qıtay, qıtaylı
🌍 Qırımtatarca: çinli, qıtaylı
🌍 Qumuqça:	çinli, qıtaylı
🌍 Qaraçay-Malqar: qıtaylı
🌍 Noğayşa: qıtay
🌏 Sıbırca:	qıtay, cın
🌍 Gagauzça: kitaylı
🌏 Saqalī: kıtay
🌏 Dulgan-Hakalī: kıtay
🌏 Tıvalap: kıdat
🌏 Salırça: Cuñgo kişi
🌏 Xakastap: xıdat
🌏 Altaylap: qıdat
🌏 Şor: qıdat
🌍 Urumça: xinalı, çinli
🌍 Karajče: chinaly, činli
🌍 Qrımçahça: çinlı
🌏 Soyot: qıtat
🌏 Tofalap: qıtat''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "камен" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "камень" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "stone" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "a stone" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "stones" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "daş" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "taş" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "камешек" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "валун":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜:	𐱃𐱁 (𐱃𐰀𐱁)
🐺 Old Turkic (bef. 13th c.): taş
🇬🇧 English: stone
🇷🇺 Русский: камень [kamen']
🇹🇷 Türkçe: taş
🇦🇿 Türkcə: daş
🇹🇲 Türkmençe: daş
🇺🇿 Oʻzbekcha: tosh
🇰🇿 Qazaqşa: tas
🇰🇬 Qırğızça: taş
🌏 Uyghurche: tash
🌍 Tatarça: taş
🌍 Başqortsa: taş
🌍 Çovaşla: çul
🌍 Qaraqalpaqsha: tas
🌍 Qırımtatarca: taş
🌍 Qumuqça: taş
🌍 Qaraçay-Malqar: taş
🌍 Noğayşa: tas
🌏 Sıbırca: taş
🌍 Gagauzça: taş
🌏 Saqalī: tās
🌏 Dulgan-Hakalī: tās
🌏 Tıvalap: daş
🌏 Salırça:	daş (taş)
🌏 Xakastap: tas
🌏 Altaylap: taş
🌏 Şor: taş
🌍 Urumça: daş (taş)
🌍 Karajče: taš (daš, tas)
🌍 Qrımçahça: taş
🌏 Soyot: daş (taş)
🌏 Tofalap: daş (taş)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "падишах" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "патшах" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бадшах" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "падшах" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "батшах" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "padishah" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "padşah" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "padişah" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "padışah" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "padshah" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pad-e shah" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "padeshah":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): padişah
🇬🇧 English:	Padishah (Padeshah, Padshah)
🇷🇺 Русский: падишах [padishakh]
🇹🇷 Türkçe: padişah
🇦🇿 Türkcə: padşah
🇹🇲 Türkmençe: patyşa
🇺🇿 Oʻzbekcha: podshoh (podsho)
🇰🇿 Qazaqşa: patşa (padıyşah, padıyşa)
🇰🇬 Qırğızça: padışa
🌏 Uyghurche: padishah
🌍 Tatarça:	patşa (padişah)
🌍 Başqortsa: batşa
🌍 Çovaşla:	patşa
🌍 Qaraqalpaqsha: patsha
🌍 Qırımtatarca: padişah (padişa)
🌍 Qumuqça:	paça
🌍 Qaraçay-Malqar: patçah
🌍 Noğayşa: patşa
🌏 Sıbırca: patşa
🌍 Gagauzça: padişah
🌏 Saqalī: padisāq
🌏 Dulgan-Hakalī: padihāk
🌏 Tıvalap: padişax
🌏 Salırça: padişa
🌏 Xakastap: padişax
🌏 Altaylap: padişax
🌏 Şor: padişax
🌍 Urumça: padşa (paduşa, padışa)
🌍 Karajče: padyša (patsah, patšach, padyšach, padišach)
🌍 Qrımçahça: padışa
🌏 Soyot: padişah
🌏 Tofalap: padişah''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шах" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şah" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shakh" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shah" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "šâh":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): şah
🇬🇧 English:	shah
🇷🇺 Русский: шах [shakh]
🇹🇷 Türkçe: şah
🇦🇿 Türkcə: şah
🇹🇲 Türkmençe: şa
🇺🇿 Oʻzbekcha: shoh
🇰🇿 Qazaqşa: şah (şa)
🇰🇬 Qırğızça: şaa (şah)
🌏 Uyghurche: shah
🌍 Tatarça:	şah
🌍 Başqortsa: şah
🌍 Çovaşla:	şax
🌍 Qaraqalpaqsha: shax
🌍 Qırımtatarca: şah
🌍 Qumuqça:	şah
🌍 Qaraçay-Malqar: şah
🌍 Noğayşa: şah
🌏 Sıbırca: şah
🌍 Gagauzça: şah
🌏 Saqalī: sāq (şaq)
🌏 Dulgan-Hakalī: hāk (şaq)
🌏 Tıvalap: şa (şax)
🌏 Salırça: şa (şah)
🌏 Xakastap: şax
🌏 Altaylap: şax
🌏 Şor: şax
🌍 Urumça: şa (şah)
🌍 Karajče: ša (sah, šach)
🌍 Qrımçahça: şah
🌏 Soyot: şah
🌏 Tofalap: şah''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "король" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "краль" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "крал" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kral" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "king" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "korol" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kıng":
        bot.send_message(message.chat.id, '''🇬🇧 English: king
🇷🇺 Русский: король [korol']
🇹🇷 Türkçe: kral
🇦🇿 Türkcə: kral, qıral (archaism), şah (South Azerbaijani)
🇹🇲 Türkmençe: korol, karol (archaism)
🇺🇿 Oʻzbekcha: qirol
🇰🇿 Qazaqşa: korol, patşa
🇰🇬 Qırğızça: korol, padışa
🌏 Uyghurche: kral, padishah, xan
🌍 Tatarça: korol
🌍 Başqortsa: korol
🌍 Çovaşla: korol, patşa
🌍 Qaraqalpaqsha: korol, patsha
🌍 Qırımtatarca: qıral
🌍 Qumuqça: qıral, paça
🌍 Qaraçay-Malqar: patçah	
🌍 Noğayşa: korol, patşa
🌏 Sıbırca: patşa
🌍 Gagauzça: kral
🌏 Saqalī: qoruol (korol)
🌏 Dulgan-Hakalī: koruol (korol), toyon
🌏 Tıvalap: xaan
🌏 Salırça: padişa, vañ
🌏 Xakastap: korol
🌏 Altaylap: korol, qaan
🌏 Şor: korol
🌍 Urumça: kıral (xıral)
🌍 Karajče: bij
🌍 Qrımçahça: qıral
🌏 Soyot: vañ
🌏 Tofalap: vañ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pussy" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "puss" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cat" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "katty" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tomcat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кошка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kedi" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pişik" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pışık" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кот" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "котик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "feline" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kitten" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кошак" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "котяра" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "котэ" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киска":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): mişkiç, muş, manu /wildcat/
🇬🇧 English: cat
🇷🇺 Русский: кот, кошка [koshka], киска [kiska]
🇹🇷 Türkçe: kedi, pişik {dial.}, pisi {used by children}
🇦🇿 Türkcə: pişik
🇹🇲 Türkmençe: pişik
🇺🇿 Oʻzbekcha: mushuk
🇰🇿 Qazaqşa: mısıq
🇰🇬 Qırğızça: mışıq
🌏 Uyghurche: müshük
🌍 Tatarça: mäçe, pesi
🌍 Başqortsa: besäy
🌍 Çovaşla:	kuşak
🌍 Qaraqalpaqsha: pıshıq
🌍 Qırımtatarca: mışıq, kedi {dial.}, pisik {dial.}, pardoş {male cat}
🌍 Qumuqça: mişik, bişew {used by children}
🌍 Qaraçay-Malqar: kiştik, kişiw {used by children}
🌍 Noğayşa: mısıq
🌏 Sıbırca: meşäk
🌍 Gagauzça: kedi, pisi
🌏 Saqalī: kuoska
🌏 Dulgan-Hakalī: kuoska (koşka)
🌏 Tıvalap:	diis, moortay, mıy-ıt, tiispey {archaism}
🌏 Salırça:	müşüx (mışux, muşux)
🌏 Xakastap: xoosxa
🌏 Altaylap: mıy, kiske, manı {wildcat}, pırzaq {archaism}
🌏 Şor: pızraq
🌍 Urumça: pişik (pisik, mışıx), maçu, pardoş (pardu, pardoy, pardos) {male cat}
🌍 Karajče: mači (meči, mačy, maci), kedi
🌍 Qrımçahça: mışıh
🌏 Soyot: hööşke, manıl (manuul) {wildcat}
🌏 Tofalap: hööşke (kööşke)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "осел" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ослиный" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ослинный" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ослиная" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ослик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ослиное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ослинные" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ass" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "donkey" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eşek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eşşek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ишак" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ишачий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ишачка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ослица" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ишачье" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "donki":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): eşäk (eşyäk, eşgäk)
🇬🇧 English: donkey, ass
🇷🇺 Русский: ишак [ishak], осёл [osyol]
🇹🇷 Türkçe: eşek
🇦🇿 Türkcə: eşşək, ulaq, uzunqulaq
🇹🇲 Türkmençe: eşek
🇺🇿 Oʻzbekcha: eshak
🇰🇿 Qazaqşa: esek
🇰🇬 Qırğızça: eşek
🌏 Uyghurche: éshek
🌍 Tatarça: işäk
🌍 Başqortsa: işäk
🌍 Çovaşla: aşak
🌍 Qaraqalpaqsha: eshek
🌍 Qırımtatarca: eşek
🌍 Qumuqça: eşek
🌍 Qaraçay-Malqar: eşek
🌍 Noğayşa: eşek
🌏 Sıbırca: işäk
🌍 Gagauzça: eşek
🌏 Saqalī: işak, osyol (ösüöl)
🌏 Dulgan-Hakalī: işak, osyol
🌏 Tıvalap: elçigen
🌏 Salırça: eşex
🌏 Xakastap: ???
🌏 Altaylap: eştek
🌏 Şor: eştek
🌍 Urumça: eşşäk (eşyäk, eşek, işek)
🌍 Karajče: ešiak (ešek, esek)
🌍 Qrımçahça: eşek
🌏 Soyot: elcîgän
🌏 Tofalap: elcîgen''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "каспийское море" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "каспий" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "каспи" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "каспийский" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "каспийское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "каспийскоеморе" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "caspian sea" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "caspi" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kaspi" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "caspy" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kaspy" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "caspian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "caspiansea" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hazar denizi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hazardenizi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hazar denızı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hazar deniz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "caspium mare" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "caspiummare" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "caspium" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "abbacuch sea" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "abbacuch" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "abiskun" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hazardeniz":
        bot.send_message(message.chat.id, '''🇬🇧 English: Caspian Sea
🇷🇺 Русский: Каспийское море [Kaspiyskoye more]
🇹🇷 Türkçe: Hazar Denizi
🇦🇿 Türkcə: Xəzər dənizi
🇹🇲 Türkmençe: Hazar deňzi
🇺🇿 Oʻzbekcha: Kaspiy dengizi, Xazar dengizi {archaism}
🇰🇿 Qazaqşa: Kaspiy teŋizi (Qaspıy teŋizi), Atıraw teŋizi {archaism, 1931}
🇰🇬 Qırğızça: Kaspiy deŋizi
🌏 Uyghurche: Kaspiy Déngizi, Hazar Déngizi (Hezer Déngizi)
🌍 Tatarça: Xäzär diñgeze
🌍 Başqortsa: Kaspiy diñgeðe (Kaspi diñgeðe)
🌍 Çovaşla: Kaspi tinösö
🌍 Qaraqalpaqsha: Kaspiy teńizi
🌍 Qırımtatarca: Hazar deñizi
🌍 Qumuqça: Xazar deñiz, Tarğu deñiz
🌍 Qaraçay-Malqar: Xazar teñiz (Xaznar teñiz)
🌍 Noğayşa: Kaspiy teñizi
🌏 Sıbırca: Qäsär tiñgese
🌍 Gagauzça: Hazar Denizi
🌏 Saqalī: Kaspiy bayğala
🌏 Dulgan-Hakalī: Kaspiy baygala
🌏 Tıvalap: Kaspiy dalay
🌏 Salırça: Xazar Deñizi, Lixäy
🌏 Xakastap: Kaspîyskay talay
🌏 Altaylap: Kaspiyskiy talay
🌏 Şor: Kaspiy talay
🌍 Urumça: Xazar dängizi (Xazar denizi)
🌍 Karajče: Chazar tieńgiźi (Chazar denizi)
🌍 Qrımçahça: Hazar dengızı
🌏 Soyot: Kaspiy dalay
🌏 Tofalap: Kaspiy dalay''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "germania" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "germany" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "германия" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "germaniya" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "almanya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "deutschland" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фрг" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "frg" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "frg" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "германский" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cermanya":
        bot.send_message(message.chat.id, '''🇬🇧 English: Germany, Germania {historical region}
🇷🇺 Русский: Германия [Germaniya]
🇹🇷 Türkçe: Almanya, Cermanya {historical region}, Nemçe {archaism}
🇦🇿 Türkcə: Almaniya, Germaniya {historical region}, Nemcə {archaism}
🇹🇲 Türkmençe: Germaniýa, Almaniýa
🇺🇿 Oʻzbekcha: Germaniya, Olmoniya
🇰🇿 Qazaqşa: Germaniya, Almaniya
🇰🇬 Qırğızça: Germaniya
🌏 Uyghurche: Gérmaniye
🌍 Tatarça: Almaniä, Germaniä
🌍 Başqortsa: Älmäniä, Germaniya
🌍 Çovaşla: Germani
🌍 Qaraqalpaqsha: Germaniya
🌍 Qırımtatarca: Almaniya
🌍 Qumuqça: Germaniya, Almaniya
🌍 Qaraçay-Malqar: Germaniya, Alman
🌍 Noğayşa: Germaniya, Almaniya
🌏 Sıbırca: Alman, Kirman
🌍 Gagauzça: Germaniya, Almaniya
🌏 Saqalī: Germaniya
🌏 Dulgan-Hakalī: Germaniya
🌏 Tıvalap: Germaniya
🌏 Salırça: Almaniya, Deguo
🌏 Xakastap: Germanîya
🌏 Altaylap: Germaniya
🌏 Şor: Germaniya
🌍 Urumça: Almaniya, Germaniya
🌍 Karajče: Germanija, Niemic Jeri
🌍 Qrımçahça: Germaniya
🌏 Soyot: Germanîya
🌏 Tofalap: Germanîya
In German: Deutschland''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "немец" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "немецкий" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "немка" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "немецкая" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "немецкое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "немецкие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "alman" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "german" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "germans" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nimsa" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nemse" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nemce" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nimce" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nemçe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nimçe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nimse" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "deutsch" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "germanic" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "almanlar":
        bot.send_message(message.chat.id, '''🇬🇧 English: German
🇷🇺 Русский: немец [nemec]
🇹🇷 Türkçe: Alman, Nemçe {archaism}
🇦🇿 Türkcə: alman, nemcə {archaism}, nemes {in Sovyet Azerbaijani}
🇹🇲 Türkmençe: alman, nemes
🇺🇿 Oʻzbekcha: nemis, olmon
🇰🇿 Qazaqşa: nemis, alman
🇰🇬 Qırğızça: nemis
🌏 Uyghurche: Gérman, Némis
🌍 Tatarça: alman
🌍 Başqortsa: nimes, alman
🌍 Çovaşla: nimöc
🌍 Qaraqalpaqsha: nemec
🌍 Qırımtatarca: alman, nemse, lemse {dial.}
🌍 Qumuqça: nemis, alman
🌍 Qaraçay-Malqar: almanlı, nemça
🌍 Noğayşa: alman, nemis
🌏 Sıbırca: almannı, kirmannı
🌍 Gagauzça: nemţä, alman
🌏 Saqalī: niemes
🌏 Dulgan-Hakalī: niemes
🌏 Tıvalap: nemets
🌏 Salırça: alman
🌏 Xakastap: nemets
🌏 Altaylap: nemets
🌏 Şor: nemets
🌍 Urumça: nemse, alman
🌍 Karajče: niemic
🌍 Qrımçahça: nemse
🌏 Soyot: nemets
🌏 Tofalap: nemets''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "germanic-speaking european" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "germanic-speaking" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "germanic speaking" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "germanic-speaking-european" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "germanic speaking european" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cermen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cerman" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "германец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "германцы" :
        bot.send_message(message.chat.id, '''🇬🇧 English: Germanic-speaking European
🇷🇺 Русский: германец [germanec]
🇹🇷 Türkçe: Cermen, Nemçe {archaism}
🇦🇿 Türkcə: german, nemcə {archaism}
🇹🇲 Türkmençe: german
🇺🇿 Oʻzbekcha: german
🇰🇿 Qazaqşa: germandıq
🇰🇬 Qırğızça: german
🌏 Uyghurche: Gérman
🌍 Tatarça: german
🌍 Başqortsa: german
🌍 Çovaşla: german
🌍 Qaraqalpaqsha: german
🌍 Qırımtatarca: german
🌍 Qumuqça: german
🌍 Qaraçay-Malqar: nemça, german
🌍 Noğayşa: german
🌏 Sıbırca: kirman (german)
🌍 Gagauzça: german
🌏 Saqalī: german
🌏 Dulgan-Hakalī: german
🌏 Tıvalap: german
🌏 Salırça: german
🌏 Xakastap: german
🌏 Altaylap: german
🌏 Şor: german
🌍 Urumça: german
🌍 Karajče: german
🌍 Qrımçahça: german
🌏 Soyot: german
🌏 Tofalap: german''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "франция" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "france" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "franse" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fransa" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "frans" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "république française":
        bot.send_message(message.chat.id, '''🇬🇧 English: France
🇷🇺 Русский: Франция [Frantsiya]
🇹🇷 Türkçe: Fransa
🇦🇿 Türkcə: Fransa, Frəngistan {archaism}
🇹🇲 Türkmençe: Fransiýa
🇺🇿 Oʻzbekcha: Fransiya
🇰🇿 Qazaqşa: Fransıya (Frantsiya)
🇰🇬 Qırğızça: Frantsiya
🌏 Uyghurche: Fransiye
🌍 Tatarça: Frantsiya (Fransa, Färänsä)
🌍 Başqortsa: Frantsiya
🌍 Çovaşla: Frantsi
🌍 Qaraqalpaqsha: Franciya
🌍 Qırımtatarca: Frenkistan
🌍 Qumuqça: Ferenk (Perenk)
🌍 Qaraçay-Malqar: Frantsiya, Perenk {archaism}
🌍 Noğayşa: Frantsiya
🌏 Sıbırca: Franсıya
🌍 Gagauzça: Franțiya
🌏 Saqalī: Bırānsıya
🌏 Dulgan-Hakalī: Frantsiya
🌏 Tıvalap: Frantsiya
🌏 Salırça: Furanka
🌏 Xakastap: Frantsiya
🌏 Altaylap: Frantsiya
🌏 Şor: Frantsiya
🌍 Urumça: Fransa
🌍 Karajče: Francija
🌍 Qrımçahça: Frantsiya
🌏 Soyot: Frantsiya
🌏 Tofalap: Frantsiya
In French: France''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "француз" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "французский" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "французкий" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fransız" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fransiz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "франк" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "french":
        bot.send_message(message.chat.id, '''🇬🇧 English: French
🇷🇺 Русский: француз [frantsuz]
🇹🇷 Türkçe: Fransız
🇦🇿 Türkcə: fransız, frəng {archaism}
🇹🇲 Türkmençe: fransuz, pereň {archaism}
🇺🇿 Oʻzbekcha: fransuz, farang, forank {archaism}
🇰🇿 Qazaqşa: fransız (frantsuz)
🇰🇬 Qırğızça: frantsuz
🌏 Uyghurche: fransuz, perengg
🌍 Tatarça: fransuz (frantsuz)
🌍 Başqortsa: frantsuz
🌍 Çovaşla: xorantus (xransus)
🌍 Qaraqalpaqsha: francuz
🌍 Qırımtatarca: frenk, fransız
🌍 Qumuqça: ferenkli (perenkli), fıransız
🌍 Qaraçay-Malqar: frantsuz, perenkli {archaism}
🌍 Noğayşa: frantsuz
🌏 Sıbırca: francuz
🌍 Gagauzça: franțuz
🌏 Saqalī: boronsūs (borontūs, poronsūs)
🌏 Dulgan-Hakalī: frantsuz
🌏 Tıvalap: frantsuz
🌏 Salırça: furankalı, fransız
🌏 Xakastap: frantsuz
🌏 Altaylap: frantsuz
🌏 Şor: frantsuz
🌍 Urumça: fransız
🌍 Karajče: francuz
🌍 Qrımçahça: frantsuz
🌏 Soyot: frantsuz
🌏 Tofalap: frantsuz''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "говорить" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "говори" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "разговаривать" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "разговаривайте" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "говорите" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "разговаривай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "speak" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to speak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "talk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to talk" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "konuş" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "konuşmak" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "söyle" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "söylemek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "выражаться" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "выражайся" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "высказываться" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "высказывайся" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рассказывай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "расказывай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "расказывать" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рассказывать":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): sözlä, tılda, savla, til yorıt, söz ula, söz qıl, ay, ay te, yaŋşa, sumlı ("speak a foreign language")
🇬🇧 English: I. speak II. talk
🇷🇺 Русский: говори, рассказывай, разговаривай
🇹🇷 Türkçe: I. konuş II. söyle
🇦🇿 Türkcə: I. danış, qonuş {archaism} II. söylə, ayt {archaism}
🇹🇲 Türkmençe: I. geple II. aýt
🇺🇿 Oʻzbekcha: I. gapir II. ayt
🇰🇿 Qazaqşa: I. söyle II. ayt
🇰🇬 Qırğızça: I. süylö II. ayt
🌏 Uyghurche: I. sözle II. éyt
🌍 Tatarça: I. söylä, söyläş II. äyt
🌍 Başqortsa: I. höylä, höyläş II. äyt
🌍 Çovaşla: somaxla, kala, kalac
🌍 Qaraqalpaqsha: I. sóyle II. ayt
🌍 Qırımtatarca: I. laf et, söylen, qonuş II. söyle, ayt
🌍 Qumuqça: I. söyle II. ayt
🌍 Qaraçay-Malqar: I. söleş II. ayt
🌍 Noğayşa: I. söyle, til şıq II. ayt, söyle
🌏 Sıbırca: käplä, käpläş, äyt
🌍 Gagauzça: lafet, sölä (söle), konuş, sözleş
🌏 Saqalī: I. sañar, tıllan II. et, kepsē
🌏 Dulgan-Hakalī: hañar, die, kepsē, çorguy
🌏 Tıvalap: I. {language_name}+lap, çugaala II. sögle, çugaala
🌏 Salırça: sözle, yanşa, kaçalaş
🌏 Xakastap: {language_name}+ta, çooxta, çooxtas, ayt, aydıs (aytıs), aasta
🌏 Altaylap: {language_name}+la, ayt, quuçında
🌏 Şor: çooqta, ayt, erbekteş 
🌍 Urumça: lafet (laf xıl), lafla, söyle (söle), sözle, xonuş, ayt (eyt)
🌍 Karajče: siozle (sioźlia), ajt (ejt)
🌍 Qrımçahça: laf et, sole, ayt
🌏 Soyot: {language_name}+la, cuğaala, sooda, soodan
🌏 Tofalap: {language_name}+la, sooda, soodan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сказать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "скажи" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "de" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "says" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to say" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "скажите" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "назови" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "назовите" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tell" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to tell" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "назвать" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tosay":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): te, ayıt
🇬🇧 English: say, tell
🇷🇺 Русский: скажи, назови
🇹🇷 Türkçe: de
🇦🇿 Türkcə: de
🇹🇲 Türkmençe: diý
🇺🇿 Oʻzbekcha: de
🇰🇿 Qazaqşa:	de, ayt
🇰🇬 Qırğızça: de, ayt
🌏 Uyghurche: de, éyt
🌍 Tatarça: äyt, di
🌍 Başqortsa: äyt, ti
🌍 Çovaşla: te, kala
🌍 Qaraqalpaqsha: de, ayt
🌍 Qırımtatarca: de
🌍 Qumuqça:	de, ayt
🌍 Qaraçay-Malqar: de, ayt
🌍 Noğayşa: de, ayt
🌏 Sıbırca: äyt, ti
🌍 Gagauzça: de, sölä
🌏 Saqalī: die, et
🌏 Dulgan-Hakalī: die
🌏 Tıvalap: sögle, de
🌏 Salırça: de (dey, di, diy, te, tey, ti, tiy), yanşa (yaşa)
🌏 Xakastap: çooxta, ayt, söle, di {archaism}
🌏 Altaylap: de, ayt
🌏 Şor: ayt
🌍 Urumça: de (di, dey, diy), ayt (eyt)
🌍 Karajče: de, ajt (ejt)
🌍 Qrımçahça: de, sole
🌏 Soyot: de
🌏 Tofalap: de''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "монстр" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "монстер" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "монстэр" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "monster" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "canavar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чудовище" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чудовише" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чудовища" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чудище" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "monstre":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): madar
🇬🇧 English: monster
🇷🇺 Русский: чудовище, чудище, монстр [monstr]
🇹🇷 Türkçe: canavar
🇦🇿 Türkcə: qulyabanı, xoxan, canavar (dialect, meaning may vary, "wolf" in standart language)
🇹🇲 Türkmençe: eýmenç janawer
🇺🇿 Oʻzbekcha: yalmogʻiz
🇰🇿 Qazaqşa:	qubıjıq
🇰🇬 Qırğızça: jomoqtordoğu çoñ janıbar
🌏 Uyghurche: yalmawuz, alwasti
🌍 Tatarça: albastı
🌍 Başqortsa: ğifrit, qurqınıs zat
🌍 Çovaşla: cam, yölmevös
🌍 Qaraqalpaqsha: bálemat
🌍 Qırımtatarca: canavar, ifrit
🌍 Qumuqça:	ajdaha
🌍 Qaraçay-Malqar: emegen, janıwar
🌍 Noğayşa: aylaq üyken
🌏 Sıbırca: äştäğı
🌍 Gagauzça: mogucu, canavar
🌏 Saqalī: jikti kütür
🌏 Dulgan-Hakalī: moñus, oburgu
🌏 Tıvalap: mañgıs, moos, amırga-moos
🌏 Salırça: mongıshar, cin-şeytañ
🌏 Xakastap: çîlbigen
🌏 Altaylap: celbegen, moñus, kerbös, çulmus
🌏 Şor: şebeldey
🌍 Urumça: xorxulux
🌍 Karajče: korchuvluch
🌍 Qrımçahça: canavar
🌏 Soyot: ee
🌏 Tofalap: ee''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pink" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "розовый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "розоватый" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "розовая" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "розовое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бледно-красный" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бледнокрасный" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "розовые" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pink color" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pink colour" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pembe":
        bot.send_message(message.chat.id, ''' 🇬🇧 In most of the cases word "red" is used in Turkic languages, because it is considered a shade of the red color.
🇷🇺 Чаще всего используется просто слово "красный", поскольку в тюркских языках розовый цвет считается оттенком красного.
🇹🇷 Çok durumda "pembe" yerine Türk lehcelerinde "kırmızı" kelimesi kullanılır, çünkü pembe kırmızı rengin tonu olarak kabul edilir.

🐺 Old Turkic (bef. 13th c.): qırğu (qızğu)
🇬🇧 English: pink
🇷🇺 Русский: розовый (-ая, -ое) [rozovyy]
🇹🇷 Türkçe: pembe, gül rengi {archaism}
🇦🇿 Türkcə: çəhrayı, gül rəngi {archaism}
🇹🇲 Türkmençe: gülgün, mawy
🇺🇿 Oʻzbekcha: pushti
🇰🇿 Qazaqşa:	qızğılt, alqızıl
🇰🇬 Qırğızça: qızğılt, külgün qızıl
🌏 Uyghurche: halreng, gülreng
🌍 Tatarça: alsu, al
🌍 Başqortsa: alhıw, al, aqhıl qıðıl, qıðğılt
🌍 Çovaşla: kören, pisev {dialect}
🌍 Qaraqalpaqsha: qızǵılt
🌍 Qırımtatarca: pempe, gülgülü (gülgüli), al
🌍 Qumuqça:	al, qızıl, qızğılt
🌍 Qaraçay-Malqar: qızğıl, çayır betli
🌍 Noğayşa: qızğılt, al-qızıl
🌏 Sıbırca: qolborañ, al
🌍 Gagauzça: pembä, gülgülü, rozova
🌏 Saqalī: teterkey (teterkēn), kıtarqay (keteykēn), oruosabay (rozovıy)
🌏 Dulgan-Hakalī: oruosabay (rozovıy)
🌏 Tıvalap: kuu-kızıl, yagaan-kızıl, ak-kızıl
🌏 Salırça: toxuñ, yuñxuñ
🌏 Xakastap: aalay (alay), xoxay {dialect}
🌏 Altaylap: ooşqı, qubaqay qızıl
🌏 Şor: qısqıltım
🌍 Urumça: gül çıray
🌍 Karajče: kyzylmuš
🌍 Qrımçahça: pempe
🌏 Soyot: aq-qızıl
🌏 Tofalap: aq-qızıl''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "англия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "england" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ingiltere" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıngıltere" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "anglia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ingilterre" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "angleterre" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "angelterre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "angliya":
        bot.send_message(message.chat.id, '''🇬🇧 English: England
🇷🇺 Русский:	Англия [Angliya]
🇹🇷 Türkçe: İngiltere, İngilterra {archaism}
🇦🇿 Türkcə: İngiltərə, İngilis bladı {archaism}
🇹🇲 Türkmençe: Angliýa, Aňgylya {archaism}
🇺🇿 Oʻzbekcha: Angliya
🇰🇿 Qazaqşa: Angliya
🇰🇬 Qırğızça: Angliya
🌏 Uyghurche: Engiliye, England
🌍 Tatarça: Angliya
🌍 Başqortsa: Angliya
🌍 Çovaşla: Angli
🌍 Qaraqalpaqsha: Angliya
🌍 Qırımtatarca: İngiltere
🌍 Qumuqça: İñilis (İngilis), Angliya
🌍 Qaraçay-Malqar: İñilis (İngilis), Angliya
🌍 Noğayşa: Angliya
🌏 Sıbırca: Angliya, Anqırstan
🌍 Gagauzça: İngiltere
🌏 Saqalī: Engiliye, Āñgılıya
🌏 Dulgan-Hakalī: Angliya
🌏 Tıvalap: Angliya
🌏 Salırça: Eñguo, İniltere
🌏 Xakastap: Anglîya
🌏 Altaylap: Angliya
🌏 Şor: Angliya
🌍 Urumça: Angliya
🌍 Karajče: Anglija
🌍 Qrımçahça: İngiltere
🌏 Soyot: Anglîya
🌏 Tofalap: Anglîya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "англичанин" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "англичанка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ангийский" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "англиский" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "англисский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ангийская" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "англиская" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "англисская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ангийское" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "англиское" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "англисское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ангийские" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "англиские" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "англисские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "english" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "englishman" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "englishwoman" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "inglis" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ingliz" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ingiliz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ınglıs" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ınglız" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıngılız" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ingilis":
        bot.send_message(message.chat.id, '''🇬🇧 English: english, englishman
🇷🇺 Русский: англичанин [anglichanin], английский [angliyskiy]
🇹🇷 Türkçe: İngiliz
🇦🇿 Türkcə: ingilis
🇹🇲 Türkmençe: iňlis
🇺🇿 Oʻzbekcha: ingliz
🇰🇿 Qazaqşa: ağılşın
🇰🇬 Qırğızça: anglis
🌏 Uyghurche: Ingiliz
🌍 Tatarça: ingliz
🌍 Başqortsa: ingliz
🌍 Çovaşla: akolçan
🌍 Qaraqalpaqsha: inglis
🌍 Qırımtatarca: ingliz
🌍 Qumuqça: iñilis (ingilis), iñilisli (ingilisli)
🌍 Qaraçay-Malqar: iñilis (ingilis), iñilisli (ingilisli)
🌍 Noğayşa: äñilşen
🌏 Sıbırca: inglis, anqır
🌍 Gagauzça: ingiliz
🌏 Saqalī: āñl, āgılıs {archaism}
🌏 Dulgan-Hakalī: angliçanin, angliyskay
🌏 Tıvalap: angli
🌏 Salırça: eñgilis (iniliz)
🌏 Xakastap: anglîçanîn, anglîyskay
🌏 Altaylap: angliçan, angliyskiy
🌏 Şor: angliçanin, angliyskay
🌍 Urumça: ingiliz
🌍 Karajče: engliz
🌍 Qrımçahça: ingliz
🌏 Soyot: angli
🌏 Tofalap: angli''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "india" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "inidian" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ındıan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ındıa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hindistan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hındıstan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hindustan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индостан" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "industan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hintistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hindstan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индустан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индийский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индостанский" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индийская" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индийское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индийские" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индусстан":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): Enätkäk
🇬🇧 English:	India
🇷🇺 Русский: Индия [Indiya]
🇹🇷 Türkçe: Hindistan
🇦🇿 Türkcə: Hindistan
🇹🇲 Türkmençe: Hindistan
🇺🇿 Oʻzbekcha: Hindiston
🇰🇿 Qazaqşa: Ündistan
🇰🇬 Qırğızça: İndiya, Indıstan {archaism}
🌏 Uyghurche: Hindistan
🌍 Tatarça:	Hindistan
🌍 Başqortsa: Hindostan
🌍 Çovaşla: İndi
🌍 Qaraqalpaqsha: Hindistan
🌍 Qırımtatarca: İndistan
🌍 Qumuqça:	Hindistan
🌍 Qaraçay-Malqar: İndustan
🌍 Noğayşa:	İndistan, İndiya
🌏 Sıbırca:	İntistan
🌍 Gagauzça:  Hindistan, İndiya
🌏 Saqalī: Ïndiye
🌏 Dulgan-Hakalī: İndiya
🌏 Tıvalap: İndiya
🌏 Salırça: Hindustan
🌏 Xakastap: Îndîya
🌏 Altaylap: İndiya
🌏 Şor: İndiya
🌍 Urumça: İndiya
🌍 Karajče: Hindistan
🌍 Qrımçahça: İndistan
🌏 Soyot: Enedheg, Îndîya
🌏 Tofalap: Îndîya
In Hindi: Bhārat''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индиец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хинди" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hind" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hindi" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hintler" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hınd" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hınt" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hındı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "indians" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ındıans" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индийка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индус" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индуист" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hindistanlı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hındıstanlı" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hindistanli" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hındıstanli" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "indus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hindus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hindu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хинду" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "инду" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hindoo" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hinduist" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "induist":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): enät, hindi (hindu)
🇬🇧 English: I. Indian II. Hindu
🇷🇺 Русский: I. индиец, индус II. индуист, индус
🇹🇷 Türkçe: I. Hint, Hindistanlı II. Hindu 
🇦🇿 Türkcə: I. hind, hindistanlı, hindi, hindli II. hindu
🇹🇲 Türkmençe: I. hindi II. indus, induizmiň tarapdary
🇺🇿 Oʻzbekcha: I. hindi, hindi II. hindu
🇰🇿 Qazaqşa: I. ündi, ündistandıq II. ündi, ündis
🇰🇬 Qırğızça: I. indiyalıq, indi, indus II. induist, indus
🌏 Uyghurche: I. Hindistanliq, Hindi II. Hindu, Hindi
🌍 Tatarça: hind, hindi
🌍 Başqortsa: I. hind II. induist
🌍 Çovaşla:	I. İndi ~ II. indus
🌍 Qaraqalpaqsha: I. hindistanlı II. indus, induist
🌍 Qırımtatarca: I. indistanlı, ind II. induist
🌍 Qumuqça:	I. hindistanlı, hind, muntali {archaism} II. indus, induist
🌍 Qaraçay-Malqar: I. industanlı II. indus, induist	
🌍 Noğayşa: I. indiy II. induist
🌏 Sıbırca: I. intiy II. induist
🌍 Gagauzça: I. hint II. induist
🌏 Saqalī: ündǖs
🌏 Dulgan-Hakalī: ündǖs
🌏 Tıvalap: I. indiy II. induist
🌏 Salırça: hindu
🌏 Xakastap: I. îndîyets, îndus II. înduîst, îndus
🌏 Altaylap: I. indiyets, indus II. induist, indus
🌏 Şor: I. indiyets, indus II. induist, indus
🌍 Urumça: indus
🌍 Karajče: I. hint, hindistanly II. Hindu 
🌍 Qrımçahça: I. indistanlı, ind II. induist
🌏 Soyot: I. îndîyets, îndus II. înduîst, îndus
🌏 Tofalap: I. îndîyets, îndus II. înduîst, îndus''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hinduism" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hinduizm" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "induizm" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "induism" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hınduısm" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hindu dini" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ınduizm" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "индуизм" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hındu dını":
        bot.send_message(message.chat.id, '''🇬🇧 English: Hinduism
🇷🇺 Русский: индуизм [induizm]
🇹🇷 Türkçe: Hinduizm
🇦🇿 Türkcə: Hindu dini, Hinduizm
🇹🇲 Türkmençe: Induizm
🇺🇿 Oʻzbekcha: Hinduiylik
🇰🇿 Qazaqşa: İnduizm
🇰🇬 Qırğızça: İnduizm
🌏 Uyghurche: Hindu dini, Hindi dini
🌍 Tatarça: Hind dine, Hinduizm
🌍 Başqortsa: İnduizm
🌍 Çovaşla: İnduizm
🌍 Qaraqalpaqsha: Induizm
🌍 Qırımtatarca: İnduizm
🌍 Qumuqça: İnduizm
🌍 Qaraçay-Malqar: İnduizm
🌍 Noğayşa: İnduizm
🌏 Sıbırca: İnduizm
🌍 Gagauzça: İnduizm
🌏 Saqalī: İnduizm
🌏 Dulgan-Hakalī: İnduizm
🌏 Tıvalap: İnduizm
🌏 Salırça: Hindu dini
🌏 Xakastap: Înduîzm
🌏 Altaylap: İnduizm
🌏 Şor: İnduizm
🌍 Urumça: İnduizm
🌍 Karajče: Hinduizm
🌍 Qrımçahça: İnduizm
🌏 Soyot: Înduîzm
🌏 Tofalap: Înduîzm''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "италия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "италийский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "italy" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıtaly" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "italya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "itali" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıtalya" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "italiya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "italia":
        bot.send_message(message.chat.id, '''🇬🇧 English: Italy
🇷🇺 Русский: Италия [Italiya]
🇹🇷 Türkçe: İtalya
🇦🇿 Türkcə: İtaliya
🇹🇲 Türkmençe: Italiýa
🇺🇿 Oʻzbekcha: Italiya
🇰🇿 Qazaqşa: İtaliya
🇰🇬 Qırğızça: İtaliya
🌏 Uyghurche: Italiye
🌍 Tatarça: İtaliya
🌍 Başqortsa: İtaliya
🌍 Çovaşla: İtali
🌍 Qaraqalpaqsha: Italiya
🌍 Qırımtatarca: İtaliya
🌍 Qumuqça: İtaliya
🌍 Qaraçay-Malqar: İtaliya
🌍 Noğayşa: İtaliya
🌏 Sıbırca: İtaliya
🌍 Gagauzça: İtaliya
🌏 Saqalī: İtaliya
🌏 Dulgan-Hakalī: İtaliya
🌏 Tıvalap: İtaliya
🌏 Salırça: İtaliya
🌏 Xakastap: Îtalîya
🌏 Altaylap: İtaliya
🌏 Şor: İtaliya
🌍 Urumça: İtaliya
🌍 Karajče: Italija
🌍 Qrımçahça: İtaliya
🌏 Soyot: İtali, Îtalîya
🌏 Tofalap: Îtalîya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "итальянец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "итальянка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "итальянский" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "итальянское" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "итальянская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "итальянские" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "italyan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "italian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıtalyan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıtalyan":
        bot.send_message(message.chat.id, '''🇬🇧 English: Italian
🇷🇺 Русский: I. итальянец, итальянка II. итальянский
🇹🇷 Türkçe: İtalyan, İtalyalı, dalyan {archaism}
🇦🇿 Türkcə: italyan, italiyalı
🇹🇲 Türkmençe: italýan
🇺🇿 Oʻzbekcha: italyan, italiyali
🇰🇿 Qazaqşa: I. italiyalıq II. italiyan
🇰🇬 Qırğızça: italyan
🌏 Uyghurche: Italyan
🌍 Tatarça: italyan
🌍 Başqortsa: italyan
🌍 Çovaşla: ital, italyan
🌍 Qaraqalpaqsha: italyan
🌍 Qırımtatarca: italyan, italiyalı
🌍 Qumuqça: italyan, italiyalı
🌍 Qaraçay-Malqar: italik, italyan, italiyaçı
🌍 Noğayşa: italyan, italiyalı
🌏 Sıbırca: italyan
🌍 Gagauzça: italyan
🌏 Saqalī: italyan
🌏 Dulgan-Hakalī: italyan
🌏 Tıvalap: itali, italyan
🌏 Salırça: italyan
🌏 Xakastap: îtalyan
🌏 Altaylap: italyan
🌏 Şor: italyan
🌍 Urumça: italyan
🌍 Karajče: italjan
🌍 Qrımçahça: italyan, italiyalı
🌏 Soyot: itali, îtalyan
🌏 Tofalap: îtalyan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кореец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кореянка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "корей" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "korean" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "koreli" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "korelı":
        bot.send_message(message.chat.id, '''🇬🇧 English: Korean
🇷🇺 Русский: кореец [koreyets], кореянка [koreyanka]
🇹🇷 Türkçe: Koreli
🇦🇿 Türkcə: koreyalı, koreist {dial.}
🇹🇲 Türkmençe: koreý
🇺🇿 Oʻzbekcha: koreys
🇰🇿 Qazaqşa: korey, käris
🇰🇬 Qırğızça: korey
🌏 Uyghurche: Chawshenlik
🌍 Tatarça: koreyalı, korey
🌍 Başqortsa: korey
🌍 Çovaşla: korey
🌍 Qaraqalpaqsha: koreyalı
🌍 Qırımtatarca: koreyalı, korey
🌍 Qumuqça: koreyalı, korey
🌍 Qaraçay-Malqar: koreyli
🌍 Noğayşa: korey
🌏 Sıbırca: äñgük, cösän {North Korean}
🌍 Gagauzça: koreyalı
🌏 Saqalī: keriey
🌏 Dulgan-Hakalī: keriey
🌏 Tıvalap: körey
🌏 Salırça: Çavşanzu (Çaoşanzu)
🌏 Xakastap: koreyets
🌏 Altaylap: korey
🌏 Şor: korey
🌍 Urumça: koreyalı, korey
🌍 Karajče: Korėjaly
🌍 Qrımçahça: koreyalı, korey
🌏 Soyot: solongos, korey
🌏 Tofalap: korey''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "корея" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "корейский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "корейская" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "корейское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "корейские" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kore" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "korea" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "corea" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "koreya":
        bot.send_message(message.chat.id, '''🇬🇧 English: Korea
🇷🇺 Русский: Корея [Koreya]
🇹🇷 Türkçe: Kore
🇦🇿 Türkcə: Koreya
🇹🇲 Türkmençe: Koreýa
🇺🇿 Oʻzbekcha: Koreya
🇰🇿 Qazaqşa: Koreya
🇰🇬 Qırğızça: Koreya
🌏 Uyghurche: Koriye (Koréye) {South Korea}, Chawshen {North Korea}
🌍 Tatarça: Koreya
🌍 Başqortsa: Koreya
🌍 Çovaşla: Korey
🌍 Qaraqalpaqsha: Koreya
🌍 Qırımtatarca: Koreya
🌍 Qumuqça: Koreya
🌍 Qaraçay-Malqar: Korey
🌍 Noğayşa: Koreya
🌏 Sıbırca: Äñgük, Cösän {North Korea}
🌍 Gagauzça: Koreya
🌏 Saqalī: Kerieye (Keriey)
🌏 Dulgan-Hakalī: Kerieye (Keriey)
🌏 Tıvalap: Körey
🌏 Salırça: Çavşan (Çaoşan)
🌏 Xakastap: Koreya
🌏 Altaylap: Koreya
🌏 Şor: Koreya
🌍 Urumça: Koreya
🌍 Karajče: Korėja
🌍 Qrımçahça: Koreya
🌏 Soyot: Solongos, Koreya
🌏 Tofalap: Koreya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "australia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "australıa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "avstraliya" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "awstraliya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "австралия" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "avusturalya" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "avusturaliya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "astraliya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "австралийский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "австралийская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "астралия":
        bot.send_message(message.chat.id, '''🇬🇧 English: Australia
🇷🇺 Русский: Австралия [Avstraliya]
🇹🇷 Türkçe: Avustralya
🇦🇿 Türkcə: Avstraliya, Astraliya {archaism}, Huland-Cədid {archaism}
🇹🇲 Türkmençe: Awstralyýa
🇺🇿 Oʻzbekcha: Avstraliya
🇰🇿 Qazaqşa: Avstraliya, Awıstral {arch.}
🇰🇬 Qırğızça: Avstraliya
🌏 Uyghurche: Awstraliye
🌍 Tatarça: Awstraliya
🌍 Başqortsa: Avstraliya
🌍 Çovaşla: Avstrali
🌍 Qaraqalpaqsha: Avstraliya
🌍 Qırımtatarca: Avstraliya
🌍 Qumuqça: Avstraliya
🌍 Qaraçay-Malqar: Avstraliya
🌍 Noğayşa: Avstraliya
🌏 Sıbırca: Awstraliya
🌍 Gagauzça: Avstraliya
🌏 Saqalī: Awstraliya
🌏 Dulgan-Hakalī: Avstraliya
🌏 Tıvalap: Avstraliya
🌏 Salırça: Avstraliya, Aodaliya
🌏 Xakastap: Avstralîya
🌏 Altaylap: Avstraliya
🌏 Şor: Avstraliya
🌍 Urumça: Avstraliya
🌍 Karajče: Australija
🌍 Qrımçahça: Avstraliya
🌏 Soyot: Avstrali, Avstralîya
🌏 Tofalap: Avstralîya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "australian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "australıan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "avstraliyan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "awstraliyan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "австралиец" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "avusturalyalı" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "avusturalyali" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "австралийка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "астралиец":
        bot.send_message(message.chat.id, '''🇬🇧 English: Australian
🇷🇺 Русский: австралиец [avstraliyets]
🇹🇷 Türkçe: Avustralyalı
🇦🇿 Türkcə: avstraliyalı
🇹🇲 Türkmençe: awstralyýaly
🇺🇿 Oʻzbekcha: avstraliyali
🇰🇿 Qazaqşa: awstraliyalıq
🇰🇬 Qırğızça: avstraliyalıq
🌏 Uyghurche: Awstraliyiliq
🌍 Tatarça: awstraliyalı
🌍 Başqortsa: avstraliyalı
🌍 Çovaşla: avstral
🌍 Qaraqalpaqsha: avstraliyalı
🌍 Qırımtatarca: avstraliyalı
🌍 Qumuqça: avstraliyalı
🌍 Qaraçay-Malqar: avstraliyalı
🌍 Noğayşa: avstraliyalı
🌏 Sıbırca: awstraliyalı
🌍 Gagauzça: avstraliyalı
🌏 Saqalī: avstraliyets
🌏 Dulgan-Hakalī: avstraliyets
🌏 Tıvalap: avstrali
🌏 Salırça: avstraliyalı
🌏 Xakastap: avstralîyets
🌏 Altaylap: avstraliyets
🌏 Şor: avstraliyets
🌍 Urumça: avstraliyalı
🌍 Karajče: australijaly
🌍 Qrımçahça: avstraliyalı
🌏 Soyot: avstralîyets
🌏 Tofalap: avstralîyets''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "для" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ради" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "for" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "для " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıçın" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "için":
        bot.send_message(message.chat.id, '''🇬🇧 These words are not used in all cases (eg. "For the God" – "Allah aşkına", "I have a gift for you – Sizə hədiyyəm var" etc.)
🇷🇺 Этот перевод используется не во всех случаях (напр. "Ради меня – mənim xətrimə", "таблетки для роста – boy dərmanı" и т.д.)

🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰇𐰲𐰇𐰤 (𐰇𐰲𐰤 , 𐰇𐰲𐰃𐰤)
🐺 Old Turkic (bef. 13th c.): üçün
🇬🇧 English: for
🇷🇺 Русский: для, ради
🇹🇷 Türkçe: için
🇦🇿 Türkcə: üçün, ötrü (ötəri)
🇹🇲 Türkmençe: üçin
🇺🇿 Oʻzbekcha: uchun
🇰🇿 Qazaqşa: üşin
🇰🇬 Qırğızça: üçün
🌏 Uyghurche: üchün
🌍 Tatarça: öçen
🌍 Başqortsa: ösön
🌍 Çovaşla: -şon/-şön, valli
🌍 Qaraqalpaqsha: ushın
🌍 Qırımtatarca: içün
🌍 Qumuqça: uçun
🌍 Qaraçay-Malqar: üçün
🌍 Noğayşa: üşin
🌏 Sıbırca: öcön
🌍 Gagauzça: için, deyni
🌏 Saqalī: ihin
🌏 Dulgan-Hakalī: ihin
🌏 Tıvalap: ujun, deeş
🌏 Salırça: için (üçün), volı (vulı)
🌏 Xakastap: üçün
🌏 Altaylap: uçun
🌏 Şor: üçün
🌍 Urumça: üçün (için, içün)
🌍 Karajče: üčiuń (učun, icin, ičiń)
🌍 Qrımçahça: içun
🌏 Soyot: tölädä
🌏 Tofalap: dääş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киргизия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киргистан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киргизстанский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кыргызстанский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киргизстан" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кыргызстан " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кыргыстан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kırgızıstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kırgızistan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kirgizistan " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kirghizia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kirgizia" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kyrghyzstan " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kirgizstan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kyrgystan":
        bot.send_message(message.chat.id, '''🇬🇧 English: Kyrgyzstan
🇷🇺 Русский: Кыргызстан [Kyrgyzstan]
🇹🇷 Türkçe: Kırgızistan
🇦🇿 Türkcə: Qırğızıstan
🇹🇲 Türkmençe: Gyrgyzystan
🇺🇿 Oʻzbekcha: Qirgʻiziston
🇰🇿 Qazaqşa: Qırğızstan
🇰🇬 Qırğızça: Qırğızstan
🌏 Uyghurche: Qirghizistan
🌍 Tatarça: Qırğızstan
🌍 Başqortsa: Qırğıðstan
🌍 Çovaşla: Korkosstan
🌍 Qaraqalpaqsha: Qırǵızstan
🌍 Qırımtatarca: Qırğızistan
🌍 Qumuqça: Qırğızstan
🌍 Qaraçay-Malqar: Qırğızstan	
🌍 Noğayşa: Qırğızstan
🌏 Sıbırca: Qırğıstan
🌍 Gagauzça: Kırgızistan
🌏 Saqalī: Kırgıstān
🌏 Dulgan-Hakalī: Kırgıstān
🌏 Tıvalap: Kırgıstan
🌏 Salırça: Kırkızıstan
🌏 Xakastap: Xırğıstan
🌏 Altaylap: Qırğıstan
🌏 Şor: Qırğıstan
🌍 Urumça: Xırğızıtan
🌍 Karajče: Kyrgyzstan
🌍 Qrımçahça: Qırğızıstan
🌏 Soyot: Hirgis ulıs, Kırgızstan
🌏 Tofalap: Kırgızstan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kyrgyz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kyrghyz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kirghiz" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kirgiz " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kırgız" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kırğız" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кыргыз" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киргиз" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киргизка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киргизский" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киргизская " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киргизское" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "киргизские":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): qırqız
🇬🇧 English: Kyrgyz (Kyrghyz, Kirghiz)
🇷🇺 Русский: кыргыз [kyrgyz]
🇹🇷 Türkçe: Kırgız
🇦🇿 Türkcə: qırğız
🇹🇲 Türkmençe: gyrgyz
🇺🇿 Oʻzbekcha: qirgʻiz
🇰🇿 Qazaqşa: qırğız
🇰🇬 Qırğızça: qırğız
🌏 Uyghurche: Qirghiz
🌍 Tatarça: qırğız
🌍 Başqortsa: qırğıð
🌍 Çovaşla: korkos
🌍 Qaraqalpaqsha: qırǵız
🌍 Qırımtatarca: qırğız
🌍 Qumuqça: qırğız
🌍 Qaraçay-Malqar: qırğız
🌍 Noğayşa: qırğız
🌏 Sıbırca: qırğıs
🌍 Gagauzça: kırgız
🌏 Saqalī: kırgīs
🌏 Dulgan-Hakalī: kırgīs
🌏 Tıvalap: kırgıs
🌏 Salırça: kırkız
🌏 Xakastap: xırğıs
🌏 Altaylap: qırğıs
🌏 Şor: qırğıs
🌍 Urumça: xırğız
🌍 Karajče: kyrgyz
🌍 Qrımçahça: qırğız
🌏 Soyot: hirgis, kırgız
🌏 Tofalap: kırgız''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cehennem" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tamu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tamı" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "damu " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tamuk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dûzah" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ад" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "адский " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hell" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gehenna" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gehennom " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "геенна" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "inferno" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "преисподняя " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "duzah" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "netherworld" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cahennem":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.):	tamu (tamuğ)
🇬🇧 English: hell, gehenna
🇷🇺 Русский: ад [ad], геенна [geyenna]
🇹🇷 Türkçe: cehennem, tamu, dûzah {arch.}
🇦🇿 Türkcə: cəhənnəm, damı {dial.}, duzəx {arch.}
🇹🇲 Türkmençe: jähennem, dowzah
🇺🇿 Oʻzbekcha: jahannam, doʻzax
🇰🇿 Qazaqşa: tozaq, jahannam, tamuq
🇰🇬 Qırğızça: tozoq, jaannam
🌏 Uyghurche: jehennem, dozaq (dozax), tamuq
🌍 Tatarça: cähännäm, tamuq
🌍 Başqortsa: yähännäm, tamuq
🌍 Çovaşla: tamok
🌍 Qaraqalpaqsha: jáhánnem, dozaq
🌍 Qırımtatarca: ceennem
🌍 Qumuqça: cahannem
🌍 Qaraçay-Malqar: jahanim
🌍 Noğayşa: yahanem
🌏 Sıbırca: yännäm (yäntäm), tämük
🌍 Gagauzça: cendem
🌏 Saqalī: üöden, allarāñı doydu, nes tüerd ütügen {arch.}
🌏 Dulgan-Hakalī: annıkī doydu
🌏 Tıvalap: tamı, Erlik oranı
🌏 Salırça: cöhännäm, dozax
🌏 Xakastap: çîr altı
🌏 Altaylap: taamı, alıs cer, qıyın cer
🌏 Şor: ???
🌍 Urumça: ceennem (cännäm, cäynäm)
🌍 Karajče: džehinnem
🌍 Qrımçahça: cehınem
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "америка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пиндостан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "amerika" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "america " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "amerıca" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "amerıka" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "американский" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "американское " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "американская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "американские":
        bot.send_message(message.chat.id, '''🇬🇧 English: America
🇷🇺 Русский: Америка [Amerika]
🇹🇷 Türkçe: Amerika, Yeni Dünya {arch.}
🇦🇿 Türkcə: Amerika, Amerqa {arch.}, Yeni Dünya {arch.}
🇹🇲 Türkmençe: Amerika, Amryka {arch.}
🇺🇿 Oʻzbekcha: Amerika
🇰🇿 Qazaqşa: Amerika, Ämerik {arch.}
🇰🇬 Qırğızça: Amerika
🌏 Uyghurche: Amérika
🌍 Tatarça: Amerika
🌍 Başqortsa: Amerika
🌍 Çovaşla: Amerika
🌍 Qaraqalpaqsha: Amerika
🌍 Qırımtatarca: Amerika, Ameriqa {arch.}
🌍 Qumuqça: Amerika
🌍 Qaraçay-Malqar: Amerika
🌍 Noğayşa: Amerika
🌏 Sıbırca: Amerika
🌍 Gagauzça: Amerika
🌏 Saqalī: Amerika, Emierike (Emerik) {arch.}
🌏 Dulgan-Hakalī: Amerika
🌏 Tıvalap: Amerika
🌏 Salırça: Amerka
🌏 Xakastap: Amerîka
🌏 Altaylap: Amerika
🌏 Şor: Amerika
🌍 Urumça: Amerika
🌍 Karajče: Ameryka (Amerika)
🌍 Qrımçahça: Amerika
🌏 Soyot: Amerikê, Amerîka
🌏 Tofalap: Amerîka''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "американец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пиндос" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "amerikan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "american " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "amerıcan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "amerıkan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "amerikalı" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "amerikali " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "amerıkalı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "американка":
        bot.send_message(message.chat.id, '''🇬🇧 English: American
🇷🇺 Русский: американец
🇹🇷 Türkçe: Amerikan, Amerikalı, Yeni Dünyalı {arch.}
🇦🇿 Türkcə: amerikan, amerikalı
🇹🇲 Türkmençe: amerikan, amerikaly, amrykaly {arch.}
🇺🇿 Oʻzbekcha: amerikalik
🇰🇿 Qazaqşa: amerikan, amerikalıq, amerikandıq
🇰🇬 Qırğızça: amerikalıq
🌏 Uyghurche: Amérikan, Amérikiliq
🌍 Tatarça: amerikalı
🌍 Başqortsa: amerikalı
🌍 Çovaşla: morikkan (mörikan)
🌍 Qaraqalpaqsha: amerikan
🌍 Qırımtatarca: amerikalı, ameriqalu {arch.}
🌍 Qumuqça: amerikan, amerikalı
🌍 Qaraçay-Malqar: amerikan, amerikanlı, amerikaçı
🌍 Noğayşa: amerikan
🌏 Sıbırca: amerikalı
🌍 Gagauzça: amerikalı
🌏 Saqalī: amerikan, emieriken (emerikēn) {arch.}
🌏 Dulgan-Hakalī: amerikan
🌏 Tıvalap: amerik, amerikan
🌏 Salırça: amerkan
🌏 Xakastap: amerîkan
🌏 Altaylap: amerikan
🌏 Şor: amerikan
🌍 Urumça: amerikan, amerikalı
🌍 Karajče: amerikaly
🌍 Qrımçahça: amerikalı
🌏 Soyot: amerîkan
🌏 Tofalap: amerîkan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "снег" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сноу" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "snow" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "снежный " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "снежная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "снежное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "снежные" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qar " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sneg":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰺
🐺 Old Turkic (bef. 13th c.): qar
🇬🇧 English: snow
🇷🇺 Русский: снег
🇹🇷 Türkçe: kar
🇦🇿 Türkcə: qar
🇹🇲 Türkmençe: gar
🇺🇿 Oʻzbekcha: qor
🇰🇿 Qazaqşa: qar
🇰🇬 Qırğızça: qar
🌏 Uyghurche: qar
🌍 Tatarça: qar
🌍 Başqortsa: qar
🌍 Çovaşla: yur
🌍 Qaraqalpaqsha: qar
🌍 Qırımtatarca: qar
🌍 Qumuqça: qar
🌍 Qaraçay-Malqar: qar
🌍 Noğayşa: qar
🌏 Sıbırca: qar
🌍 Gagauzça: kaar
🌏 Saqalī: qaar
🌏 Dulgan-Hakalī: kaar
🌏 Tıvalap: xar
🌏 Salırça: qar (kar)
🌏 Xakastap: xar
🌏 Altaylap: qar
🌏 Şor: qar
🌍 Urumça: xar (ğar)
🌍 Karajče: kar
🌍 Qrımçahça: qar
🌏 Soyot: qar
🌏 Tofalap: qar''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дочь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "доча" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дочка" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дочерний" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "девушка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "девчачий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "девочка" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дефчачий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "girl" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "girlish" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "девченка" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "девчонка" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kız" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kiz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "daughter":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰶𐰃𐰔
🐺 Old Turkic (bef. 13th c.): qız (xız)
🇬🇧 English: girl, daughter
🇷🇺 Русский: девушка, девочка, дочь
🇹🇷 Türkçe: kız
🇦🇿 Türkcə: qız
🇹🇲 Türkmençe: gyz
🇺🇿 Oʻzbekcha: qiz
🇰🇿 Qazaqşa: qız
🇰🇬 Qırğızça: qız
🌏 Uyghurche: qiz
🌍 Tatarça: qız
🌍 Başqortsa: qıð
🌍 Çovaşla: xör
🌍 Qaraqalpaqsha: qız
🌍 Qırımtatarca: qız
🌍 Qumuqça: qız
🌍 Qaraçay-Malqar: qız
🌍 Noğayşa: qız
🌏 Sıbırca: qıs
🌍 Gagauzça: kız
🌏 Saqalī: kīs
🌏 Dulgan-Hakalī: kīs
🌏 Tıvalap: kıs
🌏 Salırça: qız
🌏 Xakastap: xıs
🌏 Altaylap: qıs
🌏 Şor: qıs
🌍 Urumça: xız (ğız)
🌍 Karajče: kyz
🌍 Qrımçahça: qız
🌏 Soyot: qıs
🌏 Tofalap: qıs''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dudu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dudu kuşu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dudukuşu" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dudukuş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dudu kuş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tutu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "papağan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "popugay" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "papagay" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "parrot" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "a parrot" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "попугай" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "попугайчик" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "papagan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "papuga":
        bot.send_message(message.chat.id, '''🇬🇧 English: parrot
🇷🇺 Русский: попугай [popugay]
🇲🇳 Mongol: toti
🇹🇷 Türkçe: papağan, dudu, dudukuşu
🇦🇿 Türkcə: tutu, tutuquşu
🇹🇲 Türkmençe: toty, totyguş
🇺🇿 Oʻzbekcha: toʻti, toʻtiqush
🇰🇿 Qazaqşa: totı, totıqus
🇰🇬 Qırğızça: totu, totu quş
🌏 Uyghurche: totiqush, shatuti (shatoti)
🌍 Tatarça: tutıy, tutıy qoş
🌍 Başqortsa: tutıyğoş
🌍 Çovaşla: popugay
🌍 Qaraqalpaqsha: totı, totı qus
🌍 Qırımtatarca: papağan, dudu quş, tütü quş
🌍 Qumuqça: papağan
🌍 Qaraçay-Malqar: popugay
🌍 Noğayşa: popugay
🌏 Sıbırca: tutıy qoş
🌍 Gagauzça: papagal (papagan)
🌏 Saqalī: popugay
🌏 Dulgan-Hakalī: popugay
🌏 Tıvalap: doydu
🌏 Salırça: tudi
🌏 Xakastap: popugay
🌏 Altaylap: popugay
🌏 Şor: popugay
🌍 Urumça: papugay
🌍 Karajče: papahan
🌍 Qrımçahça: papağan
🌏 Soyot: toti
🌏 Tofalap: popugay''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sverige" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sveden" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "isvec" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ısvec" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "isveç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ısveç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "işveç" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "işves" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "швеция" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "schvetsiya":
        bot.send_message(message.chat.id, '''🇬🇧 English: Sweden
🇷🇺 Русский: Швеция [Shvetsiya]
🇹🇷 Türkçe: İsveç
🇦🇿 Türkcə: İsveç, İşves {dial.}, Svid {arch.}
🇹🇲 Türkmençe: Şwesiýa, Iswiç {arch.}
🇺🇿 Oʻzbekcha: Shvetsiya
🇰🇿 Qazaqşa: Şvesiya
🇰🇬 Qırğızça: Şvetsiya
🌏 Uyghurche: Shwétsiye
🌍 Tatarça: Eswäc, Şvetsiä
🌍 Başqortsa: Şvetsiya
🌍 Çovaşla: Şvetsi
🌍 Qaraqalpaqsha: Shvetsiya
🌍 Qırımtatarca: İsveç
🌍 Qumuqça: Şvetsiya
🌍 Qaraçay-Malqar: Şvetsiya
🌍 Noğayşa: Şvetsiya
🌏 Sıbırca: Şveciä
🌍 Gagauzça: Şvețiya
🌏 Saqalī: Şvetsiya
🌏 Dulgan-Hakalī: Şvetsiya
🌏 Tıvalap: Şved
🌏 Salırça:	Sveden, İsveç, Ruydien
🌏 Xakastap: Şvetsîya
🌏 Altaylap: Şvetsiya
🌏 Şor: Şvetsiya
🌍 Urumça: İsveç
🌍 Karajče: Švedija
🌍 Qrımçahça: İsveç
🌏 Soyot: Şvesi, Şvetsîya
🌏 Tofalap: Şvetsîya
In Swedish: Sverige''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "швед" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шведка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "isvecli" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ısveclı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "isveçli" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ısveçlı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "işveçli" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шведский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шведское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шведская" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шведские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "swedish" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "swede":
        bot.send_message(message.chat.id, '''🇬🇧 English: Swede, Swedish
🇷🇺 Русский: швед [shved], шведка, шведский
🇹🇷 Türkçe: İsveç, İsveçli
🇦🇿 Türkcə: isveç, isveçli
🇹🇲 Türkmençe: şwed, iswiç {arch.}
🇺🇿 Oʻzbekcha: shved
🇰🇿 Qazaqşa: şved, şvesiyalıq
🇰🇬 Qırğızça: şved
🌏 Uyghurche: Shwéd
🌍 Tatarça: şved
🌍 Başqortsa: şved
🌍 Çovaşla: şved
🌍 Qaraqalpaqsha: shved
🌍 Qırımtatarca: isveç, isveçli
🌍 Qumuqça: şved
🌍 Qaraçay-Malqar: şved
🌍 Noğayşa: şved
🌏 Sıbırca: şved
🌍 Gagauzça: şved
🌏 Saqalī: şved
🌏 Dulgan-Hakalī: şved
🌏 Tıvalap: şved
🌏 Salırça: sveden, isveç, Ruydien kişi
🌏 Xakastap: şved
🌏 Altaylap: şved
🌏 Şor: şved
🌍 Urumça: isveç, isveçli
🌍 Karajče: šved
🌍 Qrımçahça: isveç, isveçlı
🌏 Soyot: şved
🌏 Tofalap: şved''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мирный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "смирный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "спокойный" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "спокойная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мирное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "спокойно" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "calm" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sakin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uslu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мирная" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мирные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "спокойное" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "спокойные":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): nirvanlığ, amıl (amul), eräjlıg, inç, örüg
🇬🇧 English: calm {adj.}
🇷🇺 Русский: спокойный
🇹🇷 Türkçe: sakin, uslu, dinç (dınç) {arch.}
🇦🇿 Türkcə: dinc, sakit, diş {dial.}
🇹🇲 Türkmençe: dynç
🇺🇿 Oʻzbekcha: tinch
🇰🇿 Qazaqşa: tınış, tınıq
🇰🇬 Qırğızça: tınç
🌏 Uyghurche: tinch (tinich)
🌍 Tatarça: tınıç
🌍 Başqortsa: tınıs
🌍 Çovaşla: tonoc
🌍 Qaraqalpaqsha: tınısh
🌍 Qırımtatarca: tınç
🌍 Qumuqça: tınış
🌍 Qaraçay-Malqar: tınç
🌍 Noğayşa: tınış
🌏 Sıbırca: tınıc
🌍 Gagauzça: uslu, raat, sulhen
🌏 Saqalī: qolku, çūmpu
🌏 Dulgan-Hakalī: hımnagas, hügün
🌏 Tıvalap: dış, oojum, amır
🌏 Salırça: ağır, emonçüx
🌏 Xakastap: amır
🌏 Altaylap: tımıq, amır
🌏 Şor: abır
🌍 Urumça: tınç (tınış), arxein, ağır (avur), tınıx, raat
🌍 Karajče: tynč (tynys)
🌍 Qrımçahça: tınç (tınış), tınıh, raat
🌏 Soyot: tış (dış), amır, dölgään, caaş (çaaş), taybın
🌏 Tofalap: tış (dış), çaaş, çadığ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "palestine" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "palestin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "palestina" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "палестина" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "палестинский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "палестинская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "палестинское" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "палестинские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "филистия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пелешет" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "filistin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "filistia" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "peleset":
        bot.send_message(message.chat.id, '''🇬🇧 English: Palestine
🇷🇺 Русский: Палестина [Palestina]
🇹🇷 Türkçe: Filistin
🇦🇿 Türkcə: Fələstin
🇹🇲 Türkmençe: Pelestin
🇺🇿 Oʻzbekcha: Falastin
🇰🇿 Qazaqşa: Palestina, Pälestin {KazakGrammar}
🇰🇬 Qırğızça: Palestina
🌏 Uyghurche: Pelestin
🌍 Tatarça: Fälistin
🌍 Başqortsa: Fälästin
🌍 Çovaşla: Palestina
🌍 Qaraqalpaqsha: Palestina
🌍 Qırımtatarca: Filistin
🌍 Qumuqça: Palestina
🌍 Qaraçay-Malqar: Filistin, Palestina
🌍 Noğayşa: Palestina
🌏 Sıbırca: Pälästin
🌍 Gagauzça: Filistin, Palestina
🌏 Saqalī: Palestina
🌏 Dulgan-Hakalī: Palestina
🌏 Tıvalap: Palestin, Palestina
🌏 Salırça: Balestan
🌏 Xakastap: Palestîna
🌏 Altaylap: Palestina
🌏 Şor: Palestina
🌍 Urumça: Fälästin (Filistin)
🌍 Karajče: Pelešet
🌍 Qrımçahça: Filistin
🌏 Soyot: Palestin, Palestîna
🌏 Tofalap: Palestîna
In Arabic: Fälästıyn''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "palestinian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "палестинец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "палестинка" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "филистинец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "filistinli" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "filistian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pelestian":
        bot.send_message(message.chat.id, '''🇬🇧 English: Palestinian
🇷🇺 Русский: палестнец [palestinets], палестинка
🇹🇷 Türkçe: Filistinli
🇦🇿 Türkcə: fələstinli
🇹🇲 Türkmençe: pelestinli
🇺🇿 Oʻzbekcha: falastinlik
🇰🇿 Qazaqşa: palestinalıq, pälestindik {KazakGrammar}
🇰🇬 Qırğızça: palestinalıq
🌏 Uyghurche: pelestinlik
🌍 Tatarça: fälistin
🌍 Başqortsa: fälästin
🌍 Çovaşla: palestin
🌍 Qaraqalpaqsha: palestinalı
🌍 Qırımtatarca: filistinli
🌍 Qumuqça: palestinalı
🌍 Qaraçay-Malqar: filistinli, palestinalı
🌍 Noğayşa: palestinalı
🌏 Sıbırca: pälästinli
🌍 Gagauzça: filistinni
🌏 Saqalī: palestinets
🌏 Dulgan-Hakalī: palestinets
🌏 Tıvalap: palestin
🌏 Salırça: Balestan kişi
🌏 Xakastap: palestînets
🌏 Altaylap: palestinets
🌏 Şor: palestinets
🌍 Urumça: fälästinli (filistinli)
🌍 Karajče: pelešetli
🌍 Qrımçahça: filistinlı
🌏 Soyot: palestin, palestînets
🌏 Tofalap: palestînets''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "signature" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сигнатура" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "signatür" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sıgnatür" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "signatur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "подпись" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ımza" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "aftograf" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "avtograf" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "автограф" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "autograph" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "imza":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): tuğrağ {oghuz turkish}
🇬🇧 English: signature
🇷🇺 Русский: подпись
🇹🇷 Türkçe: imza, signatür, kol {dial.}
🇦🇿 Türkcə: imza, qol
🇹🇲 Türkmençe: gol, imza
🇺🇿 Oʻzbekcha: imzo, qoʻl
🇰🇿 Qazaqşa: qol, qoltaŋba
🇰🇬 Qırğızça: qol, qol tamğa
🌏 Uyghurche: imza, qol
🌍 Tatarça: imza, qul
🌍 Başqortsa: qultamğa, qul
🌍 Çovaşla: alo, alo pusni (alpusni), puso
🌍 Qaraqalpaqsha: qol
🌍 Qırımtatarca: imza, el {arch.}
🌍 Qumuqça: qol
🌍 Qaraçay-Malqar: qol
🌍 Noğayşa: qol
🌏 Sıbırca: qul
🌍 Gagauzça: imza
🌏 Saqalī: ilï battāhın
🌏 Dulgan-Hakalī: ilï battāhın
🌏 Tıvalap: xol
🌏 Salırça: burmax
🌏 Xakastap: xol
🌏 Altaylap: qol
🌏 Şor: qol
🌍 Urumça: elyazı (ilyazı), emza (imza)
🌍 Karajče: kol, imza
🌍 Qrımçahça: elyazı
🌏 Soyot: qol (gol, hol, ğol)
🌏 Tofalap: qol''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "thanks" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "thank u" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "thank you" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ty" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ta" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "thankee" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "спасибо" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пасиб" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пасиба" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "спасибки" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пасябки" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "спасиба" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "благодарность" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "благодарю" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "благодарствую" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "teşekkür" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "teşekkürler" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "teşekkür ederim" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çok yaşa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çokyaşa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sağol" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "takdir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sağolunuz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sağolun" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sağ ol":
        bot.send_message(message.chat.id, '''🇬🇧 English: thanks, thank you
🇷🇺 Русский: спасибо [spasibo], благодарствую
🇹🇷 Türkçe: teşekkür(ler), çok yaşa, sağ ol (sağol)
🇦🇿 Türkcə: sağ ol (sağol), təşəkkür(lər), Allah razı olsun
🇹🇲 Türkmençe: sag bol, Taňry ýalkasyn
🇺🇿 Oʻzbekcha: rahmat, tashakkur, qulluq
🇰🇿 Qazaqşa: rahmet (raqmet), Alda razı bolsın
🇰🇬 Qırğızça: ıraqmat, Teŋir jarqasın, qulduq {arch.}
🌏 Uyghurche: rexmet, teshekkür, qulluq, tazim
🌍 Tatarça: räxmät
🌍 Başqortsa: räxmät, yaqşı äle
🌍 Çovaşla: oraxmat (raxmat, örexmet, rexmet), tav, tavtapuc (tav-ta-puc), merttes {dial.}
🌍 Qaraqalpaqsha: raxmet, Táńir jarılqasın
🌍 Qırımtatarca: sağol (sağ ol), teşekkür(ler), Alla razı olsun
🌍 Qumuqça: sawbol
🌍 Qaraçay-Malqar: saw bol
🌍 Noğayşa: saw bol (sawbol), raxmet
🌏 Sıbırca: räqmät, märtäs, qolloq
🌍 Gagauzça: saa ol, teşekür, evallaa, Allaa rozolsun, şükür ederim
🌏 Saqalī: maqtanabın, maqtal, maqtalla tut, ayaqallā {arch.}
🌏 Dulgan-Hakalī: pasība
🌏 Tıvalap: çettirdim
🌏 Salırça: eŋgexci (eŋkece), raxmet
🌏 Xakastap: alğıs, alğıstapçam
🌏 Altaylap: baş bolzın, bıyan (~ bolzın), alqış (~ bolzın)
🌏 Şor: alğış polzun
🌍 Urumça: sağ ol (sav bol), ramet (rahmet), çox yaşa, Allarazosun (Alla razı olsun), avuzuña bal bolsun, evalla
🌍 Karajče: tabu (tabuv, tabe), tabuv ėteim (tabu ėtiam), sav bol
🌍 Qrımçahça: Alla razı olsın
🌏 Soyot: hayn daa, spasîbo
🌏 Tofalap: spasîbo''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "никой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "никоим" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ни" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вовсе" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вовсе не" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "совсем" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "совсем не" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "совершенно не" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "даже не" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "at all" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "not at all" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вообще не" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вобще не" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hiç" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hıç":
        bot.send_message(message.chat.id, '''🇬🇧 In most cases, {da (ta, daa) / de (te, dee) + negative} is used (eg "bir kişi de gelmedi" - "nobody came"). And the word "hiç" and all its cognates are borrowed from Farsi.
🇷🇺 В большинстве случаев используется связка {da (ta, daa) / de(te, dee) + отрицание} для усиления, можно добавить слово bir ("один") в начало предложения (напр. bir kişi de gelmedi – никто не пришёл). А само слово "hiç" и все его когнаты являются заимствованием из фарси.
🇹🇷 Çoğu durumda, {da (ta, daa) / de (te, dee) + olumsuzluk} kullanılır (örneğin, "kişi de gelmedi" - "hiç kimse gelmedi"). Ve "hiç" kelimesi ve bütün ona benzer sözler Farsça'dan alınmadır.

🇬🇧 English: no~ (nobody, never etc), at all (not at all)
🇷🇺 Русский: ни~ (нисколько, никогда, никто и т.д.) [ni], совершенно не, совсем не, вовсе не, даже не
🇹🇷 Türkçe: hiç
🇦🇿 Türkcə: heç
🇹🇲 Türkmençe: hiç
🇺🇿 Oʻzbekcha: hech
🇰🇿 Qazaqşa: eş
🇰🇬 Qırğızça: eç
🌏 Uyghurche: héch
🌍 Tatarça: hiç
🌍 Başqortsa: his
🌍 Çovaşla: ni
🌍 Qaraqalpaqsha: hesh
🌍 Qırımtatarca: iç
🌍 Qumuqça: heç
🌍 Qaraçay-Malqar: çırt
🌍 Noğayşa: eş
🌏 Sıbırca: ic
🌍 Gagauzça: hiç
🌏 Saqalī: {see note}
🌏 Dulgan-Hakalī: {see note}
🌏 Tıvalap: {see note}
🌏 Salırça: heme, heş-meş
🌏 Xakastap: çir, pir dee
🌏 Altaylap: eş
🌏 Şor: pir-da
🌍 Urumça: eç
🌍 Karajče: hieč
🌍 Qrımçahça: iç
🌏 Soyot: {see note}
🌏 Tofalap: {see note}''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дания" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "danmark" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "denmark" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "danimarka" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "danımarka" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "danimark" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "daniya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dania":
        bot.send_message(message.chat.id, '''🇬🇧 English: Denmark
🇷🇺 Русский: Дания [Daniya]
🇹🇷 Türkçe: Danimarka
🇦🇿 Türkcə: Danimarka, Danmarqa {arch.}
🇹🇲 Türkmençe: Daniýa
🇺🇿 Oʻzbekcha: Daniya
🇰🇿 Qazaqşa: Daniya
🇰🇬 Qırğızça: Daniya
🌏 Uyghurche: Daniye
🌍 Tatarça: Daniya
🌍 Başqortsa: Daniya
🌍 Çovaşla: Dani
🌍 Qaraqalpaqsha: Daniya
🌍 Qırımtatarca: Danimarka, Danimarqa {arch.}
🌍 Qumuqça: Daniya
🌍 Qaraçay-Malqar: Daniya
🌍 Noğayşa: Daniya
🌏 Sıbırca: Daniya
🌍 Gagauzça: Daniya
🌏 Saqalī: Daniya
🌏 Dulgan-Hakalī: Daniya
🌏 Tıvalap: Dani, Daniya
🌏 Salırça: Danmay
🌏 Xakastap: Danîya
🌏 Altaylap: Daniya
🌏 Şor: Daniya
🌍 Urumça: Daniya
🌍 Karajče: Danija
🌍 Qrımçahça: Danimarka
🌏 Soyot: Dani, Danîya
🌏 Tofalap: Danîya
In Danish: Danmark''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "датчанин" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "датчанка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "данский" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "данск" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "данское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "датские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "датский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "датская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "датское" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "danish" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "danimarkalı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "danimarkali" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "danımarkalı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dane":
        bot.send_message(message.chat.id, '''🇬🇧 English: Dane, Danish
🇷🇺 Русский: датчанин [datchanin]
🇹🇷 Türkçe: dan, Danimarkalı
🇦🇿 Türkcə: dan, danimarkalı, danmarqalı {arch.}
🇹🇲 Türkmençe: dat, daniýaly
🇺🇿 Oʻzbekcha: dan
🇰🇿 Qazaqşa: dat, dattıq, daniyalıq
🇰🇬 Qırğızça: dan, daniyalıq
🌏 Uyghurche: danish, daniyiliq
🌍 Tatarça: dan, daniyalı
🌍 Başqortsa: dan, daniyalı
🌍 Çovaşla: dan
🌍 Qaraqalpaqsha: dan, daniyalı
🌍 Qırımtatarca: dan, danimarkalı, danimarqalu {arch.}
🌍 Qumuqça: dan, daniyalı
🌍 Qaraçay-Malqar: daniyalı
🌍 Noğayşa: daniyalı
🌏 Sıbırca: dan, daniyalı
🌍 Gagauzça: dan, daniyalı
🌏 Saqalī: dān
🌏 Dulgan-Hakalī: dān
🌏 Tıvalap: dani
🌏 Salırça: dan
🌏 Xakastap: datçanîn
🌏 Altaylap: datçanin
🌏 Şor: datçanin
🌍 Urumça: dan, daniyalı
🌍 Karajče: dan, danijaly
🌍 Qrımçahça: dan, danimarkalı
🌏 Soyot: dani, datçanîn
🌏 Tofalap: datçanîn''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "юг" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "южный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "южная" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "южное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "южные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "south" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "southern" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "souther" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "souht" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sauth" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "güney" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "guney":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): I. berdin, kündünki buluŋ, kün ortu II. beriyäki, kün ortudın, küntün (küntin), küntünki
🇬🇧 English: I. south II. southern
🇷🇺 Русский: I. юг II. южный
🇹🇷 Türkçe: güney
🇦🇿 Türkcə: güney {South Azerbaijani}, cənub {I. North Azerbaijani}, cənubi {II. North Azerbaijani}
🇹🇲 Türkmençe: günorta
🇺🇿 Oʻzbekcha: I. janub II. janubiy
🇰🇿 Qazaqşa: oŋtüstik, küngey
🇰🇬 Qırğızça: tüştük
🌏 Uyghurche: I. jenub II. jenubiy
🌍 Tatarça: könyaq
🌍 Başqortsa: könyaq
🌍 Çovaşla: kontor
🌍 Qaraqalpaqsha: túslik
🌍 Qırımtatarca: I. cenüp II. cenübiy
🌍 Qumuqça: qıbla
🌍 Qaraçay-Malqar: qıbıla
🌍 Noğayşa: aldı yaq, qubıla
🌏 Sıbırca: könyaq
🌍 Gagauzça: üülen, güney
🌏 Saqalī: soğurū
🌏 Dulgan-Hakalī: ǖhe
🌏 Tıvalap: murnuu
🌏 Salırça: yeliŋkut, I. cenup II. cenubi
🌏 Xakastap: I. üstünzarıx (üstinzarıx) II. üstünzarxı (üstinzarxı)
🌏 Altaylap: tüştük
🌏 Şor: I. tüjülgü II. tüjülgüyi
🌍 Urumça: xıble
🌍 Karajče: kyblie (kybla), tiušliuk (tiślik)
🌍 Qrımçahça: tüşlük
🌏 Soyot: murnuu
🌏 Tofalap: I. hüŋgääri II. hüŋgäärikîî''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восток" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восточный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восточная" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восточное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восточные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "east" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eastern" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "easter" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doğu" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şark" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şarq" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şarki":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): toğar
🇬🇧 English: I. east II. eastern
🇷🇺 Русский: I. восток II. восточный
🇹🇷 Türkçe: doğu, şark {arch.}
🇦🇿 Türkcə: doğu {South Azerbaijani}, şərq {I. North Azerbaijani}, şərqi {II. North Azerbaijani}
🇹🇲 Türkmençe: gündogar
🇺🇿 Oʻzbekcha: I. sharq II. sharqiy
🇰🇿 Qazaqşa: şığıs
🇰🇬 Qırğızça: çığış (künçığış)
🌏 Uyghurche: I. sherq II. sherqiy
🌍 Tatarça: könçığış
🌍 Başqortsa: könsığış, şäreq
🌍 Çovaşla: tuxoc (xöveltuxoc)
🌍 Qaraqalpaqsha: shıǵıs (kúnshıǵıs)
🌍 Qırımtatarca: kündoğuş (küntuvuş), meşriq, şarq {I}, şarqiy {II}
🌍 Qumuqça: güntuwuş
🌍 Qaraçay-Malqar: künçıqğan
🌍 Noğayşa: küntuwar
🌏 Sıbırca: köncığış
🌍 Gagauzça: duu, günduusu
🌏 Saqalī: ilin
🌏 Dulgan-Hakalī: küntaksī, allara
🌏 Tıvalap: çöön
🌏 Salırça: günçıxqan
🌏 Xakastap: I. isker II. iskerki
🌏 Altaylap: künçığış
🌏 Şor: I. künşığıjı II. künşığıjınıyı
🌍 Urumça: doğu (gündoğuş, gündoğu, küntovuç), anadolu, 
🌍 Karajče: kiuńtuvuš (gundohušu), kadim, mizrach
🌍 Qrımçahça: kündoğış, mizrah, meşruq
🌏 Soyot: cöön
🌏 Tofalap: I. buruŋğaarı II. buruŋğaarıkîî''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ğarp" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "garp" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "garb" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "west" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "vvest" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "western" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "запад" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "западный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "западная" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "западное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bati" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "batı":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): batar
🇬🇧 English: I. west II. western
🇷🇺 Русский: I. запад II. западный
🇹🇷 Türkçe: batı, garp {arch.}
🇦🇿 Türkcə: batı {South Azerbaijani}, qərb {I. North Azerbaijani}, qərbi {II. North Azerbaijani}
🇹🇲 Türkmençe: günbatar
🇺🇿 Oʻzbekcha: I. gʻarb II. gʻarbiy
🇰🇿 Qazaqşa: batıs
🇰🇬 Qırğızça: batış (künbatış)
🌏 Uyghurche: I. gherib II. gheribiy
🌍 Tatarça: könbatış
🌍 Başqortsa: könbayış
🌍 Çovaşla: anoc (xövelanoc)
🌍 Qaraqalpaqsha: batıs (kúnbatıs)
🌍 Qırımtatarca: künbatı, mağrip, ğarp {I}, ğarbiy {II}
🌍 Qumuqça: günbatış
🌍 Qaraçay-Malqar: künbatxan
🌍 Noğayşa: künbatar
🌏 Sıbırca: könpatıw, mağrip
🌍 Gagauzça: batı
🌏 Saqalī: arğā
🌏 Dulgan-Hakalī: küntagıs
🌏 Tıvalap: barıın
🌏 Salırça: günbatqan
🌏 Xakastap: kîder
🌏 Altaylap: künbadış
🌏 Şor: I. künqonujı II. künqonujınıyı
🌍 Urumça: batı (günbatar, künbatı), disin
🌍 Karajče: kiuńbatyš (gunbatys)
🌍 Qrımçahça: künbatış, mağrup, merab
🌏 Soyot: baruun
🌏 Tofalap: I. soŋğaarı II. soŋğaarıkîî''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "юг" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "neck" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "boyun" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "boynu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "boynı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "boyni" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шея" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шейка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шейные" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шейный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шейная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шейное":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): boyun (boyın)
🇬🇧 English: neck
🇷🇺 Русский: шея
🇹🇷 Türkçe: boyun
🇦🇿 Türkcə: boyun
🇹🇲 Türkmençe: boýun
🇺🇿 Oʻzbekcha: boʻyin
🇰🇿 Qazaqşa: moyın
🇰🇬 Qırğızça: moyun
🌏 Uyghurche: boyun
🌍 Tatarça: muyın
🌍 Başqortsa: muyın
🌍 Çovaşla: moy
🌍 Qaraqalpaqsha: moyın
🌍 Qırımtatarca: boyun
🌍 Qumuqça: boyun
🌍 Qaraçay-Malqar: boyun
🌍 Noğayşa: moyın
🌏 Sıbırca: puyın
🌍 Gagauzça: boynu (boyun)
🌏 Saqalī: mōnńu (mōy, mōyun)
🌏 Dulgan-Hakalī: muoy
🌏 Tıvalap: moyun
🌏 Salırça: boyun (boyın, poynı)
🌏 Xakastap: moyın
🌏 Altaylap: moyın
🌏 Şor: moyun
🌍 Urumça: boyun (moyun)
🌍 Karajče: bojun
🌍 Qrımçahça: boyın
🌏 Soyot: moyın
🌏 Tofalap: moên''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bulut" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "облака" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "облако" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "туча" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cloud" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тучка":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰉𐰆𐰞𐰃𐱃
🐺 Old Turkic (bef. 13th c.): bulut (bulıt)
🇬🇧 English: cloud
🇷🇺 Русский: облако, туча
🇹🇷 Türkçe: bulut
🇦🇿 Türkcə: bulud
🇹🇲 Türkmençe: bulut
🇺🇿 Oʻzbekcha: bulut
🇰🇿 Qazaqşa: bult
🇰🇬 Qırğızça: bulut
🌏 Uyghurche: bulut
🌍 Tatarça: bolıt
🌍 Başqortsa: bolot
🌍 Çovaşla: pölöt
🌍 Qaraqalpaqsha: bult
🌍 Qırımtatarca: bulut
🌍 Qumuqça: bulut
🌍 Qaraçay-Malqar: bulut
🌍 Noğayşa: bulıt
🌏 Sıbırca: polot
🌍 Gagauzça: bulut
🌏 Saqalī: bılıt
🌏 Dulgan-Hakalī: bılıt
🌏 Tıvalap: bulut
🌏 Salırça: bulut
🌏 Xakastap: pulut
🌏 Altaylap: bulut
🌏 Şor: pulut
🌍 Urumça: bulut
🌍 Karajče: bulut
🌍 Qrımçahça: bulut
🌏 Soyot: bulıt
🌏 Tofalap: bulut''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "стрела" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "arrow" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "arrovv" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "arrov" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ok" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oq":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰸
🐺 Old Turkic (bef. 13th c.): oq
🇬🇧 English: arrow
🇷🇺 Русский: стрела
🇹🇷 Türkçe: ok
🇦🇿 Türkcə: ox
🇹🇲 Türkmençe: ok
🇺🇿 Oʻzbekcha: oq
🇰🇿 Qazaqşa: jebe, oq {bullet, shell, arrow}
🇰🇬 Qırğızça: jebe, oq {bullet, shell, arrow}
🌏 Uyghurche: oq
🌍 Tatarça: uq
🌍 Başqortsa: uq
🌍 Çovaşla: uxo {+ bow}, uxo yöppi, cömren
🌍 Qaraqalpaqsha: oq
🌍 Qırımtatarca: oq
🌍 Qumuqça: oq
🌍 Qaraçay-Malqar: sadaq, oq {bullet, shell, arrow}
🌍 Noğayşa: oq
🌏 Sıbırca: uq
🌍 Gagauzça: ok
🌏 Saqalī: oq, onoğos
🌏 Dulgan-Hakalī: ok
🌏 Tıvalap: sogun, ok {bullet, shell, arrow}
🌏 Salırça: ox (ux, uxu)
🌏 Xakastap: soğan, ux {bullet, shell, arrow}
🌏 Altaylap: soğoon, cebe, oq {bullet, shell, arrow}
🌏 Şor: soğan, oq {bullet, shell, arrow}
🌍 Urumça: ox
🌍 Karajče: ok
🌍 Qrımçahça: oq
🌏 Soyot: oq, soğın
🌏 Tofalap: soğun (soğın), oq {bullet, shell, arrow}''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "footprint" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "trace" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "foot print" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "trail" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "след" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "следы" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ız" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iz":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): iz (yiz)
🇬🇧 English: trail, trace
🇷🇺 Русский: след
🇹🇷 Türkçe: iz
🇦🇿 Türkcə: iz
🇹🇲 Türkmençe: yz
🇺🇿 Oʻzbekcha: iz
🇰🇿 Qazaqşa: iz
🇰🇬 Qırğızça: iz
🌏 Uyghurche: iz
🌍 Tatarça: ez
🌍 Başqortsa: eð
🌍 Çovaşla: yör
🌍 Qaraqalpaqsha: iz
🌍 Qırımtatarca: iz
🌍 Qumuqça: hız
🌍 Qaraçay-Malqar: ız
🌍 Noğayşa: ız
🌏 Sıbırca: es
🌍 Gagauzça: iz
🌏 Saqalī: suol
🌏 Dulgan-Hakalī: huol
🌏 Tıvalap: is
🌏 Salırça: iz
🌏 Xakastap: is
🌏 Altaylap: is
🌏 Şor: is
🌍 Urumça: iz
🌍 Karajče: iz
🌍 Qrımçahça: ız
🌏 Soyot: îs
🌏 Tofalap: îs''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мгла" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "смог" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дымка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "туман" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tuman" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sis" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sıs" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mist" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "smog" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fog":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱃𐰆𐰢𐰣
🐺 Old Turkic (bef. 13th c.): tuman, bus, iş
🇬🇧 English: fog, mist, smog
🇷🇺 Русский: туман [tuman], дымка, смог
🇹🇷 Türkçe: sis, pus, duman
🇦🇿 Türkcə: duman, çən
🇹🇲 Türkmençe: duman, ümür
🇺🇿 Oʻzbekcha: tuman
🇰🇿 Qazaqşa: tuman
🇰🇬 Qırğızça: tuman
🌏 Uyghurche: tuman, tütek
🌍 Tatarça: toman
🌍 Başqortsa: toman
🌍 Çovaşla: tötre
🌍 Qaraqalpaqsha: duman
🌍 Qırımtatarca: tuman, pus
🌍 Qumuqça: tuman, çars
🌍 Qaraçay-Malqar: tuban (tuman), çare
🌍 Noğayşa: tuman
🌏 Sıbırca: toman
🌍 Gagauzça: duman
🌏 Saqalī: tuman, küden
🌏 Dulgan-Hakalī: tuman
🌏 Tıvalap: tuman
🌏 Salırça: tuman
🌏 Xakastap: tuban
🌏 Altaylap: tuman
🌏 Şor: tuban
🌍 Urumça: duman (tuman), pus (puslux)
🌍 Karajče: tuman
🌍 Qrımçahça: tuman
🌏 Soyot: duman, bus
🌏 Tofalap: tuman, bus''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пятница" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пятничная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пятничный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пятничное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пятничные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "friday" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "frıday" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cuma":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): adına (ayna)
🇬🇧 English: friday
🇷🇺 Русский: пятница [pyatnitsa]
🇹🇷 Türkçe: cuma
🇦🇿 Türkcə: beşinci gün, cümə
🇹🇲 Türkmençe: anna, juma
🇺🇿 Oʻzbekcha: juma
🇰🇿 Qazaqşa: juma
🇰🇬 Qırğızça: juma
🌏 Uyghurche: jüme
🌍 Tatarça: comğa, tatar atnası {arch.}
🌍 Başqortsa: yoma
🌍 Çovaşla: ernekun
🌍 Qaraqalpaqsha: juma
🌍 Qırımtatarca: cuma
🌍 Qumuqça: cumagün
🌍 Qaraçay-Malqar: bayrım kün, juma kün
🌍 Noğayşa: yuma
🌏 Sıbırca: yoma
🌍 Gagauzça: cumaa
🌏 Saqalī: beetinse
🌏 Dulgan-Hakalī: pyatnitsa
🌏 Tıvalap: beş dugaar xün
🌏 Salırça: cuma
🌏 Xakastap: pîs xonıx
🌏 Altaylap: pyatnitsa
🌏 Şor: pejinçi kün
🌍 Urumça: cuma
🌍 Karajče: ejnekiun (ajnakiuń), džumaa
🌍 Qrımçahça: aynekünı
🌏 Soyot: pyatnîtsa
🌏 Tofalap: pyatnîtsa''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "джума" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "аль-джума" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jumuah" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cüme" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "juma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "al-jumuah" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "аль-джуму‘а" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jumu'ah":
        bot.send_message(message.chat.id, '''🇬🇧 English: Jumu'ah
🇷🇺 Русский: джума [dzhuma]
🇹🇷 Türkçe: cuma
🇦🇿 Türkcə: cümə
🇹🇲 Türkmençe: juma
🇺🇿 Oʻzbekcha: juma
🇰🇿 Qazaqşa: juma
🇰🇬 Qırğızça: juma
🌏 Uyghurche: jüme
🌍 Tatarça: comğa
🌍 Başqortsa: yoma
🌍 Çovaşla: djuma
🌍 Qaraqalpaqsha: juma
🌍 Qırımtatarca: cuma
🌍 Qumuqça: cuma
🌍 Qaraçay-Malqar: juma
🌍 Noğayşa: yuma
🌏 Sıbırca: yoma
🌍 Gagauzça: cumaa
🌏 Saqalī: juma
🌏 Dulgan-Hakalī: juma
🌏 Tıvalap: djuma
🌏 Salırça: cuma
🌏 Xakastap: cuma
🌏 Altaylap: cuma
🌏 Şor: cuma
🌍 Urumça: cuma
🌍 Karajče: džumaa
🌍 Qrımçahça: cuma
🌏 Soyot: cuma
🌏 Tofalap: cuma''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tool" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tools" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "implement" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ımplement" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "instrument" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ınstrument" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "орудие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "орудие труда" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "alet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "инструмент":
        bot.send_message(message.chat.id, '''🇬🇧 English: tool, implement, instrument
🇷🇺 Русский: инструмент [instrument], орудие {орудие труда, оружие}
🇹🇷 Türkçe: alet
🇦🇿 Türkcə: alət
🇹🇲 Türkmençe: gural
🇺🇿 Oʻzbekcha: asbob, qurol
🇰🇿 Qazaqşa: qural, aspap {musical instrument}
🇰🇬 Qırğızça: qural, aspap
🌏 Uyghurche: qoral, eswab
🌍 Tatarça: qoral, äsbap
🌍 Başqortsa: qoral
🌍 Çovaşla: koral
🌍 Qaraqalpaqsha: qural, ásbap
🌍 Qırımtatarca: alet
🌍 Qumuqça: qural
🌍 Qaraçay-Malqar: kerek
🌍 Noğayşa: alat, qural {musical instrument}
🌏 Sıbırca: qoral, şay
🌍 Gagauzça: avadannık, tertip, takım
🌏 Saqalī: tuttar sep
🌏 Dulgan-Hakalī: hep
🌏 Tıvalap: xereksel
🌏 Salırça: alet, laxcı {weapon}
🌏 Xakastap: tîrig, tibeg
🌏 Altaylap: cepsel {tool, kit, inventory, set of tools, equipment}
🌏 Şor: tibil
🌍 Urumça: alät, savut, şiy
🌍 Karajče: savut
🌍 Qrımçahça: alet, kedık
🌏 Soyot: bağacı, hereksäl, çepsäk (cepsäk) {+ weapon}
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зима" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зимний" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зимняя" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зимнее" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зимние" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kış" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "winter" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "winterly" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "winters" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "wınter":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰃𐱁
🐺 Old Turkic (bef. 13th c.): qış
🇬🇧 English: winter
🇷🇺 Русский: зима
🇹🇷 Türkçe: kış
🇦🇿 Türkcə: qış
🇹🇲 Türkmençe: gyş
🇺🇿 Oʻzbekcha: qish
🇰🇿 Qazaqşa: qıs
🇰🇬 Qırğızça: qış
🌏 Uyghurche: qish
🌍 Tatarça: qış
🌍 Başqortsa: qış
🌍 Çovaşla: xöl, xölle
🌍 Qaraqalpaqsha: qıs
🌍 Qırımtatarca: qış
🌍 Qumuqça: qış
🌍 Qaraçay-Malqar: qış
🌍 Noğayşa: qıs
🌏 Sıbırca: qış
🌍 Gagauzça: kış
🌏 Saqalī: kıhın, kısın {arch.}
🌏 Dulgan-Hakalī: kıhın
🌏 Tıvalap: kış
🌏 Salırça: qış
🌏 Xakastap: xısxı, xıs {arch.}
🌏 Altaylap: qış
🌏 Şor: qışqı
🌍 Urumça: xış (ğış)
🌍 Karajče: kyš (kys)
🌍 Qrımçahça: qış
🌏 Soyot: qış
🌏 Tofalap: qış''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лето" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "летний" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "летняя" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "летнее" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "летние" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yaz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "summer" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "summer time" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "summerly" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "summertime":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰖𐰖
🐺 Old Turkic (bef. 15th c.): yay
🇬🇧 English: summer
🇷🇺 Русский: лето
🇹🇷 Türkçe: yaz
🇦🇿 Türkcə: yay
🇹🇲 Türkmençe: ýaý
🇺🇿 Oʻzbekcha: yoz
🇰🇿 Qazaqşa: jaz
🇰🇬 Qırğızça: jay
🌏 Uyghurche: yaz
🌍 Tatarça: cäy
🌍 Başqortsa: yäy
🌍 Çovaşla: cu, culla
🌍 Qaraqalpaqsha: jaz
🌍 Qırımtatarca: yaz
🌍 Qumuqça: yay
🌍 Qaraçay-Malqar: jay
🌍 Noğayşa: yaz
🌏 Sıbırca: yäy
🌍 Gagauzça: yaz
🌏 Saqalī: sayın, say {arch.}
🌏 Dulgan-Hakalī: hayın
🌏 Tıvalap: çay
🌏 Salırça: yi
🌏 Xakastap: çayğı
🌏 Altaylap: cay
🌏 Şor: çayğı
🌍 Urumça: yaz
🌍 Karajče: jaz
🌍 Qrımçahça: yaz
🌏 Soyot: cay (çay)
🌏 Tofalap: çay (çêy)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "beniz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "benız" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "surat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "face" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лицо" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "личико" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лицевой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лицевая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "countenance" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "facial":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): yüz (yǖz), meŋgiz (meŋiz), bit
🇬🇧 English: face {n.}
🇷🇺 Русский: лицо, лик
🇹🇷 Türkçe: yüz, beniz, surat
🇦🇿 Türkcə: üz, bəniz, surət
🇹🇲 Türkmençe: ýüz, meňiz
🇺🇿 Oʻzbekcha: yüz, bet
🇰🇿 Qazaqşa: jüz, bet
🇰🇬 Qırğızça: jüz, bet
🌏 Uyghurche: yüz, mengiz (mengza), bet, roy
🌍 Tatarça: yöz, bit
🌍 Başqortsa: yöð, bit
🌍 Çovaşla: pit, pit-kuc, son
🌍 Qaraqalpaqsha: júz, bet
🌍 Qırımtatarca: yüz, beñiz, bet
🌍 Qumuqça: yüz, bet
🌍 Qaraçay-Malqar: jüz, bet, türsün
🌍 Noğayşa: yüz, bet
🌏 Sıbırca: yös, pit, cıray
🌍 Gagauzça: surat, yüz
🌏 Saqalī: sirey, ńūr
🌏 Dulgan-Hakalī: hıray
🌏 Tıvalap: arın, şıray, dürzü
🌏 Salırça: yüz
🌏 Xakastap: sıray
🌏 Altaylap: cüs, çıray, sür
🌏 Şor: çüs
🌍 Urumça: üz (yüz), bet, dizar (dızar)
🌍 Karajče: jiuź, bengiz, bet, čeraj
🌍 Qrımçahça: yuz, beñız, bet, çıray, surat
🌏 Soyot: alın, şıray
🌏 Tofalap: alın, şıray''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yüz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сто" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сотня" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сотка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "соточка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "стольник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hundred" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "one hundred" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yuz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "100":
        bot.send_message(message.chat.id, '''🇹🇷 Bu sayı anlamında yüzdür (100), organ yüzü için "beniz" yazın.
        
🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰘𐰇𐰔
🐺 Old Turkic (bef. 13th c.): yüz
🇬🇧 English: hundred
🇷🇺 Русский: сто
🇹🇷 Türkçe: yüz
🇦🇿 Türkcə: yüz
🇹🇲 Türkmençe: ýüz
🇺🇿 Oʻzbekcha: yuz
🇰🇿 Qazaqşa: jüz
🇰🇬 Qırğızça: jüz
🌏 Uyghurche: yüz
🌍 Tatarça: yöz
🌍 Başqortsa: yöð
🌍 Çovaşla: cör
🌍 Qaraqalpaqsha: júz
🌍 Qırımtatarca: yüz
🌍 Qumuqça: yüz
🌍 Qaraçay-Malqar: jüz
🌍 Noğayşa: yüz
🌏 Sıbırca: yös
🌍 Gagauzça: üz
🌏 Saqalī: sǖs
🌏 Dulgan-Hakalī: hüs
🌏 Tıvalap: çüs
🌏 Salırça: yüz
🌏 Xakastap: çüs
🌏 Altaylap: cüs
🌏 Şor: çüs
🌍 Urumça: yüz
🌍 Karajče: jiuź
🌍 Qrımçahça: yuz
🌏 Soyot: çüs
🌏 Tofalap: çüs''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ış" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "job" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "work" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "business" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bussines" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bussiness" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "работа" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дело" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бизнес" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "деловой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бизнэс" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бизнэсс" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бизнесс":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): iş
🇬🇧 English: business, job, work
🇷🇺 Русский: работа, дело
🇹🇷 Türkçe: iş
🇦🇿 Türkcə: iş
🇹🇲 Türkmençe: iş
🇺🇿 Oʻzbekcha: ish
🇰🇿 Qazaqşa: is
🇰🇬 Qırğızça: iş
🌏 Uyghurche: ish
🌍 Tatarça: eş
🌍 Başqortsa: eş
🌍 Çovaşla: öc
🌍 Qaraqalpaqsha: is
🌍 Qırımtatarca: iş
🌍 Qumuqça: iş
🌍 Qaraçay-Malqar: iş
🌍 Noğayşa: is
🌏 Sıbırca: eş
🌍 Gagauzça: iş
🌏 Saqalī: üle, īs {arch.}
🌏 Dulgan-Hakalī: üle, īs {arch.}
🌏 Tıvalap: iş
🌏 Salırça: iş
🌏 Xakastap: toğıs, is
🌏 Altaylap: iş
🌏 Şor: iş
🌍 Urumça: iş
🌍 Karajče: iš
🌍 Qrımçahça: iş
🌏 Soyot: îş
🌏 Tofalap: îş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "путь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yol" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дорога" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дорожный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тропа" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "way" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "road" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тропинка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шлях" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "path":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): yol (col)
🇬🇧 English: way, road, path
🇷🇺 Русский: дорога, путь
🇹🇷 Türkçe: yol
🇦🇿 Türkcə: yol
🇹🇲 Türkmençe: ýol
🇺🇿 Oʻzbekcha: yoʻl
🇰🇿 Qazaqşa: jol
🇰🇬 Qırğızça: jol
🌏 Uyghurche: yol
🌍 Tatarça: yul
🌍 Başqortsa: yul
🌍 Çovaşla: cul
🌍 Qaraqalpaqsha: jol
🌍 Qırımtatarca: yol
🌍 Qumuqça: yol
🌍 Qaraçay-Malqar: jol
🌍 Noğayşa: yol
🌏 Sıbırca: yul
🌍 Gagauzça: yol
🌏 Saqalī: suol
🌏 Dulgan-Hakalī: huol, orok
🌏 Tıvalap: oruk
🌏 Salırça: yol
🌏 Xakastap: çol
🌏 Altaylap: col
🌏 Şor: çol
🌍 Urumça: yol
🌍 Karajče: jol
🌍 Qrımçahça: yol
🌏 Soyot: orıq
🌏 Tofalap: oruq (orıq)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "карта" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "map" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mapa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мапа" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "harıta" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "harita" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "xarita" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "harite":
        bot.send_message(message.chat.id, '''🇬🇧 English: map
🇷🇺 Русский: карта [karta] {геогр.}
🇹🇷 Türkçe: harita
🇦🇿 Türkcə: xəritə
🇹🇲 Türkmençe: karta, haryta {arch.}
🇺🇿 Oʻzbekcha: xarita
🇰🇿 Qazaqşa: karta
🇰🇬 Qırğızça: karta
🌏 Uyghurche: xerite
🌍 Tatarça: xarita
🌍 Başqortsa: karta
🌍 Çovaşla: kartto
🌍 Qaraqalpaqsha: karta
🌍 Qırımtatarca: harita
🌍 Qumuqça: xarita, karta
🌍 Qaraçay-Malqar: karta
🌍 Noğayşa: karta
🌏 Sıbırca: karta
🌍 Gagauzça: harita
🌏 Saqalī: qārtı (qārta)
🌏 Dulgan-Hakalī: kārtı
🌏 Tıvalap: karta, çuruk {map, table, chart, picture, painting}
🌏 Salırça: ditu
🌏 Xakastap: karta
🌏 Altaylap: karta, curuq {map, table, chart, picture, painting}
🌏 Şor: karta
🌍 Urumça: karta
🌍 Karajče: karta
🌍 Qrımçahça: harita
🌏 Soyot: haartı
🌏 Tofalap: haartı''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курдюк" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курдючий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курдючный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курдючье" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tailfat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tail" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tail fat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хвост" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хвостовой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хвостик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fat tail" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurdiuk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurdyuk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kuyruk":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): qudruq (qudruğ, quduruq, quðruq)
🇬🇧 English: I. tail II. tail fat
🇷🇺 Русский: I. хвост II. курдюк [kurdyuk]
🇹🇷 Türkçe: kuyruk
🇦🇿 Türkcə: quyruq
🇹🇲 Türkmençe: guýruk
🇺🇿 Oʻzbekcha: quyruq, dum {I}, dumba {II}
🇰🇿 Qazaqşa: quyrıq
🇰🇬 Qırğızça: quyruq, dümbo {II}
🌏 Uyghurche: quyruq
🌍 Tatarça: qoyrıq
🌍 Başqortsa: qoyroq
🌍 Çovaşla: I. xüre II. kurtük (kurdyuk)
🌍 Qaraqalpaqsha: quyrıq
🌍 Qırımtatarca: quyruq
🌍 Qumuqça: quyruq
🌍 Qaraçay-Malqar: quyruq
🌍 Noğayşa: quyrıq
🌏 Sıbırca: qoyroq
🌍 Gagauzça: kuyruk
🌏 Saqalī: I. kuturuk II. qoñqoçoq sıata
🌏 Dulgan-Hakalī: kuturuk
🌏 Tıvalap: kuduruk
🌏 Salırça: qurux
🌏 Xakastap: xuzurux
🌏 Altaylap: quyruq
🌏 Şor: quzuruq
🌍 Urumça: ğuyruğ (xuryux)
🌍 Karajče: kujruch (kujruk, kujryk)
🌍 Qrımçahça: quyruh (quryuh)
🌏 Soyot: quduruq (qudurıq, qudırıq)
🌏 Tofalap: quduruq''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курица" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курится" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chicken" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chick" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "куриный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "куринный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кура" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курочка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "куриная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mcgregor" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "макгрегор" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mc gregor" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tavuk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tauk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "куриное":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): taquq (taqağu, taqığu)
🇬🇧 English: hen, chicken
🇷🇺 Русский: курица [kuritsa]
🇹🇷 Türkçe: tavuk
🇦🇿 Türkcə: toyuq, toox (töox, tȫx, tovux, taux) {dial.}
🇹🇲 Türkmençe: towuk
🇺🇿 Oʻzbekcha: tovuq
🇰🇿 Qazaqşa: tawıq
🇰🇬 Qırğızça: tooq
🌏 Uyghurche: toxu
🌍 Tatarça: tawıq
🌍 Başqortsa: tawıq
🌍 Çovaşla: çoxo
🌍 Qaraqalpaqsha: tawıq
🌍 Qırımtatarca: tavuq
🌍 Qumuqça: tawuq
🌍 Qaraçay-Malqar: tawuq
🌍 Noğayşa: tawıq
🌏 Sıbırca: tawıq
🌍 Gagauzça: tauk
🌏 Saqalī: kūrussa
🌏 Dulgan-Hakalī: kūrisa
🌏 Tıvalap: dagaa, togduk {bustard}
🌏 Salırça: tox (tōğo)
🌏 Xakastap: tañax
🌏 Altaylap: taqaa
🌏 Şor: quş
🌍 Urumça: tavux (ta'ux)
🌍 Karajče: tavuch (tavuk)
🌍 Qrımçahça: tavuh
🌏 Soyot: tahâa
🌏 Tofalap: taqqınâk''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "outer space" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "outerspace" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cosmos" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kozmoz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kosmos" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kozmos" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kosmoz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "космос" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "космический" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cosmic" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kozmik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kosmik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "космическое пространство" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uzay" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cosmo" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "космическое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "космическая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "космо":
        bot.send_message(message.chat.id, '''🇬🇧 English: space (outer space)
🇷🇺 Русский: космос [kosmos]
🇹🇷 Türkçe: uzay
🇦🇿 Türkcə: fəza (kosmik fəza), uzay
🇹🇲 Türkmençe: kosmos
🇺🇿 Oʻzbekcha: fazo
🇰🇿 Qazaqşa: ğarış
🇰🇬 Qırğızça: kosmos
🌏 Uyghurche: alem boshluqi
🌍 Tatarça: fäza (ğälämi fäza)
🌍 Başqortsa: kosmos
🌍 Çovaşla: tönçe ucloxö
🌍 Qaraqalpaqsha: kosmos
🌍 Qırımtatarca: feza
🌍 Qumuqça: kosmos
🌍 Qaraçay-Malqar: kosmos
🌍 Noğayşa: kosmos
🌏 Sıbırca: asman
🌍 Gagauzça: uzay
🌏 Saqalī: kosmos
🌏 Dulgan-Hakalī: kosmos
🌏 Tıvalap: kosmos
🌏 Salırça: alen
🌏 Xakastap: xan tîgir
🌏 Altaylap: aq-ayas
🌏 Şor: qaan tegri
🌍 Urumça: avlax
🌍 Karajče: avlak (avlach)
🌍 Qrımçahça: feza
🌏 Soyot: sansır
🌏 Tofalap: kosmos''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belgium" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belgic" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бельгийский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бельгия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "белгия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belcik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belçik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belgia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belgiya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belçika" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belcika" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belçıka" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belcıka" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бельгийски" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бельгийкая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бельгийское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бильгийские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belgique":
        bot.send_message(message.chat.id, '''🇬🇧 English: Belgium
🇷🇺 Русский: Бельгия [Belgiya]
🇹🇷 Türkçe: Belçika
🇦🇿 Türkcə: Belçika, Belcik {arch.}
🇹🇲 Türkmençe: Belgiýa, Belgýä {arch.}
🇺🇿 Oʻzbekcha: Belgiya
🇰🇿 Qazaqşa: Belgiya
🇰🇬 Qırğızça: Belgiya
🌏 Uyghurche: Bélgiye
🌍 Tatarça: Belgiä (Bilgiä, Belgiya)
🌍 Başqortsa: Belgiya
🌍 Çovaşla: Belgi
🌍 Qaraqalpaqsha: Belgiya
🌍 Qırımtatarca: Belçika
🌍 Qumuqça: Belgiya
🌍 Qaraçay-Malqar: Belgiya
🌍 Noğayşa: Belgiya
🌏 Sıbırca: Belgiya
🌍 Gagauzça: Belçika
🌏 Saqalī: Belgiya
🌏 Dulgan-Hakalī: Belgiya
🌏 Tıvalap: Belgi
🌏 Salırça: Bilişi, Belçika
🌏 Xakastap: Belgîya
🌏 Altaylap: Belgiya
🌏 Şor: Belgiya
🌍 Urumça: Belgiya
🌍 Karajče: Belgija
🌍 Qrımçahça: Belçika
🌏 Soyot: Belgi, Belgîya
🌏 Tofalap: Belgîya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belgian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бельгиец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бельгийка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belçikalı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belcikalı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belcıkalı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belcikali" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belçıkalı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "belçıkali":
        bot.send_message(message.chat.id, '''🇬🇧 English: Belgian
🇷🇺 Русский: бельгиец [belgiyets]
🇹🇷 Türkçe: Belçikalı
🇦🇿 Türkcə: belçikalı, belcikli {arch.}
🇹🇲 Türkmençe: belgiýaly, belgýäli {arch.}
🇺🇿 Oʻzbekcha: belgiyalik
🇰🇿 Qazaqşa: belgiyalıq
🇰🇬 Qırğızça: belgiyalıq
🌏 Uyghurche: Bélgiyiliq
🌍 Tatarça: belgiäle
🌍 Başqortsa: belgiyalı
🌍 Çovaşla: belgi
🌍 Qaraqalpaqsha: belgiyalı
🌍 Qırımtatarca: belçikalı
🌍 Qumuqça: belgiyalı
🌍 Qaraçay-Malqar: belgiyalı
🌍 Noğayşa: belgiyalı
🌏 Sıbırca: belgiyalı
🌍 Gagauzça: belçikalı
🌏 Saqalī: belgiyets
🌏 Dulgan-Hakalī: belgiyets
🌏 Tıvalap: belgi
🌏 Salırça: Bilişi kişi, Belçika kişi
🌏 Xakastap: belgîyets
🌏 Altaylap: belgiyets
🌏 Şor: belgiyets
🌍 Urumça: belgiyalı
🌍 Karajče: belgijaly
🌍 Qrımçahça: belçikalı
🌏 Soyot: belgi, belgîyets
🌏 Tofalap: belgîyets''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "москва" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moscow" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moskow" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moscu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moskva" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moskova" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "московский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "московская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moskov" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moskof":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): Mosqov
🇬🇧 English: Moscow
🇷🇺 Русский: Москва [Moskva]
🇹🇷 Türkçe: Moskova, Moskov (Moskof) {arch.}
🇦🇿 Türkcə: Moskva, Mosqva {arch.}
🇹🇲 Türkmençe: Moskwa (Maskwa)
🇺🇿 Oʻzbekcha: Mo'sqov, Moskva
🇰🇿 Qazaqşa: Mäskew
🇰🇬 Qırğızça: Mösköö, Maske
🌏 Uyghurche: Mesqaw
🌍 Tatarça: Mäskäw
🌍 Başqortsa: Mäskäw
🌍 Çovaşla: Muskav
🌍 Qaraqalpaqsha: Moskva
🌍 Qırımtatarca: Mosqu, Moskova
🌍 Qumuqça: Maskew
🌍 Qaraçay-Malqar: Maskaw
🌍 Noğayşa: Mäskew
🌏 Sıbırca: Mäskäw
🌍 Gagauzça: Moskova
🌏 Saqalī: Moskuoba (Moskuba, Maskuba)
🌏 Dulgan-Hakalī: Moskuoba (Moskuba, Maskuba), Moskva
🌏 Tıvalap: Moskva
🌏 Salırça: Mosiko, Moskva
🌏 Xakastap: Moskva
🌏 Altaylap: Moskva
🌏 Şor: Moskva
🌍 Urumça: Mosxa
🌍 Karajče: Maskva
🌍 Qrımçahça: Maskva
🌏 Soyot: Moskva
🌏 Tofalap: Moskva''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yıldönümü" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yıl dönümü" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yıldonumu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yildönümü" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yil dönümü" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "годовщина" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "годовшина" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "годины" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "година" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "anniversary":
        bot.send_message(message.chat.id, '''🇬🇧 English: anniversary
🇷🇺 Русский: годовщина
🇹🇷 Türkçe: yıldönümü
🇦🇿 Türkcə: ildönümü, illik, il
🇹🇲 Türkmençe: ýyllyk
🇺🇿 Oʻzbekcha: yillik
🇰🇿 Qazaqşa: jıldıq
🇰🇬 Qırğızça: jıldıq
🌏 Uyghurche: yilliq
🌍 Tatarça: yıllıq
🌍 Başqortsa: yıllıq
🌍 Çovaşla: cul uyavö, cul tultarni
🌍 Qaraqalpaqsha: jıllıq
🌍 Qırımtatarca: yıldönümi, yıllıq
🌍 Qumuqça: yıllıq
🌍 Qaraçay-Malqar: jıllıq, jıl
🌍 Noğayşa: yıllıq
🌏 Sıbırca: yıllıq
🌍 Gagauzça: yıldönümü, yıl
🌏 Saqalī: sıl tuolūta
🌏 Dulgan-Hakalī: cıl tuolūta
🌏 Tıvalap: oy
🌏 Salırça: yıllıx
🌏 Xakastap: çıl
🌏 Altaylap: cıldıq
🌏 Şor: çıl
🌍 Urumça: yıllıx
🌍 Karajče: jyl
🌍 Qrımçahça: yıllıh, yıl
🌏 Soyot: oy, çıl (cıl)
🌏 Tofalap: çıl''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шакал" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шакалий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шакалье" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шакалья" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çakal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cakal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jackal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jakal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jacal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shakal":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): ajru (azru, arzu)
🇬🇧 English: jackal
🇷🇺 Русский: шакал [shakal]
🇹🇷 Türkçe: çakal
🇦🇿 Türkcə: çaqqal
🇹🇲 Türkmençe: şagal, gyzyljagurt
🇺🇿 Oʻzbekcha: chiyaboʻri, shoqol
🇰🇿 Qazaqşa: şiyeböri (şüyeböri), şağal, qorqaw qasqır
🇰🇬 Qırğızça: çöö, körkoo
🌏 Uyghurche: chilböre (chil böri)
🌍 Tatarça: çül bürese
🌍 Başqortsa: sül bürehe
🌍 Çovaşla: şakal
🌍 Qaraqalpaqsha: saǵal (shaǵal)
🌍 Qırımtatarca: çaqal
🌍 Qumuqça: çağan
🌍 Qaraçay-Malqar: çaqan
🌍 Noğayşa: azru (arzu), suyqın
🌏 Sıbırca: cül püre (cül pürese)
🌍 Gagauzça: şakal
🌏 Saqalī: sir ıta
🌏 Dulgan-Hakalī: hir ıta
🌏 Tıvalap: şöö-börü, çerlik ıt
🌏 Salırça: işt buuri, çoğe
🌏 Xakastap: şakal
🌏 Altaylap: arğı
🌏 Şor: şakal
🌍 Urumça: çakal
🌍 Karajče: ahas
🌍 Qrımçahça: çaqal
🌏 Soyot: şöövörî
🌏 Tofalap: şööbörü''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "совершить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сверши" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "соверши" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "свершить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вершить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "верши" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "производи" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "производить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "произвести" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yap" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yapmak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eyle" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eylemek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "делай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сделай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "делать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сделать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to do" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "do" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "make" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to make" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to construct" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "construct" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "perform" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to perform" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "выполни" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "выполнить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мастерить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мастери" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "смастери" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сместерить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "делат" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сделат" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "твори" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "творить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "действуй" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "действовать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "исполняй" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "исполнять" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "etmek":
        bot.send_message(message.chat.id, '''🇬🇧 English: do, make, construct, perform
🇷🇺 Русский: действуй, делай, сделай
🇹🇷 Türkçe: et (eyle), yap
🇦🇿 Türkcə: et (elə), qayır
🇹🇲 Türkmençe: et, ýasa
🇺🇿 Oʻzbekcha: qil, yasa
🇰🇿 Qazaqşa: qıl, jasa, et
🇰🇬 Qırğızça: qıl, jasa
🌏 Uyghurche: qil, et, yasa
🌍 Tatarça: eşlä, it, qıl, yasa
🌍 Başqortsa: eşlä, it, qıl, yaha
🌍 Çovaşla: tu, öcle
🌍 Qaraqalpaqsha: isle, et, qıl, jasa
🌍 Qırımtatarca: et (eyle), yap, yasa
🌍 Qumuqça: et, işle
🌍 Qaraçay-Malqar: et, işle
🌍 Noğayşa: et
🌏 Sıbırca: eşlä, it, qıl, yasa
🌍 Gagauzça: et, yap
🌏 Saqalī: gın, oñor
🌏 Dulgan-Hakalī: gın, ülelē, oñor
🌏 Tıvalap: kıl, büdür
🌏 Salırça: et, qıl, yasa
🌏 Xakastap: it
🌏 Altaylap: et, edip sal, cazap sal
🌏 Şor: işte, iştep sal
🌍 Urumça: et, yap, yasa
🌍 Karajče: ėt´, išlia, kyl
🌍 Qrımçahça: et (eyle), yap, yasa, qıl
🌏 Soyot: qıl
🌏 Tofalap: qıl, çasa, çasap qağ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "scorpio" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "scorpion" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "scorp" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "скорп" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "скорпион" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "akrep" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "akreb" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çayan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "skorpion" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "scorpione" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "scorpius" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "скорпионий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "scorpiu":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.):	çayan (çıyan, çadan, caðan)
🇬🇧 English: scorpion
🇷🇺 Русский: скорпион [skorpion]
🇹🇷 Türkçe: akrep
🇦🇿 Türkcə: əqrəb, çayan
🇹🇲 Türkmençe: içýan
🇺🇿 Oʻzbekcha: chayon
🇰🇿 Qazaqşa: şayan {+ crustacea}, sarışayan, qırşayan
🇰🇬 Qırğızça: çayan
🌏 Uyghurche: chayan, séroqéshek
🌍 Tatarça: çayan
🌍 Başqortsa: sayan
🌍 Çovaşla: skorpion
🌍 Qaraqalpaqsha: shayan
🌍 Qırımtatarca: çayan, aqrep
🌍 Qumuqça: alperek, aqırap, çayan
🌍 Qaraçay-Malqar: uw gıbı
🌍 Noğayşa: sarı biy, şayan {+ crustacea, gryllotalpa}
🌏 Sıbırca: cayan, aqrap
🌍 Gagauzça: skorpion
🌏 Saqalī: skorpion
🌏 Dulgan-Hakalī: skorpion
🌏 Tıvalap: skorpion
🌏 Salırça: caca
🌏 Xakastap: skorpîon
🌏 Altaylap: skorpion
🌏 Şor: skorpion
🌍 Urumça: skarpion
🌍 Karajče: skorpion
🌍 Qrımçahça: çayan, aqrep
🌏 Soyot: skorpîon
🌏 Tofalap: skorpîon''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "switzerland" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "swiss" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "switz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "швейцария" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "швецария" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "швейцарский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "isviçre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "İsviçre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ısvıçre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "isvıçre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ısviçre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "швейцарское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "швейцарская":
        bot.send_message(message.chat.id, '''🇬🇧 English: Switzerland
🇷🇺 Русский: Швейцария [Shveytsariya]
🇹🇷 Türkçe: İsviçre, Svisera {arch.}
🇦🇿 Türkcə: İsveçrə, İşvesrə {dial.}
🇹🇲 Türkmençe: Şweýsariýa
🇺🇿 Oʻzbekcha: Shveysariya
🇰🇿 Qazaqşa: Şveytsariya
🇰🇬 Qırğızça: Şveytsariya
🌏 Uyghurche: Shwéytsariye
🌍 Tatarça: Şveytsariya
🌍 Başqortsa: Şveytsariya
🌍 Çovaşla: Şveytsari
🌍 Qaraqalpaqsha: Shveytsariya
🌍 Qırımtatarca: İsviçre
🌍 Qumuqça: Şveytsariya
🌍 Qaraçay-Malqar: Şveytsariya
🌍 Noğayşa: Şveytsariya
🌏 Sıbırca: Şveytsariya
🌍 Gagauzça: Elveţiya
🌏 Saqalī: Şveytsariya
🌏 Dulgan-Hakalī: Şveytsariya
🌏 Tıvalap: Şveytsariya
🌏 Salırça: İsviçre, Ruyşi
🌏 Xakastap: Şveytsarîya
🌏 Altaylap: Şveytsariya
🌏 Şor: Şveytsariya
🌍 Urumça: Şveytsariya
🌍 Karajče: Šveicarija
🌍 Qrımçahça: İsviçre
🌏 Soyot: Şveytsarîya
🌏 Tofalap: Şveytsarîya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "эчпочмак" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "очпочмак" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "эщпощмак" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ощпощмак" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "учпочмак" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "треугольник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "трехугольник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "triangle" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "triangl" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "üçgen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "üçbucak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "üç bucak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "öçpoçmaq" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "öçpoçmak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ocpocmaq" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "△" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "триугольник":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): üçgül (üçgil)
🇬🇧 English: triangle
🇷🇺 Русский: треугольник, эчпочмак {tatar-bashkir dish}
🇹🇷 Türkçe: üçgen {neologism, since 1937}, üçbucak, müselles
🇦🇿 Türkcə: üçbucaq
🇹🇲 Türkmençe: üçburçluk
🇺🇿 Oʻzbekcha: uchburchak
🇰🇿 Qazaqşa: üşburış
🇰🇬 Qırğızça: üç burçtuq
🌏 Uyghurche: üch bujek (üchburjek), üchbulung
🌍 Tatarça: öçpoçmaq
🌍 Başqortsa: ösmöyöş {△}, ösbosmaq {tatar-bashkir dish}
🌍 Çovaşla: vic köteslöx
🌍 Qaraqalpaqsha: úsh múyeshlik
🌍 Qırımtatarca: üçköşe (~lik)
🌍 Qumuqça: üçbuççaqlıq, üç müyüşlük
🌍 Qaraçay-Malqar: üçmüyüş
🌍 Noğayşa: üş müyis (~lik)
🌏 Sıbırca: öcmöyöşlök
🌍 Gagauzça: üçköşeli
🌏 Saqalī: üs munnuk
🌏 Dulgan-Hakalī: üs muñnuk
🌏 Tıvalap: üş-buluñçuk
🌏 Salırça: üş dumcux (ucdumcux)
🌏 Xakastap: üs puluñ (~nığ)
🌏 Altaylap: üçtoluq (üçtolıq)
🌏 Şor: üştoluq
🌍 Urumça: üçköşe (~lik)
🌍 Karajče: üč miujiuš (ic mivis)
🌍 Qrımçahça: uçköşe (~lık)
🌏 Soyot: üş-bulıñ
🌏 Tofalap: üş-buluñ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "славян" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "славянин" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "славянки" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "славянка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "славянский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "славянская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "славянское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "славянские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "slavic" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "slav" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "slawe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "islav" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıslav" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "slavyan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "slavian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "slavka" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "слав":
        bot.send_message(message.chat.id, '''🇬🇧 English: Slav, Slavic
🇷🇺 Русский: славянин [slavyanin]
🇹🇷 Türkçe: İslav (Slav), Sakalibe {arch.}
🇦🇿 Türkcə: slavyan, urus-murus {dial.}, səqləb {arch.}
🇹🇲 Türkmençe: slawýan, islawän {arch.}
🇺🇿 Oʻzbekcha: slavyan
🇰🇿 Qazaqşa: slavyan
🇰🇬 Qırğızça: slavyan
🌏 Uyghurche: Slaw
🌍 Tatarça: ıslaw
🌍 Başqortsa: slavyan, ıslaw {arch.}
🌍 Çovaşla:	slavyan
🌍 Qaraqalpaqsha: slavyan
🌍 Qırımtatarca: slav
🌍 Qumuqça: slavyan
🌍 Qaraçay-Malqar: slavyan
🌍 Noğayşa: slavyan, orıs {east slav}
🌏 Sıbırca: slavyan
🌍 Gagauzça: slavyan
🌏 Saqalī: slavyan
🌏 Dulgan-Hakalī: slavyan
🌏 Tıvalap: slavyan
🌏 Salırça:	slav, sılafu
🌏 Xakastap: slavyan
🌏 Altaylap: slavyan
🌏 Şor: slavyan
🌍 Urumça: slav, xazax {east slav}
🌍 Karajče: slav
🌍 Qrımçahça: slav
🌏 Soyot: slavyan
🌏 Tofalap: slavyan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bayram" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bairam" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "feast" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "holiday" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "holi day" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "праздник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "праздничный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "праздничная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "праздничное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "праздничные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "день отдыха" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "празднование" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "празник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "празьник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "празьдник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "прасник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "baryam":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): bayram (baðram)
🇬🇧 English: feast, holiday
🇷🇺 Русский: праздник
🇹🇷 Türkçe: bayram
🇦🇿 Türkcə: bayram
🇹🇲 Türkmençe: baýram
🇺🇿 Oʻzbekcha: bayram
🇰🇿 Qazaqşa: meyram, mereke
🇰🇬 Qırğızça: mayram
🌏 Uyghurche: bayram
🌍 Tatarça: bäyräm
🌍 Başqortsa: bayram
🌍 Çovaşla: uyav, payran (peyrem)
🌍 Qaraqalpaqsha: bayram
🌍 Qırımtatarca: bayram
🌍 Qumuqça: bayram
🌍 Qaraçay-Malqar: bayram
🌍 Noğayşa: bayram
🌏 Sıbırca: payram
🌍 Gagauzça: yortu, bayram
🌏 Saqalī: tañara kün
🌏 Dulgan-Hakalī: tañara kün
🌏 Tıvalap: bayırlal
🌏 Salırça: ayit (heyit)
🌏 Xakastap: ülükün, payram
🌏 Altaylap: bayram
🌏 Şor: payram
🌍 Urumça: yortu, bayram
🌍 Karajče: chydž, bajram
🌍 Qrımçahça: bayram (baryam)
🌏 Soyot: bayır, ulığ-hün
🌏 Tofalap: uluğ-hün''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bağ" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bahçe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bahça" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бахча" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сад" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "садик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "садовый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "садный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "садовое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "садовая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "садовые" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "garden" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "garten" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "orchard":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): bağ, bağça, çeçäklik {floral garden}, yemişlik {orchard}
🇬🇧 English: garden, orchard
🇷🇺 Русский: сад [sad], садик
🇹🇷 Türkçe: bağ, bahçe
🇦🇿 Türkcə: bağ, bağça
🇹🇲 Türkmençe: bag, bakja
🇺🇿 Oʻzbekcha: bogʻ, bogʻcha
🇰🇿 Qazaqşa: baw, baqşa
🇰🇬 Qırğızça: baq, baqça
🌏 Uyghurche: bagh, baghche (baghcha)
🌍 Tatarça: baqça, bağ
🌍 Başqortsa: baqsa, bağ
🌍 Çovaşla: paxça, pax
🌍 Qaraqalpaqsha: baǵ, baqsha
🌍 Qırımtatarca: bağça
🌍 Qumuqça: baw, baxça
🌍 Qaraçay-Malqar: baxça (baçxa)
🌍 Noğayşa: baw, baqşa
🌏 Sıbırca: paqca, bağ {arch.}
🌍 Gagauzça: baa, başça
🌏 Saqalī: olordū oyūr, sāt (sad)
🌏 Dulgan-Hakalī: sad
🌏 Tıvalap: sad
🌏 Salırça: bağ (pağ)
🌏 Xakastap: sad
🌏 Altaylap: sad
🌏 Şor: sad
🌍 Urumça: bağ, baxça
🌍 Karajče: bah, bachča
🌍 Qrımçahça: bağ, bağça
🌏 Soyot: sad
🌏 Tofalap: saat''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "никях" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "никах" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "свадба" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "свадьба" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "свадъба" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "брак" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "брачный союз" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "брачный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "wedding" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nikah" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "marriage" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "matrimony" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nikâh" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "düğün" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "evlenme" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "evlilik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "женитьба" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бракосочетание" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "венчание" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "wedlock":
        bot.send_message(message.chat.id, '''🇷🇺 Брак указан в значении брачного союза, для брака в значении дефекта введите "дефект".
        
🇬🇧 English: I. wedding II. marriage, matrimony, wedlock
🇷🇺 Русский: I. свадьба II. брак (брачный союз между мужчиной и женщиной)
🇹🇷 Türkçe: I. düğün, nikâh, evlenme II. evlilik
🇦🇿 Türkcə: I. toy I. nikah, kəbin
🇹🇲 Türkmençe: I. toý II. nika
🇺🇿 Oʻzbekcha: I. toʻy (nikoh toʻyi) II. nikoh, uylanish
🇰🇿 Qazaqşa: I. toy (üyleniw toyı) II. neke
🇰🇬 Qırğızça: I. toy (üylönüü toyu) II. nike
🌏 Uyghurche: I. toy, öylenme II. nikah, turmush
🌍 Tatarça: I. tuy II. nikah, öylänü
🌍 Başqortsa: I. tuy II. nikah, öyläneşew
🌍 Çovaşla: I. tuy II. avlanu, moşorlanu
🌍 Qaraqalpaqsha: I. toy (úyleniw toyı) II. neke
🌍 Qırımtatarca: I. toy, dügün II. evlilik, evlenüv, evlenme, nikâh
🌍 Qumuqça: I. toy II. üyleniw, nikah
🌍 Qaraçay-Malqar: I. toy (üylenñen toy) II. üyleniw, nekâh
🌍 Noğayşa: I. toy (üylenüw toyı) II. neke, üylenüw
🌏 Sıbırca: I. tuy II. nekä, öylänew
🌍 Gagauzça: I düün, toy (evlenmak toyu) II. evlenmak
🌏 Saqalī: I urū II. kergen qolbohū, kergen buolū
🌏 Dulgan-Hakalī: I. kurum II. kergen buolū
🌏 Tıvalap: I. kuda II. aşak-kaday bolçuru, ögleniri, öglenişkeni
🌏 Salırça: I. doy II. nigah
🌏 Xakastap: I. toy II. xonıx kîbeleeni
🌏 Altaylap: I. toy II. alıjar
🌏 Şor: I. toy II. alışqan
🌍 Urumça: I. dügün, toy II. dügün teskeresi
🌍 Karajče: I. diugiun, toy II. chuppa
🌍 Qrımçahça: I. dugun, toy II. nikâh, hupa
🌏 Soyot: I. toy II. gerlelge
🌏 Tofalap: I. toy II. gerlelge''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фаршированный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фаршированый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фаршированная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фаршированные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фаршированное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "наполненный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "наполненная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "наполненное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "наполненные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "долма" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "толма" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "далма" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тулма" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дулма" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сарма" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дурма" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sarma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dolma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tolma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "stuffed" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "stuffing" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "filling" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "filled" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dressed" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dressing" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cabbage roll" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sarma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dolma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tolma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "голубцы" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "голубец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tulma":
        bot.send_message(message.chat.id, '''🇬🇧 In some languages, dolma and sarma are equivalent synonym words, in some languages dolma means a dish of stuffed leaves, and sarma means cabbage rolls, but in other languges vice versa.
🇷🇺 В некоторых языках долма и сарма равнозначные слова-синонимы, в некоторых долма означает блюдо из листьев, а сарма – голубцы, а в некоторых – наоборот. 
        
🇬🇧 English: dolma, sarma, cabbage roll, stuffed food
🇷🇺 Русский:	долма [dolma] + голубцы {cabbage roll}
🇹🇷 Türkçe: dolma {from ottoman: طوٓلمه‎} [tolma], sarma
🇦🇿 Türkcə: dolma
🇹🇲 Türkmençe: dolama
🇺🇿 Oʻzbekcha: doʻlma
🇰🇿 Qazaqşa: dolma {<🇷🇺<🇦🇿???}
🇰🇬 Qırğızça: dolma {<🇷🇺<🇦🇿???}, oromo
🌏 Uyghurche: ???
🌍 Tatarça: tulma
🌍 Başqortsa: ???
🌍 Çovaşla: ???
🌍 Qaraqalpaqsha: ???
🌍 Qırımtatarca: dolma, sarma
🌍 Qumuqça: dolma
🌍 Qaraçay-Malqar: dolma {arch.}
🌍 Noğayşa: ???
🌏 Sıbırca: ???
🌍 Gagauzça: dolma, sarma
🌏 Saqalī: ???
🌏 Dulgan-Hakalī: ???
🌏 Tıvalap: ???
🌏 Salırça: ???
🌏 Xakastap: ???
🌏 Altaylap: ???
🌏 Şor: ???
🌍 Urumça: dolma, sarma (sarmax)
🌍 Karajče: dolma, sarma
🌍 Qrımçahça: tolma, sarma
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дефективный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дефектность" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "деффектный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дефект" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "недостаток" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "изъян" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "изьян" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "defect" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "defekt" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "flaw" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kusur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "noksan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eksiklik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bozukluk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kem" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kemçi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kemlik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kemçilik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kemçiklik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nöksan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "несоответствие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "недочет" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "огрех" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "упущение" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уродство" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "порок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "деффект" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дефектный":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): irinçü, äksüklüg, käm, çolmaq, mün
🇬🇧 English: defect, flaw
🇷🇺 Русский: дефект [defekt], недостаток, изъян, брак
🇹🇷 Türkçe: kusur, noksan, eksiklik, bozukluk, kem
🇦🇿 Türkcə: qüsur, nöqsan, çatışmazlıq, kəm, kəmlik
🇹🇲 Türkmençe: kem, bozuklyk, ýetmezçilik
🇺🇿 Oʻzbekcha: kamchilik, nuqson, illat
🇰🇿 Qazaqşa: aqaw, kemistik, jetimsizdik, kemşilik, min
🇰🇬 Qırğızça: kemçilik, kemtik, min
🌏 Uyghurche: qusur, nuqsan, kemchilik
🌍 Tatarça: citeşsezlek, kimçelek
🌍 Başqortsa: yeteşheðlek, kämselek, boðoqloq
🌍 Çovaşla: citmenlöx, koltok, posok
🌍 Qaraqalpaqsha: kemshilik, jetispeslik
🌍 Qırımtatarca: qusur, eksiklik, nuqsan (~lıq)
🌍 Qumuqça: buzuqluq, kemçilik
🌍 Qaraçay-Malqar: buzuq, kemlik, qıyaw
🌍 Noğayşa: kemşilik, yetispewlik, min
🌏 Sıbırca: yeteşmälelek, yeteşmäw, men
🌍 Gagauzça: kusur, iysik (esik), çentik, maana
🌏 Saqalī: jiek, eñkil, omso
🌏 Dulgan-Hakalī: iteges
🌏 Tıvalap: çetpes, ürelik, duudu
🌏 Salırça: gem, kemtüx
🌏 Xakastap: kîremet
🌏 Altaylap: cek, tutaq, cedikpes
🌏 Şor: qoptaş
🌍 Urumça: kem, eksiklik, maana
🌍 Karajče: kusur, ėksiklik
🌍 Qrımçahça: qusur, eksıklık
🌏 Soyot: dutuu, ürääşkin
🌏 Tofalap: dutuu, ürääşkin''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "средняя азия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "средняяазия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "средняя-азия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "центральнаяазия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "центральная-азия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "центральная азия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "orta asya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "orta asiya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ortasya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ortaasya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "orta-asya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "türküstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "türkistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "turkestan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "turkistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "туркестан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "туркестанский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "туркистан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюркестан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюркистан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "central asia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "centralasia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sovyet central asia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soviet central asia":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): Türkistan
🇬🇧 English: Turkistan (Turkestan), Central Asia
🇷🇺 Русский: Туркестан [Turkestan], Центральная Азия
🇹🇷 Türkçe: Türkistan
🇦🇿 Türkcə: Türküstan
🇹🇲 Türkmençe: Türküstan
🇺🇿 Oʻzbekcha: Turkiston
🇰🇿 Qazaqşa: Türkistan
🇰🇬 Qırğızça: Türkstan
🌏 Uyghurche: Türkistan
🌍 Tatarça: Törkistan
🌍 Başqortsa: Törköstan
🌍 Çovaşla: Turkestan
🌍 Qaraqalpaqsha: Túrkistan
🌍 Qırımtatarca: Türkistan
🌍 Qumuqça: Türkistan
🌍 Qaraçay-Malqar: Türkistan
🌍 Noğayşa: Türkistan
🌏 Sıbırca: Törköstan
🌍 Gagauzça: Türkistan
🌏 Saqalī: Türkistan
🌏 Dulgan-Hakalī: Türkistan
🌏 Tıvalap: Türkistan
🌏 Salırça: Türkisitan
🌏 Xakastap: Türkistan
🌏 Altaylap: Türkistan
🌏 Şor: Türkistan
🌍 Urumça: Türkistan
🌍 Karajče: Turkistan
🌍 Qrımçahça: Türkistan
🌏 Soyot: Türkistan
🌏 Tofalap: Türkistan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "east turkistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eastern turkistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "east-turkistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eastturkistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "east turkestan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eastturkestan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "east-turkestan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eastern turkestan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восточный туркестан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восточный туркистан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восточныйтуркестан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восточныйтуркистан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восточный-туркестан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восточный-туркистан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doğu türkistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doğu türkestan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doğu-türkistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doğutürkistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уйгурстан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уйгурия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уйгуристан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uyghuristan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uighuristan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uyguristan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uyghurstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uighurstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uygurstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uyğurstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uyğuristan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uyguristan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uiguristan":
        bot.send_message(message.chat.id, '''🇬🇧 English: East Turkestan (East Turkistan)
🇷🇺 Русский: Восточный Туркестан
🇹🇷 Türkçe: Doğu Türkistan
🇦🇿 Türkcə: Doğu Türküstan, Şərqi Türküstan
🇹🇲 Türkmençe: Gündogar Türküstan (Gündogar Türkistan)
🇺🇿 Oʻzbekcha: Sharqiy Turkiston
🇰🇿 Qazaqşa: Şığıs Türkistan
🇰🇬 Qırğızça: Çığış Türkstan
🌏 Uyghurche: Sherqiy Türkistan
🌍 Tatarça: Könçığış Törkistan
🌍 Başqortsa: Könsığış Törköstan
🌍 Çovaşla: Tuxoc Turkestan
🌍 Qaraqalpaqsha: Shıǵıs Túrkistan
🌍 Qırımtatarca: Şarqiy Türkistan
🌍 Qumuqça: Güntuwuş Türkistan
🌍 Qaraçay-Malqar: Künçıqğan Türkistan
🌍 Noğayşa: Küntuwar Türkistan
🌏 Sıbırca: Köncığış Törköstan
🌍 Gagauzça: Günduusu Türkistan
🌏 Saqalī: İlin Türkistan
🌏 Dulgan-Hakalī: Küntaksī Türkistan
🌏 Tıvalap: Çöön Türkistan
🌏 Salırça: Günçıxqan Türkisitan
🌏 Xakastap: İskerki Türkistan
🌏 Altaylap: Künçığış Türkistan
🌏 Şor: Künşığıjınıyı Türkistan
🌍 Urumça: Doğu Türkistan
🌍 Karajče: Mizrach Turkistan
🌍 Qrımçahça: Mizrah Türkistan
🌏 Soyot: Cöön Türkistan
🌏 Tofalap: Buruŋğaarıkîî Türkistan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "coffee" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "koffee" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kofe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cofe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cofee" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "coffe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кофе" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kahve" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кофэ" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кофейный":
        bot.send_message(message.chat.id, '''🇬🇧 English: coffee
🇷🇺 Русский: кофе [kofe]
🇹🇷 Türkçe: kahve
🇦🇿 Türkcə: qəhvə
🇹🇲 Türkmençe: kofe, kahwa {arch.}, kufä {arch.}
🇺🇿 Oʻzbekcha: qahva
🇰🇿 Qazaqşa: kofe, kopiye {arch.}
🇰🇬 Qırğızça: kofe
🌏 Uyghurche: qehwe
🌍 Tatarça: qähwä, quf {arch.}
🌍 Başqortsa: qähwä
🌍 Çovaşla: kofe
🌍 Qaraqalpaqsha: kofe
🌍 Qırımtatarca: qave
🌍 Qumuqça: qahwa
🌍 Qaraçay-Malqar: kofe
🌍 Noğayşa: kofe
🌏 Sıbırca: kopi
🌍 Gagauzça: kafe
🌏 Saqalī: kofe, kuoppuy {arch.}
🌏 Dulgan-Hakalī: kofe
🌏 Tıvalap: kofe
🌏 Salırça: kafey
🌏 Xakastap: kofe
🌏 Altaylap: kofe
🌏 Şor: kofe
🌍 Urumça: xave
🌍 Karajče: kava (kahve)
🌍 Qrımçahça: qave
🌏 Soyot: kofe, borgol
🌏 Tofalap: kofe, borgol''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tea" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çay" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чайный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чайная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чайное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чайные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chay" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "teon":
        bot.send_message(message.chat.id, '''🇬🇧 English: tea
🇷🇺 Русский: чай [chay]
🇹🇷 Türkçe: çay
🇦🇿 Türkcə: çay
🇹🇲 Türkmençe: çaý
🇺🇿 Oʻzbekcha: choy
🇰🇿 Qazaqşa: şay
🇰🇬 Qırğızça: çay
🌏 Uyghurche: chay
🌍 Tatarça: çäy
🌍 Başqortsa: säy
🌍 Çovaşla: çey
🌍 Qaraqalpaqsha: chay
🌍 Qırımtatarca: çay
🌍 Qumuqça: çay
🌍 Qaraçay-Malqar: çay
🌍 Noğayşa: şay
🌏 Sıbırca: cäy (cay)
🌍 Gagauzça: çay
🌏 Saqalī: çey
🌏 Dulgan-Hakalī: çāy
🌏 Tıvalap: şay
🌏 Salırça: çā (çay, çäy)
🌏 Xakastap: çey
🌏 Altaylap: çay
🌏 Şor: şay
🌍 Urumça: çay
🌍 Karajče: čaj, harbata
🌍 Qrımçahça: çay
🌏 Soyot: şäy (şêy)
🌏 Tofalap: şey (şêy)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уйгур" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уйгурка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уйгурский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уйгурская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уйгурское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уйгурские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uygur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uigur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uighur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uyğur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uighuri" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uighurs" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uyghurs" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uiğur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uyghur":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜:𐰆𐰖𐰍𐰺
🐺 Old Turkic (bef. 13th c.): uyğur
🇬🇧 English: Uyghur
🇷🇺 Русский: уйгур [uygur]
🇹🇷 Türkçe: Uygur
🇦🇿 Türkcə: uyğur
🇹🇲 Türkmençe: uýgur
🇺🇿 Oʻzbekcha: uygʻur
🇰🇿 Qazaqşa: uyğır
🇰🇬 Qırğızça: uyğur
🌏 Uyghurche: Uyghur
🌍 Tatarça: uyğır
🌍 Başqortsa: uyğır
🌍 Çovaşla: uygur
🌍 Qaraqalpaqsha: uyǵır
🌍 Qırımtatarca: uyğur
🌍 Qumuqça: uyğur
🌍 Qaraçay-Malqar: uyğur
🌍 Noğayşa: uyğur
🌏 Sıbırca: uyğır
🌍 Gagauzça: uygur
🌏 Saqalī: uygūr
🌏 Dulgan-Hakalī: uygur
🌏 Tıvalap: uygur
🌏 Salırça: vuyvur (vuyğur)
🌏 Xakastap: uyğur
🌏 Altaylap: uyğur
🌏 Şor: uyğur
🌍 Urumça: uyğur
🌍 Karajče: ujgur
🌍 Qrımçahça: uygur
🌏 Soyot: tuha (tufa)
🌏 Tofalap: uyğur''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "геноцид" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genocide" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genocid" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genoside" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genosid" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "genocyde" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soy kırım" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soy kirim" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soykırım" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soykirim" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soy kırımı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soy kirimi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soykırımı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soykirimi":
        bot.send_message(message.chat.id, '''🇬🇧 English: genocide
🇷🇺 Русский: геноцид [genotsid]
🇹🇷 Türkçe: soykırım
🇦🇿 Türkcə: soyqırım
🇹🇲 Türkmençe: gyrgyn
🇺🇿 Oʻzbekcha: genotsid
🇰🇿 Qazaqşa: genotsid
🇰🇬 Qırğızça: tuqumqurut
🌏 Uyghurche: soy qirim
🌍 Tatarça: qırğın
🌍 Başqortsa: genotsid
🌍 Çovaşla: genotsid
🌍 Qaraqalpaqsha: genocid
🌍 Qırımtatarca: soyqırım
🌍 Qumuqça:	???
🌍 Qaraçay-Malqar: soyqırım
🌍 Noğayşa: genotsid
🌏 Sıbırca: genocid
🌍 Gagauzça: genoțid
🌏 Saqalī: genotsid
🌏 Dulgan-Hakalī: genotsid
🌏 Tıvalap: genotsid
🌏 Salırça: ???
🌏 Xakastap: genotsîd
🌏 Altaylap: genotsid
🌏 Şor: genotsid
🌍 Urumça: ???
🌍 Karajče: ???
🌍 Qrımçahça: soyqırım
🌏 Soyot: genotsîd
🌏 Tofalap: genotsîd''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to like" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "like" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "нравиться" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "нравится" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "нравься" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ставь лайк" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "like it" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "put like" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "put a like" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "put the like" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "like!" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "beğen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "beğenmek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "begen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "beğen koy":
        bot.send_message(message.chat.id, '''🇬🇧 It is verb, for preposition, adverb, adjective enter "as" or "such as".
        
🇬🇧 English: like! {verb}
🇷🇺 Русский:	нравиться {нет формы императива, можно попытаться перевести как "пусть тебе понравится", также можно перевести как "ставь лайк"}
🇹🇷 Türkçe: beğen
🇦🇿 Türkcə: bəyən
🇹🇲 Türkmençe: ýak
🇺🇿 Oʻzbekcha: yoq
🇰🇿 Qazaqşa: una
🇰🇬 Qırğızça: jaq
🌏 Uyghurche: yaq
🌍 Tatarça: oşa
🌍 Başqortsa: oqşa
🌍 Çovaşla: yura
🌍 Qaraqalpaqsha: una
🌍 Qırımtatarca: begen
🌍 Qumuqça: uşa
🌍 Qaraçay-Malqar: jarat
🌍 Noğayşa: una
🌏 Sıbırca: oşa
🌍 Gagauzça: been
🌏 Saqalī: söbület
🌏 Dulgan-Hakalī: höbülē
🌏 Tıvalap: sonuurga
🌏 Salırça: gala
🌏 Xakastap: xın
🌏 Altaylap: cara
🌏 Şor: kölen
🌍 Urumça: begen (beğen, beyen)
🌍 Karajče: bijen (begen, bijan)
🌍 Qrımçahça: begen
🌏 Soyot: ınaq tur
🌏 Tofalap: ekkisin''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "alike" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "словно" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "подобно" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "подобный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "в качестве" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "as" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "such as" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "similar to" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gibi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gıbı":
        bot.send_message(message.chat.id, '''🇬🇧 English: as, like {prep., adj.}, such as, similar to
🇷🇺 Русский: как, подобно, словно, в качестве
🇹🇷 Türkçe: gibi
🇦🇿 Türkcə: kimi
🇹🇲 Türkmençe: kimin, ýaly
🇺🇿 Oʻzbekcha: kabi
🇰🇿 Qazaqşa: sıyaqtı, sekildi
🇰🇬 Qırğızça: sıyaqtuu
🌏 Uyghurche: kebi
🌍 Tatarça: kebek
🌍 Başqortsa: hımaq, kewek
🌍 Çovaşla: pek (pak, kap), yevör
🌍 Qaraqalpaqsha: sıyaqlı
🌍 Qırımtatarca: kibi
🌍 Qumuqça: yimik, -day/-dey
🌍 Qaraçay-Malqar: kibik
🌍 Noğayşa: sekinli, -day/-dey
🌏 Sıbırca: şigelle, -tay/-täy
🌍 Gagauzça: gibi
🌏 Saqalī: kurduk
🌏 Dulgan-Hakalī: kördük, kaytak
🌏 Tıvalap: deg
🌏 Salırça: kama
🌏 Xakastap: çilî
🌏 Altaylap: çilep
🌏 Şor: -dığ/-dig
🌍 Urumça: kibi (gibi, kibik, yibik)
🌍 Karajče: kibik, -ley
🌍 Qrımçahça: kıbık
🌏 Soyot: şılıyı, değ
🌏 Tofalap: çılacı, değ (teğ)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "целкач" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "целковый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "целковой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "целковая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "целковое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рубль" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рублевый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рубли" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рублевая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ruble" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rouble":
        bot.send_message(message.chat.id, '''🇬🇧 English: rouble
🇷🇺 Русский: рубль [rubl'], целковый [tselkolvyy]
🇹🇷 Türkçe: ruble
🇦🇿 Türkcə: rubl, (uruːbəl) {dial.}
🇹🇲 Türkmençe: rubl, som {arch.}
🇺🇿 Oʻzbekcha: rubl
🇰🇿 Qazaqşa: sölkebay, som {arch.}
🇰🇬 Qırğızça: rubl
🌏 Uyghurche: rubli, som
🌍 Tatarça: sum, täñkä
🌍 Başqortsa: hum, täñkä
🌍 Çovaşla: tenkö, manet, sum
🌍 Qaraqalpaqsha: manat
🌍 Qırımtatarca: ruble, kümüş
🌍 Qumuqça: manat
🌍 Qaraçay-Malqar: som
🌍 Noğayşa: mänet
🌏 Sıbırca: mänit, täñkä, sum
🌍 Gagauzça: ruble, karbona
🌏 Saqalī: solkuobay
🌏 Dulgan-Hakalī: holkuobay
🌏 Tıvalap: tögerik
🌏 Salırça: rubl, lubu
🌏 Xakastap: salkovay, manit
🌏 Altaylap: salqoboy (salqay)
🌏 Şor: salqovay (salqovıy)
🌍 Urumça: ruble, kümüş
🌍 Karajče: riuble (ruble), kachkan, kiumiuš
🌍 Qrımçahça: kumış
🌏 Soyot: solhooboy
🌏 Tofalap: solhoovay''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сhristmas" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рождество" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рождественный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рождественский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rojdestvo" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "noel" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рожество" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "xmas" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "xxxsmas" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "noël" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nativity" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "milat yortusu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doğuş bayramı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kutsal doğuş":
        bot.send_message(message.chat.id, '''🇬🇧 English: сhristmas
🇷🇺 Русский: рождество [roždestvo]
🇹🇷 Türkçe: noel
🇦🇿 Türkcə: milad
🇹🇲 Türkmençe: roždestwo
🇺🇿 Oʻzbekcha: milod
🇰🇿 Qazaqşa: rojdestvo
🇰🇬 Qırğızça: rojdestvo
🌏 Uyghurche: rojistiwa
🌍 Tatarça: raştıwa
🌍 Başqortsa: raştıwa
🌍 Çovaşla: raştav
🌍 Qaraqalpaqsha: rojdestvo
🌍 Qırımtatarca: milât
🌍 Qumuqça: rojdestvo
🌍 Qaraçay-Malqar: rojdestvo
🌍 Noğayşa: rojdestvo
🌏 Sıbırca: rojdestvo
🌍 Gagauzça: kolada
🌏 Saqalī: orohuospa
🌏 Dulgan-Hakalī: roždestvo
🌏 Tıvalap: rojdestvo
🌏 Salırça: şeŋdan
🌏 Xakastap: kölede
🌏 Altaylap: rojdestvo
🌏 Şor: rojdestvo
🌍 Urumça: xurtoz-bayram
🌍 Karajče: roždestvo
🌍 Qrımçahça: rojdestvo
🌏 Soyot: rojdestvo
🌏 Tofalap: rojdestvo''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cap" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шапка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шапочный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шляпа" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шляпный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шапочная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шапочное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шапочные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шляпная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шляпное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шляпные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şapka" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şapke":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 13th c.): börk
🇬🇧 English: hat, cap
🇷🇺 Русский: шапка [shapka]
🇹🇷 Türkçe: şapka
🇦🇿 Türkcə: papaq
🇹🇲 Türkmençe: papak, telpek
🇺🇿 Oʻzbekcha: telpak, qalpoq
🇰🇿 Qazaqşa: börik, qalpaq
🇰🇬 Qırğızça: qalpaq, bapaq
🌏 Uyghurche: bök, telpek
🌍 Tatarça: bürek
🌍 Başqortsa: bürek, käpäs
🌍 Çovaşla: cölök, puxça
🌍 Qaraqalpaqsha: bórik, telpek
🌍 Qırımtatarca: qalpaq, papaq
🌍 Qumuqça: börk, papax
🌍 Qaraçay-Malqar: börk, papax
🌍 Noğayşa: börk, papaq
🌏 Sıbırca: pürek
🌍 Gagauzça: kalpak
🌏 Saqalī: bergehe
🌏 Dulgan-Hakalī: bergehe
🌏 Tıvalap: bört
🌏 Salırça: zorax
🌏 Xakastap: pörik
🌏 Altaylap: börük
🌏 Şor: pörük
🌍 Urumça: börk, xalpax
🌍 Karajče: biork, kalpak
🌍 Qrımçahça: qalpah
🌏 Soyot: bört
🌏 Tofalap: bört''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mısır" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "misir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "egypt" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "egipt" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "egyptian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "egiptian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "египет" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "йегипет" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "египетский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "египетская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "египетское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "египетские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "misiri" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "egypti":
        bot.send_message(message.chat.id, '''🇹🇷 Bitki anlamında "mısır" için "maize" veya "corn" yazın.
        
🇬🇧 English: Egypt
🇷🇺 Русский: Египет [Yegipet]
🇹🇷 Türkçe: Mısır
🇦🇿 Türkcə: Misir
🇹🇲 Türkmençe: Müsür
🇺🇿 Oʻzbekcha: Misr
🇰🇿 Qazaqşa: Mısır
🇰🇬 Qırğızça: Yegipet
🌏 Uyghurche: Misir
🌍 Tatarça: Misır
🌍 Başqortsa: Mısır
🌍 Çovaşla: Yegipet
🌍 Qaraqalpaqsha: Mısır
🌍 Qırımtatarca: Mısır
🌍 Qumuqça: Misri
🌍 Qaraçay-Malqar: Misir
🌍 Noğayşa: Misir
🌏 Sıbırca: Misır
🌍 Gagauzça: Mısır
🌏 Saqalī: Egïpet
🌏 Dulgan-Hakalī: Yegipet (Egïpet)
🌏 Tıvalap: Yegipet
🌏 Salırça: Misir
🌏 Xakastap: Yegîpet
🌏 Altaylap: Yegipet
🌏 Şor: Yegipet
🌍 Urumça: Misir
🌍 Karajče: Misir (Mysyr, Micri)
🌍 Qrımçahça: Mısır
🌏 Soyot: Yegîpet
🌏 Tofalap: Yegîpet
In Arabic: Misr''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "maize" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "corn" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "маис" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кукуруза" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kokoroz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kukuruz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kukuruza" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кукурузный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кукурузная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кукурузное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кукурузные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mısırbuğday" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mısırbuğda" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сахарная кукуруза" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кукуруза сахарная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "джугара" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dzhugara" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "джагара" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dzhagara" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "djagara" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jagara" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jugara" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mısır buğdası":
        bot.send_message(message.chat.id, '''🇬🇧 English: corn, maize
🇷🇺 Русский: кукуруза [kukuruza], маис [mais]
🇹🇷 Türkçe: mısır
🇦🇿 Türkcə: qarğıdalı, {dialects: qardalı, qarqundey, peyğəmbəri, məkə, hacıbuğda, sütül, kakruz}
🇹🇲 Türkmençe: mekgejöwen
🇺🇿 Oʻzbekcha: makkajoʻxori
🇰🇿 Qazaqşa: jügeri
🇰🇬 Qırğızça: jügörü
🌏 Uyghurche: qonaq (kömmiqonaq)
🌍 Tatarça: mäkkäy (Mäkkä bodayı), Misır bodayı, kukuruz
🌍 Başqortsa: Qäğbä boyðayı, kukuruz
🌍 Çovaşla: çakan tulo, kukkurus
🌍 Qaraqalpaqsha: mákke-júweri
🌍 Qırımtatarca: mısırboğday, afrata {dial.}
🌍 Qumuqça: habijay (habijday)
🌍 Qaraçay-Malqar: nartüx, jügeri
🌍 Noğayşa: närtük, äjibiyday
🌏 Sıbırca: Misır potay, kukuruza
🌍 Gagauzça: mısır, papşoy
🌏 Saqalī: kukurūza
🌏 Dulgan-Hakalī: kukuruza
🌏 Tıvalap: kukuruza, çoçak-taraa
🌏 Salırça: qonax, bogu
🌏 Xakastap: kukuruza
🌏 Altaylap: kukuruza
🌏 Şor: kukuruza
🌍 Urumça: misirboğday, lazut, örekebaş
🌍 Karajče: mysyr, basadohan
🌍 Qrımçahça: mısırboğday
🌏 Soyot: kukuruza
🌏 Tofalap: kukuruza''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şiş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shish" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şış" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ödem" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ödema" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "edema" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "swelling" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "edema" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fluid retention" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "brochette" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "skewer" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shampur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shampour" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шампур" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вертел" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вертело" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "китайские палочки" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "отек" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "опухоль" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şişik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "эдема":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): şiş (şış)
🇬🇧 English: I. skewer, brochette, shish II. swelling, edema, fluid retention
🇷🇺 Русский: I. шампур [shampur], вертел II. отёк, опухоль, шишка
🇹🇷 Türkçe: şiş
🇦🇿 Türkcə: şiş
🇹🇲 Türkmençe: çiş
🇺🇿 Oʻzbekcha: I. six II. shish
🇰🇿 Qazaqşa: I. ispara, istik II. isik
🇰🇬 Qırğızça: I. şiş II. şişik
🌏 Uyghurche: I. zix II. ishshiq
🌍 Tatarça: şeş
🌍 Başqortsa: şeş
🌍 Çovaşla: I. şampur II. şıso
🌍 Qaraqalpaqsha: I. is II. isik
🌍 Qırımtatarca: şiş
🌍 Qumuqça: I. çiş II. şişik
🌍 Qaraçay-Malqar: I. şiş (tiş) II. köbüw, köbgen, doğura, duqur
🌍 Noğayşa: I. sis II. sisik
🌏 Sıbırca: şeş
🌍 Gagauzça: şiş
🌏 Saqalī: I. ütehe II. ihï, iskeñ
🌏 Dulgan-Hakalī: I. ütehe II. ihï, iskeñ
🌏 Tıvalap: I. şiş II. ıjık
🌏 Salırça: çiş
🌏 Xakastap: sis
🌏 Altaylap: I. tiş II. tijik
🌏 Şor: I. şiş II. şijig
🌍 Urumça: şiş
🌍 Karajče: šiš (sis)
🌍 Qrımçahça: I. şiş II. şişık
🌏 Soyot: I. şîş I. ışıq
🌏 Tofalap: I. şîş I. ışıq''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shishkebab" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shish kebab" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shishkebap" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shish kebap" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shishkabab" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shish kabab" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "middle estern bbq" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шашлык" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шашлычный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шиш-кебаб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шиш-кабаб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шиш кебаб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шиш кабаб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шишкебаб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шишкабаб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шиш кебап" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шишкебап" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shahlyk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shashlik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şişkebab" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şişkebap" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şiş kebabı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şiş kebap" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şişlik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şış kebabi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şiş kebabi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şaşlık":
        bot.send_message(message.chat.id, '''🇬🇧 English: shish kebab
🇷🇺 Русский: шашлык [shashlyk]
🇹🇷 Türkçe: şiş kebabı
🇦🇿 Türkcə: şiş kabab, şişlik
🇹🇲 Türkmençe: çişlik
🇺🇿 Oʻzbekcha: sixkabob
🇰🇿 Qazaqşa: şaşlıq
🇰🇬 Qırğızça: şiş kebep
🌏 Uyghurche: zix kawipi
🌍 Tatarça: şaşlık
🌍 Başqortsa: şaşlık
🌍 Çovaşla: şaşlık
🌍 Qaraqalpaqsha: shashlık
🌍 Qırımtatarca: şiş kebabı, şaşlıq
🌍 Qumuqça: çişlik
🌍 Qaraçay-Malqar: şişlik (tişlik)
🌍 Noğayşa: sislik
🌏 Sıbırca: şaşlık
🌍 Gagauzça: şiş kebabı
🌏 Saqalī: üöler et
🌏 Dulgan-Hakalī: üöler et
🌏 Tıvalap: şişteen et
🌏 Salırça: çiş kaorou
🌏 Xakastap: sisteen ît
🌏 Altaylap: tiştegen et
🌏 Şor: şişteen et
🌍 Urumça: şaşlık
🌍 Karajče: šišlik (siślik)
🌍 Qrımçahça: şaşlıq
🌏 Soyot: şîştään et
🌏 Tofalap: şîştään et''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kebab" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kabab" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kabap" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kebap" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кебаб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кебеп" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кабаб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кабоб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кябаб" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кавап" :
        bot.send_message(message.chat.id, '''🇬🇧 English: kebab
🇷🇺 Русский: кебаб [kebab]
🇹🇷 Türkçe: kebap
🇦🇿 Türkcə: kabab
🇹🇲 Türkmençe: kebap
🇺🇿 Oʻzbekcha: kabob
🇰🇿 Qazaqşa: käwäp
🇰🇬 Qırğızça: kebep
🌏 Uyghurche: kawap
🌍 Tatarça: käbap
🌍 Başqortsa: käbab
🌍 Çovaşla: kebab
🌍 Qaraqalpaqsha: kábap
🌍 Qırımtatarca: kebap
🌍 Qumuqça: kabap
🌍 Qaraçay-Malqar: kebab
🌍 Noğayşa: kebap
🌏 Sıbırca: käbäp
🌍 Gagauzça: kebab
🌏 Saqalī: kebab
🌏 Dulgan-Hakalī: kebab
🌏 Tıvalap: kebab
🌏 Salırça: kaorou
🌏 Xakastap: kebab
🌏 Altaylap: kebab
🌏 Şor: kebab
🌍 Urumça: kebap
🌍 Karajče: kebab
🌍 Qrımçahça: kebab
🌏 Soyot: kebab
🌏 Tofalap: kebab''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "coin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moneta" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sikke" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "madeni para" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "монета" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "madenî para" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чекан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чеканная монета" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чеканной монетой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чеканая монета" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "звонкая монета" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "монетка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "madenı para" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "coın" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "demir para" :
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): yarmaq (yartmaq), bişi, benäk {small}
🇬🇧 English: coin
🇷🇺 Русский: монета [moneta] (чеканная монета)
🇹🇷 Türkçe: sikke, gümüş {silver}
🇦🇿 Türkcə: sikkə, dəmir pul
🇹🇲 Türkmençe: şaýy, zikge, teňňe {silver}
🇺🇿 Oʻzbekcha: tanga
🇰🇿 Qazaqşa: teŋge, mänet
🇰🇬 Qırğızça: moneta, tıyın {penny}
🌏 Uyghurche: tengge
🌍 Tatarça: täñkä
🌍 Başqortsa: täñkä
🌍 Çovaşla: tenke, manet {silver}
🌍 Qaraqalpaqsha: teńge
🌍 Qırımtatarca: manet, kümüş {silver}
🌍 Qumuqça: temir aqça, gümüş {silver}
🌍 Qaraçay-Malqar: uwaq açxa
🌍 Noğayşa: mänet, noqırat {silver}
🌏 Sıbırca: manet, kömöş {silver}
🌍 Gagauzça: mangır, left {gold, silver}
🌏 Saqalī: manńıat
🌏 Dulgan-Hakalī: manńıat
🌏 Tıvalap: çoos, möñgün {silver}
🌏 Salırça: kozı, ax helli
🌏 Xakastap: manit {silver}
🌏 Altaylap: möñün {silver}, tenke {silver, arch.}
🌏 Şor: moneta
🌍 Urumça: dämir pul, manat {gold}
🌍 Karajče: sikke, kiumiuš {silver}
🌍 Qrımçahça: quruş
🌏 Soyot: müngen, moneta
🌏 Tofalap: moneta''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "no longer" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "no more" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "more" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "более" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "больше" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "daha":
        bot.send_message(message.chat.id, '''🇬🇧 English: — {forms the comparative of the following adjective, adverb or particip}, no more, no longer, more= {"many" + affixes below (ex. "köbirek" – köp + -irek) or words below + "many" (ex. "daha çok", see "many"} 
🇷🇺 Русский:	более, больше= {слово "много" + аффиксы, написанные ниже позволят составить слово "больше" (напр. köbirek – köp + -irek),  если вместо аффикса написано слово, то оно идет первым (напр. daha çok) см. "много"}
🇹🇷 Türkçe: daha
🇦🇿 Türkcə: daha, -rax/-rəh (-raq/-rək) {dial.}
🇹🇲 Türkmençe: has, -rak/-räk
🇺🇿 Oʻzbekcha: -roq
🇰🇿 Qazaqşa: -raq/-req/-ıraq/-irek
🇰🇬 Qırğızça: -raaq/-reek/-rooq/-röök/-ıraaq/-ireek/-uraaq/-üröök
🌏 Uyghurche: -raq/-rek
🌍 Tatarça: -raq/-räk
🌍 Başqortsa: -raq/-räk/-ıraq/-eräk
🌍 Çovaşla: -rax/-rex
🌍 Qaraqalpaqsha: -raq/-req
🌍 Qırımtatarca: daa, -ça/-ca/-çe/-ce
🌍 Qumuqça: dahı da
🌍 Qaraçay-Malqar: biraz, -raq/-rek
🌍 Noğayşa: -raq/-req/-ıraq/-irek
🌏 Sıbırca: -raq/-räk
🌍 Gagauzça: taa
🌏 Saqalī: orduk
🌏 Dulgan-Hakalī: orduk
🌏 Tıvalap: ulam
🌏 Salırça: -rax/räx/-rıx/-rex
🌏 Xakastap: îleede, ulamox tıñ
🌏 Altaylap: onoñ, -lap/-lep/-löp/-tap/-tep/-töp
🌏 Şor: -araq
🌍 Urumça: daa, -rax/-rek, -ca/-ce
🌍 Karajče: daha (daa), -rach/-rek, -ča/-če
🌍 Qrımçahça: daa, -ca/-ce/-ça/-çe
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "solidarity" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "солидарность" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dayanışma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dayanisma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "единодушие":
        bot.send_message(message.chat.id, '''🇬🇧 English: solidarity
🇷🇺 Русский: солидарность
🇹🇷 Türkçe: dayanışma
🇦🇿 Türkcə: həmrəylik
🇹🇲 Türkmençe: raýdaşlyk
🇺🇿 Oʻzbekcha: birdamlik, hamjihatlik
🇰🇿 Qazaqşa: tilektestik
🇰🇬 Qırğızça: tilekteştik
🌏 Uyghurche: ittipaqliq
🌍 Tatarça: berdämlek, teläktäşlek
🌍 Başqortsa: teläktäşlek
🌍 Çovaşla: pörşuxoşlox
🌍 Qaraqalpaqsha: tilekleslik
🌍 Qırımtatarca: birdemlik
🌍 Qumuqça: ittifaqlıq
🌍 Qaraçay-Malqar: birinnetlilik
🌍 Noğayşa: birniyetlilik
🌏 Sıbırca: pertämnek
🌍 Gagauzça: dayanışmak
🌏 Saqalī: bïr sanālanī
🌏 Dulgan-Hakalī: bïr hanālanī
🌏 Tıvalap: çañgıs ep-setkildii
🌏 Salırça: ???
🌏 Xakastap: pir çöptig polğanı
🌏 Altaylap: bir küündü bolorı
🌏 Şor: pir çöptig polğanı
🌍 Urumça: birsözlük
🌍 Karajče: birsahys
🌍 Qrımçahça: bırdemlıq
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "solidary" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "солидарный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dayanışma içinde olan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dayanisma icinde olan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dayanışık" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dayanisik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "accomplice" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "солидарная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "единодушный":
        bot.send_message(message.chat.id, '''🇬🇧 English: solidary, accomplice
🇷🇺 Русский: солидарный
🇹🇷 Türkçe: dayanışık
🇦🇿 Türkcə: həmrəy
🇹🇲 Türkmençe: raýdaş
🇺🇿 Oʻzbekcha: birdam, hamjihat
🇰🇿 Qazaqşa: tilektes
🇰🇬 Qırğızça: tilekteş
🌏 Uyghurche: ittipaqli
🌍 Tatarça: berdäm, teläktäş
🌍 Başqortsa: teläktäş
🌍 Çovaşla: pörşuxoşlo
🌍 Qaraqalpaqsha: tilekles
🌍 Qırımtatarca: birdem
🌍 Qumuqça:	bir pikrulu
🌍 Qaraçay-Malqar: birinnetli
🌍 Noğayşa: birniyetli
🌏 Sıbırca: pertäm
🌍 Gagauzça: dayanışık
🌏 Saqalī: bïr sanālāq
🌏 Dulgan-Hakalī: bïr hanālāk
🌏 Tıvalap: çañgıs ep-setkildig
🌏 Salırça: ???
🌏 Xakastap: pir çöptig
🌏 Altaylap: bir küündü
🌏 Şor: pir çöptig
🌍 Urumça: birsözlü
🌍 Karajče: birsahysly, birsioźliu
🌍 Qrımçahça: bırdem
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "единомыслие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikirdaşlık" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фикердешлек" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фикердашлек" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdəşlek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdäşlek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdaşlık" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdeşlek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdeşlek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdeslek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdaşlık" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdaslek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fıkerdeslek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "agreement of opinion" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "like-mindedness" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "unanimity":
        bot.send_message(message.chat.id, '''🇬🇧 English: unanimity, like-mindedness
🇷🇺 Русский: единомыслие
🇹🇷 Türkçe: fikirdaşlık
🇦🇿 Türkcə: fikirdaşlıq
🇹🇲 Türkmençe: pikirdeşlik
🇺🇿 Oʻzbekcha: fikrdoshlik
🇰🇿 Qazaqşa: pikirlestik
🇰🇬 Qırğızça: pikirdeştik
🌏 Uyghurche: pikirdashliq
🌍 Tatarça: fikerdäşlek
🌍 Başqortsa: fekerðäşlek
🌍 Çovaşla: pörşuxoşlox
🌍 Qaraqalpaqsha: pikirleslik
🌍 Qırımtatarca: fikirdeşlik
🌍 Qumuqça: pikrudaşlıq
🌍 Qaraçay-Malqar: pikirdeşlik
🌍 Noğayşa: pikirdeslik
🌏 Sıbırca: pekertäşlek
🌍 Gagauzça: fikirdaşlık
🌏 Saqalī: bïr sanā
🌏 Dulgan-Hakalī: bïr hanā
🌏 Tıvalap: bir dömey bodaldıı
🌏 Salırça:	nöxörsidalıx
🌏 Xakastap: pir sağınğanı
🌏 Altaylap: bir sanaa-şüültelü bolorı
🌏 Şor: pir sağınğanı
🌍 Urumça: fikirdaşlıx
🌍 Karajče: fikirdašlyk
🌍 Qrımçahça: fıkırdaşlıh
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "единомышленник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikirdaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фикердеш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "единомысленный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "единомышленный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "фикердаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdəş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdäş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdeş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "единомышленик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdes" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "like-minded person" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fikerdas" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "like-minded" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "accomplice" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "like-minded-person" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "единомышленница":
        bot.send_message(message.chat.id, '''🇬🇧 English: like-minded, accomplice
🇷🇺 Русский: единомышленник
🇹🇷 Türkçe: fikirdaş
🇦🇿 Türkcə: fikirdeş
🇹🇲 Türkmençe: pikirdeş
🇺🇿 Oʻzbekcha: fikrdosh
🇰🇿 Qazaqşa: pikirles
🇰🇬 Qırğızça: pikirdeş
🌏 Uyghurche: pikirdash
🌍 Tatarça: fikerdäş
🌍 Başqortsa: fekerðäş
🌍 Çovaşla: pörşuxoşlo
🌍 Qaraqalpaqsha: pikirles
🌍 Qırımtatarca: fikirdeş
🌍 Qumuqça: pikrudaş
🌍 Qaraçay-Malqar: pikirdeş
🌍 Noğayşa: pikirdes
🌏 Sıbırca: pekertäş
🌍 Gagauzça: fikirdaş
🌏 Saqalī: bïr sanālāq
🌏 Dulgan-Hakalī: bïr hanālāk
🌏 Tıvalap: bir dömey üzeldig
🌏 Salırça: ???
🌏 Xakastap: tööy sağıstığ, pir sağıstığ
🌏 Altaylap: bir sanaa-şüültelü, tüñey sanaalu
🌏 Şor: pir sağıstığ
🌍 Urumça: fikirdaş
🌍 Karajče: fikirdaš
🌍 Qrımçahça: fıkırdaş
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "plasticine" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "plasticıne" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oyunhamur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oyunhamuru" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oyun-hamur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oyun-hamuru" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oyun hamur" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oyun hamuru" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "plastilin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пластилин" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "plastelin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пластелин" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "plastelina" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "plastilin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пластилиновый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пластелиновый":
        bot.send_message(message.chat.id, '''🇬🇧 English: plasticine
🇷🇺 Русский: пластилин [plastilin]
🇹🇷 Türkçe: oyun hamuru
🇦🇿 Türkcə: plastilin, oyun xəmiri
🇹🇲 Türkmençe: plastilin
🇺🇿 Oʻzbekcha: plastilin
🇰🇿 Qazaqşa: ermeksaz, somsoqta
🇰🇬 Qırğızça: plastilin
🌏 Uyghurche: plastilin, oyun xémiri
🌍 Tatarça: plastilin
🌍 Başqortsa: plastilin
🌍 Çovaşla: plastilin
🌍 Qaraqalpaqsha: plastilin
🌍 Qırımtatarca: plastilin
🌍 Qumuqça: plastilin
🌍 Qaraçay-Malqar: plastilin
🌍 Noğayşa: plastilin
🌏 Sıbırca: plastilin
🌍 Gagauzça: plastilin
🌏 Saqalī: plastilin
🌏 Dulgan-Hakalī: plastilin
🌏 Tıvalap: plastilin
🌏 Salırça: şoŋpini
🌏 Xakastap: plastîlîn
🌏 Altaylap: plastilin
🌏 Şor: plastilin
🌍 Urumça: plastilin
🌍 Karajče: plastilin
🌍 Qrımçahça: plastilin
🌏 Soyot: plastîlîn
🌏 Tofalap: plastîlîn''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oyun" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "game" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "игра" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "игровой" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gaming" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gamıng" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "геймерский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "игровая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "игровое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "игровые" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "геймерская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "геймерское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "геймерские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гра":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): oyun
🇬🇧 English: game
🇷🇺 Русский: игра
🇹🇷 Türkçe: oyun
🇦🇿 Türkcə: oyun
🇹🇲 Türkmençe: oýun
🇺🇿 Oʻzbekcha: oʻyin
🇰🇿 Qazaqşa: oyın
🇰🇬 Qırğızça: oyun
🌏 Uyghurche: oyun
🌍 Tatarça: uyın
🌍 Başqortsa: uyın
🌍 Çovaşla: voyo
🌍 Qaraqalpaqsha: oyın
🌍 Qırımtatarca: oyun
🌍 Qumuqça: oyun
🌍 Qaraçay-Malqar: oyun
🌍 Noğayşa: oyın
🌏 Sıbırca: uyın
🌍 Gagauzça: oyun
🌏 Saqalī: ōnńū
🌏 Dulgan-Hakalī: ōynū
🌏 Tıvalap: oyun
🌏 Salırça: oyun
🌏 Xakastap: oyın
🌏 Altaylap: oyın
🌏 Şor: oyun
🌍 Urumça: oyun
🌍 Karajče: ojun
🌍 Qrımçahça: oyın
🌏 Soyot: oyın
🌏 Tofalap: oyın''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тесто" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dough" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hamur":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): un
🇬🇧 English: dough
🇷🇺 Русский: тесто [testo]
🇹🇷 Türkçe: hamur
🇦🇿 Türkcə: xəmir, xamır {dial.}
🇹🇲 Türkmençe: hamyr
🇺🇿 Oʻzbekcha: xamir
🇰🇿 Qazaqşa: qamır
🇰🇬 Qırğızça: qamır
🌏 Uyghurche: xémir
🌍 Tatarça: qamır
🌍 Başqortsa: qamır
🌍 Çovaşla: çusta
🌍 Qaraqalpaqsha: qamır
🌍 Qırımtatarca: hamır
🌍 Qumuqça: xamur
🌍 Qaraçay-Malqar: tılı
🌍 Noğayşa: qamır, iylengen un
🌏 Sıbırca: qamır
🌍 Gagauzça: hamur
🌏 Saqalī: tieste
🌏 Dulgan-Hakalī: testo
🌏 Tıvalap: dalgan
🌏 Salırça: simen, kotan, aş
🌏 Xakastap: testa (teste)
🌏 Altaylap: teste
🌏 Şor: çeeste
🌍 Urumça: xamur (amur)
🌍 Karajče: chamur
🌍 Qrımçahça: hamur
🌏 Soyot: testo
🌏 Tofalap: testo''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ant" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ante" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "муравей" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "моровей" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "karınca" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "karinca" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "муравеи" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "formicidae" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "emmet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "моровеи" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "formica" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "муравьиный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "муравейный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "муравьиная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "муравинный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "муравиный":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴‎𐰆𐰢𐰆𐰺𐰽𐰍𐰀
🐺 Old Turkic (bef. 15th c.): qomursğa (qumursğa), çömäli (çümäli, çimäli), qarınça (qarınçaq)
🇬🇧 English: ant
🇷🇺 Русский: муравей
🇹🇷 Türkçe: karınca
🇦🇿 Türkcə: qarışqa, qarınca {arch.}
🇹🇲 Türkmençe: garynja
🇺🇿 Oʻzbekcha: chumoli, qumursqa
🇰🇿 Qazaqşa: qumırsqa (qırmısqa)
🇰🇬 Qırğızça: qumursqa
🌏 Uyghurche: chömüle (chümüle)
🌍 Tatarça: qırmısqa
🌍 Başqortsa: qırmıþqa (qımırþqa)
🌍 Çovaşla: kotko, xurt-kotko
🌍 Qaraqalpaqsha: qumırsqa
🌍 Qırımtatarca: qırmısqa (qımırsqa), qarınca
🌍 Qumuqça: qomursğa (xomursğa)
🌍 Qaraçay-Malqar: qumursxa, gumuljuq
🌍 Noğayşa: qumırsqa
🌏 Sıbırca: qımırısqa (qomrısqa, qımrısqa), küzrüm
🌍 Gagauzça: karımca
🌏 Saqalī: kımırdağas
🌏 Dulgan-Hakalī: hirikte
🌏 Tıvalap: kımıskayak
🌏 Salırça: qumusqan (qımısqan)
🌏 Xakastap: xımısxa (xumırsxa)
🌏 Altaylap: çımalı (çubalgı), küzürüm, qomısqaş, sarı sideş
🌏 Şor: qımısqaş (qımırtaş)
🌍 Urumça: ğarınca (xarınca), xırmısxa (xımırsxa)
🌍 Karajče: kyrmyska (kumurstka, kumuska, kymyrsak)
🌍 Qrımçahça: qırmısqa
🌏 Soyot: hımısqa
🌏 Tofalap: hımısqa''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oath" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "plight" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "vow" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "swear" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "божба" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "присяга" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "клятва" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yemin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yemın" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "andaman":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰦
🐺 Old Turkic (bef. 15th c.): ant (and)
🇬🇧 English: oath, plight, vow {n.}, swear {n.}
🇷🇺 Русский: клятва, присяга, божба
🇹🇷 Türkçe: yemin, ant
🇦🇿 Türkcə: and
🇹🇲 Türkmençe: ant, kasam
🇺🇿 Oʻzbekcha: ont, qasam
🇰🇿 Qazaqşa: ant, sert
🇰🇬 Qırğızça: ant, qasam
🌏 Uyghurche: qesem, ant
🌍 Tatarça: ant
🌍 Başqortsa: ant
🌍 Çovaşla: tupa, ant
🌍 Qaraqalpaqsha: ant, sert (shárt)
🌍 Qırımtatarca: ant, yemin
🌍 Qumuqça: ant
🌍 Qaraçay-Malqar: ant
🌍 Noğayşa: ant
🌏 Sıbırca: ant, wäqtä, şirt
🌍 Gagauzça: emin
🌏 Saqalī: andağar
🌏 Dulgan-Hakalī: andağar
🌏 Tıvalap: dañgırak
🌏 Salırça: şat, ant
🌏 Xakastap: xarğanıs, oballanıs, sîrt
🌏 Altaylap: antıq, çert (şert, şelt)
🌏 Şor: qarğanış, şerteniş
🌍 Urumça: ant, emin
🌍 Karajče: ant, jiemiń, sert, ebajy
🌍 Qrımçahça: ant, yemın, isfat
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to buy" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "buy" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to purchase" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "покупать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "купить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "купи" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "almak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "satınal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "satinal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "satinalmak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "satınalmak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "satın al" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "satin al" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "satin-al" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "satın-al" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "satın-almak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "satin-almak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "возьми" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "взять" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "брать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "приобрести" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "приобрети" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "обрети" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "обрести" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "take" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to take" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "забери" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "заберать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "забири" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "забирать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "get" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to get" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "recieve" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to recieve" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "receive" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to receive" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "получи" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "получай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "получать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бери":
        bot.send_message(message.chat.id, '''🇬🇧 In the Turkic languages, “to take” and “to buy” are the same word (al-), but to clarify the purchase “satın al” (“satıp al”) is used.
🇷🇺 В тюркских языках "брать" и "покупать" обозначается одним словом, но для уточнения о покупке говорят "satın al" ("satıp al").
🇹🇷 Türk lehcelerinde almak ve satın almak aynı kelimedir, lâkin belirtmek Türkiye türkçesindeki gibi için satın al (satıp al) kelimeleri kullanılır.

🇬🇧 English: II. take II. buy, purchase {v.} III. get IV. receive
🇷🇺 Русский: возьми, бери II. купи IV. получи
🇹🇷 Türkçe: al
🇦🇿 Türkcə: I. götür, ala {not verb}, al {very rarely} II. al (satın al)
🇹🇲 Türkmençe: al
🇺🇿 Oʻzbekcha: ol
🇰🇿 Qazaqşa: al
🇰🇬 Qırğızça: al
🌏 Uyghurche: al
🌍 Tatarça: al
🌍 Başqortsa: al
🌍 Çovaşla: il
🌍 Qaraqalpaqsha: al
🌍 Qırımtatarca: al
🌍 Qumuqça: al
🌍 Qaraçay-Malqar: al
🌍 Noğayşa: al
🌏 Sıbırca: al
🌍 Gagauzça: al
🌏 Saqalī: I. ıl II. ıl, atīlas
🌏 Dulgan-Hakalī: I. ıl II. atīlas
🌏 Tıvalap: al
🌏 Salırça: al
🌏 Xakastap: al
🌏 Altaylap: al
🌏 Şor: al
🌍 Urumça: al
🌍 Karajče: I. al II. satynal, kiustinal
🌍 Qrımçahça: al
🌏 Soyot: I. al II. satıp al
🌏 Tofalap: I. al II. satıp al''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to have" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to own" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "have" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "есть" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "имеется" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иметь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "имеются" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "имееться" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иметься" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "имеються" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "существует" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "существуют" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "var" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "I have" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "i have" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıhave" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "has" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to has" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "he has" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "she has" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "имется":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰉𐰺
🐺 Old Turkic (bef. 15th c.): bar
🇬🇧 English: there is, there are, to have, to own
🇷🇺 Русский: есть, имеется, имеются, существует, существуют
🇹🇷 Türkçe: var
🇦🇿 Türkcə: var
🇹🇲 Türkmençe: bar
🇺🇿 Oʻzbekcha: bor
🇰🇿 Qazaqşa: bar
🇰🇬 Qırğızça: bar
🌏 Uyghurche: bar
🌍 Tatarça: bar
🌍 Başqortsa: bar
🌍 Çovaşla: pur
🌍 Qaraqalpaqsha: bar
🌍 Qırımtatarca: bar
🌍 Qumuqça: bar
🌍 Qaraçay-Malqar: bar
🌍 Noğayşa: bar
🌏 Sıbırca: par
🌍 Gagauzça: var
🌏 Saqalī: bār
🌏 Dulgan-Hakalī: bār
🌏 Tıvalap: bar
🌏 Salırça: var (bar, par)
🌏 Xakastap: par
🌏 Altaylap: bar
🌏 Şor: par
🌍 Urumça: var (bar)
🌍 Karajče: bar
🌍 Qrımçahça: var
🌏 Soyot: bar
🌏 Tofalap: bar''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mongholia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "monggolia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "монголия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mongolia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moğolistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mogolistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mogolıstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moğolıstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moğolstan":
        bot.send_message(message.chat.id, '''🇬🇧 English: Mongolia
🇷🇺 Русский: Монголия [Mongoliya]
🇹🇷 Türkçe: Moğolistan
🇦🇿 Türkcə: Monqolustan, Moñğolstan {dial.}
🇹🇲 Türkmençe: Mongoliýa
🇺🇿 Oʻzbekcha: Moʻgʻuliston
🇰🇿 Qazaqşa: Moŋğoliya
🇰🇬 Qırğızça: Mongoliya
🌏 Uyghurche: Mongghuliye
🌍 Tatarça: Mongoliya
🌍 Başqortsa: Mongoliya
🌍 Çovaşla: Monxuli
🌍 Qaraqalpaqsha: Mongoliya
🌍 Qırımtatarca: Moğolistan
🌍 Qumuqça: Mongoliya
🌍 Qaraçay-Malqar: Monğol
🌍 Noğayşa: Moŋılstan
🌏 Sıbırca: Moñqorstan
🌍 Gagauzça: Mogolistan
🌏 Saqalī: Moğol Sire
🌏 Dulgan-Hakalī: Monguoliya
🌏 Tıvalap: Mool
🌏 Salırça: Muŋgu
🌏 Xakastap: Mool
🌏 Altaylap: Moñol
🌏 Şor: Mool
🌍 Urumça: Moğolistan
🌍 Karajče: Mongolija
🌍 Qrımçahça: Mongolistan
🌏 Soyot: Mongol Ulıs
🌏 Tofalap: Mongol Ulus''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "monghol" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "monggol" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "монгол" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mongol" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "moğol" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mogol" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "монголка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мынкол" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мын кол" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "монгольский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mongolian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "monggolian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mongholian":
        bot.send_message(message.chat.id, '''🇬🇧 English: Mongol
🇷🇺 Русский: монгол [mongol]
🇹🇷 Türkçe: Moğol
🇦🇿 Türkcə: monqol, məğul (مغول) {arch.}, moñğol {dial.}
🇹🇲 Türkmençe: mongol, mogol {arch.}
🇺🇿 Oʻzbekcha: moʻgʻul
🇰🇿 Qazaqşa: moŋğol
🇰🇬 Qırğızça: mongol
🌏 Uyghurche: Mongghul
🌍 Tatarça: mongol
🌍 Başqortsa: mongol
🌍 Çovaşla: monxul
🌍 Qaraqalpaqsha: mongol
🌍 Qırımtatarca: moğol
🌍 Qumuqça: mongol
🌍 Qaraçay-Malqar: monğollu
🌍 Noğayşa: moŋıl
🌏 Sıbırca: moñqor
🌍 Gagauzça: mogol
🌏 Saqalī: moğol
🌏 Dulgan-Hakalī: monguol
🌏 Tıvalap: mool
🌏 Salırça: muŋguzu
🌏 Xakastap: mool, moñul {dial.}
🌏 Altaylap: moñol
🌏 Şor: mool
🌍 Urumça: moğol
🌍 Karajče: mongol
🌍 Qrımçahça: mongol
🌏 Soyot: mongol
🌏 Tofalap: mongol''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "plane" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "airplane" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "aeroplane" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "самолет" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "аэроплан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "аироплан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "айроплан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "самолетный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "аэробус" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "uçak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tayare" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tayyare" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "aeroplan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "teyyare":
        bot.send_message(message.chat.id, '''🇬🇧 English: airplane, aeroplane
🇷🇺 Русский: самолёт [samolyot], аэроплан [aeroplan]
🇹🇷 Türkçe: uçak, tayyare
🇦🇿 Türkcə: təyyarə, uçaq
🇹🇲 Türkmençe: uçar
🇺🇿 Oʻzbekcha: tayyora, uchoq
🇰🇿 Qazaqşa: uşaq
🇰🇬 Qırğızça: uçaq
🌏 Uyghurche: ayrupilan, uchqu
🌍 Tatarça: oçqıç
🌍 Başqortsa: osqos
🌍 Çovaşla: vöcköc
🌍 Qaraqalpaqsha: ???
🌍 Qırımtatarca: uçaq, tayyare
🌍 Qumuqça: uçaq
🌍 Qaraçay-Malqar: uçxuç
🌍 Noğayşa: uşaq
🌏 Sıbırca: ocqoc
🌍 Gagauzça: uçak
🌏 Saqalī: kötör-āl
🌏 Dulgan-Hakalī: sömölüöt, garaplān
🌏 Tıvalap: ujar-xeme
🌏 Salırça: fici
🌏 Xakastap: samolyot, aeroplan
🌏 Altaylap: samolyot, aeroplan
🌏 Şor: samolyot, aeroplan
🌍 Urumça: uçax
🌍 Karajče: ???
🌍 Qrımçahça: uçaq, tayyare
🌏 Soyot: uşar-hemä
🌏 Tofalap: ceraplaan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "Iran" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "İran" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iran" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıran" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иран" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иранский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иранская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "irani" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıranı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iranian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıranıan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иранское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иранские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iranic":
        bot.send_message(message.chat.id, '''🇬🇧 English: Iran
🇷🇺 Русский: Иран [iran]
🇹🇷 Türkçe: İran
🇦🇿 Türkcə: İran
🇹🇲 Türkmençe: Eýran
🇺🇿 Oʻzbekcha: Eron
🇰🇿 Qazaqşa: İran
🇰🇬 Qırğızça: İran
🌏 Uyghurche: Iran
🌍 Tatarça: İran
🌍 Başqortsa: İran
🌍 Çovaşla: İran
🌍 Qaraqalpaqsha: Iran
🌍 Qırımtatarca: İran
🌍 Qumuqça: İran
🌍 Qaraçay-Malqar: İran
🌍 Noğayşa: İran
🌏 Sıbırca: İran
🌍 Gagauzça: İran
🌏 Saqalī: İrān
🌏 Dulgan-Hakalī: İrān
🌏 Tıvalap: İran
🌏 Salırça: İran
🌏 Xakastap: Îran
🌏 Altaylap: İran
🌏 Şor: İran
🌍 Urumça: İran
🌍 Karajče: Iran
🌍 Qrımçahça: İran
🌏 Soyot: Îran
🌏 Tofalap: Îran''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "afghanistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "afghanıstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "afganistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "afganıstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "афганистан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "афганский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "афганистанский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "авганистан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "авган" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "афган" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "авганский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "afghan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "afgan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "afghani" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "afganistani" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "afganıstanı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "afghanistani":
        bot.send_message(message.chat.id, '''🇬🇧 English: Afghanistan
🇷🇺 Русский: Афганистан [Afganistan]
🇹🇷 Türkçe: Afganistan
🇦🇿 Türkcə: Əfqanıstan
🇹🇲 Türkmençe: Owganystan
🇺🇿 Oʻzbekcha: Afgʻoniston
🇰🇿 Qazaqşa: Awğanstan
🇰🇬 Qırğızça: Ooğanstan
🌏 Uyghurche: Afghanistan
🌍 Tatarça: Äfğanstan
🌍 Başqortsa: Afğanstan
🌍 Çovaşla: Afganistan
🌍 Qaraqalpaqsha: Afǵanstan
🌍 Qırımtatarca: Afğanistan
🌍 Qumuqça: Afğan
🌍 Qaraçay-Malqar: Afgan
🌍 Noğayşa: Afğanistan
🌏 Sıbırca: Awğanstan
🌍 Gagauzça: Afganistan
🌏 Saqalī: Afganistān
🌏 Dulgan-Hakalī: Afganistān
🌏 Tıvalap: Afganistan
🌏 Salırça: Afxan
🌏 Xakastap: Afganîstan
🌏 Altaylap: Afganistan
🌏 Şor: Afganistan
🌍 Urumça: Afganistan
🌍 Karajče: Afganistan
🌍 Qrımçahça: Afğanistan
🌏 Soyot: Afganîstan
🌏 Tofalap: Afganîstan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "болгария" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "болгаристан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "булгария" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "булгаристан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bulgaristan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bulgarıstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bulgary" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bolgary" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bolgaristan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bolgarıstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bulgaria" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bolgaria" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bolgariya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bulgariya":
        bot.send_message(message.chat.id, '''🇬🇧 English: Bulgaria
🇷🇺 Русский: Болгария [Bolgariya]
🇹🇷 Türkçe: Bulgaristan
🇦🇿 Türkcə: Bolqarıstan, Bulğarıstan {dial.}
🇹🇲 Türkmençe: Bolgarystan
🇺🇿 Oʻzbekcha: Bolgariya
🇰🇿 Qazaqşa: Bolgariya
🇰🇬 Qırğızça: Bolgariya
🌏 Uyghurche: Bulghariye
🌍 Tatarça: Bolğarstan
🌍 Başqortsa: Bolğarstan
🌍 Çovaşla: Tonayci Polxarö
🌍 Qaraqalpaqsha: Bolgariya
🌍 Qırımtatarca: Bulğaristan
🌍 Qumuqça:	Bolğaristan
🌍 Qaraçay-Malqar: Bolgariya
🌍 Noğayşa: Bulğarstan
🌏 Sıbırca: Uŋ Polğar El
🌏 Salırça: Bulgariya, Bolcaliya
🌍 Gagauzça: Bulgariya
🌍 Urumça: Bulğaristan
🌍 Karajče: Bulgarija
🌍 Qrımçahça: Bulğaristan
🌏 Saqalī: Bolgariya
🌏 Dulgan-Hakalī: Bolgariya
🌏 Tıvalap: Bolgariya
🌏 Xakastap: Bolgarîya
🌏 Altaylap: Bolgariya
🌏 Şor: Bolgariya
🌏 Soyot: Bolgarîya
🌏 Tofalap: Bolgarîya''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bulgarian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bulğar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bolğar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bolgarian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "болгарин" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "болгарка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "булгар" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "болгар" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "болгарский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "болгарская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "болгарское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "болгарские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bolgar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bulgar":
        bot.send_message(message.chat.id, '''🇬🇧 English: Bulgarian
🇷🇺 Русский: болгар [bolgar]
🇹🇷 Türkçe: Bulgar
🇦🇿 Türkcə: bolqar, bulğar {dial.}
🇹🇲 Türkmençe: bolgar
🇺🇿 Oʻzbekcha: bolgar, bulgʻor {arch.}
🇰🇿 Qazaqşa: bolgar
🇰🇬 Qırğızça: bolgar
🌏 Uyghurche: Bulghar
🌍 Tatarça: bolğar
🌍 Başqortsa: bolğar
🌍 Çovaşla: polxar
🌍 Qaraqalpaqsha: bolgar
🌍 Qırımtatarca: bulğar
🌍 Qumuqça:	bolğar
🌍 Qaraçay-Malqar: bolgar
🌍 Noğayşa: bulğar
🌏 Sıbırca: uŋ polğar
🌏 Salırça: bulgar, Bolcaliya kişi
🌍 Gagauzça: tukan
🌍 Urumça: bulğar (bolğar)
🌍 Karajče: bulgar
🌍 Qrımçahça: bulğar
🌏 Saqalī: bolgar
🌏 Dulgan-Hakalī: bolgar
🌏 Tıvalap:	bolgar
🌏 Xakastap: bolgar
🌏 Altaylap: bolgar, pulgar {arch.}
🌏 Şor:	bolgar
🌏 Soyot: bolgar
🌏 Tofalap: bolgar''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ısrael" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "israel" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "isreal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "israil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ısraıl" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ısrail" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "israıl" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "израиль" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "исраил" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "исраиль" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "израил" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "израильский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "израильская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "исраэль" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "израэль" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "исраель" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "израель":
        bot.send_message(message.chat.id, '''🇬🇧 English: Israel
🇷🇺 Русский: Израиль [Izrail]
🇹🇷 Türkçe: İsrail
🇦🇿 Türkcə: İsrail
🇹🇲 Türkmençe: Ysraýyl
🇺🇿 Oʻzbekcha: Isroil
🇰🇿 Qazaqşa: İzrail
🇰🇬 Qırğızça: İzrail
🌏 Uyghurche: Israiliye
🌍 Tatarça: İsrail
🌍 Başqortsa: İzrail
🌍 Çovaşla: İzrail
🌍 Qaraqalpaqsha: İzrail
🌍 Qırımtatarca: İsrail
🌍 Qumuqça: İzrail
🌍 Qaraçay-Malqar: İsrail
🌍 Noğayşa: İzrail
🌏 Sıbırca: İsrail
🌍 Gagauzça: İsrail
🌏 Saqalī: İsrail
🌏 Dulgan-Hakalī: İzrail
🌏 Tıvalap: İzrail
🌏 Salırça: Yiseliye
🌏 Xakastap: Îzraîl
🌏 Altaylap: İzrail
🌏 Şor: İzrail
🌍 Urumça: İsrail
🌍 Karajče: Jisraelʻ (Israjelʻ)
🌍 Qrımçahça: Srel (İsrael)
🌏 Soyot: Îzraîl
🌏 Tofalap: Îzraîl''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jew" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jewish" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "juden" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jude" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jud" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yahudi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yahudı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yehudi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yehudı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cuhut" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çıfıt" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "çufut" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "еврей" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иудаист" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "иудей" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жид" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "израильтянин" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "израильтянка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жидовка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "жидовский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "еврейский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "еврейка":
        bot.send_message(message.chat.id, '''🇬🇧 English: Jew
🇷🇺 Русский: еврей [yevrey]
🇹🇷 Türkçe: Yahudi
🇦🇿 Türkcə: yahudi (yəhudi), cuhud
🇹🇲 Türkmençe: ýahudy, jöhit
🇺🇿 Oʻzbekcha: yahudiy, isroil
🇰🇿 Qazaqşa: jöyit
🇰🇬 Qırğızça: jööt
🌏 Uyghurche: Yehudi (Yehudiy), Johut
🌍 Tatarça: yähüd
🌍 Başqortsa: yähüd
🌍 Çovaşla: yevrey
🌍 Qaraqalpaqsha: jóhit
🌍 Qırımtatarca: yeudi, çufut
🌍 Qumuqça: yahudi, cuhut
🌍 Qaraçay-Malqar: çuwut
🌍 Noğayşa: yuwıt (jüyit)
🌏 Sıbırca: yäbräy (dyäbräy)
🌍 Gagauzça: çıfıt, yahudi
🌏 Saqalī: jebiriey (jerebey, jeberiey, yevrey), ısīt (isït, jıd)
🌏 Dulgan-Hakalī: jebiriey (jerebey, jeberiey, yevrey)
🌏 Tıvalap: yevrey
🌏 Salırça: yehudi
🌏 Xakastap: yevrey
🌏 Altaylap: yevrey
🌏 Şor: yevrey
🌍 Urumça: çufut (çofut, cıfut), yağudi (yahudu, yaudi), yudlu-şerifli, izrayil
🌍 Karajče: rabban, jisrajel'
🌍 Qrımçahça: çufut, yeudi, srel
🌏 Soyot: yevrey
🌏 Tofalap: yevrey''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to come" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "come" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "comes" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "приходи" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "приди" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gel" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gelmek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "приходить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "приезжай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "приехать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "приезжать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "прийти" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "прилететь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "прилети" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "приплыви" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "приплыть":
        bot.send_message(message.chat.id, '''🇷🇺 Данное слово означает "прийти" любым средством, поэтому переводы слов "приехать", "прилететь", "приплыть" и так далее будут одинаковыми.

🐺 Old Turkic (bef. 15th c.): kel
🇬🇧 English: come
🇷🇺 Русский: приходи, приди
🇹🇷 Türkçe: gel
🇦🇿 Türkcə: gəl
🇹🇲 Türkmençe: gel
🇺🇿 Oʻzbekcha: kel
🇰🇿 Qazaqşa: kel
🇰🇬 Qırğızça: kel
🌏 Uyghurche: kel
🌍 Tatarça: kil
🌍 Başqortsa: kil
🌍 Çovaşla: kil
🌍 Qaraqalpaqsha: kel
🌍 Qırımtatarca: kel
🌍 Qumuqça: gel
🌍 Qaraçay-Malqar: kel
🌍 Noğayşa: kel
🌏 Sıbırca: kil
🌍 Gagauzça: gel
🌏 Saqalī: kel
🌏 Dulgan-Hakalī: kel
🌏 Tıvalap: kel
🌏 Salırça: gel
🌏 Xakastap: kîl
🌏 Altaylap: kel
🌏 Şor: kel
🌍 Urumça: gäl (kel, gel, yel)
🌍 Karajče: kel
🌍 Qrımçahça: kel
🌏 Soyot: kel (gel)
🌏 Tofalap: kel''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hungari" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hungary" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "vengria" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hungaria" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "vengriya" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "венгрия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "macaristan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "macarstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "macarıstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "magyarország" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "magyarorszag":
        bot.send_message(message.chat.id, '''🇬🇧 English: Hungary
🇷🇺 Русский: Венгрия [Vengriya]
🇹🇷 Türkçe: Macaristan
🇦🇿 Türkcə: Macarıstan
🇹🇲 Türkmençe: Majarystan
🇺🇿 Oʻzbekcha: Mojariston
🇰🇿 Qazaqşa: Majarstan
🇰🇬 Qırğızça: Majarstan
🌏 Uyghurche: Majaristan
🌍 Tatarça: Macarstan
🌍 Başqortsa: Majarstan
🌍 Çovaşla: Xunkori
🌍 Qaraqalpaqsha: Vengriya
🌍 Qırımtatarca: Macaristan
🌍 Qumuqça: Majaristan
🌍 Qaraçay-Malqar: Majar
🌍 Noğayşa: Majarstan
🌏 Sıbırca: Majarstan
🌍 Gagauzça: Ungariya, Macaristan
🌏 Saqalī: Vengriya
🌏 Dulgan-Hakalī: Vengriya
🌏 Tıvalap: Vengriya
🌏 Salırça: Macaristan
🌏 Xakastap: Xungarîya
🌏 Altaylap: Vengriya
🌏 Şor: Vengriya
🌍 Urumça: Ungariya, Macaristan
🌍 Karajče: Madžaristan
🌍 Qrımçahça: Macaristan
🌏 Soyot: Vengrîya
🌏 Tofalap: Vengrîya
In Magyar: Magyarország''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hungarian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hungar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "vengr" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hungarıan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "venger" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "macar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "majar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "венгр" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "венгерский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "венгерская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "венгерское" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "венгерские" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "венгер" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "венгерка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "magyar":
        bot.send_message(message.chat.id, '''🇬🇧 English: Hungarian, Magyar
🇷🇺 Русский: венгр [vengr]
🇹🇷 Türkçe: Macar
🇦🇿 Türkcə: macar
🇹🇲 Türkmençe: majar
🇺🇿 Oʻzbekcha: mojar (mojor)
🇰🇿 Qazaqşa: majar
🇰🇬 Qırğızça: majar
🌏 Uyghurche: Majar
🌍 Tatarça: macar
🌍 Başqortsa: majar
🌍 Çovaşla: xunkor, maçar
🌍 Qaraqalpaqsha: vengr (venger)
🌍 Qırımtatarca: macar
🌍 Qumuqça: majar
🌍 Qaraçay-Malqar: majarlı
🌍 Noğayşa: majar
🌏 Sıbırca: majar
🌍 Gagauzça: ungar, macar
🌏 Saqalī: vengr (venger), majar {arhc.}
🌏 Dulgan-Hakalī: vengr (venger)
🌏 Tıvalap: vengr (venger)
🌏 Salırça: macar
🌏 Xakastap: xungar
🌏 Altaylap: vengr (venger)
🌏 Şor: vengr (venger)
🌍 Urumça: ungar, macar
🌍 Karajče: madžar
🌍 Qrımçahça: macar
🌏 Soyot: vengr (venger)
🌏 Tofalap: vengr (venger)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "давать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "подать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "подай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "отдай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "отдать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "подавать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "подавай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "отдавай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "отдавать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вручи" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вручить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to give" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "give" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ver" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "vermek":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): ber (ver)
🇬🇧 English: give!
🇷🇺 Русский: дай, отдай, подай, вручи
🇹🇷 Türkçe: ver
🇦🇿 Türkcə: ver
🇹🇲 Türkmençe: ber
🇺🇿 Oʻzbekcha: ber
🇰🇿 Qazaqşa: ber
🇰🇬 Qırğızça: ber
🌏 Uyghurche: ber
🌍 Tatarça: bir
🌍 Başqortsa: bir
🌍 Çovaşla: par
🌍 Qaraqalpaqsha: ber
🌍 Qırımtatarca: ber
🌍 Qumuqça: ber
🌍 Qaraçay-Malqar: ber
🌍 Noğayşa: ber
🌏 Sıbırca: pir
🌍 Gagauzça: ver
🌏 Saqalī: bier
🌏 Dulgan-Hakalī: bier
🌏 Tıvalap: beer
🌏 Salırça: ver (ber, per)
🌏 Xakastap: pîr
🌏 Altaylap: ber
🌏 Şor: per
🌍 Urumça: ver (ber)
🌍 Karajče: ver (ber)
🌍 Qrımçahça: ver
🌏 Soyot: ber
🌏 Tofalap: ber''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "but" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "however" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "how ever" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ama" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "amma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lakin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "läkin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lâkin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lakın" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "läkın" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lâkın" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "но" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == ", но" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == ",но" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == ", но " \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "однако" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "однакож" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "однакоже" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "однако ж" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "однако же":
        bot.send_message(message.chat.id, '''🇬🇧 English: but, however
🇷🇺 Русский: но, однако
🇹🇷 Türkçe: ama, lakin
🇦🇿 Türkcə: amma, lakin
🇹🇲 Türkmençe: emma
🇺🇿 Oʻzbekcha: ammo, biroq, lekin
🇰🇿 Qazaqşa: biraq
🇰🇬 Qırğızça: biroq
🌏 Uyghurche: lékin, amma (emma)
🌍 Tatarça: läkin, ämma
🌍 Başqortsa: läkin, ämmä
🌍 Çovaşla: capax, ismasa
🌍 Qaraqalpaqsha: biraq, lekin
🌍 Qırımtatarca: lâkin, amma
🌍 Qumuqça: tek, amma
🌍 Qaraçay-Malqar: amma, alay a
🌍 Noğayşa: ama
🌏 Sıbırca: ämmä, alayta
🌍 Gagauzça: ama, ne ki
🌏 Saqalī: ol da buollar, ol gınan baran, ol erēri
🌏 Dulgan-Hakalī: bagar (bahar)
🌏 Tıvalap: ındıg-daa bolza, ındıg bolza-daa, ınçalza-daa, ınçalzajok, ınçaarga, xarın, ınçanmıje
🌏 Salırça: lekin, dağı
🌏 Xakastap: çe
🌏 Altaylap: ce, andıy da bolzo
🌏 Şor: —
🌍 Urumça: ama (aman), ille (illem), lakin (lakim), tek
🌍 Karajče: amma, lakin (liakin), tek, alok, andok (andoch)
🌍 Qrımçahça: lâkin, amma
🌏 Soyot: harın, ıńcalsa ta
🌏 Tofalap: ıńcalsa ta, ındığ ta bolsa''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sonra" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soñra" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soŋra" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "after" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "later" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "позже" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "потом" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "после" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "затем" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "патом" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пожже":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): soŋ, ançıp (ınçıp), ötrü (ötürü), udu (uðu), üzä, andan (andın, antın), inğaru (ingärü), keyin (keðin, kedin, kidin, ken, kän, kin), kesrä (kisrä), basa
🇬🇧 English: later, after
🇷🇺 Русский: позже, потом, после, затем
🇹🇷 Türkçe: sonra
🇦🇿 Türkcə: sonra, sora {dial.}
🇹🇲 Türkmençe: soň, soňra
🇺🇿 Oʻzbekcha: keyin, soʻng, soʻngra
🇰🇿 Qazaqşa: keyin, soŋ, soŋıra
🇰🇬 Qırğızça: kiyin, soŋ, anan
🌏 Uyghurche: kéyin (kiyin), ize, en'gize
🌍 Tatarça: annarı, soñ, soñraq
🌍 Başqortsa: aðaq, aðaqtan, huñ, huñınan
🌍 Çovaşla: vara, irtsen {v.}
🌍 Qaraqalpaqsha: keyin, soń, sońıraq
🌍 Qırımtatarca: soñ, soñra
🌍 Qumuqça: soñ, soñra
🌍 Qaraçay-Malqar: sora, artda
🌍 Noğayşa: soŋ, soŋıraq, özek
🌏 Sıbırca: suñ, suñnan
🌍 Gagauzça: sora
🌏 Saqalī: qoyut, onton, kenniki, kelin
🌏 Dulgan-Hakalī: koyut, onton
🌏 Tıvalap: oon, soonda, söölünde
🌏 Salırça: soŋ, arcı
🌏 Xakastap: soonañ, oray
🌏 Altaylap: kiyninde, soñında, soondo
🌏 Şor: anañ, soonda
🌍 Urumça: sora
🌍 Karajče: son, sonra (sondra, sondrach)
🌍 Qrımçahça: son, soñra
🌏 Soyot: soŋ, soonda
🌏 Tofalap: soŋ, soonda''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "место" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "местность" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "грунт" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "земля" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "почва" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "локация" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "location" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "place" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ground" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "grount" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "earth" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eardh" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "terra" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yer" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "toprak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "torpak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yerküre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yerküresi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yer küre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "landing" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "landings" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "land":
        bot.send_message(message.chat.id, '''🇬🇧 English: I. location, place II. ground, land, earth, soil III. Earth {planet Terra}
🇷🇺 Русский: место ~ местность ~ земля ~ почва III. Земля
🇹🇷 Türkçe: yer ~ toprak III. Dünya, Yerküre
🇦🇿 Türkcə: yer ~ torpaq III. Yer
🇹🇲 Türkmençe: orun ~ ýer ~ toprak III. Ýer
🇺🇿 Oʻzbekcha: joy, oʻrin ~ yer ~ tuproq III. Yer
🇰🇿 Qazaqşa: orın ~ jer ~ topıraq III. Jer
🇰🇬 Qırğızça: orun ~ jay ~ jer ~ topuraq III. Jer
🌏 Uyghurche: orun, jay ~ yer ~ tupraq III. Yer
🌍 Tatarça: urın ~ cir ~ tufraq III. Cir
🌍 Başqortsa: urın ~ yer ~ tupraq III. Yer
🌍 Çovaşla: cör ~ topra III. Cör
🌍 Qaraqalpaqsha: orın ~ jay ~ jer ~ topıraq III. Jer
🌍 Qırımtatarca: yer~ topraq III. Yer, Dünya, Zemin
🌍 Qumuqça: yer ~ topuraq III. Yer, Dünya
🌍 Qaraçay-Malqar: orun ~ jer ~ topuraq III. Jer
🌍 Noğayşa: orın ~ yer ~ topıraq III. Yer
🌏 Sıbırca: urın ~ yer ~ tupraq ~ Yer
🌍 Gagauzça: er (yer) ~ topraq III. Er (Yer), Dünnä
🌏 Saqalī: sir ~ buor III. Sir
🌏 Dulgan-Hakalī: hir ~ buor III. Hir
🌏 Tıvalap: orun ~ çer ~ dovuraq III. Çer
🌏 Salırça: orın ~ yer ~ torax III. Yer, Zimin
🌏 Xakastap: orın ~ çîr ~ tobırax III. Çîr
🌏 Altaylap: ordı ~ cer ~ tobraq III. Cer
🌏 Şor: orın ~ çer ~ tobraq III. Çer
🌍 Urumça: orun ~ yer ~ toprax III. Yer
🌍 Karajče: orun ~ jer ~ toprach (toprak) III. 
🌍 Qrımçahça: orın ~ yer ~ toprah III. Yer
🌏 Soyot: orın ~ çer (cer) ~ tohıraq III. Çer (Cer)
🌏 Tofalap: orun ~ çer ~ topraq III. Çer''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "en" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "eni" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "width" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "witdh" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "most" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "best" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "biggest" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bigest" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "worst" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ширина" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "самый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "самая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "самое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "самые" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "превосходная степень" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "наи-" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "наиболее" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "наилучший" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лучший" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лучшая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лучшее" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лучшие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "линейный размер":
        bot.send_message(message.chat.id, '''🇬🇧 English: I. width II. most {~st: biggest, fastest etc}
🇷🇺 Русский: I. ширина II. самый {превосходная степень}, наиболее
🇹🇷 Türkçe: en
🇦🇿 Türkcə: I. en II. ən
🇹🇲 Türkmençe: I. in II. iň
🇺🇿 Oʻzbekcha: I. en II. eng
🇰🇿 Qazaqşa: I. en II. eŋ
🇰🇬 Qırğızça: I. en II. eŋ
🌏 Uyghurche: I. en II. eng
🌍 Tatarça: iñ
🌍 Başqortsa: iñ
🌍 Çovaşla: I. an II. çon, çi
🌍 Qaraqalpaqsha: I. en II. eń
🌍 Qırımtatarca: I. en II. eñ
🌍 Qumuqça: I. en II. iñ
🌍 Qaraçay-Malqar: I. en II. em
🌍 Noğayşa: I. en II. eŋ
🌏 Sıbırca: iñ
🌍 Gagauzça: en
🌏 Saqalī: I. ketite II. orduk
🌏 Dulgan-Hakalī: I. ien II. muñ
🌏 Tıvalap: I. delgemi II. eñ
🌏 Salırça: I. en II. xutu (xudu), -cux {yaxşıcux - best}, -tan ~ (-tän ~) {yaxşıtan yaxşı - best}
🌏 Xakastap: I. în II. îñ
🌏 Altaylap: I. en II. eñ
🌏 Şor: I. en II. eñne
🌍 Urumça: I. en II. eñ (en)
🌍 Karajče: ėn
🌍 Qrımçahça: I. en II. eñ
🌏 Soyot: I. en II. eñ
🌏 Tofalap: I. en II. eñ''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to want" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to wish" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хотеть" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "wants" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хоти" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "желать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "желай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "просить" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "проси" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iste" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "istemek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıste" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıstemek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dile" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dilemek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dıle" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dılemek":
        bot.send_message(message.chat.id, '''🇬🇧 Also in the Turkic languages the verb "come" instead of "want" is often used (for example, "he wants to sleep" - "yatmağı gəlir")
🇷🇺 Также в тюркских языках часто используется глагол "приходить" вместо "хотеть", (например "он хочет спать" – "yatmağı gəlir")

🇬🇧 English: want! wish!
🇷🇺 Русский: хоти! желай! проси!
🇹🇷 Türkçe: iste, dile
🇦🇿 Türkcə: istə, dilə
🇹🇲 Türkmençe: isle
🇺🇿 Oʻzbekcha: ista, tila, xohla
🇰🇿 Qazaqşa: qala, tile
🇰🇬 Qırğızça: qaala, tile
🌏 Uyghurche: xala, iste
🌍 Tatarça: telä
🌍 Başqortsa: telä
🌍 Çovaşla: yolon, köle, sun
🌍 Qaraqalpaqsha: qále, tile
🌍 Qırımtatarca: iste, tile {wish smb smth}
🌍 Qumuqça: süy, iste {arch.}
🌍 Qaraçay-Malqar: süy, talpır, itinir, izle {wish smb smth}
🌍 Noğayşa: tile, süy
🌏 Sıbırca: telä
🌍 Gagauzça: iste
🌏 Saqalī: bağar
🌏 Dulgan-Hakalī: bagar
🌏 Tıvalap: -(ı)ksa/-(i)kse, küze
🌏 Salırça: xala
🌏 Xakastap: xın, sağın
🌏 Altaylap: küünze
🌏 Şor:	sana, qın
🌍 Urumça: ste (iste), tile (dile)
🌍 Karajče: iste, kile (klie)
🌍 Qrımçahça: ste
🌏 Soyot: -(ı)ksa/-(î)ksä
🌏 Tofalap: turula''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bitig" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bitik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "betik" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "битиг" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бичиг" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "книга" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "книжка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "книженция" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "book" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kitab" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kitap":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): bitig {+ writing, writ, letter, document} {biti- from chinese}, nom {sogdian loanword}, kitab {arab loanword}
🇬🇧 English: book
🇷🇺 Русский: книга [kniga]
🇹🇷 Türkçe: kitap, betik {+ writing, writ, letter, document}, bitik {dial.}
🇦🇿 Türkcə: kitab, betik {purism, non-dictionary word}
🇹🇲 Türkmençe: kitap
🇺🇿 Oʻzbekcha: kitob
🇰🇿 Qazaqşa: kitap
🇰🇬 Qırğızça: kitep, biçik {arch. + writing, writ, letter, document}, nom {non-dictionary word}
🌏 Uyghurche: kitap, pütük {+ writing, writ, letter, document}
🌍 Tatarça: kitap, bitek {arch. + writing, writ, letter, document}
🌍 Başqortsa: kitap
🌍 Çovaşla: köneke {knögge <- kniga}
🌍 Qaraqalpaqsha: kitap
🌍 Qırımtatarca: kitap
🌍 Qumuqça: kitap
🌍 Qaraçay-Malqar: kitab
🌍 Noğayşa: kitap
🌏 Sıbırca: kitap, picek
🌍 Gagauzça: kitap, kiyat (kiat) {+ paper, letter}
🌏 Saqalī: kinige (kińïge), sul tuos {arch.}, suruk {arch.}
🌏 Dulgan-Hakalī: kinige (kinïge, knige)
🌏 Tıvalap: nom
🌏 Salırça: kitap (kitab, kitip)
🌏 Xakastap: kînde, piçik {arch.}, xam {arch.}
🌏 Altaylap: biçik {+ writing, writ, scripture, certificate}
🌏 Şor: nom
🌍 Urumça: kitap, kiat (kağat) {+ paper, letter, document}
🌍 Karajče: kytab (kitab), bitik {+ writing, writ, letter, document}, jazmach {+ writing, writ, letter, document}, jazyš {+ writing, writ, letter, document}
🌍 Qrımçahça: kıtab (kitab), sefer, humaş (+ bible)
🌏 Soyot: nom
🌏 Tofalap: hineek''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бабка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бабушка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бабуся" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бабу" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gramdmother" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "grand mother" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "grand-mother" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nine" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "nene" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "büyükanne" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "büyük ana" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "büyükana" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "büyük-anne" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "granny" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "grandma" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "büyük-ana" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gammy" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "büyük anne":
        bot.send_message(message.chat.id, '''* {p.} — paternal, по отцу, babasının annesi, {m.} — maternal, по матери, annesinin annesi
        
🇬🇧 English: grandmother
🇷🇺 Русский: бабушка
🇹🇷 Türkçe: büyükanne, nine (nene)
🇦🇿 Türkcə: nənə
🇹🇲 Türkmençe: ene, mama
🇺🇿 Oʻzbekcha: buvi (bibi)
🇰🇿 Qazaqşa: äje, ulı şeşe, apa
🇰🇬 Qırğızça: çoŋ ene {p.}, tay ene {m.}
🌏 Uyghurche: moma (muma)
🌍 Tatarça: äbi, däw äni
🌍 Başqortsa: öläsäy, qartäsäy {p.}
🌍 Çovaşla: pappi, nyanne, asanne (aslo anne) {p.}, apay (apa, epi) {p.}, mami (mama, mamak, monami, mamu, mamoşo) {p.}, kukamay {m.}
🌍 Qaraqalpaqsha: áje, mama-sheshe, apa
🌍 Qırımtatarca: qartana (kata), büyükana (bita)
🌍 Qumuqça: ullu ana
🌍 Qaraçay-Malqar: qart ana, amma
🌍 Noğayşa: äye, ene, üyken ana
🌏 Sıbırca: qartinä (qartnä), nänä (önnä)
🌍 Gagauzça: mali
🌏 Saqalī: ebe, ebe emēqsin
🌏 Dulgan-Hakalī: emēksin
🌏 Tıvalap: kırgan-ava, ene
🌏 Salırça: xaca (haca), nina
🌏 Xakastap: uluğ ice (ülce) {p.}, aaca {p.}, tay ice (teyce) {m.}
🌏 Altaylap: caana (caanaq) {p.}, qarğan ene {p.}, taay ene (tayna) {m.}
🌏 Şor: üüçe {p.}, nanek {m.}
🌍 Urumça: äbä, bukana (bökene), xartana
🌍 Karajče: inna (nene)
🌍 Qrımçahça: pekana
🌏 Soyot: qırğan-ava
🌏 Tofalap: qırğan-aba, enê''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "spring" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "springtime" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ilkyaz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ilk yaz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ılkyaz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ilkbahar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ılkbahar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ilk bahar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ılk bahar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bahar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "весна" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "весенний" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "весенняя" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "весеннее" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "весенние" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "vernal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ilk-bahar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "spring time":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): yaz
🇬🇧 English: spring
🇷🇺 Русский: весна
🇹🇷 Türkçe: ilkbahar, ilkyaz, bahar
🇦🇿 Türkcə: yaz, bahar
🇹🇲 Türkmençe: ýaz, bahar
🇺🇿 Oʻzbekcha: bahor, koʻklam
🇰🇿 Qazaqşa: köktem, jazğıturım {arch.}
🇰🇬 Qırğızça: jaz
🌏 Uyghurche: bahar, eteyaz (etiyaz), purjun, köklem
🌍 Tatarça: yaz
🌍 Başqortsa: yað
🌍 Çovaşla: cur, curkunne
🌍 Qaraqalpaqsha: kóklem, báhár
🌍 Qırımtatarca: baar
🌍 Qumuqça: yaz, yazbaş, yazlıq
🌍 Qaraçay-Malqar: jaz
🌍 Noğayşa: yazlıq
🌏 Sıbırca: yas
🌍 Gagauzça: ilkyaz, bahar
🌏 Saqalī: sās
🌏 Dulgan-Hakalī: hās
🌏 Tıvalap: ças
🌏 Salırça: yaz
🌏 Xakastap: çasxı, ças
🌏 Altaylap: cas
🌏 Şor: çasqı
🌍 Urumça: yazbaş (yazbaşı), baar (bayır)
🌍 Karajče: jazbašy, bahar
🌍 Qrımçahça: baar
🌏 Soyot: ças (cas)
🌏 Tofalap: ças''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "autumn" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "autunm" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "the fall" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fall" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "güz" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "falltime" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fall time" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "autum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "autumn time" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "autumntime" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "autumnal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fallnal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "осень" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "осенний" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "осенняя" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "осеннее" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "осенние" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "son-bahar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е').replace(' ', '') == "sonbahar":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): küz
🇬🇧 English: autumn, fall
🇷🇺 Русский: осень
🇹🇷 Türkçe: sonbahar, güz
🇦🇿 Türkcə: güz, payız
🇹🇲 Türkmençe: güýz
🇺🇿 Oʻzbekcha: kuz
🇰🇿 Qazaqşa: küz
🇰🇬 Qırğızça: küz
🌏 Uyghurche: küz
🌍 Tatarça: köz
🌍 Başqortsa: köð
🌍 Çovaşla: kör, körkunne
🌍 Qaraqalpaqsha: gúz
🌍 Qırımtatarca: küz
🌍 Qumuqça: güz
🌍 Qaraçay-Malqar: küz, qaç
🌍 Noğayşa: küz
🌏 Sıbırca: kös
🌍 Gagauzça: güz
🌏 Saqalī: kühün (küsün), küs {arch.}
🌏 Dulgan-Hakalī: kühün
🌏 Tıvalap: küs
🌏 Salırça: guz
🌏 Xakastap: küs, küskü
🌏 Altaylap: küs
🌏 Şor: küskü
🌍 Urumça: güz (küz)
🌍 Karajče: kiuź
🌍 Qrımçahça: küz
🌏 Soyot: küs
🌏 Tofalap: küs''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dragon" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "драгон" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "drakon" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дракон" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "драконий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "драконья" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "драконье" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "драконьи" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ejder" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ejderha" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ajderha" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "evreğen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зилант" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зилент":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): yel bükä, loŋ (luu, lū)
🇬🇧 English: dragon
🇷🇺 Русский: дракон [drakon]
🇹🇷 Türkçe: ejderha
🇦🇿 Türkcə: əjdaha
🇹🇲 Türkmençe: aždarha
🇺🇿 Oʻzbekcha: ajdaho (ajdarho, ajdar)
🇰🇿 Qazaqşa: aydahar (ajdaha)
🇰🇬 Qırğızça: ajıdaar
🌏 Uyghurche: ejdiha (hejdiha, ejdar)
🌍 Tatarça: ajdaha, läw
🌍 Başqortsa: ajdaha
🌍 Çovaşla: actaha, yuxxa, cölen (vöre cölen)
🌍 Qaraqalpaqsha: aydarha
🌍 Qırımtatarca: ajderha
🌍 Qumuqça: ajdaha
🌍 Qaraçay-Malqar: ullu jılan, ajdahan {arch.}
🌍 Noğayşa: azdaa
🌏 Sıbırca: äştäğı (äştağı)
🌍 Gagauzça: ajder, zın, evrem
🌏 Saqalī: luo (luo qān), uot moğoy
🌏 Dulgan-Hakalī: uot moñoy
🌏 Tıvalap: ulu
🌏 Salırça: poğınıx, luŋ
🌏 Xakastap: moos, cır çılan, xuuğulğan, çîlbigen
🌏 Altaylap: ulu (uulu, uluu)
🌏 Şor: ???
🌍 Urumça: ajder (ajdar)
🌍 Karajče: ačdaha (adžydahyr)
🌍 Qrımçahça: ajderha
🌏 Soyot: luu
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хаан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "каган" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хакан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хаган" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ханский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qaghan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qagan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qağan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "khakan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "khaghan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "khan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kağan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hakan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "han" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "xan":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰴𐰍𐰣‎
🐺 Old Turkic (bef. 15th c.): xan, qağan
🇬🇧 English: khan, qaghan, khagan
🇷🇺 Русский: хан, каган, хаган
🇹🇷 Türkçe: han, kağan, hakan
🇦🇿 Türkcə: xan, xaqan
🇹🇲 Türkmençe: han, kagan
🇺🇿 Oʻzbekcha: xon, xoqon, qagʻan
🇰🇿 Qazaqşa: han, qağan
🇰🇬 Qırğızça: xan, qağan
🌏 Uyghurche: xan, qaghan, xaqan
🌍 Tatarça: xan, qağan, qahan
🌍 Başqortsa: xan, qağan
🌍 Çovaşla: xun, xukon, xakan, kagan
🌍 Qaraqalpaqsha: xan, qaǵan
🌍 Qırımtatarca: han, haqan
🌍 Qumuqça: xan, xaqan
🌍 Qaraçay-Malqar: xan, qağan
🌍 Noğayşa: xan, qağan
🌏 Sıbırca: qan, qağan
🌏 Salırça: xan, kağan, kahan
🌍 Gagauzça: han, kagan
🌍 Urumça: xan, xagan
🌍 Karajče: chan, chagan
🌍 Qrımçahça: han, haqan
🌏 Saqalī: qān
🌏 Dulgan-Hakalī: kān
🌏 Tıvalap: xaan
🌏 Xakastap: xan
🌏 Altaylap: qaan
🌏 Şor: xan
🌏 Soyot: haan
🌏 Tofalap: haan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yarasa" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "the bat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "a bat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gecekuşu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gece kuşu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "летучая мышь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "летучаямышь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "нетопырь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кожан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chiroptera" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "microchiroptera" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "microbat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кажан":
        bot.send_message(message.chat.id, '''‎🐺 Old Turkic (bef. 15th c.): yarısa (yersgü, aya yersgü)
🇬🇧 English: the bat
🇷🇺 Русский: летучая мышь
🇹🇷 Türkçe: yarasa, gece kuşu
🇦🇿 Türkcə: yarasa, şəbpərə, gecəquşu
🇹🇲 Türkmençe: ýarganat (ýarkanat, ýerkanat)
🇺🇿 Oʻzbekcha: koʻrshapalak, yorqanot
🇰🇿 Qazaqşa: jarqanat (jarğanat)
🇰🇬 Qırğızça: jarğanat
🌏 Uyghurche: shepireng (shepereng)
🌍 Tatarça: yarqanat
🌍 Başqortsa: yarğanat
🌍 Çovaşla: cerci (cara cerci)
🌍 Qaraqalpaqsha: jarǵanat
🌍 Qırımtatarca: yelqanat (yarqanat)
🌍 Qumuqça: warqanat, geçequş
🌍 Qaraçay-Malqar: bittir
🌍 Noğayşa: yarğanat
🌏 Sıbırca: yarısqı, yabalaq (tön yabalaq), yaruqanat
🌏 Salırça: yarasan (yarasen)
🌍 Gagauzça: yarasa (yarasa kuşu)
🌍 Urumça: gecä uçan sıçan
🌍 Karajče: jarykanat (jarykanatly, jeri-kanaty), gedžekušu
🌍 Qrımçahça: gecekuşı
🌏 Saqalī: kınattāq kutuyaq, sarıı kınat
🌏 Dulgan-Hakalī: harıı kınat
🌏 Tıvalap: çaskı
🌏 Xakastap: çarxanat
🌏 Altaylap: carğanat
🌏 Şor: çarğanat
🌏 Soyot: casqa
🌏 Tofalap: çapqış''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "birthday" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "birth day" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "day of birth" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yaş günü" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yaşgünü" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yaş gün" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yaşgün" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yaşı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doğum günü" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doğumgünü" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doğum gün" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "doğumgün" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "деньрождения" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "день рождение" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "деньрождение" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "деньрожденье" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "день рожденье" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "день рожденья" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "деньрожденья" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "днюха" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "именины" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "день рождения" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "др":
        bot.send_message(message.chat.id, '''🇬🇧 English: birthday
🇷🇺 Русский: день рождения
🇹🇷 Türkçe: doğum günü, yaş günü
🇦🇿 Türkcə: I. ad günü, yaşı II. doğum günü {day of birth}
🇹🇲 Türkmençe: doglan güni
🇺🇿 Oʻzbekcha: tugʻilan kun
🇰🇿 Qazaqşa: tuwğan kün
🇰🇬 Qırğızça: tuulğan künü
🌏 Uyghurche: tughulghan küni
🌍 Tatarça: tuğan köne
🌍 Başqortsa: tıwğan kön
🌍 Çovaşla: tovan kun
🌍 Qaraqalpaqsha: tuwılǵan kúni
🌍 Qırımtatarca: doğğan künü
🌍 Qumuqça: tuwğan günü
🌍 Qaraçay-Malqar: tuwğan kün
🌍 Noğayşa: tuwğan küni
🌏 Sıbırca: towğan köne
🌏 Salırça: doğgan gün, doğgusi günü
🌍 Gagauzça: duuma günü, yaşı
🌍 Urumça: doğan kün
🌍 Karajče: tuvhan kiuniu
🌍 Qrımçahça: doğan künı
🌏 Saqalī: törȫbüt kün
🌏 Dulgan-Hakalī: törȫbüt küne
🌏 Tıvalap: törüttengen xünü
🌏 Xakastap: töreen küni
🌏 Altaylap: çıqqan kün
🌏 Şor: şıqqan kün
🌏 Soyot: törêen hünü
🌏 Tofalap: törään hünü''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "знай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "знать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ведай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ведать" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "умей" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "уметь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "know" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to know" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "to know how" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "know how" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bil" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bilmek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bıl" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bılmek":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰋𐰃𐰠
🐺 Old Turkic (bef. 15th c.): bil
🇬🇧 English: know!
🇷🇺 Русский: знай! умей!
🇹🇷 Türkçe: bil
🇦🇿 Türkcə: bil
🇹🇲 Türkmençe: bil
🇺🇿 Oʻzbekcha: bil
🇰🇿 Qazaqşa: bil
🇰🇬 Qırğızça: bil
🌏 Uyghurche: bil
🌍 Tatarça: bel
🌍 Başqortsa: bel
🌍 Çovaşla: pöl
🌍 Qaraqalpaqsha: bil
🌍 Qırımtatarca: bil
🌍 Qumuqça: bil
🌍 Qaraçay-Malqar: bil
🌍 Noğayşa: bil
🌏 Sıbırca: pel
🌏 Salırça: bil
🌍 Gagauzça: bil
🌍 Urumça: bil
🌍 Karajče: bil
🌍 Qrımçahça: bıl
🌏 Saqalī: bil
🌏 Dulgan-Hakalī: bil
🌏 Tıvalap: bil
🌏 Xakastap: pil
🌏 Altaylap: bil
🌏 Şor: pil
🌏 Soyot: bil
🌏 Tofalap: bil''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gazete" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gazet" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gazeta" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gazetta" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gazette" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "news paper" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "newspaper" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "газета" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "газетный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "газетная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "газетное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "газетные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "газет" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рузнама":
        bot.send_message(message.chat.id, '''🇬🇧 English: newspaper
🇷🇺 Русский: газета [gazeta]
🇹🇷 Türkçe: gazete
🇦🇿 Türkcə: qəzet, ruznamə {arch.}
🇹🇲 Türkmençe: gazet
🇺🇿 Oʻzbekcha: gazeta, roʻznoma
🇰🇿 Qazaqşa: gazet (gäzet)
🇰🇬 Qırğızça: gezit
🌏 Uyghurche: gézit
🌍 Tatarça: gazeta (gäcit)
🌍 Başqortsa: gäzit
🌍 Çovaşla: xacat
🌍 Qaraqalpaqsha: gazeta
🌍 Qırımtatarca: gazet, ceride
🌍 Qumuqça: gazet
🌍 Qaraçay-Malqar: gazet
🌍 Noğayşa: gazet
🌏 Sıbırca: gäsit
🌏 Salırça: boci
🌍 Gagauzça: gazete (gazeta)
🌍 Urumça: ğazet (gazet)
🌍 Karajče: gazeta
🌍 Qrımçahça: gazeta
🌏 Saqalī: qahıat (qasıat)
🌏 Dulgan-Hakalī: gazet (kahıat)
🌏 Tıvalap: solun
🌏 Xakastap: gazeta
🌏 Altaylap: gazet
🌏 Şor: gazet
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "1000" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "1 000" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тысяча" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тысича" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тыща" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тыщща" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тысыча" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "thousand" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tousand" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bin":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐰋𐰃𐰭‎
🐺 Old Turkic (bef. 15th c.): biŋ
🇬🇧 English: thousand
🇷🇺 Русский: тысяча [tysyacha]
🇲🇳 Mongol: myang
🇹🇷 Türkçe: bin
🇦🇿 Türkcə: min
🇹🇲 Türkmençe: müň
🇺🇿 Oʻzbekcha: ming
🇰🇿 Qazaqşa: mıŋ
🇰🇬 Qırğızça: miŋ
🌏 Uyghurche: ming
🌍 Tatarça: meñ
🌍 Başqortsa: meñ
🌍 Çovaşla: pin
🌍 Qaraqalpaqsha: mıń
🌍 Qırımtatarca: miñ
🌍 Qumuqça:	miñ
🌍 Qaraçay-Malqar: miñ
🌍 Noğayşa: mıŋ
🌏 Sıbırca: mıŋ
🌏 Salırça: miŋ
🌍 Gagauzça: bin
🌍 Urumça: biñ
🌍 Karajče: min
🌍 Qrımçahça: bin
🌏 Saqalī: tıhīnça, muñ {arch.}
🌏 Dulgan-Hakalī: tıhıçça
🌏 Tıvalap: muñ
🌏 Xakastap: muñ
🌏 Altaylap: muñ
🌏 Şor: muñ
🌏 Soyot: mıñ
🌏 Tofalap: uluğ-san''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "10000" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "10 000" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "10,000" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "10.000" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "10, 000" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "10. 000" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "десять тысяч всадников" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "десятитысячное войско" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "несметное войско" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "десять тысяч" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "десять тысячей" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "десятьтысяч" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ten thousand" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ten thousands" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tenthousand" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "unit of ten thousand" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "division" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tumen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "a bunch of" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tümen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дивизия" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тысяцкий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "множество" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тьма" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тумен" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тумэн" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тумень" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тумэнь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюмен" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюмэн" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюмень" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тюмэнь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тумань" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "toman" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tümmin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tüm min" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "on bin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "divizyon" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "myriad" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мириада" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "miriad" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "miryad" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "miriada" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "miryada" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "miriyad" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "miriyada" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "onbin":
        bot.send_message(message.chat.id, '''‎🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱅𐰇𐰢𐰤
🐺 Old Turkic (bef. 15th c.): tümän
🇬🇧 English: tumen, division, ten thousand, a bunch of, myriad
🇷🇺 Русский: десять тысяч, тумен, дивизия, тысяцкий, множество, тьма, десятитысячное войско, несметное войско, мириада
🇲🇳 Mongol: tümen
🇭🇺 Magyar: tömény
🇹🇷 Türkçe: tümen
🇦🇿 Türkcə: tümən
🇹🇲 Türkmençe: tümen
🇺🇿 Oʻzbekcha: tuman
🇰🇿 Qazaqşa: tümen
🇰🇬 Qırğızça: tümön
🌏 Uyghurche: tümen
🌍 Tatarça: tömän
🌍 Başqortsa: tömän
🌍 Çovaşla: tömen
🌍 Qaraqalpaqsha: túmen
🌍 Qırımtatarca: tümen
🌍 Qumuqça: tümen
🌍 Qaraçay-Malqar: tümen
🌍 Noğayşa: tümen
🌏 Sıbırca: tömän
🌏 Salırça: tümen
🌍 Gagauzça: tümen
🌍 Urumça: tümen
🌍 Karajče: tiumiań
🌍 Qrımçahça: tümen
🌏 Saqalī: tümen
🌏 Dulgan-Hakalī: tümen
🌏 Tıvalap: tümen
🌏 Xakastap: tümen
🌏 Altaylap: tümen
🌏 Şor: tüben
🌏 Soyot: tümen
🌏 Tofalap: tümen''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "greece" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "greese" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hellas" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ellada" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "греция" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yunanistan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yunanıstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yunanstan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "эллада" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "элада":
        bot.send_message(message.chat.id, '''‎🇬🇧 English: Greece, Hellas
🇷🇺 Русский: Греция [Gretsiya]
🇹🇷 Türkçe: Yunanistan
🇦🇿 Türkcə: Yunanıstan, Rum {arch.}
🇹🇲 Türkmençe: Gresiýa
🇺🇿 Oʻzbekcha: Yunoniston
🇰🇿 Qazaqşa: Grekiya
🇰🇬 Qırğızça: Gretsiya, Grekiya
🌏 Uyghurche: Grésiye, Yunan {arch.}
🌍 Tatarça: Yunanstan
🌍 Başqortsa: Gretsiya
🌍 Çovaşla: Gretsi
🌍 Qaraqalpaqsha: Yunanstan
🌍 Qırımtatarca: Yunanistan, Rum vilâyeti {arch.}
🌍 Qumuqça: Yunanistan
🌍 Alança (krc): Urum
🌍 Noğayşa: Yunanstan
🌏 Sıbırca: Greciya, Älin (Älin El)
🌏 Salırça: Rom, Şila
🌍 Gagauzça: Yunanistan
🌍 Urumça: Urum
🌍 Karajče: Grecija
🌍 Qrımçahça: Yunanistan, Gretsiya
🌏 Saqalī: Gretsiya
🌏 Dulgan-Hakalī: Gretsiya
🌏 Tıvalap: Gretsiya
🌏 Xakastap: Gretsîya
🌏 Altaylap: Gretsiya
🌏 Şor: Gretsiya
🌏 Soyot: Gretsîya
🌏 Tofalap: Gretsîya
In Greek: Ellaða''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "greek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hellene" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hellen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hellenic" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "grecian" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "грек" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "греческий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гречанка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "греческая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "греческое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "греческие" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rûm" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "urum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "урум" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rumi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rûmi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rumî" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rûmî" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "румей" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ромей" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rumey" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "romey" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rumei" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "romei" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yunan":
        bot.send_message(message.chat.id, '''🇬🇧 English: Greek
🇷🇺 Русский: грек [grek], румей [rumey]
🇹🇷 Türkçe: Yunan, Rum (Urum)
🇦🇿 Türkcə: yunan, bərzan {dial.}, rumi {arch.}
🇹🇲 Türkmençe: grek, ýunan {arch.}
🇺🇿 Oʻzbekcha: yunon
🇰🇿 Qazaqşa: grek
🇰🇬 Qırğızça: grek
🌏 Uyghurche: yunan, grék
🌍 Tatarça: yunan, grik
🌍 Başqortsa: grek
🌍 Çovaşla: grek
🌍 Qaraqalpaqsha: yunan
🌍 Qırımtatarca: yunan, urum
🌍 Qumuqça: yunan, urumlu
🌍 Alança (krc): urum, urumlu
🌍 Noğayşa: yunan, urımlı
🌏 Sıbırca: grek, älin
🌏 Salırça: rom, romlu, Şila kişi
🌍 Gagauzça: urum, yunan
🌍 Urumça: I. urum (rum) II. tat, girek
🌍 Karajče: urum, javan
🌍 Qrımçahça: urum, danğalaq
🌏 Saqalī: grek
🌏 Dulgan-Hakalī: grek
🌏 Tıvalap: grek
🌏 Xakastap: grek
🌏 Altaylap: grek
🌏 Şor: grek
🌏 Soyot: grek
🌏 Tofalap: grek''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "buckwheat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fagopyrum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "buck wheat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гречка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гречиха" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "греча" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гречневая крупа" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ядрица" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гречневая каша" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гречишный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гречневый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гречневая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гречишная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "karabuğday" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kara buğday":
        bot.send_message(message.chat.id, '''🇬🇧 English: buckwheat, fagopyrum
🇷🇺 Русский: гречиха [grechikha], гречка, греча, гречневая крупа, ядрица
🇹🇷 Türkçe: karabuğday
🇦🇿 Türkcə: qarabaşaq, qara düyü {arch.}
🇹🇲 Türkmençe: garabugdaý
🇺🇿 Oʻzbekcha: qorabugʻdoy, marjumak
🇰🇿 Qazaqşa: qaraqumıq
🇰🇬 Qırğızça: kara kürüç
🌏 Uyghurche: üch qirliq qara bughday, chawmey (chomey)
🌍 Tatarça: qaraboday
🌍 Başqortsa: qaraboyðay
🌍 Çovaşla: xuratul
🌍 Qaraqalpaqsha: ???
🌍 Qırımtatarca: qara boğday, arnavut tarısı
🌍 Qumuqça: qaratari, qaramaşaq, qarabuday
🌍 Alança (krc): reçka, qara buday {+ rye}
🌍 Noğayşa: qarayarma
🌏 Sıbırca: qara potay
🌏 Salırça: sagät (soğät, sağat)
🌍 Gagauzça: karabooday
🌍 Urumça: xaraboğday
🌍 Karajče: kara birtik
🌍 Qırımçahça: qaraboğday
🌏 Saqalī: ???
🌏 Dulgan-Hakalī: ???
🌏 Tıvalap: kırlıg taraa, mıyıraq
🌏 Xakastap: xırlıx
🌏 Altaylap: ???
🌏 Şor: ???
🌏 Soyot: ???, mırıyaq {plantae viviparae}
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "peafowl" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "peacock" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pea hen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "peahen" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pea fowl" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pea cock" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pavo" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "павлин" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "павлиний" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pawlin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pavlin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tavus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tavuskuş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tavuskuşu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tavus kuş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tavus kuşu":
        bot.send_message(message.chat.id, '''🇬🇧 English: peafowl, peacock, peahen, pavo
🇷🇺 Русский: павлин [pavlin]
🇲🇳 Mongol: togos
🇹🇷 Türkçe: tavus
🇦🇿 Türkcə: tovuz quşu
🇹🇲 Türkmençe: tawus
🇺🇿 Oʻzbekcha: tovus
🇰🇿 Qazaqşa: tawıs
🇰🇬 Qırğızça: toos
🌏 Uyghurche: tawus (toz)
🌍 Tatarça: tawis
🌍 Başqortsa: tawis
🌍 Çovaşla: turtkoş
🌍 Qaraqalpaqsha: tawıs
🌍 Qırımtatarca: tavus
🌍 Qumuqça: tawus
🌍 Alança (krc): altın tawuq
🌍 Noğayşa: totıgus
🌏 Sıbırca: tutıy qoş
🌏 Salırça: kunse (kunsi, kunsey)
🌍 Gagauzça: tavus, paun
🌍 Urumça: tavus (taos)
🌍 Karajče: tavus kuš, bij tavuhu
🌍 Qırımçahça: tavus
🌏 Saqalī: pavlin
🌏 Dulgan-Hakalī: pavlin
🌏 Tıvalap: doos
🌏 Xakastap: mayat, pavlîn
🌏 Altaylap: toñus
🌏 Şor: qıyğılıq
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чеснок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чесночок" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чесночек" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sarımsak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sarmısak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "samırsak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sarimsak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sarmisak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "samirsak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "garlic" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "allium sativum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "alliumsativum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "allium-sativum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "чесночный":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): sarımsaq (sarumsaq, samırsaq, samursaq, sarmısaq, sarmusaq), usqun, satun, qamğaq, basar {mountain ~}
🇬🇧 English: garlic, allium sativum
🇷🇺 Русский: чеснок [chesnok]
🇲🇳 Mongol: sarimsag, sarims
🇹🇷 Türkçe: sarımsak
🇦🇿 Türkcə: sarımsaq
🇹🇲 Türkmençe: sarymsak
🇺🇿 Oʻzbekcha: sarimsoq
🇰🇿 Qazaqşa: sarımsaq
🇰🇬 Qırğızça: sarımsaq
🌏 Uyghurche: samsaq
🌍 Tatarça: sarımsaq
🌍 Başqortsa: harımhaq
🌍 Çovaşla: ıxra (ukro), uksom
🌍 Qaraqalpaqsha: sarımsaq
🌍 Qırımtatarca: sarımsaq
🌍 Qumuqça: samursaq
🌍 Alança (krc): sarısmaq
🌍 Noğayşa: sarımsaq
🌏 Sıbırca: sarımsaq
🌏 Salırça: samsax (samzax)
🌍 Gagauzça: sarmısak (sarımsak)
🌍 Urumça: sarımsax
🌍 Karajče: sarymsak (sarymsach)
🌍 Qırımçahça: samırsax (sarımsax)
🌏 Saqalī: çoçunāq (çesnok)
🌏 Dulgan-Hakalī: ???
🌏 Tıvalap: koş-soguna
🌏 Xakastap: çama {mountain ~}, mañırsın (maxursum, mağırsum) {field ~}
🌏 Altaylap: uskum
🌏 Şor: çer oqsumu
🌏 Soyot: ???
🌏 Tofalap: çapa''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "helicopter" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "chopper" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "helikopter" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dikuçar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dikuçan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dik uçar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "döner kanat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dönerkanat" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вертолет" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "🚁" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "вертолетный":
        bot.send_message(message.chat.id, '''🇬🇧 English: helicopter, chopper
🇷🇺 Русский: вертолёт [vertolyot]
🇹🇷 Türkçe: helikopter, dikuçar {purism}, döner kanat {purism}
🇦🇿 Türkcə: dikuçar, helikopter, vertolyot
🇹🇲 Türkmençe: dikuçar
🇺🇿 Oʻzbekcha: tikuchar, vertolyot
🇰🇿 Qazaqşa: tikuşaq, vertolyot
🇰🇬 Qırğızça: tik uçaq, vertolyot
🌏 Uyghurche: tik uchar
🌍 Tatarça: boralaq, vertolyot
🌍 Başqortsa: vertolyot
🌍 Çovaşla: vertolöt
🌍 Qaraqalpaqsha: vertolyot
🌍 Qırımtatarca: helikopter, tikuçar, vertolöt
🌍 Qumuqça: vertolyot
🌍 Alança (krc): vertolyot
🌍 Noğayşa: vertolyot
🌏 Sıbırca: vertolyot
🌏 Salırça: cişinci
🌍 Gagauzça: vertolyot
🌍 Urumça: vertolyot, elikopter
🌍 Karajče: vertoljot
🌍 Qırımçahça: vertolyot
🌏 Saqalī: vertolyot
🌏 Dulgan-Hakalī: vertolyot
🌏 Tıvalap: vertolyot
🌏 Xakastap: vertolyot
🌏 Altaylap: vertolyot
🌏 Şor: vertolyot
🌏 Soyot: vertolyot
🌏 Tofalap: vertolyot''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "monkey" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "guenon" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "обезьяна" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "обезяна" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мартышка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "обезяний" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "обезьяний" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "maymun" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "haplorhini" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "haplorhin" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сухоносый примат" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "simia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "🙈" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "🙉" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "🙊" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "🐵" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "🐒" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "haplorhine":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): beçin (biçin), keylig
🇬🇧 English: monkey, guenon
🇷🇺 Русский: обезьяна [obezyana], мартышка
🇹🇷 Türkçe: maymun
🇦🇿 Türkcə: meymun
🇹🇲 Türkmençe: maýmyn, bijin
🇺🇿 Oʻzbekcha: maymun
🇰🇿 Qazaqşa: maymıl
🇰🇬 Qırğızça: maymıl
🌏 Uyghurche: maymun
🌍 Tatarça: maymıl
🌍 Başqortsa: maymıl
🌍 Çovaşla: upote, maymol
🌍 Qaraqalpaqsha: maymıl
🌍 Qırımtatarca: maymun, şamek, nanay
🌍 Qumuqça: maymun
🌍 Alança (krc): maymul
🌍 Noğayşa: maymıl
🌏 Sıbırca: maymıl
🌏 Salırça: bicin
🌍 Gagauzça: maymun
🌍 Urumça: maymun (maymul)
🌍 Karajče: majmun, šamek
🌍 Qırımçahça: maymun
🌏 Saqalī: ebisiyēne, qaya iççite, tıkārı (tīrākı)
🌏 Dulgan-Hakalī: ???
🌏 Tıvalap: sarbaşkın
🌏 Xakastap: maymuun, saraamcın
🌏 Altaylap: kiji-kiyik, meçin, almın
🌏 Şor: ???
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ferrum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "iron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ıron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ferum" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "temir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "demir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "железо" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "железный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "железная":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜: 𐱅𐰢𐰼
🐺 Old Turkic (bef. 15th c.): temir (temür)
🇬🇧 English: iron, ferrum, Fe
🇷🇺 Русский: железо
🇲🇳 Mongol: tömör
🇹🇷 Türkçe: demir
🇦🇿 Türkcə: dəmir
🇹🇲 Türkmençe: demir
🇺🇿 Oʻzbekcha: temir
🇰🇿 Qazaqşa: temir
🇰🇬 Qırğızça: temir
🌏 Uyghurche: tömür
🌍 Tatarça: timer
🌍 Başqortsa: timer
🌍 Çovaşla: timör
🌍 Qaraqalpaqsha: temir
🌍 Qırımtatarca: demir
🌍 Qumuqça: temir
🌍 Alança (krc): temir
🌍 Noğayşa: temir
🌏 Sıbırca: timer
🌏 Salırça: dimur (temur)
🌍 Gagauzça: demir
🌍 Urumça: demir (temir)
🌍 Karajče: demir (tiemir)
🌍 Qırımçahça: demır
🌏 Saqalī: timir
🌏 Dulgan-Hakalī: timir
🌏 Tıvalap: demir
🌏 Xakastap: tîmir
🌏 Altaylap: temir
🌏 Şor: tebir
🌏 Soyot: demîr (temîr)
🌏 Tofalap: demîr (temîr)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ütük" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ütüg" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "utyug" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ütü" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "flatiron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "flat iron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "clothes iron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "clothesiron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "smoothing iron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soldering iron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "brand iron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "searing iron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "solderingiron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "brandiron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "searingiron" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "утюг" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "железко" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "утюжный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "smoothingiron":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): ütüg (ütük)
🇬🇧 English: iron (clothes iron), flatiron, smoothing iron
🇷🇺 Русский: утюг [utyug]
🇹🇷 Türkçe: ütü
🇦🇿 Türkcə: ütü
🇹🇲 Türkmençe: ütük
🇺🇿 Oʻzbekcha: dazmol
🇰🇿 Qazaqşa: ütik
🇰🇬 Qırğızça: ütük
🌏 Uyghurche: dezmal, ötük
🌍 Tatarça: ütük
🌍 Başqortsa: ütek
🌍 Çovaşla: yakatmoş, utyug
🌍 Qaraqalpaqsha: útik
🌍 Qırımtatarca: ütü
🌍 Qumuqça: itiw
🌍 Alança (krc): itiw
🌍 Noğayşa: ıytuw, ütik {arch.}
🌏 Sıbırca: öygäk, tarsımal
🌏 Salırça: yindu
🌍 Gagauzça: ütü
🌍 Urumça: ütü
🌍 Karajče: iutiu (iti)
🌍 Qırımçahça: ütu
🌏 Saqalī: ötǖk
🌏 Dulgan-Hakalī: ötǖk
🌏 Tıvalap: iliir, xaarııl
🌏 Xakastap: ilör, utyug
🌏 Altaylap: ülüür, utyug
🌏 Şor: uyuq
🌏 Soyot: utyuuk
🌏 Tofalap: uçuuk (utyuuk)''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "молоко" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "молока" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "milk" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "süt" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "молочный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "молочная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "молочное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "молочные" :
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): süt
🇬🇧 English: milk
🇷🇺 Русский: молоко
🇲🇳 Mongol: süü
🇹🇷 Türkçe: süt
🇦🇿 Türkcə: süd
🇹🇲 Türkmençe: süýt
🇺🇿 Oʻzbekcha: sut
🇰🇿 Qazaqşa: süt
🇰🇬 Qırğızça: süt
🌏 Uyghurche: süt
🌍 Tatarça: söt
🌍 Başqortsa: höt
🌍 Çovaşla: söt
🌍 Qaraqalpaqsha: sút
🌍 Qırımtatarca: süt
🌍 Qumuqça: süt
🌍 Alança (krc): süt
🌍 Noğayşa: süt
🌏 Sıbırca: söt
🌏 Salırça: süt
🌍 Gagauzça: süt
🌍 Urumça: süt
🌍 Karajče: siut (sit)
🌍 Qırımçahça: süt
🌏 Saqalī: ǖt
🌏 Dulgan-Hakalī: emiy, ǖt
🌏 Tıvalap: süt
🌏 Xakastap: süt
🌏 Altaylap: süt
🌏 Şor: süt
🌏 Soyot: süt
🌏 Tofalap: süt''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurultáj" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurultaj" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurultay" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qurultay" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kurultai" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "curultai" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "congress" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kongre" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "congres" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kongres" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kongress" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "конгресс" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "конгрес" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "собрание" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курултай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сьезд" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хурал" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "хуралдай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "съезд":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): qurultay
🇬🇧 English: kurultai, meeting, congress, diet
🇷🇺 Русский: курултай [kurultay], собрание, съезд, конгресс
🇲🇳 Mongol: khuraldai, khural
🇭🇺 Magyar: kurultáj
🇹🇷 Türkçe: kurultay
🇦🇿 Türkcə: qurultay
🇹🇲 Türkmençe: gurultaý
🇺🇿 Oʻzbekcha: qurultoy
🇰🇿 Qazaqşa: qurıltay
🇰🇬 Qırğızça: qurultay
🌏 Uyghurche: qurultay
🌍 Tatarça: qorıltay
🌍 Başqortsa: qoroltay
🌍 Çovaşla: kurultay
🌍 Qaraqalpaqsha: qurıltay
🌍 Qırımtatarca: qurultay
🌍 Qumuqça: qurultay
🌍 Alança (krc): qurultay
🌍 Noğayşa: qurultay
🌏 Sıbırca: qoroltay
🌏 Salırça: gurultay
🌍 Gagauzça: kurultay
🌍 Urumça: xurultay
🌍 Karajče: kurultaj
🌍 Qırımçahça: qurıltay
🌏 Saqalī: kurultāy
🌏 Dulgan-Hakalī: kurultāy
🌏 Tıvalap: xural
🌏 Xakastap: xuralday
🌏 Altaylap: qurultay
🌏 Şor: çıılış
🌏 Soyot: suğlaan
🌏 Tofalap: suğlaan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "семья" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "семъя" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "семейство" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "семейка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "семейный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "семеное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "семейная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "family" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "familia" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "aile":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): eb, urluğ
🇬🇧 English:	family
🇷🇺 Русский:	семья [semya]
🇲🇳 Mongol: ail, ger bül
🇹🇷 Türkçe: aile
🇦🇿 Türkcə: ailə, uruq {dial.}, əhli-əyal {arch.}
🇹🇲 Türkmençe: maşgala, öý-işik
🇺🇿 Oʻzbekcha: oila
🇰🇿 Qazaqşa: otbası
🇰🇬 Qırğızça: üy-bülö
🌏 Uyghurche: aile (ailie)
🌍 Tatarça: ğailä
🌍 Başqortsa: ğailä
🌍 Çovaşla: kilyış (kil, yış)
🌍 Qaraqalpaqsha: úy-ishi
🌍 Qırımtatarca: qorantа, aile
🌍 Qumuqça: ahlü, üyahlü, aile
🌍 Alança (krc): üydegi, üyür
🌍 Noğayşa: äyel, üy-işi
🌏 Sıbırca: qäilä
🌏 Salırça: öyci, çimsaŋ
🌍 Gagauzça: aylä
🌍 Urumça: ocax, tayfa, xoranda
🌍 Karajče: uruv, choranda
🌍 Qırımçahça: aile, horanta
🌏 Saqalī: ıal, jie kergen
🌏 Dulgan-Hakalī: kergen
🌏 Tıvalap: ög-büle, ög işti, ög
🌏 Xakastap: söbire, semya
🌏 Altaylap: bile
🌏 Şor: töl
🌏 Soyot: öğ-îşti
🌏 Tofalap: öğ îşti''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "soap" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sapo" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sabun" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sabın" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "savın" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mylo" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мыло" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мыльный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мыльная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мыльное":
        bot.send_message(message.chat.id, '''🇬🇧 English: soap
🇷🇺 Русский: мыло [mylo]
🇲🇳 Mongol: savan
🇭🇺 Magyar: szappan
🇯🇵 Nihongo: sekken
🇹🇷 Türkçe: sabun
🇦🇿 Türkcə: sabun, savın {dial.}
🇹🇲 Türkmençe: sabyn
🇺🇿 Oʻzbekcha: sovun
🇰🇿 Qazaqşa: sabın
🇰🇬 Qırğızça: samın
🌏 Uyghurche: sovun (sopun)
🌍 Tatarça: sabın
🌍 Başqortsa: habın
🌍 Çovaşla: supon
🌍 Qaraqalpaqsha: sabın
🌍 Qırımtatarca: sabun
🌍 Qumuqça: sapun
🌍 Alança (krc): sabın
🌍 Noğayşa: sabın
🌏 Sıbırca: sabın
🌏 Salırça: yizi
🌍 Gagauzça: sabun
🌍 Urumça: sabon (sabun)
🌍 Karajče: sabun (sapun)
🌍 Qırımçahça: sabun
🌏 Saqalī: mīla, qayaq {arch.}
🌏 Dulgan-Hakalī: ???
🌏 Tıvalap: savañ
🌏 Xakastap: sabın
🌏 Altaylap: samın
🌏 Şor: sabın
🌏 Soyot: ???
🌏 Tofalap: mîîlê''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "товары" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mal" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "davar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tavar" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cattle" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "скоты" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "beasts" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "livestock" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "live stock" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "stock" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "goods" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "property" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "asset" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "commodity" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "скот" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "скотина" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "товар" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тавар" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "благо" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "имущество" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "товарный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "скотский" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "скотный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "имущественный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "stock":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. 15th c.): mal, tabar (tavar), barım, yılqı
🇬🇧 English: cattle, beasts, livestock, stock, goods, property, asset, commodity
🇷🇺 Русский: скот, скотина, товар, благо, имущество
🇲🇳 Mongol: mal
🇹🇷 Türkçe: mal, davar
🇦🇿 Türkcə: mal, davar
🇹🇲 Türkmençe: mal
🇺🇿 Oʻzbekcha: mol
🇰🇿 Qazaqşa: mal, tawar
🇰🇬 Qırğızça: mal, tabar
🌏 Uyghurche: mal
🌍 Tatarça: mal, mal-tuwar
🌍 Başqortsa: mal, tawar
🌍 Çovaşla: vılox, mul, tavar
🌍 Qaraqalpaqsha: mal
🌍 Qırımtatarca: mal, tuvar
🌍 Qumuqça: mal
🌍 Alança (krc): mal
🌍 Noğayşa: mal, tuwar
🌏 Sıbırca: mal, mal-tuwar, tawar
🌏 Salırça: mal
🌍 Gagauzça: mal
🌍 Urumça: mal, tuvar
🌍 Karajče: mal, tuvar
🌍 Qırımçahça: mal, tuvar
🌏 Saqalī: süöhü, tabār
🌏 Dulgan-Hakalī: hüöhü, tabār
🌏 Tıvalap: mal
🌏 Xakastap: mal
🌏 Altaylap: mal
🌏 Şor: mal
🌏 Soyot: mal, tavaar
🌏 Tofalap: mal, tavaar''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kapu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kapı" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kapi" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gate" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gates" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "door" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дверь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дверной" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "врата" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "двер" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "враты" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "дверная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "dervaze" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "darvaza" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "darvaze" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ворота":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜 (.VIII-X c): 𐰴𐰯𐰍
🐺 Old Turkic (bef. XV c.): qapığ (qapuğ, qapağ, qapğa), eşik, el
🇬🇧 English: I. door II. gate
🇷🇺 Русский: I. дверь II. ворота [vorota] врата
🇭🇺 Magyar: I. ajtó II. kapu
🇹🇷 Türkçe: kapı
🇦🇿 Türkcə: qapı, kapu {terekeme dial.}, darvaza {II}, alaqapı {II}
🇹🇲 Türkmençe: I. gapy II. derweze
🇺🇿 Oʻzbekcha: I. eshik II. darvoza
🇰🇿 Qazaqşa: I. esik II. qaqpa
🇰🇬 Qırğızça: I. eşik II. darbaza
🌏 Uyghurche: I. ishik I. derwaza
🌍 Tatarça: I. işek II. qapqa
🌍 Başqortsa: I. işek II. qapqa
🌍 Çovaşla: I. alok II. xapxa
🌍 Qaraqalpaqsha: I. esik II. dárwaza
🌍 Qırımtatarca: qapı, araba qapı {II}
🌍 Qumuqça: qapu, eşik {I}, qapular {II}
🌍 Alança (krc): eşik, qabaq eşik {II}
🌍 Noğayşa: qapı, esik {I}
🌏 Sıbırca: I. işek II. qapqa
🌏 Salırça: gavu (gō)
🌍 Gagauzça: I. kapu II. tokat(lar)
🌍 Urumça: xapı (ğapı, xapu, kapu), çızıx xapusu {II}, araba xapu {II}
🌍 Karajče: kapu, ešik, kabak {II}
🌍 Qırımçahça: qapu, araba-qapu {II}
🌏 Saqalī: ān, olbuor āna {II}, bütey āna {II}
🌏 Dulgan-Hakalī: ān
🌏 Tıvalap: ejik, xaalga
🌏 Xakastap: izik, xalxa {II}
🌏 Altaylap: ejik, qaalğa {II}, ötküş {II}
🌏 Şor: I. ejik II. parata
🌏 Soyot: ecîk, haalğa
🌏 Tofalap: ecîk''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мыш" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мышь" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мышка" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мышиный" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мышиная" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мышиное" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мышыный" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мьшья" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мышьной" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мышье" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мышый" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мыший" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "срущий" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "какающий" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "испражняющий" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "срущийся" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "какающийся" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "испражняющийся" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mouse" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mice" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "muridae" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "muridaes" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "murid" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "murids" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "muride" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "fare" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sıçan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "siçan" \
             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "murides":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜 (.VIII-X c): 𐰚‎𐰇𐰾‎𐰚‎𐰇 (𐰚‎𐰇𐰾𐰏‎𐰇)
🐺 Old Turkic (bef. XV c.): sıçğan (sıçqan), küskü (küsgü), ablan {one of animals from muridae family}
🇬🇧 English: mouse
🇷🇺 Русский: мышь
🇹🇷 Türkçe: fare, sıçan
🇦🇿 Türkcə: siçan (sıçan)
🇹🇲 Türkmençe: syçan
🇺🇿 Oʻzbekcha: sichqon
🇰🇿 Qazaqşa: tışqan
🇰🇬 Qırğızça: çıçqan
🌏 Uyghurche: chashqan
🌍 Tatarça: tıçqan
🌍 Başqortsa: sısqan
🌍 Çovaşla: şoşı
🌍 Qaraqalpaqsha: tıshqan
🌍 Qırımtatarca: sıçan
🌍 Qumuqça: çıçqan
🌍 Alança (krc): çıçxan
🌍 Noğayşa: şışqan
🌏 Sıbırca: cıcqan
🌏 Salırça: geme (kämä, keme) {+ rat}
🌍 Gagauzça: sıçan, patkan, farä
🌍 Urumça: sıçan
🌍 Karajče: syčan (šyčan, syčkan)
🌍 Qırımçahça: sıçan {+ rat}, sıçançıx
🌏 Saqalī: kutuyaq
🌏 Dulgan-Hakalī: kutuyak
🌏 Tıvalap: küske
🌏 Xakastap: küske
🌏 Altaylap: çıçqan
🌏 Şor: şışqan
🌏 Soyot: küskä, hulığına
🌏 Tofalap: mırneêşqa, hün qızı''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "совообразный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "совиный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сова" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "owl" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "baykuş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bay kuş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "strigiforme" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "strigiformes" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bay kuşu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "strigidae" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "strigidaes" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gece yırtıcı kuşu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yırtıcı gece kuşu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gecekuşu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "gece kuşu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "baykuşu":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. XV c.): qoburğa, yabaqulaq, ügi (ühi)
🇬🇧 English: owl
🇷🇺 Русский: сова
🇹🇷 Türkçe: baykuş, gece yırtıcı kuşu (yırtıcı gece kuşu, gecekuşu)
🇦🇿 Türkcə: bayquş (bəyquş)
🇹🇲 Türkmençe: baýguş
🇺🇿 Oʻzbekcha: yapaloqqush, boyqush, boyoʻgʻli
🇰🇿 Qazaqşa: japalaq, üki
🇰🇬 Qırğızça: ükü
🌏 Uyghurche: bayqush, üke, yapilaq, qarghuyapilaq
🌍 Tatarça: yabalaq
🌍 Başqortsa: yabalaq, öke
🌍 Çovaşla: tomana, üxö
🌍 Qaraqalpaqsha: bayıwlı, úki
🌍 Qırımtatarca: bayquş, miyavquş
🌍 Qumuqça: kikimaw, yabalaq, oburyabalaq
🌍 Alança (krc): gılın quş, uku
🌍 Noğayşa: yapalaq, obırğus, maŋqa qus
🌏 Sıbırca: payğış, ögö
🌏 Salırça: uğu, biyaguş (piyaguş)
🌍 Gagauzça: baykuşu, kukumävka (kukumeauka), ukü, gecä kuşu
🌍 Urumça: bayğuş, yapalax, ağlavuxxuş, yecexuş, yılavuxxuş (yılavxuş)
🌍 Karajče: bajkuš, meči kušy
🌍 Qırımçahça: bayğuş (bayquş)
🌏 Saqalī: mekçirge
🌏 Dulgan-Hakalī: leñkey
🌏 Tıvalap: ügü, inek-sokpa, mejergen
🌏 Xakastap: tasxa
🌏 Altaylap: meçirtke, bağay quş, caman quş, ükü
🌏 Şor: tasqaçaq
🌏 Soyot: hügi
🌏 Tofalap: behîrgen''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "rabbit" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "leporidae" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "leporidaes" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hare" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "hares" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jackrabbit" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "jack rabbit" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oryctolagus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "oryctolagu" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "bunny" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "pika" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "пищуха" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ушкан" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "заяц" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кролик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "заец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "заиц" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зай" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "зайка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tavşan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tawşan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "lepus":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜 (.VIII-X c): 𐱃𐰉𐰽𐰍𐰣
🐺 Old Turkic (bef. XV c.): tavşan (tabışğan, tawışğan, tawışqan), quyanığ
🇬🇧 English: rabbit
🇷🇺 Русский: заяц [zayats], кролик [krolik], ушкан [ushkan]
🇹🇷 Türkçe: tavşan
🇦🇿 Türkcə: dovşan
🇹🇲 Türkmençe: towşan
🇺🇿 Oʻzbekcha: quyon
🇰🇿 Qazaqşa: qoyan
🇰🇬 Qırğızça: qoyon
🌏 Uyghurche: toshqan, qoyan
🌍 Tatarça: quyan
🌍 Başqortsa: quyan
🌍 Çovaşla: kuyan, mulkaç
🌍 Qaraqalpaqsha: qoyan
🌍 Qırımtatarca: tavşan, qoyan
🌍 Qumuqça: tawşan, qoyan
🌍 Alança (krc): qoyan
🌍 Noğayşa: qoyan, tawşan, tolay
🌏 Sıbırca: quyan, auq
🌏 Salırça: doşan (doşen)
🌍 Gagauzça: tavşam (tauşam, tauşan)
🌍 Urumça: tavşan (dauşan, davuşan), xoyan
🌍 Karajče: tavšan (dafsan), kojan
🌍 Qırımçahça: tavşan, qoyan
🌏 Saqalī: kuobaq
🌏 Dulgan-Hakalī: uskān, kuobak
🌏 Tıvalap: kodan, koygun
🌏 Xakastap: xozan
🌏 Altaylap: qoyon, tulay
🌏 Şor: qozan
🌏 Soyot: hodan, şımdağa
🌏 Tofalap: hodan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "невод" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "тенета" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "паутина" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сетка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сеть" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "tor" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "net" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "web" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "рыболовная сеть" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ловчая сеть" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "паучья сеть" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сеть паука" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "spider web" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сеть рыбака" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "spiderweb" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "spider-web" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "spider's web" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cobweb" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cob web" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ağ":
        bot.send_message(message.chat.id, '''🐺 Old Turkic (bef. XV c.): tor, izdäŋ
🇬🇧 English: net, web
🇷🇺 Русский: сеть, сетка, паутина
🇲🇳 Mongol: tor
🇹🇷 Türkçe: ağ
🇦🇿 Türkcə: tor, qurum
🇹🇲 Türkmençe: tor, kerep
🇺🇿 Oʻzbekcha: toʻr
🇰🇿 Qazaqşa: tor
🇰🇬 Qırğızça: tor, jele
🌏 Uyghurche: tor, uwa
🌍 Tatarça: yätmä, çeltär, päräwez
🌍 Başqortsa: seltär, aw
🌍 Çovaşla: tora, tetel, karo
🌍 Qaraqalpaqsha: tor, aw
🌍 Qırımtatarca: ağ
🌍 Qumuqça: tor, aw
🌍 Alança (krc): aw
🌍 Noğayşa: aw, tor
🌏 Sıbırca: aw, celtär, misan, şälem
🌏 Salırça: dor
🌍 Gagauzça: aa
🌍 Urumça: av, angarak
🌍 Karajče: av, chamator, kurum
🌍 Qırımçahça: ağ, qurum
🌏 Saqalī: ilim
🌏 Dulgan-Hakalī: mūñka, ilim, argīta
🌏 Tıvalap: çetki
🌏 Xakastap: sözirbe, ağıspa, hıl
🌏 Altaylap: şüün
🌏 Şor: sözürbe, qıl
🌏 Soyot: çetki (cetki)
🌏 Tofalap: çetki''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "сандак" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "посаженный отец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "восприемник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "крестный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "крестный отец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sandek" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sandak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sendak" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mafya babası" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "mafia babası" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кум" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kirve" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кирва" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кирве" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kirva" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kirvo" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "siktutan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sik tutan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "godfather":
        bot.send_message(message.chat.id, '''🇬🇧 English: godfather
🇷🇺 Русский: кум, крёстный отец✝️
🇹🇷 Türkçe: kirve☪️ ️vaftiz babası✝️, baba {The Godfather}
🇦🇿 Türkcə: kirvə☪️ xaç atası✝️
🇹🇲 Türkmençe: sünnet ata☪️ çokundyran ata✝️
🇺🇿 Oʻzbekcha: сhoʻqintirgan ota✝️
🇰🇿 Qazaqşa: ökil ata, kindik äke
🇰🇬 Qırğızça: ökül ata, çoqundurup at qoyuçu ata✝️
🌏 Uyghurche: ataqata, choqundurghan ata✝️
🌍 Tatarça: isem atası
🌍 Başqortsa: isem atahı
🌍 Çovaşla: pısok atte, xöresna atte✝️
🌍 Qaraqalpaqsha: at qoyǵan ata, shoqındırǵan áke✝️
🌍 Qırımtatarca: vaftiz babası✝️
🌍 Qumuqça: sünnetçi☪️
🌍 Alança (krc): emçek ata
🌍 Noğayşa: baba☪️
🌏 Sıbırca: isem atası
🌏 Salırça: guru aba
🌍 Gagauzça: nuna
🌍 Urumça: kalata, aşlı (xaşli, xaçlı)✝️ xıstan baba✝️
🌍 Karajče: kum ata
🌍 Qırımçahça: sağdaq✡️☪️
🌏 Saqalī: ńājı, süreqtēbit ağa (süreqtēq ağa)✝️
🌏 Dulgan-Hakalī: ???
🌏 Tıvalap: ???
🌏 Xakastap: kirösteen pabazı✝️
🌏 Altaylap: ???
🌏 Şor: ???
🌏 Soyot: ???
🌏 Tofalap: ???''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "yaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "возраст" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "age" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "years" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "года" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "годы" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лет" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лет":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜 (.VIII-X c): 𐰖𐱁
🐺 Old Turkic (bef. XV c.): yaş, qarı, yıl-yaş
🇬🇧 English: age {one of the stages of life}
🇷🇺 Русский: возраст, годы {аналогично русскому "лет" и "года", напр. "мне 25 лет" или "мне 23 года"}
🇹🇷 Türkçe: yaş
🇦🇿 Türkcə: yaş
🇹🇲 Türkmençe: ýaş
🇺🇿 Oʻzbekcha: yosh
🇰🇿 Qazaqşa: jas
🇰🇬 Qırğızça: jaş
🌏 Uyghurche: yash
🌍 Tatarça: yäş
🌍 Başqortsa: yäş
🌍 Çovaşla: cul
🌍 Qaraqalpaqsha: jas
🌍 Qırımtatarca: yaş
🌍 Qumuqça: yaş, yıl
🌍 Alança (krc): jıl
🌍 Noğayşa: yas
🌏 Sıbırca: yäş
🌏 Salırça: yaş
🌍 Gagauzça: yaş
🌍 Urumça: yaş
🌍 Karajče: jaš
🌍 Qırımçahça: yaş
🌏 Saqalī: sās
🌏 Dulgan-Hakalī: hās
🌏 Tıvalap: xar, nazın
🌏 Xakastap: ças
🌏 Altaylap: caş
🌏 Şor: çaş
🌏 Soyot: çıl (cıl), nasın, qar
🌏 Tofalap: çıl, nasın''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "овца" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "овец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "бараш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "барашка" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "барашек" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "sheep" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ovis" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "avis" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qoyun" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "koyun" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "курдючная овца" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "овца ордынская" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ovis aries" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "ewe" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "баран":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜 (.VIII-X c): 𐰴𐰆𐰪 (𐰸𐰆𐰪)
🐺 Old Turkic (bef. XV c.): qoy (qoɲ, qon), qoyun (qoyın)
🇬🇧 English: sheep, ovis
🇷🇺 Русский: овца, барашек, баран [baran]
🇲🇳 Mongol: khoni (khonö, khoɲ)
🇹🇷 Türkçe: koyun
🇦🇿 Türkcə: qoyun
🇹🇲 Türkmençe: goýun
🇺🇿 Oʻzbekcha: qoʻy
🇰🇿 Qazaqşa: qoy
🇰🇬 Qırğızça: qoy
🌏 Uyghurche: qoy
🌍 Tatarça: sarıq, quy
🌍 Başqortsa: harıq, quy
🌍 Çovaşla: surox, kuy
🌍 Qaraqalpaqsha: qoy
🌍 Qırımtatarca: qoy, qoyun
🌍 Qumuqça: qoy
🌍 Alança (krc): qoy
🌍 Noğayşa: qoy
🌏 Sıbırca: quy
🌏 Salırça: goy
🌍 Gagauzça: koyun
🌍 Urumça: xoy, xoyun (ğoyun)
🌍 Karajče: koj
🌍 Qırımçahça: qoy, qoyın
🌏 Saqalī: barān
🌏 Dulgan-Hakalī: barān
🌏 Tıvalap: xoy
🌏 Xakastap: xoy
🌏 Altaylap: qoy
🌏 Şor: qoy
🌏 Soyot: hoy
🌏 Tofalap: hoy''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кызылбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кизилбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кизильбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кызыльбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кызильбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кызилбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кизылбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кизыльбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кезельбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гизилбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гизильбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гызыльбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гызильбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гызилбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гизылбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гизыльбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гезельбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "гызылбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kızılbaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qızılbaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qizilbaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qizilbash" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qizilbas" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qızılbas" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kızılbash" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kizilbaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kizilbash" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kizilbas" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kezelbash" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qezelbash" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qazilbash" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kazilbash" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kizilbaix" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qizilbaix" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kizilbasch" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qizilbasch" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kizilbaŝ" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qizilbaŝ" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qızıl baş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kızıl baş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qızıl-baş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kızıl-baş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qizil bash" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kizil bash" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qizil-bash" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kizil-bash" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kizilbasj" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qizilbasj" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "quizilbache" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kuizilbache" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qizilbaș" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kizilbaș" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kisilbasch" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qisilbasch" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "котакпас" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qisilbasch" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "котакпас" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qisilbasch" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "котакпас" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qisilbasch" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "котакпас" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "котакбас" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "котакбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "котакпаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кутакбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "кутакбаш" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qutaqbaş" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qotaqbas" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "Қотақбас" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "қотақбас" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "qizilbāsh":
        bot.send_message(message.chat.id, '''🇬🇧 English: qizilbash
🇷🇺 Русский: кызылбаш [kyzylbash]
🇹🇷 Türkçe: kızılbaş
🇦🇿 Türkcə: qızılbaş
🇹🇲 Türkmençe: gyzylbaş
🇺🇿 Oʻzbekcha: qizilbosh
🇰🇿 Qazaqşa: qızılbas
🇰🇬 Qırğızça: qızılbaş
🌏 Uyghurche: qizilbash
🌍 Tatarça: qızılbaş
🌍 Başqortsa: qıðılbaş
🌍 Çovaşla: xörlöpuc
🌍 Qaraqalpaqsha: qızılbas
🌍 Qırımtatarca: qızılbaş
🌍 Qumuqça: qızılbaş
🌍 Alança (krc): qızılbaş
🌍 Noğayşa: qızılbas
🌏 Sıbırca: qısılpaş
🌏 Salırça: qızılbaş
🌍 Gagauzça: kızılbaş
🌍 Urumça: xızılbaş
🌍 Karajče: kyzylbaš
🌍 Qırımçahça: qızılbaş
🌏 Saqalī: kıhılbas
🌏 Dulgan-Hakalī: kıhılbas
🌏 Tıvalap: kızılbaş
🌏 Xakastap: xızılpas
🌏 Altaylap: qızılbaş
🌏 Şor: qızılpaş
🌏 Soyot: qızılbaş
🌏 Tofalap: qızılbaş''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "martyr" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "martir" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shahid" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shaheed" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şehit" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shehid" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "shehit" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шахид" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шехид" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шахит" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "шехит" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мученик" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "мученник" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "страдалец" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "погибший за веру" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "şehıt":
        bot.send_message(message.chat.id, '''🇬🇧 English: martyr, shahid
🇷🇺 Русский: мученик, шахид
🇹🇷 Türkçe: şehit
🇦🇿 Türkcə: şəhid
🇹🇲 Türkmençe: şehit
🇺🇿 Oʻzbekcha: shahid
🇰🇿 Qazaqşa: şeyit
🇰🇬 Qırğızça: şeyit
🌏 Uyghurche: shéhit (shéyit, shehid)
🌍 Tatarça: şähit
🌍 Başqortsa: şähit
🌍 Çovaşla: asap kurno cın, şeremet
🌍 Qaraqalpaqsha: sheyit
🌍 Qırımtatarca: şeit
🌍 Qumuqça: şahit
🌍 Alança (krc): şeyit
🌍 Noğayşa: şayıt
🌏 Sıbırca: şähit
🌏 Salırça: şehit
🌍 Gagauzça: şehit
🌍 Urumça: martiros, şehit
🌍 Karajče: učmachly, ystyrynhan uluslaryna
🌍 Qırımçahça: şeet
🌏 Saqalī: muñnāq
🌏 Dulgan-Hakalī: muñnāk
🌏 Tıvalap: xinçekke tavarışkan
🌏 Xakastap: îleglig kizi
🌏 Altaylap: qıynalğan, şıralağan
🌏 Şor: qıyalanğan
🌏 Soyot: qalğan
🌏 Tofalap: qalğan''', reply_markup=markup_menu)

    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "cygnus" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "swan" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "swans" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лебедь" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лебядиный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лебядиная" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лебядиное" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лебядиные" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лебединый" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лебединая" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лебединое" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лебединые" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лебяжий" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "лебединный" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "kuğu":
        bot.send_message(message.chat.id, '''🐺 𐰚𐰇𐰚𐱅𐰇𐰼𐰜 (.VIII-X c): 𐰴𐰆𐰍𐰆 : 𐰴𐰆𐰽
🐺 Old Turkic (bef. XV c.): quğu, quğu quş
🇬🇧 English: swan
🇷🇺 Русский: лебедь
🇹🇷 Türkçe: kuğu
🇦🇿 Türkcə: qu, qu quşu
🇹🇲 Türkmençe: guw
🇺🇿 Oʻzbekcha: oqqush
🇰🇿 Qazaqşa: aqquw
🇰🇬 Qırğızça: aq quu
🌏 Uyghurche: aqqu
🌍 Tatarça: aqqoş
🌍 Başqortsa: aqqoş
🌍 Çovaşla: akoş
🌍 Qaraqalpaqsha: aqquw
🌍 Qırımtatarca: aqquş
🌍 Qumuqça: quw
🌍 Alança (krc): qañqaz, duwadaq
🌍 Noğayşa: quw, aqquw
🌏 Sıbırca: aqqoş
🌏 Salırça: axquş
🌍 Gagauzça: kuu
🌍 Urumça: axxuş
🌍 Karajče: kuv, akkuv, kuhu
🌍 Qırımçahça: ahquş
🌏 Saqalī: kuba
🌏 Dulgan-Hakalī: kuba
🌏 Tıvalap: kuu, kuu kuş
🌏 Xakastap: xuu
🌏 Altaylap: quu
🌏 Şor: quu
🌏 Soyot: quu, aq-quu
🌏 Tofalap: quu, aq-quu''', reply_markup=markup_menu)


    elif message.text.replace('İ', 'i').lower().replace('ё', 'е') == "AAAA" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "AAAA" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "AAAA" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "AAAA" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "AAAAA" \
            or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "AAAA":
        bot.send_message(message.chat.id, '''AAAA''', reply_markup=markup_menu)

    else:
        bot.send_message(message.chat.id, hesbisey)

#cd /Users/royalnagiyev/PycharmProjects/projectoglu
#git add .
#git commit -am "make it better"
#git push heroku master
#Āā Ēē Ïï Īī Ōō Ȫȫ Ūū Ǖǖ Ŋŋ Êê
# elif message.text.lower() == "&&&" \
#             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "&&&"\
#             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "&&&"\
#             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "&&&"\
#             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "&&&"\
#             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "&&&"\
#             or message.text.replace('İ', 'i').lower().replace('ё', 'е') == "&&&":
#         bot.send_message(message.chat.id, '''&&&''', reply_markup=markup_menu)


bot.polling()