# My Code Bot

مساعد برمجي عربي على Telegram يعمل مع Gemini.

## مسار التشغيل الموصى به: Cloudflare Workers

هذا هو المسار الأساسي للمشروع لأنه لا يحتاج إلى Python أو Gunicorn أو Render، ويعمل كـ webhook serverless. خطة Workers Free حاليًا تسمح حتى 100,000 طلب يوميًا، ولا توجد مدة خمول تجعل Worker يتوقف مثل خدمة Render Free.

المشروع موجود في:
- cloudflare-worker/src/index.js
- cloudflare-worker/wrangler.jsonc
- cloudflare-worker/package.json

### أسرار Cloudflare

أضف هذه القيم في Worker > Variables and Secrets:
- TELEGRAM_TOKEN = توكن BotFather الكامل، بما فيه النقطتان
- GEMINI_API_KEY = مفتاح Gemini
- SETUP_SECRET = قيمة عشوائية خاصة لتأمين إعداد webhook
- TELEGRAM_WEBHOOK_SECRET = اختياري لكنه موصى به

لا تضع أي سر في GitHub أو wrangler.jsonc.

### النشر من GitHub

في Cloudflare:
1. Workers & Pages
2. Create application
3. Import a repository
4. اختر haderyemen-ux/mycode_ai_bot
5. Root directory = cloudflare-worker
6. Save and Deploy

بعد النشر أضف الأسرار، ثم افتح:
https://YOUR-WORKER.workers.dev/setup?key=YOUR-SETUP-SECRET

ثم:
https://YOUR-WORKER.workers.dev/health

يجب أن تكون:
- telegram_configured = true
- telegram_format_valid = true
- gemini_configured = true

بعدها أرسل /start للبوت.

## Render

تم الإبقاء على Render كمسار بديل في:
- bot.py
- requirements.txt
- Procfile
- render.yaml

إعداد Render يستخدم Secret Files لتفادي مشكلة إدخال توكن Telegram في Environment Variables. المسار المتوقع:
 /etc/secrets/telegram_token.txt
و
 /etc/secrets/gemini_api_key.txt

لكن Render Free يوقف خدمة الويب بعد 15 دقيقة من عدم وجود طلبات واردة، لذلك Cloudflare Workers هو المسار الأبسط للبوت المجاني المستمر.

## Gemini

تم تثبيت نموذج Gemini الأساسي على:
gemini-3.8-flash

مع دعم نماذج Gemini 3 الأخرى عند الحاجة.
