import requests
import argparse

def print_messages(username, events):
    """Prints the events for the given username."""
    print(f"Events for {username}:")
    for event in events:
        print(f"{event['created_at']}: {username} {event['type']} {event['repo']['name']}")

def fetch_user_events(username):
    """Fetches the GitHub events for the given username."""
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching events: {response.status_code}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(prog="github-activity")
    parser.add_argument("username", type=str, help="Username of the user you want to check")
    
    # Parse the arguments
    args = parser.parse_args()
    
    try:
        events = fetch_user_events(args.username)
        print_messages(args.username, events)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()