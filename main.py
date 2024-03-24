"""Main script to generate RSS feed from Github releases."""

from datetime import datetime

import pytz

from rss_notification.feed_entry import FeedEntry
from rss_notification.feed_generator import Feed
from rss_notification.settings_loader import SettingsLoader

settings = SettingsLoader()
env = settings.load_env()

feed = Feed()
feed.generate_fg(
    feed_id=env.get("LINK"),
    title=env.get("TITLE"),
    subtitle=env.get("TITLE"),
    link=env.get("LINK"),
)
feed.generate_rss(
    [
        FeedEntry(
            id=datetime.now().isoformat(),
            title=env.get("TITLE"),
            link=env.get("LINK"),
            description="",
            pubDate=pytz.timezone("Etc/UTC").localize(datetime.now()),
        )
    ],
    env.get("OUT_DIR"),
)
