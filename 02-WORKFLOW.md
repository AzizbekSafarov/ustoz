# 13-oktabr uchun taklif qilingan birga ishlash tartibimiz

Sana: 2026-yil 9-oktabr. Yo‘nalish: “Eng yaxshi veb-sayt”, Samarqand viloyat bosqichi. Bu bizning tayyorgarlik rejamiz. Tashkilotchining tasdiqlangan bileti va texnik tartibi kelganda vaqt, vosita va topshirish usulini shunga moslaymiz.

Manbalar, sovrin, mezonlar va PDFlar orasidagi farqlar: [To‘liq tadqiqot](01-RESEARCH.md).

## 1. Kim nima qiladi?

| Siz | Men — Codex orqali |
|---|---|
| Ekspert bergan biletning to‘liq matni va materiallarini berasiz | Talablarni majburiy funksiyalar, mazmun, ko‘rinish va topshirishga ajrataman |
| Qolgan vaqt va joydagi texnik cheklovni aytasiz | Bajarish tartibini qisqartiraman, ishlaydigan holatni saqlayman |
| Foydalanuvchi maqsadini va muhim dizayn tanlovini tekshirasiz | Kodni yozaman, ishga tushiraman, xatolarni tekshiraman va tuzataman |
| Saytni o‘zingiz ishlatib ko‘rasiz | Takrorlanuvchi sinovlar va kerakli dalillarni tayyorlayman |
| Nimani yaratganimiz va qanday ishlashini tushunib olasiz | Fayllar xaritasi, funksiyalar, cheklovlar va tahrir usulini tushuntiraman |
| Ekspert oldida taqdimot va savol-javobni olib borasiz | Mashqda himoya matni va savollar bilan tayyorlayman |

**Asosiy kod yozuvchi — Codex.** Antigravity, joydagi reglament ruxsat bersa, qo‘shimcha tekshiruv yoki zaxira vosita bo‘ladi. Bir xil faylni ikki agent bir paytda tahrirlamaydi. Vositalar orasida almashganda joriy holat, ishlatish buyrug‘i va hali ochiq xatolar yozib qoldiriladi.


AI bilan ishlash videoda nazarda tutilgan. Boshqa insondan masofaviy yechim yoki yordam olish masalasi bundan alohida; mezonlar loyihasida bunday yordam taqiqlangan. Biz tanlov joyidagi ruxsat etilgan AI ilovasida ishlaymiz.

## 2. Tanlov kompyuteriga o‘tish

Bugungi kompyuterdagi loyiha fayllari tanlov kompyuteriga avtomatik ko‘chmaydi. O‘sha kompyuterda ishlashim uchun kerakli loyiha papkasi Codexda ochilishi va fayllar shu yerda bo‘lishi kerak. Yangi chat ochilsa, quyidagi qisqa boshlang‘ich matn yetarli:

**Yangi PCdagi amaliy ketma-ketlik:** Codexni ochish → tashkilotchi ruxsat etgan akkauntga kirish → foydalanish limitini tekshirish → yangi tanlov papkasini ochish → bilet va qisqa boshlang‘ich matnni berish. Shaxsiy akkaunt yoki faqat tashkilotchi ajratgan hisobdan foydalanish joydagi tartibga bog‘liq. Antigravity va Codex hisoblari hamda limitlari alohida aniqlanadi.


Limitni tejash rejasi: tanlov uchun qisqa alohida chat; bilet va materiallar bir to‘plamda; bitta asosiy AI yozuvchi; kichik xatolar uchun butun loyihani qayta yaratmaslik; avval majburiy amallar; oddiy tahrirga ortiqcha uzoq tahlil sarflamaslik. Qolgan limit ikki soatga yetishini faqat foizdan kafolatlab bo‘lmaydi.

