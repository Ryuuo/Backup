import httplib2, os
from apiclient import discovery
import gmail_auth

def gmail_get_service():
    credentials = gmail_auth.gmail_user_auth()
    http = credentials.authorize(httplib2.Http())

    service = discovery.build('gmail', 'v1', http=http)
    return service

def gmail_get_messages():
    service = gmail_get_service()
    messages = service.users().messages()
    msg_list = messages.list(userId='me', maxResults=1).execute()

    for msg in msg_list['messages']:
        topid = msg['id']
        msg = messages.get(userId='me', id=topid).execute()
        #print("--------------------")
        #print(msg['snippet'])
        return msg['snippet']

gmail_get_messages()
