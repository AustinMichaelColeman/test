import requests

def get_payment_details(payment_id, access_token):
    url = f"https://api.paypal.com/v1/payments/payment/{payment_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Replace with your actual access token and payment id
access_token = "your_access_token"
payment_id = "your_payment_id"

payment_details = get_payment_details(payment_id, access_token)
if payment_details is not None:
    print(payment_details)
else:
    print("Failed to get payment details.")