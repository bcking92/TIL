from slack import RTMClient
from decouple import config

@RTMClient.run_on(event="message")
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    if 'Hello' in data['text']:
        channel_id = data['channel']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!",
        )
    if '식단' in data['text']:
        channel_id = data['channel']
        web_client.files_upload(channels=channel_id,file ='sikdan.png',title = 'sikdan')

slack_token = config('SLACK_TOKEN')
rtm_client = RTMClient(token=slack_token, connect_method='rtm.start')
rtm_client.start()