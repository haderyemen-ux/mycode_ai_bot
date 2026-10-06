# My Code Bot — Cloudflare Worker

Stable serverless deployment path for My Code Bot.

Required secrets:
- TELEGRAM_TOKEN: complete BotFather token, including the colon.
- GEMINI_API_KEY: Gemini API key.
- SETUP_SECRET: random value used only to authorize webhook setup.
- TELEGRAM_WEBHOOK_SECRET: optional but recommended random value for webhook validation.

Cloudflare stores Worker secrets encrypted and exposes them only at runtime.

Cloudflare deployment:
1. Open Workers & Pages.
2. Create application, then Import a repository.
3. Select the GitHub repository haderyemen-ux/mycode_ai_bot.
4. Set Root directory to cloudflare-worker.
5. Save and Deploy.
6. Add the secrets under the Worker Variables and Secrets settings.
7. Open /setup?key=YOUR-SETUP-SECRET on the Worker once.
8. Open /health and verify telegram_configured=true, telegram_format_valid=true, gemini_configured=true.

The Worker uses direct HTTPS calls to Telegram Bot API and Gemini REST API, so there is no Python process, Gunicorn process, or SDK runtime dependency.
