import slack
from decouple import config
from pprint import pprint


slack_token = config('SLACK_TOKEN')
client = slack.WebClient(token=slack_token)

# client.chat_postMessage(
#     channel = '#random',
#     text="hi 8tons baby"
# )

print(client.channels_info(channel= 'CL2THS73L'))
client.files_upload(channels='CL2THS73L',file ='sikdan.png',title = 'sikdan')