import random

start_subs = ''
subs = ''

def start_subs():
  global start_subs
  global subs

  start_subs = random.randint(1, 100)
  start_subs = subs

def display_subs():
  global start_subs
  global subs

  print('\nsubs: ' + str(subs))



cheese = input('welcome to youtubey simulator would you like to start y/n?')

if cheese == 'n':
  print('\nyou didnt accept your offer of becoming a popular youtubey person. and didnt go BRRRRRRRRRRRRRRRRRRRRRRRR Big sad boii times R.I.P ')

if cheese == 'y': 
  cheese = input('\nso you became a youtubey person youll start of with RANDOM youtubey subs. gain subs by obtaining plushies, gear, promotion softwares, and by making videos Enjoy your experince!!!!! TYPE START TO PLAY')

  def genre():
    global cheese

    cheese = input('\npick your genre\ngaming\nvlogs\nmusic\nbeauty')
    if cheese == 'gaming':
      print('you picked gaming')
      display_subs()
    elif cheese == 'vlogs':
      print('')
    elif cheese == 'music':
      print('')
    elif cheese == 'beauty':
      print('')

  if cheese == 'start':
    genre()


    
  