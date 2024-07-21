import requests
import time
import datetime

def read_api_keys(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def claim_reward(api_key):
    url = "https://clicker.game-bomb.ru/claim"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
        "Cache-Control": "no-cache",
        "Content-Length": "2",
        "Content-Type": "application/json",
        "Origin": "https://app.game-bomb.ru",
        "Pragma": "no-cache",
        "Priority": "u=1, i",
        "Referer": "https://app.game-bomb.ru/",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\", \"Microsoft Edge WebView2\";v=\"126\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
        "X-Api-Key": api_key
    }
    
    response = requests.post(url, headers=headers, data="{}")
    return response.status_code, response.text

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\rCountdown: {timer}", end="")
        time.sleep(1)
        seconds -= 1
    print("\nCountdown finished. Restarting tasks...\n")

def main():
    api_keys = read_api_keys('data.txt')
    num_accounts = len(api_keys)
    print(f"Total number of accounts: {num_accounts}")

    while True:
        for index, api_key in enumerate(api_keys):
            print(f"Processing account {index + 1}/{num_accounts}")
            status_code, response_text = claim_reward(api_key)
            print(f"Status Code: {status_code}, Response: {response_text}")
            if index < num_accounts - 1:
                print("Waiting for 5 seconds before switching to the next account...\n")
                time.sleep(5)
        
        print(f"All {num_accounts} accounts have been processed. Starting countdown for 3000 seconds...\n")
        countdown_timer(3000)

if __name__ == "__main__":
    main()
