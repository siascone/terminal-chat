from aiohttp import web
import socketio

# initialize server socket
server_socket = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
server_socket.attach(app)

# set clients variable to hold people currently in chat
clients = {}

# handle client joining chat
@server_socket.event
async def join_chat_room(sid, message):
    # grab username from joining client
    username = message.get('username', sid)
    room = message.get('room')
    print(f'{username} joined the chat')
    # todo: add new user to list of clients currently in chat
    clients[sid] = username
    # notify other users in chat of new user joining
    server_socket.enter_room(sid, message['room'])
    user_joined = f'{username} has joined the chat'
    await server_socket.emit('receive_message', {'message': user_joined, 'from': 'TerminalChat', 'username': username, 'clients': clients})

# planned handeling of client leaving chat room
@server_socket.event
async def leave_chat_room(sid, message):
    server_socket.leave_room(sid, message['room'])

# send message to clients in chat
@server_socket.event
async def send_to_clients(sid, message):
    await server_socket.emit('receive_message', {'message': message['message'], 'from': message['username'], 'username': 'TerminalChat', 'clients': False}, room=message['room'])

# handle new sockets connecting to server_socket
@server_socket.event
async def connect(sid, environ):
    await server_socket.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)

# handle when connected sockets leave server_socket
@server_socket.event
async def disconnect(sid):
    # notify other members of chat that client has left
    username = clients[sid]
    left_chat = f'{username} has left the chat.'
    await server_socket.emit('receive_message', {'message': left_chat, 'from': 'TerminalChat', 'username': username, 'clients': clients})
    del clients[sid]
    # log disconnect of client
    print(f'{username} disconnected')

# run program
if __name__ == '__main__':
    web.run_app(app)
