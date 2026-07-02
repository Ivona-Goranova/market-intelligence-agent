import base64
import os

import requests
from dotenv import load_dotenv


class EbayAuthService:
    def get_access_token(self) -> str:
        load_dotenv()

        client_id = os.getenv("EBAY_CLIENT_ID")
        client_secret = os.getenv("EBAY_CLIENT_SECRET")

        if not client_id or not client_secret:
            raise ValueError("EBAY_CLIENT_ID oder EBAY_CLIENT_SECRET fehlt in .env")

        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        url = "https://api.ebay.com/identity/v1/oauth2/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded_credentials}",
        }

        data = {
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope",
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code != 200:
            raise Exception(f"eBay Auth Fehler: {response.status_code} - {response.text}")

        return response.json()["access_token"]