```text
Biz Ustoz AI “Zamonaviy kasblar”, “Eng yaxshi veb-sayt” yo‘nalishidamiz.
Viloyat bosqichi. Ish faqat tashkilotchi ruxsat etgan sharoitda bajariladi.
Ballar: funksiya 30, mazmun 20, UX/UI 10, taqdimot 10,
zamonaviy texnologiya 20, kreativlik 10.
Mahalliy batafsil texnik mezonlar PDFi tasdiqqa taqdim etilgan loyiha edi;
hozir berilgan bilet va reglamentga amal qil.
Sen asosiy kod yozuvchi va tekshiruvchi, men vazifa va himoyani boshqaraman.
Avval majburiy ishlaydigan amallar, keyin dizayn va foydali kreativ detal.
Mavjud fayllarni o‘qi, qisqa reja tuz va ishni boshlagin.
Har muhim bosqichda ishlaydigan holat va qolgan ishni qisqa ayt.
Bilmagan faktni yoki o‘tkazilmagan sinovni bajarilgan deb ko‘rsatma.
```

Bu tayyorgarlik yozuvini olib kirish yoki ko‘chirish joydagi tartibga bog‘liq. Oldindan yaratilgan to‘liq saytni tanlov ishi sifatida topshirish rejaning bir qismi emas; haqiqiy mavzu joyida beriladi.

### 2.1. Faqat tashkilotchi bergan akkaunt ruxsat etilsa

Siz aniqlashtirgan ehtimoliy holat: shaxsiy akkauntga kirish taqiqlanadi va har ishtirokchiga tashkilotchi tayyorlagan akkaunt beriladi. Bu hozircha tasdiqlangan tadbir tartibi emas; shunday shart bo‘lsa, quyidagi reja qo‘llanadi.

- Tanlovdagi imkoniyatni ajratilgan akkauntning tarifi, modeli, qolgan limiti va ruxsatlari belgilaydi. Shaxsiy Plus shu boshqa akkauntga o‘tmaydi. Yangi emailning o‘zi akkaunt Free ekanini bildirmaydi.
- Dastlab ajratilgan hisobda model ishlashi, boshlang‘ich limit, limitning individual yoki umumiy ekanligi va muammo yuz bersa kimga murojaat qilinishi aniqlanadi. Yetarli resursni ta’minlash tashkilotchining texnik tayyorgarligiga bog‘liq; biz berilmagan limitni kafolatlay olmaymiz.
- Limit kichik bo‘lsa, bilet va materiallar bitta qisqa topshiriqda beriladi; sodda mos stack tanlanadi; avval majburiy oqim quriladi; keyingi so‘rovlar aniq xato yoki kichik tahrirga qaratiladi. Butun saytni qayta yaratish va keraksiz uzoq qidiruvdan qochamiz.
- Fayllar saqlanadi va sizga matn, rang, ma’lumot hamda oddiy validatsiya joylari ko‘rsatiladi. AI limiti tugashi saqlangan saytni yo‘q qilmaydi: uni brauzerda ishlatish va qo‘lda tahrirlash mumkin. O‘z saytini oddiy ishlatish AI so‘rovi emas; saytning o‘zi AI API chaqirsa, bu alohida masala.
- Boshqa AI vositasiga o‘tish faqat joydagi ruxsat doirasida. Ajratilgan hisoblar juda cheklangan bo‘lsa, kam so‘rovli to‘liq mashq bizning ustuvor tayyorgarligimiz bo‘ladi.

## 3. Dastlabki 15 daqiqa

Videoda akkauntga kirish uchun 15 daqiqa berilishi aytilgan. Mashqda shu ketma-ketlikni sinaymiz:

| Daqiqa | Amal |
|---|---|
| 0–5 | Codexga ChatGPT akkaunti, ruxsat bo‘lsa Antigravityga yosh talabi mos Google akkaunti orqali kirish; autentifikatsiya muammosini aniqlash |
| 5–8 | Loyiha papkasi va brauzerni ochish; ishlatish muhiti, fayl yozish va terminal imkoniyatini tekshirish |
| 8–12 | Oddiy sinov sahifasini ishga tushirish; brauzerda ochilishini va bitta tugma ishlashini tekshirish |
| 12–15 | Qolgan foydalanish limiti, loyiha saqlash va topshirish yo‘lini aniqlash; haqiqiy bilet uchun tayyor turish |

Sinov loyihasi mashq vositasi. Uni tanlov ishiga qo‘shish tasdiqlangan tartibga bog‘liq; mezonlar loyihasida qo‘shilmasligi aytilgan.

