from http import client
from ipaddress import ip_address
from socketio import AsyncClient
from aioconsole import ainput
import asyncio

# make a client class that can accept usernames and join server
class Client:
    def __init__(self, username):
        self.username = username

    def join_server(self):
        # set IP Address and PORT for connecting to server
        IP = '0.0.0.0'
        PORT = '8000'

        # set username and room_name variables
        username = self.username
        # todo test if I can do this without a room name
        room_name = 'main'

        # initialize client_socket and complete IP Address
        client_socket = AsyncClient()
        ip_address = 'http://' + IP + ':' + PORT

        # handle connecting to server
        @client_socket
        async def connect():
            print('Connected to TerminalChat')
            await client_socket.emit('join_chat_room', {'room': room_name, 'username': username})
        
        # handle client receivng messages from server/other chat members
        @client_socket
        async def receive_message(message):
            # first if prevents client from receiving 'client has joined the chat'
            if username != message['username']:
                # grab message sender name
                sender = message['from']
                # handle the name that displays when message is sent
                # if client sends message have message display in client 
                # terminal as 'You' otherwise as 'Sender'
                if username == sender:
                    print('You: ' + message['message'])
                else:
                    print(sender + ': ' + message['message'])

        # handle sending of messages to server/other clients
        async def send_message():
            # repeatedly wait for input from client and send when input is given
            while True:
                await asyncio.sleep(0.01)
                message_being_sent = await(input)
                await client_socket.emit('send_to_clients_in_chat', {'message': message_being_sent, 'username': username, 'room_name': room_name})

        # connect to server via client ip_address
        async def connect_to_server(ip_address):
            await client_socket.connect(ip_address)
            await client_socket.wait()

        # establish connection to server and open sending of messages
        async def main(ip_address):
            await asyncio.gather(
                connect_to_server(ip_address),
                send_message()
            )
        
        # start client chat loop
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(ip_address))