import requests
import json

def report_victim_account(victim_username, access_token, reason):
    # Set the request headers.
    headers = {
        "Authorization": "Bearer {}".format(access_token),
        "Content-Type": "application/json",
    }

    # Set the request body.
    body = {
        "reason": reason,
    }

    # Make the request to Instagram Graph API.
    response = requests.post(
        f"https://graph.instagram.com/v12.0/{victim_username}/reports",
        headers=headers,
        data=json.dumps(body),
    )

    # Check the response status code.
    if response.status_code == 200:
        print("The victim account has been reported.")
    else:
        print("An error occurred while reporting the victim account.")

if __name__ == "__main__":
    victim_username = input("Enter the username of the victim account: ")
    access_token = input("Enter your Instagram access token: ")
    reason = input("Enter the reason for reporting the victim account: ")
    report_victim_account(victim_username, access_token, reason)
