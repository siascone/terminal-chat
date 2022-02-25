from aiohttp import web
import socketio

# initialize server socket
server_socket = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
server_socket.attach(app)

# handle client joining chat
@server_socket.event
async def join_chat_room(sid, message):
    # grab username from joining client
    username = message.get('username', sid)
    print(f'{username} joined the chat')
    # todo: add new user to list of clients currently in chat
    
    # notify other users in chat of new user joining
    server_socket.enter_room(sid, message['room'])
    user_joined = f'{username} has joined the chat'
    await server_socket.emit('receive_message', {'message': user_joined, 'from': 'TerminalChat', 'username': username})

# planned handeling of client leaving chat room
@server_socket.event
async def leave_chat_room(sid, message):
    server_socket.leave_room(sid, message['room'])

# send message to clients in chat
@server_socket.event
async def send_to_clients(sid, message):
    await server_socket.emit('receive_message', {'message': message['message'], 'from': message['username'], 'username': 'TerminalChat'}, room=message['room'])

# handle new sockets connecting to server_socket
@server_socket.event
async def connect(sid, environ):
    await server_socket.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)

# handle when connected sockets leave server_socket
@server_socket.event
def disconnect(sid):
    # future improvement, bettern identify disconnected client:
    # can use sid but would like username
    # print(f'Client id: {sid} disconnected')
    print('Client disconnected')

# run program
if __name__ == '__main__':
    web.run_app(app)
