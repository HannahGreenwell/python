# Build a database using a dictionary
import pickle

# Use a nested dictionary to create a database of movies, books, albums, or whatever you want, with appropriate fields for each item.
best_chinese_movies = {
  'raise_the_red_lantern': {
    'full_title': 'Raise the Red Lantern',
    'director': 'Zhang Yimou',
    'year': 1992,
    'length': 125,
    'rating': 'PG',
    'actors': ['Gong Li', 'Ma Jingwu', 'He Saifei'],
  },
  'red_sorghum': {
    'full_title': 'Red Sorghum',
    'director': 'Zhang Yimou',
    'year': 1988,
    'length': 91,
    'rating': 'M',
    'actors': ['Gong Li', 'Jiang Wen', 'Teng Rujun'],
  },
  'lost_in_beijing': {
    'full_title': 'Lost in Beijing',
    'director': 'Li Yu',
    'year': 2007,
    'length': 118,
    'rating': 'M',
    'actors': ['Fan Bingbing', 'Tong Dawei', 'Tony Ka Fei Leung'],
  },
  'chungking_express': {
    'full_title': 'Chungking Express',
    'director': 'Wong Kar-Wai',
    'year': 1994,
    'length': 108,
    'rating': 'PG',
    'actors': ['Faye Wong', 'Tony Chiu-Wai Leung', 'Takeshi Kaneshiro'],
  },
  'the_god_of_cookery': {
    'full_title': 'The God of Cookery',
    'director': 'Stephen Chow',
    'year': 1996,
    'length': 95,
    'rating': 'M',
    'actors': ['Stephen Chow', 'Karen Mok', 'Nancy Sit'],
  }
}

# Create functions to let a user:

# Lookup an item by the top level key (which we'll call the ID) and print out a formatted entry of all the fields for the record found, e.g. find_by_id(db, 'ulysses'). A polite error message should be printed if the key does not exist.
def find_by_id(database, id):
  if id in database:
    selected_item = database[id]
    for key, value in selected_item.items():
      print('{}: {}'.format(key.replace('_', ' ').capitalize(), value))
  else:
    print('Sorry, item not found.')


# Search for an item by the value of a specific fields, e.g. find_by_field(db, 'year', 1974). It should print the details of any record that matches. Bonus: allow substring matches for string values.
def find_by_field(database, field, search_value):
  for key in database:
    current_record = database[key]
    if field in current_record:
      current_value = current_record[field]
      if type(current_value) == str:
        if current_value.lower().find(search_value.lower()) > -1:
          print(current_record)
      elif type(current_value) == list:
        if search_value in current_value:
          print(current_record)
      else:
        if current_value == search_value:
          print(current_record) 


# Add a new item by passing in the key-value pairs as keyword arguments, e.g. create_record(db, 'debt', full_title='Debt: The First 5,000 Years', author='David Graeber', ...etc...). Your function should give an error if a record with the same ID (top-level key) already exists!
def create_record(database, id, **kwargs):
  if id in database:
    print('Sorry, item already in database.')
  else:
    database[id] = kwargs
    

# Edit an item interactively, specifying the ID in the function call, and then using input() to update each key-value pair, after printing the current value for that key (use a for loop to do this). Bonus: allow the user to just press enter to keep the existing values.
def update_record(database, id):
  if id in database:
    record_to_update = database[id]
    for key, value in record_to_update.items():
      print('Current {}: {}'.format(key, value))
      new_value = input('New {}: '.format(key))
      if new_value:
        record_to_update[key] = new_value
  else:
    print('Sorry, item not found.')


# Work out how to save/load your dictionary to/from disk, so any changes made are preserved (hint: 'pickle').
with open('best_chinese_movies.pickle', 'wb') as file:
  pickle.dump(best_chinese_movies, file)

with open('best_chinese_movies.pickle', 'rb') as file:
  file_contents = pickle.load(file)