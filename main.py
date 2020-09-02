import random

subs = 0
subs_per_video = random.randint(0, 500)

def display_subs():
  global subs

  print('\nsubs: ' + str(subs))

def video():
  global subs
  global subs_per_video

  print('you made a video.')
  print('\nyou got ' + str(subs_per_video) + ' from that video!')
  subs = subs + subs_per_video
  print('\nyou now have ' + str(subs) + ' subscribers!')

cheese = input('welcome to youtubey simulator would you like to start y/n?')

if cheese == 'n':
  print('\nyou didnt accept your offer of becoming a popular youtubey person. and didnt go BRRRRRRRRRRRRRRRRRRRRRRRR Big sad boii times R.I.P ')

if cheese == 'y': 
  cheese = input('\nso you became a youtubey person youll start of with RANDOM youtubey subs. gain subs by obtaining plushies, gear, promotion softwares, and by making videos Enjoy your experince!!!!! TYPE START TO PLAY')

  def game_start():
    global cheese

    cheese = input('\npick your genre\ngaming\nvlogs\nmusic\nbeauty')
    if cheese == 'gaming':
      print('you picked gaming')
      display_subs()
      cheese = input('press v to make a video ')
      if cheese == 'v':
        video()
    elif cheese == 'vlogs':
      print('you picked vlogs')
      display_subs()
    elif cheese == 'music':
      print('you picked music')
      display_subs()
    elif cheese == 'beauty':
      print('you picked beauty')
      display_subs()

  if cheese == 'start':
    while True:
      game_start()


    
  