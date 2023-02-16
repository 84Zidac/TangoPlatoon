# Your User class goes here
class User:
    everyones_posts = []
    def __init__(self, first_name, last_name, email, drivers_licence='not provided', age='not provided', sex='not provided', location='not provided', posts=None):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._drivers_licence = drivers_licence
        self._age = int(age)
        self._sex = sex
        self._location = location
        self._posts = [] if posts is None else posts

    def __str__(self):
        return f"Name={self._last_name, self._first_name} \n Email: {self._email} \n Drivers Licence ={self._drivers_licence} \n Age={self._age} Sex={self._sex} \n Location= {self._location}"
    
    def post(self, post_str):
      User.everyones_posts.append(f"{self._first_name} said: {post_str}")
      self._posts.append(f"{self._first_name} said: {post_str}")
    
    def del_post(self, post_to_rem):
      try:
        User.everyones_posts.remove(f"{self._first_name} said: {post_to_rem}")
        self._posts.remove(f"{self._first_name} said: {post_to_rem}")
      except ValueError:
        print("That post was not found")
      
    def my_posts(self):
      print(self._posts)
      
    def all_posts(self):
      print(User.everyones_posts)


