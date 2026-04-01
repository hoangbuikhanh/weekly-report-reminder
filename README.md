# Weekly Report Reminder

A GitHub Action bot that sends a beautifully formatted Google Chat reminder to the **JS Projects** group every Friday at 4:00 PM (GMT+7), reminding project leads to submit their weekly reports.

## Setup

### 1. Create a Google Chat Webhook

1. Open your **JS Projects** Google Chat space
2. Click the space name > **Apps & integrations** > **Webhooks**
3. Name it (e.g., "Weekly Report Bot") and click **Save**
4. Copy the webhook URL

### 2. Add GitHub Secret

In your GitHub repo: **Settings > Secrets and variables > Actions > New repository secret**

| Secret | Description |
|--------|-------------|
| `GOOGLE_CHAT_WEBHOOK_URL` | The webhook URL from step 1 |

### 3. Schedule

The bot runs automatically every **Friday at 4:00 PM GMT+7** (9:00 AM UTC).

You can also trigger it manually via **Actions > Weekly Report Reminder > Run workflow**.

## Local Testing

```bash
pip install -r requirements.txt
python main.py --dry-run
```

## Card Preview

The reminder card includes:
- Header with date
- Deadline notice
- Action required
- Report checklist (accomplishments, plans, blockers)
