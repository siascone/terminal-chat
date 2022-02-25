from socketio import AsyncClient
from aioconsole import ainput
import asyncio
import sys

# make a client class that can accept usernames and join server
class Client:
    def __init__(self, username):
        self.username = username

    def join_server(self):
        # set IP Address and PORT for connecting to server
        IP = '0.0.0.0'
        PORT = '8080'

        # set username and room variables
        username = self.username
        room = 'main'

        # initialize client_socket and complete IP Address
        client_socket = AsyncClient()
        full_ip = 'http://'+IP+':'+PORT

        # handle connecting to server
        @client_socket.event
        async def connect():
            print('Connected to TerminalChat')
            await client_socket.emit('join_chat_room', {'room': room, 'username': username})

        # handle close of server
        @client_socket.event
        def disconnect():
            # future improvement, exicute system exit without error message
            print('Goodbye! Press Ctrl+c to exit.')

        # handle client receivng messages from server/other chat members
        @client_socket.event
        async def receive_message(message):
            # prevent client from receiving 'client has joined the chat'
            if username != message['username']:
                # grab message sender username
                sender = message['from']
                # handle the name that displays when message is sent if client 
                # sends message have message display in client terminal as 'You'
                # otherwise as 'Sender'
                if username == sender:
                    print(f"You: {message['message']}")
                else:
                    print(f"{sender}: {message['message']}")

        # handle sending of messages to server/other clients
        async def send_message():
            # repeatedly wait for input from client and send when input is given
            while True:
                await asyncio.sleep(0.01)
                message_being_sent = await ainput()
                await client_socket.emit('send_to_clients', {'message': message_being_sent, 'username': username, 'room': room})

        # connect to server via client full_ip address
        async def connect_to_server(ip):
            await client_socket.connect(ip)
            await client_socket.wait()

        # establish connection to server and open sending of messages
        async def main(ip):
            await asyncio.gather(
                connect_to_server(ip),
                send_message()
            )

        # start client chat loop
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main(full_ip))
        # if clinet kills terminal print goodbye message instead of error
        except:
            # future improvment, boradcast to other in chat that clinet has left
            # future improvement, exicute system exit without error message
            print('Goodbye! Press Ctrl+c to exit.')
