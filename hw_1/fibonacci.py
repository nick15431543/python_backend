import json

from my_send import send_

async def fibonacci(scope, receive, send):
    query = scope['path'][11:]

    try:
        n = int(query)
    except:
        await send_(send, body=b'422 Unprocessable Entity', header='text/plain', status=422)
        return
    
    if n < 0:
        await send_(send, body=b'400 Bad Request', header='text/plain', status=400)
        return
    A = [0 for i in range(n + 1)]
    res = 0
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        A[1] = 1
        for i in range(2, n + 1):
            A[i] = A[i - 1] + A[i - 2]
        res = A[n]
    
    await send_(send, body=json.dumps({'result': res}).encode('utf-8'), header=b'application/json', status=200)