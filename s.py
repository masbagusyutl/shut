import requests
import time
import json

def read_api_keys(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def login(api_key_payload):
    url = "https://clicker.game-bomb.ru/authorize"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
        "Cache-Control": "no-cache",
        "Content-Length": "358",
        "Content-Type": "application/x-www-form-urlencoded",
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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }
    
    response = requests.post(url, headers=headers, data=api_key_payload)
    response.encoding = 'utf-8' if response.encoding is None else response.encoding
    return response.status_code, response.json()

def claim_reward(access_token):
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
        "X-Api-Key": access_token
    }
    
    response = requests.post(url, headers=headers, data="{}")
    response.encoding = 'utf-8' if response.encoding is None else response.encoding
    return response.status_code, response.json()

def get_channel_tasks(access_token):
    url = "https://clicker.game-bomb.ru/channels"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
        "Cache-Control": "no-cache",
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
        "X-Api-Key": access_token
    }
    
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8' if response.encoding is None else response.encoding
    return response.status_code, response.json()

def get_sponsor_tasks(access_token):
    url = "https://clicker.game-bomb.ru/sponsors"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
        "Cache-Control": "no-cache",
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
        "X-Api-Key": access_token
    }
    
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8' if response.encoding is None else response.encoding
    return response.status_code, response.json()

def claim_task_reward(access_token, task_type, task_id):
    url = f"https://clicker.game-bomb.ru/{task_type}/{task_id}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
        "Cache-Control": "no-cache",
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
        "X-Api-Key": access_token
    }
    
    response = requests.post(url, headers=headers)
    response.encoding = 'utf-8' if response.encoding is None else response.encoding
    return response.status_code, response.json()

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\rCountdown: {timer}", end="")
        time.sleep(1)
        seconds -= 1
    print("\nCountdown finished. Restarting tasks...\n")

def print_account_details(details):
    print("\nAccount Details:")
    print(f"Name: {details.get('first_name')}")
    print(f"Balance: {details.get('balance')}")
    print(f"Balance USD: {details.get('balance_usd')}")
    print(f"Available to Mine: {details.get('available_to_mine')}")
    print(f"Last Mine At: {details.get('last_mine_at')}\n")

def print_task_info(title, tasks):
    print(f"{title}:")
    for task in tasks:
        print(f"ID: {task.get('id')}")
        print(f"Title: {task.get('title')}")
        print(f"Reward: {task.get('reward')}")
        print(f"Reward SHTB: {task.get('reward_shtb')}")
        print(f"Is Available: {task.get('is_available')}\n")

def print_reward_details(task_type, reward_response):
    print(f"{task_type.capitalize()} Task Reward:")
    print(f"New Balance: {reward_response.get('new_balance')}")
    print(f"New Balance SHTB: {reward_response.get('new_balance_shtb')}\n")

def print_claim_reward_details(reward_response):
    print("Claim Reward Details:")
    print(f"Balance: {reward_response.get('balance')}")
    print(f"Last Mine At: {reward_response.get('last_mine_at')}\n")

def main():
    api_keys = read_api_keys('data.txt')
    num_accounts = len(api_keys)

    print(f"Starting processing {num_accounts} accounts...\n")

    while True:
        for index, api_key_payload in enumerate(api_keys):
            print(f"Processing account {index + 1}/{num_accounts}")
            status_code, login_response = login(api_key_payload)
            if status_code == 200:
                access_token = login_response.get("access_token")
                print_account_details(login_response)

                status_code, channel_tasks = get_channel_tasks(access_token)
                if status_code == 200:
                    print_task_info("Channel Tasks", channel_tasks)

                status_code, sponsor_tasks = get_sponsor_tasks(access_token)
                if status_code == 200:
                    print_task_info("Sponsor Tasks", sponsor_tasks)

                for task in channel_tasks:
                    if task.get("is_available"):
                        task_id = task.get("id")
                        status_code, reward_response = claim_task_reward(access_token, "channels", task_id)
                        if status_code == 200:
                            print_reward_details("Channel", reward_response)

                for task in sponsor_tasks:
                    if task.get("is_available"):
                        task_id = task.get("id")
                        status_code, reward_response = claim_task_reward(access_token, "sponsors", task_id)
                        if status_code == 200:
                            print_reward_details("Sponsor", reward_response)

                status_code, reward_response = claim_reward(access_token)
                if status_code == 200:
                    print_claim_reward_details(reward_response)

            if index < num_accounts - 1:
                print("Waiting for 5 seconds before switching to the next account...\n")
                time.sleep(5)

        print(f"All {num_accounts} accounts have been processed. Starting countdown for 3000 seconds...\n")
        countdown_timer(3000)

if __name__ == "__main__":
    main()
