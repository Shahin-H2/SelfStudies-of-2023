"""Break reminder: an hourly desktop notification to take a break.

Runs in the terminal and shows a desktop notification titled "ALERT!!!"
with the message "Take a break! It has been an hour!", asking plyer to
keep it on screen for 10 seconds. The first notification appears as
soon as the script starts; after each one the script sleeps for an
hour (3600 seconds) and then shows the next. Press Ctrl+C to stop it.

Needs the third-party plyer package (``pip install plyer``). That is
enough on Windows; on macOS plyer also needs pyobjus, and on Linux it
needs the Python dbus package or the notify-send command. If plyer is
missing, the script prints an install hint and exits with status 1. If
plyer has no way to show notifications, plyer first prints its own
traceback or warnings, then the script adds a short hint and exits
with status 1.
"""

import sys
import time

try:
    from plyer import notification
except ImportError:
    sys.exit("This script needs the plyer package: pip install plyer")

TITLE = "ALERT!!!"
MESSAGE = "Take a break! It has been an hour!"
TIMEOUT_SECONDS = 10
INTERVAL_SECONDS = 60 * 60


def main():
    """Show the break notification right away, then once every hour."""
    while True:
        notification.notify(
            title=TITLE, message=MESSAGE, timeout=TIMEOUT_SECONDS
        )
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBreak reminder stopped.")
    except NotImplementedError:
        # plyer raises this when it has no way to show notifications.
        sys.exit(
            "plyer cannot show notifications on this system.\n"
            "On macOS it also needs pyobjus: pip install pyobjus\n"
            "On Linux it needs the Python dbus package or notify-send."
        )
