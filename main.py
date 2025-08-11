import requests

username = input("Enter Github Username:")

#calling Github api
Url = f"https://api.github.com/users/{username}/events"


#Sending get requests to GitHub Api
response = requests.get(Url)


#checking response status and handling errors
if response.status_code == 200:
    events = response.json()

    for event in events[:10]:
        print(f"- {event['type']} at {event['created_at']}")
    else:
        print(f"error: {response.status_code} could cot fetch data")