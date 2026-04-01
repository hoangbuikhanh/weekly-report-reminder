import argparse
import os
import sys

from src.notifier import send_to_google_chat


def main() -> None:
    parser = argparse.ArgumentParser(description="Weekly Report Reminder")
    parser.add_argument("--dry-run", action="store_true", help="Print payload without sending")
    args = parser.parse_args()

    webhook_url = os.environ.get("GOOGLE_CHAT_WEBHOOK_URL", "")
    if not webhook_url and not args.dry_run:
        print("Error: GOOGLE_CHAT_WEBHOOK_URL not set", file=sys.stderr)
        sys.exit(1)

    send_to_google_chat(webhook_url, dry_run=args.dry_run)
    print("Reminder sent successfully.")


if __name__ == "__main__":
    main()
