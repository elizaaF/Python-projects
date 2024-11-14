import random 
import string 

def passwors_generator(min_length, numbers=True, special_characters=True):
  letters = string.ascii_letters
  digits = string.digits
  special_char = string.punctuation

  charachter = letters
  if numbers:
    charachter += digits
  if special_characters:
    charachter += special_char

  pwd = ''
  meets_criteria = False
  has_numbers = False
  has_Sepcial = False 

  while not meets_criteria or len(pwd) < min_length:
    new_char = random.choice(charachter)
    pwd += new_char 

    if new_char in digits:
      has_numbers = True
    elif new_char in special_char:
      has_Sepcial = True

    meets_criteria = True
    if numbers:
      meets_criteria = has_numbers
    if special_characters:
      meets_criteria = meets_criteria and has_Sepcial

      return pwd 
    

min_length = int(input('Enter the minimum length: '))
has_number = input('Do you want to have numbers(y/n)? ').lower() == 'y'
has_special = input('Do you want to have a special character (y/n)? ').lower() == 'y'
pwd = passwors_generator(min_length, has_number, has_special)
print(pwd)

