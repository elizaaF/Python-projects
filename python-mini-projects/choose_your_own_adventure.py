name = input('Type your name: ')
print('Welcome', name, 'to this adventure!')

answer = input('You are on a first road, it has come to an end and you can go left or right. Which ways would you like to go? ').lower()

if answer == 'left':
  answer = input('You come to a river, you can walk around it or swim across it, Type walk to walk around it or swim across it?')
  
  if answer == 'swim':
    print('You swam across and eaten by an alligator.')
  elif answer == 'walk':
    print('You walked for many miles, ran out of water and you lost the game.')
  else:
    print('Not a valid option. You lose.')

elif answer == 'right':
  answer = input('you come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ')

  if answer == 'back':
    print('You go back and lose.')
  elif answer == 'cross':
    answer = input('you you cross the bridge and meet a stranger. do you talk to them (yes/no)?')

    if answer == 'yes':
      print('You talk to stranger and they give you gold. You WIN!.')
    elif answer == 'no':
      print('you ignore the stranger and they are offended and you lose.')
    else:
      print('Not valid option. You lose.')
  else:
    print('Not a valid option. You lose.')

else:
  print('Not valid option. You lose.')

print('Thank you for trying', name)
