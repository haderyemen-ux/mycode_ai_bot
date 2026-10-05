# My Code Bot

Telegram coding assistant powered by Gemini.

## Netlify deployment

This repository includes a dedicated Netlify Functions implementation in:

`netlify/functions/bot.mjs`

Netlify serves the static status page from `index.html`.

### Required Netlify Environment Variables

Set these in the Netlify project under Environment Variables and make sure their scope includes **Functions**:

- `TELEGRAM_TOKEN` = the complete BotFather token, including the `:`.
- `GEMINI_API_KEY` = the Gemini API key.
- `SETUP_SECRET` = a private random string used only to authorize webhook setup.
- `TELEGRAM_WEBHOOK_SECRET` = optional secret used by Telegram when calling the webhook.
- `GEMINI_MODELS` = optional comma-separated models. Default: `gemini-3.8-flash,gemini-3.6-flash`.
- `MAX_HISTORY` = optional, default `12`.
- `MAX_OUTPUT_TOKENS` = optional, default `4096`.
- `TEMPERATURE` = optional, default `0.25`.

Do not put these secrets in `netlify.toml` or source code.

### After the first Netlify deploy

1. Open `/health` and verify `telegram_format_valid` and `gemini_configured` are true.
2. Open `/setup?key=YOUR_SETUP_SECRET` once. This calls Telegram `setWebhook` and registers the bot commands.
3. Send `/start` to the bot.

The webhook endpoint is:

`/telegram/webhook`

## Render fallback

The original Python/Flask implementation remains in `bot.py` so the repository can still be used on Render.
