# CVECrawlerBot

This is CVE finder bot. It can find certain CVE that you looking for, for now.
How to use it?
1. Create a telegram bot in BotFather in telegram.
2. Download bot.py file and extract where you want.
3. Copy your personal bot tocken and paste it in bot = telebot.TeleBot("Copy Tocken Here") string in bot.py file.
4. Start program and send /start message to your bot.
5. Then just type CVE that you want to find

Example: 
  input: CVE-2017-6345
  output:
    CVE id: CVE-2017-6345
    Source :cve@mitre.org
    .....
    ....
    ...

Also you need to install telebot and requests modules via pip install.
