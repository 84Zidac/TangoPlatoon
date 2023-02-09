def deaf_grandma():
  goodbye = 0
  while True:
    kid = input('>')
    if kid == "":
      print('WHAT?')
    elif kid == 'GOODBYE' and goodbye < 1:
      print('LEAVING SO SOON')

deaf_grandma()
