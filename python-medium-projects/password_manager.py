pwd = input('What is the master password? ')
def view():
  with open('password.txt', 'r') as f:
    for line in f.readlines():
      data = line.rstrip()
      user, passw = data.split('|')
      print('User:', user, "| Passwords", passw)
def add():
  name = input('Account Name: ')
  password = input('Password: ')

  with open('password.txt', 'a') as f:
    f.write(name + '|' + password + '\n')

while True:
  mode = input('Would you like to add a nsw password or view existing ones (view, add), press Q to quit?').lower()
  if mode == 'q':
    quit()

  if mode == 'view':
    view()
  elif mode == 'add':
    add()
  else:
    print('Invalid mode.')