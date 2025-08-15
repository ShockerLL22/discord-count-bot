import httpx
import asyncio

data = {
    "order": "service",
    "service": "229",
    "link": "https://www.tiktok.com/@tahel4555/photo/7538163022238321928",
    "uuid": "b52700b7-48d2-4b60-b22b-1816a1b3b656",
    "videoId": "7538163022238321928"
}

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://zefame.com",
    "referer": "https://zefame.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

async def send_requests():
    async with httpx.AsyncClient() as client:
        while True:
            response = await client.post(
                "https://zefame-free.com/api_free.php?action=order",
                data=data,
                headers=headers
            )
            print(response.status_code, response.text)
            await asyncio.sleep(0.5)

asyncio.run(send_requests())
