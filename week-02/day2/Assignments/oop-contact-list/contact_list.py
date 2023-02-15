class ContactList:
  
  def __init__(self, list_name, contact_dict=None):
    self._list_name = list_name
    self._contact_dict = [] if contact_dict is None else contact_dict
    
  def add_contact(self, contact_dict):
    self._contact_dict.append(contact_dict)

  def remove_contact(self, name_to_rem):
    for contact in self._contact_dict:
      if contact['name'] == name_to_rem:
        self._contact_dict.remove(contact)
        return('found and removed')
    return('Contact not found')
        
  def find_shared_contacts(self, other_list):
    matches = []
    for contact in self._contact_dict:
      for other_contact in other_list._contact_dict:
        if contact == other_contact:
          matches.append(contact)
    if matches == []:
      return('No matches')
    return matches
      
    


friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'},{'name':'Carlos', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_newest_list = ContactList('newest list')
my_new_list = ContactList('new list')
my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)
my_friends_list.remove_contact('Alice')
my_new_list.add_contact({'name': 'Frank', 'number': '123-456'})
print(my_new_list._contact_dict)
print(my_friends_list._contact_dict)
print(my_newest_list._contact_dict)

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
print(friends_i_work_with)


# contact_dict=None
# [] if contact_dict is None else contact_dict