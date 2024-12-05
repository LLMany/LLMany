# Requests

## New chat request
Request:
```
{
"type": "new_chat",
"model_type": the type/provider of the model,
"model": the name of the model
}
```
Returned value:
```
{
"type": "new_chat",
"model_type": the type/provider of the model,
"model": the name of the model
"chat_id": id of the chat
}
```
## Delete request
Request:
```
{
"type": "delete_chat",
"chat_id": id of the chat,
}
```
Returned value:
```
{
"type": "delete_chat",
"chat_id": id of the chat,
"status": Bool
}
```
## All chats request
Request:
```
{
"type": "all_chats",
}
```
Returned value:
```
{
"type": "all_chats",
"chats": [
    {
    "model_type": the type/provider of the model,
    "model": the name of the model
    "chat_id": id of the chat
    }
]
}
```
## Chat history request
Request:
```
{
"type": "chat_history",
"chat_id": the id of the chat
}
```
Returned value:
```
{
"type": "chat_history",
"chat_id": the id of the chat
"messages":
    [
        {
        "role": "user"/"model"
        "contents": the contents of the message
        }
    ]
}
```
## Message request
Request:
```
{
"type": "message",
"chat_id": the id of the chat",
"contents": the content of the message
}
```
Returned value:
```
{
"type": "message",
"chat_id": id of the chat
"content": the content of the message
}

```
