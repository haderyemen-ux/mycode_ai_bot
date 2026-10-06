# My Code Bot — Cloudflare Worker

هذا هو مسار التشغيل الأساسي للبوت.

## الأسرار المطلوبة

في Worker > Variables and Secrets أضف:

- TELEGRAM_TOKEN: توكن BotFather الكامل، بما فيه :
- GEMINI_API_KEY: مفتاح Gemini

لا تضع الأسرار في GitHub أو wrangler.jsonc.

يمكن إضافة TELEGRAM_WEBHOOK_SECRET اختياريًا، لكن البرنامج ينشئ سر webhook تلقائيًا من توكن Telegram عند عدم وجوده.

## النشر

في Cloudflare:
1. Workers & Pages
2. Create application
3. Import a repository
4. اختر haderyemen-ux/mycode_ai_bot
5. Root directory = cloudflare-worker
6. Save and Deploy

بعد نجاح أول Deploy، أضف السرّين ثم افتح:
https://YOUR-WORKER.workers.dev/setup

هذا يسجل أو يعيد تسجيل webhook في Telegram تلقائيًا.

ثم افتح:
https://YOUR-WORKER.workers.dev/health

يجب أن ترى:
- telegram_configured: true
- telegram_format_valid: true
- gemini_configured: true

بعدها أرسل /start للبوت.

## لماذا هذا المسار؟

Cloudflare Workers Free حاليًا يسمح حتى 100,000 طلب يوميًا ولا يوقف Worker بعد 15 دقيقة من الخمول. كما أن قيم الأسرار تُخزن كـ Secrets مشفرة وتصل للتطبيق وقت التشغيل.

Gemini 3.8 Flash هو النموذج الأساسي المستخدم في Worker.
