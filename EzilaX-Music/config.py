
# EzilaX-Music Telegram bot project
# Copyright (C) 2021  Sadew Jayasekara
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Sadew Jayasekara

from os import getenv
import os
from dotenv import load_dotenv
from EzilaX-Music.helpers.modhelps import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "EzilaX")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Ezila_Updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/584b1539d736325fab377.jpg")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_USERNAME = getenv("BOT_USERNAME", "EzilaXBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "EzilaXHelper")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Ezila_Support")
PROJECT_NAME = getenv("PROJECT_NAME", "SD Botz")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Sadew451/EzilaX-Music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1548967589 1793906138").split()))

# Updator Configs
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/sadew451/EzilaX-Music")
U_BRANCH = "master"
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

# Your MongoDB url
DATABASE_URL = os.environ.get("DATABASE_URL")
# Your Log Channel! Make a private channel and get it's ID
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# If you need to broadcast messages as a copy or Forwarded Message
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
# your telegram id
OWNER_ID = os.environ.get("OWNER_ID", "")
