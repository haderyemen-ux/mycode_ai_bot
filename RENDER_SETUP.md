# My Code Bot — Render setup

## Telegram token

Use one Render environment variable:

- Key: `TELEGRAM_BOT_TOKEN_B64`
- Value: the URL-safe, unpadded Base64 encoding of the complete BotFather token.

Do not put the Telegram token into `TELEGRAM_BOT_ID` alone. The numeric bot ID is only the part before the colon; Telegram authentication requires the complete token in the form `<id>:<secret>`.

### Windows PowerShell

Run this locally on your own computer. Never paste the real token into GitHub.

```powershell
$token = 'PASTE_YOUR_COMPLETE_BOTFATHER_TOKEN_HERE'
[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($token)).TrimEnd('=').Replace('+','-').Replace('/','_')
```

Copy only the Base64 output into Render:

```
Key:   TELEGRAM_BOT_TOKEN_B64
Value: <the Base64 output>
```

The application decodes this value internally and reconstructs the exact Telegram token before creating the Telegram client.

## Gemini

Use:

```
Key:   GEMINI_API_KEY
Value: <your Gemini API key>
```

## Render start command

```
gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120 bot:app
```

## Health check

```
/health
```

The health endpoint never displays the Telegram token or Gemini key.
