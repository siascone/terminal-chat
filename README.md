# TerminalChat
TerminalChat is a simple group chat program for your terminal(command prompt). 
To run the program:
1. download or clone the repo to your local machine
2. open 2+ terminals(command prompts) 
3. cd into the project's root directory in each open terminal(command prompt)
4. in one terminal run `python3 server.py`
5. in all other terminals run `python3 join_chat.py` and enter a username
 
## Technologies/Libraries utilized in current iteration
- python - codebase language
- python-socketio - Socket.IO clients/servers implemented for python
- asyncio - provides ability to run concurrent code via async/await
- aiohttp - provides an asynchronous HTTP client/server for asyncio and Python
- ainput - 

## Approach

### Initial research/testing
I began this task by walking through the following tutorials on pythonprogramming.net
- [Sockets Tutorial with Python3](https://pythonprogramming.net/sockets-tutorial-python-3/)
- [Socket Chatroom Server](https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/)

From these tutorials I gained a deeper understand of sockets and how they work as 
endpoints in a communication between networked programs. I also got a bit of 
exposure to buffering messages in order to prevent/preempt any data transfer that is 
too large from causing any issues.

### A deeper dive and look into socketio
Following the above mentioned walkthroughs I dove into the docs on [python-socketio](https://python-socketio.readthedocs.io/en/latest/) after which I found another useful tutorial by user Dhanush on dev.to:
- [Build a terminal ChatApp using python](https://dev.to/imdhanush/build-a-terminal-chatapp-using-python-2392) by Dhanush

From this tutorial I was able to expand on the concepts demonstrated and turn the 
client.py file from a static client socket with a predefined into a Client class 
that can accept a username and join a server when prompted by a user.

### Additional research/tutorials
- [socket](https://docs.python.org/3/library/socket.html?highlight=socket#module-socket)
- [threading](https://docs.python.org/3/library/threading.html)
- [python-socketio](https://python-socketio.readthedocs.io/en/latest/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [aioconsole](https://aioconsole.readthedocs.io/en/latest/)
- [aiohttp](https://docs.aiohttp.org/en/stable/)
- [Creating Command-line Based Chat Room using Python](https://hackernoon.com/creating-command-line-based-chat-room-using-python-oxu3u33) by Yashraj Singh Chouhan


## Playground repo for initial testing/walkthroughs
- [python-sockets](https://github.com/siascone/python-sockets)