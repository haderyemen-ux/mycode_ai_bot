# START HERE — My Code Bot

## المسار الموصى به

استخدم Cloudflare Worker الموجود داخل:
cloudflare-worker

## خطوات النشر

1. افتح Cloudflare Workers & Pages.
2. اختر Create application.
3. اختر Import a repository.
4. اربط GitHub واختر haderyemen-ux/mycode_ai_bot.
5. اضبط Root directory على:
cloudflare-worker
6. اضغط Save and Deploy.

## بعد أول Deploy

في Worker → Settings → Variables and Secrets أضف:

TELEGRAM_TOKEN
القيمة: توكن BotFather الكامل كما هو، بما في ذلك :

GEMINI_API_KEY
القيمة: مفتاح Gemini

لا تضف TELEGRAM_BOT_ID بدل التوكن الكامل.

## تفعيل Telegram

بعد إضافة السرّين، افتح:

https://YOUR-WORKER.workers.dev/setup

الصفحة ستسجل webhook تلقائيًا على عنوان Worker الحالي.

ثم افتح:

https://YOUR-WORKER.workers.dev/health

القيم الصحيحة:

telegram_configured: true
telegram_format_valid: true
gemini_configured: true

ثم أرسل /start للبوت.

## ملاحظة

لا ترسل أي Token أو API key هنا في المحادثة. استخدم قيم الأسرار داخل Cloudflare فقط.
