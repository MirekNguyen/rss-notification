import os
from dotenv import load_dotenv
import argparse

class SettingsLoader:
    def load_env(self)-> dict:
        load_dotenv()
        parser = argparse.ArgumentParser(description="Github RSS")
        parser.add_argument("-o", "--output", required=True, action="store", help="Output (required)")
        parser.add_argument("-t", "--title", required=True, action="store", help="Title (required)")
        parser.add_argument("-l", "--link", required=True, action="store", help="Link (required)")
        args = parser.parse_args()

        return {
            "GITHUB_TOKEN": self.__env("GITHUB_TOKEN"),
            "USER": self.__env("USER"),
            "TITLE": args.title,
            "LINK": args.link,
            "OUT_DIR": args.output
        }
    def __env(self, key: str):
        return os.environ.get(key, os.getenv(key))
