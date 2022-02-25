from client import Client

# get username for new chat member
username = input('Please enter a username: ')

# initialize a new Client instance
new_client = Client(username)

# join new client to the chat server
new_client.join_server()