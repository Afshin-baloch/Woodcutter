from instabot import Bot
import time

# ایجاد یک شیء از کلاس Bot
bot = Bot()

# ورود به حساب اینستاگرام
bot.login(username="your_username", password="your_password")

# ارسال یک کامنت
bot.comment("post_link_or_media_id", "Your comment here!")

# خروج از حساب اینستاگرام
bot.logout()

