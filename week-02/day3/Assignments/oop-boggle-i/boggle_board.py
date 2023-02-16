import random


class BoggleBoard:

  def __init__(self):
    pass
  
  @staticmethod 
  def shake():
    dice_dict = {'1': 'AAEEGN',
                 '2': 'ELRTTY',
                 '3': 'AOOTTW',
                 '4': 'ABBJOO',
                 '5': 'EHRTVW',
                 '6': 'CIMOTU',
                 '7': 'DISTTY',
                 '8': 'EIOSST',
                 '9': 'DELRVY',
                 '10': 'ACHOPS',
                 '11': 'HIMNQU',
                 '12': 'EEINSU',
                 '13': 'EEGHNW',
                 '14': 'AFFKPS',
                 '15': 'HLNNRZ',
                 '16': 'DEILRX'
                 }
    new_line = ''

    for dice, letters in dice_dict.items():
      rand_num = random.randrange(0,5)
      new_letter = letters[rand_num]
      if new_letter == 'Q':
        new_letter = 'Qu '
      else:
        new_letter = new_letter + '  '
      new_line = new_line + new_letter
      if len(new_line) == 12:
        print(new_line)
        new_line = ''



BoggleBoard.shake()