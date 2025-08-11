import argparse
import requests


#setting up argurment parser
parser = argparse.ArgumentParser(description="Fetch recent activity for user")
parser.add_argument("username", help="Github username to fetch activity for")
parser.add_argument("-n", "--number", type=int, default=5, help="Number of events to display")

#parse the argurment
args = parser.parse_args()

#calling Github api
Url = f"https://api.github.com/users/{username}/events"


#Sending get requests to GitHub Api
response = requests.get(Url)


#checking response status and handling errors
if response.status_code == 200:
    events = response.json()
    if not events:
        print(f"No recent activity found for user '{args.username}'.")
    else:
        for event in events[:args.number]:
             print(f"- {event['type']} at {event['created_at']}")
else:
        print(f"error: {response.status_code} could cot fetch data")