# 🤖 Bio Mute Bot

A powerful Telegram moderation bot that mutes users based on bio content (like links or @usernames), welcomes members, warns for links in messages, supports customizable mute durations, and even broadcasts messages/images across all users and groups.

---

## 🌐 Features

- Auto-mute users who join with links or @usernames in their bio or name
- Welcome message with custom buttons
- Warn & mute system for link spammers
- Private and group mute notifications
- Broadcast system (text, image, buttons)
- Owner commands (restart, stats, mute duration, etc.)
- MongoDB-based storage
- Heroku and VPS ready

---

## 🚀 Deploy

### 🔵 Heroku (One-Click)

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/riteshxcoder/Biolink)

> Fill in the required variables during deployment.

---

### 🟢 VPS Deploy (Ubuntu/Debian)

```bash
# Clone the repo
git clone https://github.com/riteshxcoder/Biolink.git
cd biolink

# Install dependencies
sudo apt update
sudo apt install ffmpeg python3-pip -y

# Install Python requirements
pip3 install -r requirements.txt

# Add env variables
cp .env.example .env  # and fill it manually

# Start bot
python3 -m bot
