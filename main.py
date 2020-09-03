import random

green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_cyan = "\033[0;96m"
bright_blue = "\033[0;94m"


shop_items = ''
subs = 0
subs_per_video = random.randint(0, 5)
video_total = 0

def display_subs():
  global subs

  print('\nsubs: ' + str(subs))

def video():
  global subs
  global subs_per_video
  global video_total

  print('you made a video.')
  video_total += 1
  subs_per_video = random.randint(0, 5)
  print('\nyou got ' + str(subs_per_video) + ' from that video!')
  subs = subs + subs_per_video
  print('\nyou now have ' + str(subs) + ' subscribers!')
  print('\nyou have made ' + str(video_total) + ' total videos!')

def shop_method():
  global shop_items

  shop_items = (white + '\n\n\nGEAR\ngaming headset\ncost:1 video and 1 subscribers\nbenifits +1 subscriber gain to videos\n\n\ngaming tablet\ncost: 10 videos and 30 subscribers\nbenifits +1 views from better quality +2 subs\n\n\nOP gaming thumbnails\ncost 20 videos and 80 subscribers\nbenifits +10 subscriber gain to videos and + 50 views\n\n\ngaming computer\ncost 40 videos and and 140 subscribers\nbenifits +15 subscibers +10 watchtime +100 views\n\n\ngaming blue yeti\ncosts 60 videos and 200 subscribers\nbenifits +30 subscribers +20 watchtime +150 views\n\n\n')
  
  print(shop_items)

  cheese = input('press b to buy a gaming headset')

  if cheese == 'b':
    print('\nyou bought a headset!!')
    shop_items = (white + '\n\n\nGEAR\ngaming tablet\ncost: 10 videos and 30 subscribers\nbenifits +1 views from better quality +2 subs\n\n\nOP gaming thumbnails\ncost 20 videos and 80 subscribers\nbenifits +10 subscriber gain to videos and + 50 views\n\n\ngaming computer\ncost 40 videos and and 140 subscribers\nbenifits +15 subscibers +10 watchtime +100 views\n\n\ngaming blue yeti\ncosts 60 videos and 200 subscribers\nbenifits +30 subscribers +20 watchtime +150 views\n\n\n')
           

cheese = input('welcome to youtubey simulator would you like to start y/n?')

if cheese == 'n':
  print('\nyou didnt accept your offer of becoming a popular youtubey person. and didnt go BRRRRRRRRRRRRRRRRRRRRRRRR Big sad boii times R.I.P ')

if cheese == 'y': 
  print(red + '\nso you became a youtubey person... gain subs by obtaining plushies, gear, promotion softwares, and by making videos. Enjoy your experince!')
  cheese = input('TYPE START TO PLAY  ')

  def game_start():
    global cheese

    cheese = input(bright_blue + '\npick your genre\ngaming\nvlogs\nmusic\nbeauty')
    if cheese == 'gaming':
      print('you picked gaming')
      display_subs()
      cheese = input(green + 'press v to make a video ')
      if cheese == 'v':
        video()
    elif cheese == 'vlogs':
      print('you picked vlogs')
      display_subs() 
      cheese = input(green + 'press v to make a video ')
      if cheese == 'v':
        video()
  
    elif cheese == 'music':
      print('you picked music')
      display_subs()
      cheese = input(green + 'press v to make a video ')
      if cheese == 'v':
        video()
    elif cheese == 'beauty':
      print('you picked beauty')
      display_subs()
      cheese = input(green + 'press v to make a video ')
      if cheese == 'v':
        video()

  if cheese == 'start':
    while True:
      game_start()
      if video_total == 1:
        print('\ncongratulations on making your first video! you can now buy a headset with your ' + str(subs) + ' subscribers!')
        cheese = input('\npress s to got to the shop ')
        if cheese == 's':
          shop_method()






    
  