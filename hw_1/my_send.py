async def send_(send, body, header, status):
    await send({
    "type": "http.response.start",
    "status": status,
    "headers": [
      [b"content-type", header],
    ]
    })
    await send({
        "type": "http.response.body",
        "body": body,
    })