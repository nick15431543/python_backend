import json

from my_send import send_

async def mean(scope, receive, send):
    query = await receive()

    try:
        data = json.loads(query['body'].decode('utf-8'))
    except:
        await send_(send, body=b'422 Unprocessable Entity', header='text/plain', status=422)
        return
    
    if type(data) != list:
        await send_(send, body=b'400 Bad Request', header='text/plain', status=400)
        return
    
    data_new = []
    for i in data:
        try:
            k = float(i)
            data_new.append(k)
        except:
            await send_(send, body=b'400 Bad Request', header='text/plain', status=400)
            return
    
    if len(data_new) == 0:
        await send_(send, body=b'400 Bad Request', header='text/plain', status=400)
        return
    
    await send_(send, body=json.dumps({'result': sum(data_new) / len(data_new)}).encode('utf-8'), header=b'application/json', status=200)