import json
from datetime import datetime, timezone, timedelta

import requests

VN_TZ = timezone(timedelta(hours=7))


def _get_friday_date() -> str:
    now = datetime.now(VN_TZ)
    return now.strftime("%d/%m/%Y")


def build_card_payload() -> dict:
    friday_date = _get_friday_date()

    return {
        "cardsV2": [{
            "cardId": "weekly-report-reminder",
            "card": {
                "header": {
                    "title": "Weekly Report Reminder",
                    "subtitle": f"Friday, {friday_date}",
                    "imageUrl": "https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/edit_note/default/48px.svg",
                    "imageType": "CIRCLE",
                },
                "sections": [
                    {
                        "widgets": [
                            {
                                "decoratedText": {
                                    "icon": {"knownIcon": "CLOCK"},
                                    "topLabel": "Deadline",
                                    "text": "<b>Today, 6:00 PM</b>",
                                },
                            },
                            {
                                "decoratedText": {
                                    "icon": {"knownIcon": "DESCRIPTION"},
                                    "topLabel": "Action Required",
                                    "text": "Submit your <b>weekly report</b>",
                                },
                            },
                        ],
                    },
                    {
                        "header": "Checklist",
                        "widgets": [
                            {
                                "textParagraph": {
                                    "text": (
                                        "1. What did you accomplish this week?\n"
                                        "2. What are your plans for next week?\n"
                                        "3. Any blockers or risks?"
                                    ),
                                },
                            },
                        ],
                    },
                    {
                        "widgets": [
                            {
                                "textParagraph": {
                                    "text": "<i>Please submit on time. Thank you!</i>",
                                },
                            },
                        ],
                    },
                ],
            },
        }],
    }


def send_to_google_chat(webhook_url: str, dry_run: bool = False) -> bool:
    payload = build_card_payload()

    if dry_run:
        print(json.dumps(payload, indent=2))
        return True

    resp = requests.post(
        webhook_url,
        json=payload,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        timeout=15,
    )
    resp.raise_for_status()
    return True
