# FallbackBot

A small Telegram bot. When someone sends a message in DM or a group, it replies with a custom message.

Built with [wzgram](https://github.com/rjriajul/wzgram).

## How it works

- Replies to every text message in DMs and groups
- `MESSAGE` supports HTML formatting
- Picks a random image from `PIC` each time
- Adds a red button that opens your backup bot

## Variables

| Variable | Required | Description |
|---|---|---|
| `API_ID` | Yes | Telegram API ID |
| `API_HASH` | Yes | Telegram API hash |
| `BOT_TOKEN` | Yes | Token from @BotFather |
| `MESSAGE` | No | Notice text, HTML supported. Use `\n` for a new line |
| `PIC` | No | Image links separated by a space |
| `BUTTON_TEXT` | No | Text shown on the button |
| `BUTTON_LINK` | No | Link opened by the button |

Example:

```
MESSAGE=<b>Use my alt:</b>\n<i>@xyzbot</i>
PIC=https://example.com/1.jpg https://example.com/2.jpg
BUTTON_TEXT=Use Backup Bot
BUTTON_LINK=https://t.me/xyzbot
```

The button only appears if both `BUTTON_TEXT` and `BUTTON_LINK` are set.

## Deploy

### Docker

```bash
docker build -t fallbackbot .
docker run --env-file .env fallbackbot
```

### Render

1. Fork or push this repo to GitHub
2. Create a new **Web Service** and select the repo (Docker is detected automatically)
3. Add the variables above under Environment
4. Deploy

On the free plan Render sleeps the service after 15 minutes without traffic. Ping the service URL every 5 minutes with a monitor to keep it awake.

## Notes

- Photo captions are limited to 1024 characters, so keep `MESSAGE` short
- To reply to every message in groups, turn off Privacy Mode in @BotFather (`/setprivacy`)
- Stop this bot once your main bot is back online

