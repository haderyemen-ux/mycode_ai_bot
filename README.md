# My Code Bot

مساعد برمجي عربي على Telegram يعمل مع Gemini.

## الحل الأساسي: Cloudflare Workers

مسار Cloudflare هو المسار الموصى به لهذا البوت. Worker يعمل كـ webhook serverless، فلا يحتاج إلى Python أو Gunicorn أو عملية تعمل باستمرار.

خطة Cloudflare Workers Free الحالية تسمح حتى 100,000 طلب يوميًا، ولا يوجد فيها إيقاف بعد 15 دقيقة من الخمول مثل Render Free.

### ملفات المشروع

- cloudflare-worker/src/index.js
- cloudflare-worker/wrangler.jsonc
- cloudflare-worker/package.json

### الأسرار المطلوبة

في Cloudflare Worker > Variables and Secrets أضف فقط:

- TELEGRAM_TOKEN = توكن BotFather الكامل، بما فيه النقطتان
- GEMINI_API_KEY = مفتاح Gemini

ولا تضع الأسرار في GitHub.

### النشر

1. Cloudflare Dashboard → Workers & Pages.
2. Create application → Import a repository.
3. اختر المستودع haderyemen-ux/mycode_ai_bot.
4. اجعل Root directory = cloudflare-worker.
5. Save and Deploy.
6. أضف السرّين السابقين.
7. افتح عنوان Worker ثم /setup مرة واحدة.
8. افتح /health للتحقق.

يجب أن يظهر:
telegram_configured = true
telegram_format_valid = true
gemini_configured = true

بعد ذلك أرسل /start في Telegram.

### Render

تم إبقاء مسار Render كخيار بديل داخل:
- bot.py
- requirements.txt
- Procfile
- render.yaml

لكن Render Free يوقف خدمة الويب بعد 15 دقيقة بدون طلبات واردة. لذلك ليس هو المسار الأساسي لهذا البوت.

### Gemini

النموذج الأساسي:
gemini-3.8-flash

وهو نموذج متاح حاليًا في Gemini API، وله طبقة مجانية وفق صفحة التسعير الرسمية.
