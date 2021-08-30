import requests #dependency
print("Enter your webhook url: ")
url = input() #webhook url, from here: https://i.imgur.com/f9XnAew.png
print("\nEnter your message content (not embeded): ")
ct = input()
print("\nEnter the name of the bot: ")
usr = input()
print("\nEnter the .png avatar URL if you want: ")
ava = input()
#for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data = {
    "content" : ct,
    "avatar_url" : ava,
    "username" : usr
}

#leave this out if you dont want an embed
#for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
print("\nEnter the description (embeded): ")
disem = input() #webhook url, from here: https://i.imgur.com/f9XnAew.png
print("\nEnter your title (embeded): ")
titem = input()
data["embeds"] = [
    {
        "description" : disem,
        "title" : titem
    }
]

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))
