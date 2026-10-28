# Mahalliy va internet manbalari reyestri

> MAQOM: 2026-10-09 holatidagi tarixiy tadqiqot/tayyorgarlik qaydi. 13-oktabrga oid reja joriy sana, bosqich yoki natija deb olinmaydi. Hozirgi vazifa va reglament ustuvor. [Kontekst maqomi](https://azizbeksafarov.github.io/ustoz/CONTEXT-STATUS.md).

Tekshirilgan ma’lumotlar 2026-yil 9-oktabr holatiga. Bir xil e’lonni ko‘chirgan norasmiy sahifalar yangi mustaqil tasdiq deb hisoblanmagan. Ko‘rsatilgan sanalar e’lon sanasi; ular tanlov bosqichining boshlanish sanasi bilan aralashtirilmaydi.

## Mahalliy manbalar

| ID | Manba | Maqom va foydalanish |
|---|---|---|
| L1 | [34-19 q-q.pdf](sources/34-19-q-q.pdf), 18 bet | Imzo va muhrli iyul qo‘shma qarori. Ishtirok, bosqichlar, asosiy mezonlar, mualliflik, apellyatsiya. [OCR matni](sources/34-19-q-q-ocr.txt). |
| L2 | [Veb-sayt mezonlari](sources/Eng_yaxshi_veb_sayt_baholash_mezonlari.pdf), 11 bet | Tashkilotchilar tasdig‘iga taqdim etilgan loyiha. Texnik tartiblar va 21 kichik ko‘rsatkich; yakuniy tasdiq deb ko‘rsatilmaydi. [O‘qilgan matn](sources/veb-mezonlari-text.txt). |
| L3 | [Tashkilotchilar rasmi](sources/tashkilotchilar.png) | Foydalanuvchi yuborgan poster. Hamkorlar logotiplari va mashina tasvirlari. |
| L4 | [Video transkripti](04-VIDEO-POSTER.md) | Foydalanuvchi yuborgan ko‘rsatma matni; audio mustaqil qayta tinglanmagan. |

## Rasmiy internet e’lonlari

| ID | Sana | Manba | Tadqiqotdagi ahamiyati |
|---|---|---|---|
| W1 | 2026-08-14 | [Ustoz AI /3134](https://t.me/ustozai/3134) | Avvalgi 20-avgust muddati va pul mukofotlari davri. Hozirgi jadval sifatida olinmaydi. |
| W2 | 2026-09-03 | [Ustoz AI /3213](https://t.me/ustozai/3213) | Ariza muddati 10-sentabrgacha uzaytirilgani; eski pul mukofotlari xabari. |
| W3 | 2026-09-07 | [Ustoz AI /3228](https://t.me/ustozai/3228) | Changan bilan hamkorlik muhokamasi haqidagi avvalgi xabar; yakuniy sovrin uchun W4–W6 kuchliroq manbalar. |
| W4 | 2026-09-28, 16:25 | [Oila va xotin-qizlar qo‘mitasi](https://gov.uz/oz/wcu/news/view/225579) | Uchta Changan, uch yo‘nalish, sertifikat, ariza 30-sentabrgacha. |
| W5 | 2026-09-28 | [Kasbiy ta’lim agentligi /2763](https://t.me/kasb_edu/2763) | 1-o‘rin sohiblariga uchta Changan Uni-E; 14–30 yosh, sertifikat, uch bosqich. |
| W6 | 2026-09-28 | [Ustoz AI /3331](https://t.me/ustozai/3331) | Changan e’loni va 30-sentabr ariza muddati. |
| W7 | 2026-10-05 | [Ustoz AI /3357](https://t.me/ustozai/3357) | Veb-sayt yo‘nalishi uchun ko‘rsatma videosi sahifasi. |
| W8 | 2026-10-05 | [Ustoz AI /3356](https://t.me/ustozai/3356) | Mobilografiya yo‘nalishi videosi; veb bilet yoki veb vaqt limiti sifatida foydalanilmaydi. |
| W9 | 2026-10-07, 08:05 | [O‘zbekiston tumani hokimligi](https://gov.uz/oz/yaypan/news/view/229498) | Farg‘onada tuman bosqichi o‘tkazilgani; oktabrdagi tanlov faoliyati. Samarqand manzili emas. |

Telegram sahifalari rasmiy kanallarning ochiq veb ko‘rinishidan ham tekshirilgan. Asosiy havola uchun kanalning kanonik t.me manzili berilgan.

## Sayt, dashboard va API

| ID | Manba | Natija |
|---|---|---|
| W10 | [ustoz.ai/tanlov](https://ustoz.ai/tanlov/) | Hozir qabul yakunlangan yozuvi; 30-sentabr muddati. |
| W11 | [Saytdagi nizom](https://ustoz.ai/tanlov/nizom.pdf) | 10 betlik tahrir; mahalliy qaror bilan jadval, teng ball, texnik tahrir va mezon tartibi solishtirilgan. [Nusxa](sources/ustoz-ai-saytdagi-nizom.pdf), [matn](sources/sayt-nizomi-text.txt). |
| W12 | [Dashboard](https://ustoz.ai/tanlov/dashboard) | 9-oktabr taxminan 19:10 Toshkent vaqtidagi agregat statistika. Ism/telefon/email ko‘chirilmagan. |
| W13 | [App dastur fayli](https://ustoz.ai/tanlov/assets/App-DUrR6nsF.js) | Ommaviy frontenddagi API baza, ariza va sertifikat tekshirish vazifalari. |
| W14 | [Dashboard dastur fayli](https://ustoz.ai/tanlov/assets/Dashboard-CniU0oMk.js) | Ro‘yxat va eksport yo‘llari; ism/sertifikat avtomatik ogohlantirishi ma’nosi. |
| W15 | [Dastlabki dastur fayli](https://ustoz.ai/tanlov/assets/index-CxuqA5lE.js) | Saytning ommaviy frontend tuzilishini ko‘rish uchun ishlatilgan. Asset nomlari sayt yangilanganda o‘zgarishi mumkin. |
| W16 | [Qisqa ro‘yxat havolasi](https://clck.ru/3V7zkP) | Tanlov sahifasiga yo‘naltirish tekshirilgan. |

API bazasi: `https://api.ustozaibot.uz/api/v1`. Frontenddagi yo‘llar: `POST /applications`, `GET /applications`, `GET /applications/export`, sertifikat identifikatori bilan verify yo‘llari. Bular to‘liq API hujjati emas. Tadqiqotda ariza yuborilmadi, arizachilarning kontaktlari eksport qilinmadi.

## Hududiy aloqa va Ustoz AI loyihasi

| ID | Manba | Natija |
|---|---|---|
| W17 | [SAMARQANDLIK YOSHLAR — @yiasamyosh](https://t.me/yiasamyosh) | Samarqand Yoshlar ishlari agentligi kanali; aniq 13-oktabr bino/soat e’loni topilmagan. |
| W18 | [@samyoshbot](https://t.me/samyoshbot) | Kanal ko‘rsatgan mahalliy aloqa. Hech qanday xabar yuborilmagan. |
| W19 | [Yoshlar ishlari agentligi kontaktlari](https://gov.uz/oz/yoshlar/contacts) | Respublika rasmiy aloqa manbasi. |
| W20 | [Ustoz AI loyiha sahifasi](https://gov.uz/oz/yoshlar/sections/view/28204) | Loyihaning umumiy maqsadi va ta’lim konteksti. Eski loyiha ko‘rsatkichlari tanlov natijasi deb olinmagan. |

## AI xizmatlari bo‘yicha rasmiy manbalar

- [Codex kirish va foydalanish limitlari](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan): ChatGPT akkaunti orqali kirish; tarif va vazifaga bog‘liq limitlar. Yangi kompyuter mavjud hisobni avtomatik Free qilmaydi yoki foydalanishni yangilamaydi.
- [Codex ilovasi](https://developers.openai.com/codex/app), [autentifikatsiya](https://developers.openai.com/codex/auth): rasmiy mahsulot hujjatlari; tekshiruvda learn.chatgpt.com yo‘nalishlari ham ko‘rindi.
- [Google Antigravity FAQ](https://antigravity.google/docs/faq): shaxsiy Google akkaunti, 18+ talabi, O‘zbekiston hududiy mavjudligi va o‘z limitlari. ChatGPT Plus bu xizmatning obunasi emas.
- [Antigravity hujjatlari](https://www.antigravity.google/docs): ilovaga oid rasmiy hujjatlar; joydagi versiya va sozlamalar alohida bo‘lishi mumkin.

## Hali noma’lum

Samarqandning aniq bino/zal va soati; amaliy ishning aniq limiti; finalning yangi sanasi; hududiy yakuniy tarkib; tasdiqlangan texnik tahrir; hisoblar/model/limitlarni tenglashtirish; topshirish kanali; yangilangan 2–3-o‘rin mukofotlari; avtomobil komplektatsiyasi va topshirish tafsilotlari. Bu joylar taxmin bilan to‘ldirilmagan.

Fayllar yaxlitligi va statistik faktlar [07-FACTS.json](07-FACTS.json) da. Bayonlar va tafovutlar [01-RESEARCH.md](01-RESEARCH.md) da batafsil.


## 2026-10-28 qoidalar bo‘yicha qayta tekshiruv

- https://ustoz.ai/tanlov/nizom.pdf — qayta olingan nusxa avvalgi hash bilan bir xil.
- https://zamonaviykasblar2026.uz/ — ochiq tushuntirish matni: vazifa bir vaqtda beriladi; 15 daqiqa himoya; 6 mezon/100 ball. Yangi imzolangan nizom topilmadi.
- Asl qaror va mezonlar loyihasi yuqoridagi manbalarda o‘z maqomida saqlanadi. Yangi amaliy vaqt, akkaunt/tarif va tayyor backend bo‘yicha qo‘shimcha rasmiy ko‘rsatma aniqlanmadi.

Joriy xulosa 08-CURRENT.md’da. Yangi qoida o‘rniga statistika, natija yozuvlari yoki portalning texnik arxitekturasi ishlatilmaydi.
