#! /Users/yuu/repos/line-messaging-api/venv/bin/python3.12
from setuptools import setup

setup(
    name="line-messaging-api",
    version="0.1.0",
    description="A simple LINE messaging API sender.",
    author="yuu",
    packages=["line_messaging_api"],
    package_dir={"line_messaging_api": "line-messaging-api"},
    install_requires=[
        "python-dotenv",
        "line-bot-sdk",
        "setuptools"
    ],
    entry_points={
        "console_scripts": [
            "line-messaging-api = line_messaging_api.main:main",
        ],
    },
)