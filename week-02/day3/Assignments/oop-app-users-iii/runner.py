# Import and create your users here
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser


sara = FreeUser('Sara', 'Smithers', 'MsSmithers@email.com', 'ASD991', '32', 'F', 'Florida')
falicity = PremiumUser('Falicity', 'Armstrong', 'FArmstrong@email.com', 'JUT639', '19', 'F', 'Denmark')
dave = FreeUser('Dave', 'Jones', 'dj@email.com', 'SAE123', '34', 'M', 'Texas')
tom = PremiumUser('Tom', 'Smith', 'Toms@email.com', 'ABC890', '20', 'M', 'Utah')
sue = PremiumUser('Sue', 'Best', 'best_sue@email.com', 'JWE653', '55', 'F', 'Kansas')
tom.post('Hello')
dave.post('Hello')
dave.post('Hello')
dave.post('Hello')
dave.post('Hello')
dave.post('Hello')
dave.post('Hello tom')
dave.del_post('Hello')
sue.post('hello all')
sara.post('i love this app')
sara.post('Its the best app ever')
sara.post('How many posts can i make')
sara.del_post('i love this app')
sara.post('i hate this app')
sue.my_posts()
sue.all_posts()
sara.my_posts()
# User.all_posts()