# My Code Bot

Telegram coding assistant powered by Gemini.

## Netlify deployment

This repository includes a dedicated Netlify Functions implementation in:

`netlify/functions/bot.mjs`

Netlify serves the static status page from `public/index.html`.

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

## Render deployment

The production Render service uses `bot.py` behind Gunicorn.

### Required Render Environment Variables

Do **not** put the Telegram token in the Render **Key** field.

Use these exact Keys:

- `TELEGRAM_BOT_ID` = the numeric part before the colon.
- `TELEGRAM_BOT_SECRET` = the part after the colon.
- `GEMINI_API_KEY` = your Gemini API key.

For example, a BotFather token shaped like `1234567890:AAxxxx...` is entered as:

`TELEGRAM_BOT_ID = 1234567890`

`TELEGRAM_BOT_SECRET = AAxxxx...`

The application rebuilds `1234567890:AAxxxx...` internally, so no Render Key contains a colon.

### Render start command

`gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120 bot:app`

Save the environment variables with **Save, rebuild, and deploy** (or **Save and deploy** when the build does not need to change).

The application logs only non-secret configuration status. A healthy startup should show `telegram_source=split`, `telegram_format_valid=True`, and `gemini_configured=True`.

Render automatically exposes `RENDER_EXTERNAL_URL` to web services; the application uses it to register the Telegram webhook when available.

Do not commit secret values to GitHub.
