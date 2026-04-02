import json
from datetime import datetime, timezone, timedelta

import requests

VN_TZ = timezone(timedelta(hours=7))


def build_payload() -> dict:
    now = datetime.now(VN_TZ)
    date_str = now.strftime("%d/%m/%Y")

    return {
        "cardsV2": [{
            "cardId": "weekly-report-reminder",
            "card": {
                "header": {
                    "title": "Weekly Report Reminder",
                    "subtitle": f"Friday, {date_str}",
                    "imageUrl": "https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/edit_note/default/48px.svg",
                    "imageType": "CIRCLE",
                },
                "sections": [
                    {
                        "widgets": [{
                            "textParagraph": {
                                "text": (
                                    "@Bui Khanh Hoang tạo cho a con bot vào nhóm JS Projects "
                                    "nhắc project lead weekly report vào 4h chiều thứ 6 nhé"
                                    "<br><br>a tin mỗi e"
                                    "<br><br>🍻"
                                ),
                            },
                        }],
                    },
                ],
            },
        }],
    }


def send_to_google_chat(webhook_url: str, dry_run: bool = False) -> bool:
    payload = build_payload()

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
