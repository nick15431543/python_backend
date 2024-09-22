import math
import json

from my_send import send_

async def factorial(scope, receive, send):
    query = scope['query_string'].decode('utf-8')

    try:
        n = int(query.split('=')[1])
    except:
        await send_(send, body=b'422 Unprocessable Entity', header='text/plain', status=422)
        return

    try:
        n = math.factorial(n)
    except:
        await send_(send, body=b'400 Bad Request', header='text/plain', status=400)
        return
    
    await send_(send, body=json.dumps({'result': n}).encode('utf-8'), header=b'application/json', status=200)