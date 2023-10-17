player_database = ["waffle","soar","pixel"]
ID = input("ID #:")
if ID in player_database:
  print("player registered:", player_database[ID])
elif ID not in player_database:
  print("ID not found")