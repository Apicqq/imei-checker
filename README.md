# IMEI Checker

## Overview
This project provides two ways to check the IMEI of a device:
1. **REST API Endpoint** – Allows clients to check an IMEI via a POST request.
2. **Telegram Bot** – Enables users to check an IMEI through a Telegram chat interface.

Both implementations have different authentication mechanisms to control access.

## Features
- Validate device IMEI numbers.
- Authentication mechanisms for both API and Telegram bot.
- Proper error handling and formatted responses.

## Authentication
### API Authentication
- Users must include a valid authentication token in the POST request.
- If the token is missing or invalid, an error response is returned.

### Telegram Bot Authentication
- The bot maintains a whitelist of authorized users.
- If a user is not in the whitelist, they are not allowed to interact with the bot.

## Usage
### API Endpoint
**Endpoint:**
```
POST api/check-imei
```
**Request Body:**
```json
{
  "imei": "123456789012345",
  "token": "your_api_token"
}
```
**Response (Success):**
```json
{
  "id": "YSdND8mNwZUetltM",
  "type": "api",
  "status": "successful",
  "orderId": null,
  "service": {
    "id": 12,
    "title": "Mock service with only successful results"
  },
  "amount": "0.00",
  "deviceId": "351344354167758",
  "processedAt": 1738247095,
  "properties": {
    "deviceName": "MacBook Pro (13-inch, M1, 2020)",
    "image": "https://sources.imeicheck.net/images/8b91be1ca35d97e277d12adece9b8cb1.png",
    "imei": "351344354167758",
    "meid": "35134435416775",
    "imei2": "318927473162150",
    "serial": "SU7FVK553LNQ4",
    "estPurchaseDate": 1430834131,
    "repairCoverage": true,
    "technicalSupport": true,
    "replacement": true,
    "purchaseCountry": "United States",
    "apple/region": "AT&T USA",
    "lostMode": false,
    "usaBlockStatus": "Reported stolen by a T-Mobile customer"
  }
}
```
**Response (Error - Invalid Token):**
```json
{
  "errors": {
    "deviceId": [
      "The device id must be between 8 and 15 characters"
    ]
  }
}
```

### Telegram Bot
- Send an IMEI number as a message.
- If the user is whitelisted, the bot will return the IMEI check result.
- If the user is not whitelisted, they will receive access denied message.

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/imei-checker.git
   cd imei-checker
   ```
2. Install dependencies:
   ```sh
   poetry install
   ```
3. Set up environment variables:
   ```sh
   cp .env.example .env
   ```
   Edit `.env` and configure all environment variables.
4. Run the FastAPI server:
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
5. Start the Telegram bot:
   ```sh
   python bot.py
   ```

