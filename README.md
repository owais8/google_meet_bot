# google_meet_bot
* [Prerequisites](#Prerequisites)
* [What is inside notebook](#What-is-inside-notebook?)
* [How to run script](#How-to-run-script?)

Presenting "Tabedar Shaagird (تابعدار شاگرد ), A selenium based Python Bot that automatically joins Google Meet meetings. Automatically turns off your microphone and camera before joining. Always joins and leaves the meeting at specified time.
## Prerequisites
* Python3 ([Download](https://www.python.org/downloads/))
* ChromeDriver ([Download](https://chromedriver.chromium.org/))

## Configurations
* Turn off two factor authorization on your google account

  Make sure that two factor authorization is off on your google account otherwise you will not be able to use this bot
  
* Email/Password

  Don't forget to replace the text "WRITE YOUR EMAIL HERE B/W THESE TWO QUOTES" and  "WRITE YOUR PASSWORD HERE B/W THESE TWO QUOTES" with your email/password of your google 
  account respectively (these credentials will be used to login into google meet)
  
* ChromeDriver

  You will also have to download ChromeDriver (Link given above). As soon as you download it replace the text "ENTER PATH OF CHROMIUM DRIVER HERE" in 27 line with path of your
  exe file
 
 * google_meet_data.csv file
 
   This file contains all your timetable for the week. Just fill in all the information there for week and let the bot handle everything for you. Make sure that you enter time
   in 24h format and day as "Monday", "Tuesday" etc.

## How to run script

1. Download all the neccessary files mentioned in "Prerequisites" section
2. Follow all the steps mentioned in "Configuration" section
3. Run google_meet_bot.py file and see the magic 
