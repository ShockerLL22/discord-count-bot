import requests
import time

url = "https://zefame-free.com/api_free.php?action=order"
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://zefame.com",
    "referer": "https://zefame.com/",
    "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
data = {
    "action": "order",
    "service": "232",
    "link": "https://www.tiktok.com/@hadar.houta/photo/7536679096932142343",
    "uuid": "482fa303-0b70-452c-8b51-d7c52ede5872",
    "videoId": "7536679096932142343"
}

while True:
    r = requests.post(url, headers=headers, data=data)
    print(r.text)
    time.sleep(5)


