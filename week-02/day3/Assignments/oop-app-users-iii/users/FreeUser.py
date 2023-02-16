from .User import User

class FreeUser(User):
  
  
  
  def post(self, post_str):
    if len(self._posts) < 2:
      User.everyones_posts.append(f"{self._first_name} said: {post_str}")
      self._posts.append(f"{self._first_name} said: {post_str}")
      print(f'{self._first_name} you have {2-(len(self._posts))} posts left')
    else:
      print(f'{self._first_name} you have reached your maximum of two posts')