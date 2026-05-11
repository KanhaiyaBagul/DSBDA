import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}
req = requests.get('https://www.flipkart.com/apple-iphone-15-black-128-gb/product-reviews/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&page=1', headers=headers)
with open('flipkart_output.html', 'w', encoding='utf-8') as f:
    f.write(req.text)
print("Status Code:", req.status_code)