Login va tasdiqlash imkoniyatini 12-oktabrgacha tekshirib olish foydali. Hisobga kirishda telefon yoki boshqa qurilma kerak bo‘lsa, foydalanish joydagi tartibga mos bo‘lishi kerak. Antigravityning rasmiy FAQida 18+ talabi bor; ikki ilovadan birini ishlata olmaslik loyihaning to‘xtab qolishiga sabab bo‘lmasligi uchun bir vosita bilan ham ishni tugatishni mashq qilamiz. [Google FAQ](https://antigravity.google/docs/faq), [Codex kirish va limitlar](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan).

## 4. Bilet kelishi bilan beriladigan so‘rov

```text
BILETNING TO‘LIQ MATNI:
[ekspert bergan matn]

BERILGAN MATERIALLAR:
[papka/fayllar, matn, test ma’lumoti, rasm va logotiplar]

AMALIY ISH VAQTI:
[rasmiy limit va hozir qolgan daqiqa]

TEXNIK SHARTLAR:
[ruxsat etilgan vositalar, internet, hosting yoki lokal ishlatish,
saqlash talabi, topshirish formatlari]

Avval mavjud loyiha va muhitni o‘qi. Biletdagi majburiy talablarning
qisqa jadvalini tuz. Eng sodda mos texnologiyani tanla va ishni boshlagin.
Asosiy foydalanuvchi amallari oxirigacha ishlasin. Tugma, forma va
havolalarni tekshir. Kontentni biletdagi ma’lumotga mos yoz.
Mobil holat, xato kiritish, bo‘sh natija va kerak bo‘lsa saqlashni tekshir.
Faqat muhim noaniqlik bo‘lsa so‘ra; qolganida oqilona qaror bilan davom et.
```

Men “majburiy talab → amalga oshirilgan joy → qanday tekshiriladi” jadvalini yuritaman. Yangi qo‘shimcha asosiy talablar bajarilgandan keyin kiritiladi.

## 5. Texnologiyani qanday tanlaymiz?

| Vazifa | Odatda mos boshlanish |
|---|---|
| Kontent, katalog, filtr, forma va oddiy tasdiq | HTML/CSS/JavaScript; kam bog‘liqlik va tez ishga tushirish |
| Bir-biriga bog‘liq ekranlar, bir nechta interaktiv holat, murakkabroq UI | Muhit tayyor bo‘lsa React/Vite |
| Biletda server, umumiy ma’lumotlar, haqiqiy autentifikatsiya yoki serverda saqlash talab qilingan | Talabga mos eng kichik backend; qolgan imkoniyatlar shundan kelib chiqadi |
| No-code bilan vazifa to‘liq bajariladigan va loyiha ko‘rish/nusxalash mumkin bo‘lgan holat | Ruxsat etilgan no-code vosita |

Stackni brendi uchun tanlamaymiz. Talablar lokal saqlash bilan bajarilsa, `localStorage` qanday chegaraga egaligini himoyada ochiq aytamiz. Server kerak bo‘lsa, uni lokal saqlash bilan almashtirib, “to‘liq backend” deb ko‘rsatmaymiz.

## 6. 120 daqiqalik mashq rejimi

**Bu mashq ssenariysi. 13-oktabrdagi haqiqiy limit hali tasdiqlanmagan.** Taklif etilgan hujjatdagi 10/80/20/10 taqsimot asosida:

| Daqiqa | Ish | Yakundagi dalil |
|---|---|---|
| 0–10 | Bilet, majburiy amallar, kontent va topshirish; qisqa reja | Talablar jadvali va foydalanuvchi oqimi |
| 10–25 | Ishga tushadigan asos, sahifalar/ekranlar va navigatsiya | Brauzerda ochilgan ishlaydigan loyiha |
| 25–65 | Asosiy amallar, ma’lumot, forma/filtr, natija va kerakli saqlash | Har majburiy amal boshidan oxirigacha ishlaydi |
| 65–90 | Mazmunni tekislash, mobil ko‘rinish, UI, bitta foydali kreativ detal | Biletga mos, ko‘rishga tayyor mahsulot |
| 90–110 | Quyidagi sinovlar, xatolarni tuzatish | Bajarilgan sinov va ochiq cheklovlar qaydi |
| 110–120 | Topshirish, loyiha nusxasi va qisqa tavsif; demo tayyorligi | Kelishilgan usulda ochiladigan yakuniy ish |

Vaqt boshqa bo‘lsa, reja → yaratish → sinov → topshirish nisbatini moslaymiz. Oxirgi qismdagi topshirish va tekshiruv uchun vaqt saqlanadi. AI kutishi, paket o‘rnatilishi va odatiy xato tuzatish ham umumiy vaqtning ichida.

Qisqa boshqaruv so‘rovlari:

```text
45 daqiqa qoldi. Biletdagi hali bajarilmagan majburiy amallarni yoz.
Eng muhimini yakunla, so‘ng xato va mobil holatlarni tekshir.
```

```text
20 daqiqa qoldi. Hozirgi ishlaydigan holatni saqla.
Majburiy oqimlarni sinab ko‘r, faqat natijaga xalal berayotgan xatolarni tuzat.
Topshirish yo‘riqnomasi va aniq cheklovlarni yoz.
```

```text
10 daqiqa qoldi. Topshirishga tayyorla: havola yoki run buyrug‘i,
manba fayllar, bajarilgan testlar, qisqa tavsif va talab qilingan dalillar.
Sinab ko‘rilmagan narsani ishlaydi deb yozma.
```

## 7. Amaliy sinov ro‘yxati

Sayt qurilganda mazmunli sinovlar o‘tkazamiz. Har bandning natijasi va ochiq xatosi yoziladi.

- Biletning har majburiy foydalanuvchi amali boshidan yakuniy natijagacha ishlaydi.
- Bo‘sh forma, noto‘g‘ri format va chegaraviy qiymat tushunarli xabar beradi.
- Filtr/qidiruvda natija chiqishi va natija topilmasligi ishlaydi.
- Saqlash talab qilingan bo‘lsa, yangilashdan keyingi holat tekshiriladi.
- Menyu, havola, CTA, modal ochish/yopish va ortga qaytish ishlaydi.
- 390, 768, 1366 px — mashqdagi uch ekran kengligi; kontent kesilmaydi va keraksiz yonlama surish yo‘q.
- Klaviatura bilan asosiy amal bajariladi, fokus ko‘rinadi, forma maydonlari nomlangan.
- Matn, sana, nom va qiymatlar ekranlar bo‘ylab mos; vaqtinchalik matn qolmagan.
- Rasm va boshqa resurslar ochiladi; konsolda muhim xato yo‘q.
- Yakuniy nusxa kelishilgan muhitda run yo‘riqnomasi bilan ochiladi.

Avtomatlashtirish foydali bo‘lsa qilamiz; faqat kodga o‘xshab yozilgan tekshiruvlar bilan vaqt sarflamaymiz. Foydalanuvchi oqimini amalda ko‘rish asosiy dalil bo‘ladi.

## 8. Kichik tahrirni bilish

Mahalliy imzoli qarorda ekspertning real vaqtda kichik tahrir so‘rash huquqi bor. Saytdagi nizom va mezonlar loyihasida shu masala farq qiladi. Shu sabab siz quyidagilarni mashqda o‘zingiz bajarasiz:

1. Sarlavha yoki tugma matnini almashtirish.
2. Asosiy rangni o‘zgartirish.
3. Katalogga bitta element qo‘shish yoki olib tashlash.
4. Forma tekshiruvi va natija matni qayerda yozilganini topish.
5. Faylni saqlab, brauzerdagi natijani qayta ko‘rish.

Men loyiha qurilgach shu tahrirlar uchun aniq fayl va joyni ko‘rsataman. Bu shunchaki yodlangan taqdimotdan tashqari mahsulotni boshqarishni ham tayyorlaydi.

## 9. Topshirish uchun tayyorlik

Joydagi yo‘riqnoma qaysi materialni talab qilsa, o‘shani topshiramiz. Mashqdagi paket:

- Ishlaydigan havola yoki mahalliy ishga tushirish usuli.
- Tahrirlanadigan manba va kerakli assetlar; run buyrug‘i.
- Qisqa tavsif: bilet, foydalanuvchi, funksiyalar, texnologiya, testlar va cheklovlar.
- Olingan g‘oya/shablon/rasmlar manbalari va zarur litsenziya qaydi.
- Talab qilinsa AIning asosiy so‘rovlari va muhim o‘zgarishlar tarixi.
- Loyiha hujjatidagi tavsiya bo‘yicha 3–5 ekran tasviri va 1–2 daqiqalik asosiy amal yozuvi; aniq majburiyligi tasdiqlanmagan.

Zaxira tasvir/video ishlaydigan saytning o‘rnini bosa olmaydi. Domen sotib olishni majburiy deb olmaymiz. Haqiqiy to‘lov yoki odamlarning shaxsiy ma’lumotlari o‘rniga biletdagi test ma’lumotidan foydalanamiz. Maxfiy kalitlar frontend yoki ochiq topshirish fayliga kiritilmaydi.

## 10. 15 daqiqalik himoya

### Birinchi 5 daqiqa — muammo va yechim

“Bizning foydalanuvchimiz — … . Uning muammosi — … . Bilet bo‘yicha majburiy talablar — … . Sayt foydalanuvchiga … amalni bajarib … natijani olishga yordam beradi. … texnologiyani … sabab tanladik.”

Keyin mavzuga moslik, foydali farq va asosiy texnik qarorni qisqa ko‘rsatish. Slayd tayyorlash majburiyligi topilmadi; ishlaydigan sayt bilan tushuntirishni mashq qilamiz.

### Keyingi 5 daqiqa — ishlayotgan mahsulot

Bir to‘liq foydalanuvchi oqimi; keyin noto‘g‘ri kiritish yoki bo‘sh natija; so‘ng mobil ko‘rinish va kerakli saqlash. Har namoyish qaysi talabni qoplashini aytish. Faqat bosh sahifa va animatsiyani aylantirish bilan cheklanmaslik.

### Oxirgi 5 daqiqa — savol-javob

Mashqda javob beradigan savollar:

- Kimning qaysi muammosi hal bo‘ldi?
- Nega shu texnologiyani tanladingiz?
- AI nima qildi, siz nimani tekshirdingiz va o‘zgartirdingiz?
- Ma’lumot qayerda saqlanadi, brauzer yangilansa nima bo‘ladi?
- Noto‘g‘ri qiymat yoki natija topilmaganda nima qiladi?
- Qaysi funksiyalar demo, qaysilari to‘liq ishlaydi?
- Qaysi manbadan g‘oya/shablon olindi va nima moslashtirildi?
- Ko‘proq vaqt berilsa eng foydali keyingi o‘zgarish nima?

Natijani va’da qilishdan ko‘ra dalil ko‘rsatamiz: ishlaydigan oqim, sinov va ochiq cheklov. Kichik tahrir talabi qo‘llansa, yuqoridagi mashq yordam beradi.

## 11. 10–13-oktabr mashq jadvali

| Kun | Mashq | O‘lchanadigan natija |
|---|---|---|
| 10-oktabr | Birinchi 120 daqiqalik to‘liq mashq; masalan, yoshlar kurslari katalogi va ariza | 2 bog‘liq amal, mobil holat, xato tekshirish, topshirish |
| 11-oktabr | Boshqa mavzu: masalan, Samarqand sayohat marshruti yoki hunarmandlar katalogi | Yangi biletga moslashish; bo‘sh natija, saqlash va resurs muammosi |
| 12-oktabr | Login sinovi, 15 daqiqa himoya, 5 kichik tahrir, ishga tushirishni qaytarish | Akkaunt, run, tushuntirish va qo‘lda tahrir tayyorligi |
| 13-oktabr | Haqiqiy bilet va joydagi limit asosida ish | Majburiy funksiyalar, tekshiruv, topshirish, himoya |

Bu mavzular o‘zimiz tanlagan mashq misollari; tanlovning haqiqiy mavzusi oldindan aniqlanmagan. Mazkur tadqiqot davomida musobaqaga tayyor to‘liq loyiha qurilmadi. Keyingi mashqda shu tartibni amalda sinash mumkin.
