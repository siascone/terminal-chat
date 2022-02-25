from http import server
import socketio
from aiohttp import web

# initialize server socket
server_socket = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
server_socket.attach(app)

# handle client joining chat
@server_socket.event
async def join_chat_room(sid, message):
    # grab username from joining client
    username = message.git('name', sid)
    print(username + ' joined the chat')

    # todo: add new user to list of clients currently in chat

    # notify other users in chat of new user joining
    new_user_joined = username + ' has joined the chat!'
    await server_socket.emit('receive_message', {'message': new_user_joined, 'from': 'TerminalChat', 'name': username})

@server_socket.event
async def leave_chat_room(sid, message):
    server_socket.emit(sid, message['room'])

# send message to clients in chat
@server_socket.event
async def sent_to_clients_in_chat(sid, message):
    await server_socket.emit('receive_message', {'message': message['message'], 'from': message['username'], 'username]': ''}, room=message['chat_room'])

# handle new sockets connecting to server_socket
@server_socket.event
async def connect(sid, environ):
    await server_socket.emit('my_response', {'data': 'Connected', 'count':0}, room=sid)

# handle when connected sockets leave server_socket
async def disconnect(sid, message):
    # grab username and make leave message to send to users still in chat
    username = message['username']
    user_left = username + ' has left the chat.'
    await server_socket.emit('receive_message', {'message': user_left, 'from': 'TerminalChat', 'name': username})
    print(message['username'] + ' disconnnected')

@server_socket.event
async def receive_message(message):
    print(message['from'] + ': ' + message['message'])

if __name__ == '__main__':
    web.run_app(app)
