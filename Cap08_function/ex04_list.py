# %%
def print_message(messages):
    for message in messages:
        print(message)
            
list_messages = [
    'Hello everyone',
    'Good to see you studying Python',
    'Hope you are enjoying our course'
    ]

print_message(list_messages)
# %%
def send_message(messages, sent):
    for message in messages:
        print(message)
        sent.append(message)
            
list_messages = [
    'Hello everyone',
    'Good to see you studying Python',
    'Hope you are enjoying our course'
    ]
sent_message = []

send_message(list_messages, sent_message)
print()
print(sent_message)
print(list_messages)
# %%
