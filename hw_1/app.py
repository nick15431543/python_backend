from factorial import factorial
from fibonacci import fibonacci
from mean import mean
from my_send import send_

async def app(scope, receive, send) -> None:
    if scope["path"] == "/factorial":
        await factorial(scope, receive, send)
    elif len(scope['path']) >= 10 and scope['path'][:10] == '/fibonacci':
        await fibonacci(scope, receive, send)
    elif scope["path"] == "/mean":
        await mean(scope, receive, send)
    else:
        await send_(send, body=b'404 Not Found', header='text/plain', status=404)