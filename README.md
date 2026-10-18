# Ustoz — tanlovning to‘liq konteksti

Mahalliy fayllar va rasmiy internet manbalaridan yig‘ilgan ma’lumotlar. Yangilangan: **2026-10-09**. Yo‘nalish: “Eng yaxshi veb-sayt”, “Zamonaviy kasblar”. Qisqa izohlar bilan birga asl manbalar va to‘liq o‘qilgan matnlar saqlangan.

Asosiy sahifa: **https://azizbeksafarov.github.io/ustoz/**. GitHub manzili: **https://github.com/AzizbekSafarov/ustoz**.

**Barcha ma’lumotni bitta faylda o‘qish: [ai.md](ai.md).** Brauzer uchun [to‘liq o‘qish sahifasi](ai.html). AIga avval shu to‘liq kontekst havolasini berish mumkin. Qisqa kirish [00-START-HERE.md](00-START-HERE.md) da.

## Nizomlarning to‘liq matni

Uchta hujjat, jami **39 sahifa**, asl o‘zbek tilida va qisqartirilmagan holda:

- [Barchasi — brauzerda](https://azizbeksafarov.github.io/ustoz/nizom.html).
- [Barchasi — AI uchun Markdown](https://azizbeksafarov.github.io/ustoz/nizom.md) yoki [oddiy TXT](https://azizbeksafarov.github.io/ustoz/nizom.txt).
- [Imzoli qaror va barcha ilovalar](transcripts/qaror.md), [saytdagi nizom](transcripts/sayt.md), [mezonlar loyihasi](transcripts/mezon.md).

Matnga tayyorlangan sana: 2026-10-18. Tadqiqot 2026-10-09 holatida qoladi. Imzoli skanning jadvallari asl tasvirdan tiklandi; muhr, imzo va noaniq qo‘lyozma rekvizitlari PDFda saqlangan. Asl PDF va dastlabki OCR matnlari o‘zgartirilmagan. Loyiha tasdiqlangan qoida sifatida talqin qilinmaydi.

Qayta yaratish: `python -B build_transcripts.py`. Tekshirish: `python -B verify_transcripts.py`. To‘liq matnlar `ai.md` ichiga ham kiritilgan.

## Fayllar

- **00-START-HERE.md** — AI avval o‘qiydigan qisqa kontekst.
- **01-RESEARCH.md** — to‘liq tadqiqot, manbalar va farqlar.
- **02-WORKFLOW.md** — ish, sinov, topshirish va himoya tartibi.
- **03-STATISTICS.csv** — faqat hududiy agregat statistika.
- **04-VIDEO-POSTER.md** — yuborilgan video matni, poster va ishtirokchi bildirgan kontekst.
- **05-SOURCES.md** — mahalliy va internet manbalari reyestri, sanalar va maqomlar.
- **06-SCORE-WORKPLAN.md** — barcha 21 ko‘rsatkich, ishlash va baholash dalillari.
- **07-FACTS.json** — AI va dasturlar uchun tuzilgan faktlar, agregatlar va manba holatlari.
- **ai.md / ai.html** — yuqoridagi ma’lumotlar va uch PDFning o‘qilgan matnlari bir joyda.
- **sources/** — foydalanuvchi taqdim etgan ikki mahalliy PDF va saytdan olingan nizom nusxasi. Mahalliy fayllar tayyorgarlik materiallaridir; 11 betlik mezonlar tasdiqqa taqdim etilgan loyiha.
- **MANIFEST.json** — paket fayllari, o‘lchamlari va SHA-256 tekshirish qiymatlari.

## Ma’lumotlarni to‘g‘ri talqin qilish

100 ballning asosiy og‘irliklari imzoli qarordan; 21 kichik ko‘rsatkich va taxminan ikki soatlik hududiy vaqt tasdiqqa taqdim etilgan loyihadan. 13-oktabr Samarqand sanasi ishtirokchi bergan; bino va soat tasdiqlanmagan. Dashboard arizalari keladigan raqiblar soni emas. Manba ziddiyatlari saqlangan, taxmin bilan yo‘qotilmagan.

Bu bilim paketi haqiqiy bilet yoki tayyor tanlov sayti emas. Havoladan foydalanish va hisoblar bo‘yicha joydagi reglamentga amal qilinadi.

## Joylashtirish variantlari

**GitHub Gist:** to‘rtta matn faylini bitta gistga qo‘shish. Qisqa kontekst uchun Raw havolasini nusxalash. Asl PDFlar Gist matn paketiga kiritilmaydi.

**GitHub repository:** butun paketni joylashtirish; README yoki 00-START-HERE.md asosiy kirish nuqtasi. PDFlar uchun sources/ papkasidagi fayllar. GitHub Pages alohida chiroyli veb sahifa kerak bo‘lsa qo‘shilishi mumkin, AI konteksti uchun majburiy emas.

**Notion:** qisqa va to‘liq matnni sahifalarga qo‘yib Publish qilish. AIga ishchi workspace havolasi emas, nashr qilingan sahifa havolasi beriladi.

GitHub Gistdagi Secret holat qidiruvdan yashiradi, lekin havolani bilgan odam o‘qiy oladi; bu private saqlash emas. Matn nusxalaridan shaxsiy obuna, joriy foydalanish foizlari va reset tafsilotlari olib tashlangan. Ism, telefon, email, parol yoki API kaliti kiritilmagan. Asl tashkilotchi PDFlarida rasmiy shaxslar imzolari va muhrlar bor.

## Yangi AIga beriladigan so‘rov

```text
Quyidagi havoladagi ai.md to‘liq kontekstini ochib o‘qi:
[nashr qilingandan keyingi haqiqiy havola]

Tasdiqlangan qoidalar, loyiha takliflari va hali noma’lum holatlarni ajrat.
Tushunganingni qisqa ayt. Keyin men haqiqiy bilet, materiallar,
ajratilgan vaqt va joydagi akkaunt cheklovlarini beraman.
Asl manbani tekshirish kerak bo‘lsa sources/ ichidagi PDFlarni o‘qi.
```

Havola ochilmasa, 00-START-HERE.md matnini chatga qo‘yish yoki faylini yuklash mumkin. Qisqa kontekstdan boshlash to‘liq hisobotni har safar o‘qitishga nisbatan kamroq matn talab qiladi; aniq sarf AI xizmatiga bog‘liq.
