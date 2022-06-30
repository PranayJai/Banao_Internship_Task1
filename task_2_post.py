import requests

url = "https://www.flickr.com/services/rest/?method=flickr.blogs.postPhoto&format=json&nojsoncallback=1&oauth_consumer_key=40746a6e5f1a219afba59e859460b29f&oauth_token=72157720841081236-3a2b45167e5bb819&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1650963855&oauth_nonce=pugA4KLv6qr&oauth_version=1.0&oauth_signature=5CjEqgvpDuk3%2FaU5X70G1rN5jdY%3D"

payload={}
headers = {
  'Cookie': 'ccc=%7B%22needsConsent%22%3Afalse%2C%22managed%22%3A0%2C%22changed%22%3A0%2C%22info%22%3A%7B%22cookieBlock%22%3A%7B%22level%22%3A0%2C%22blockRan\
    %22%3A0%7D%7D%7D; flrbgdrp=1650957728-8bcc361428bf90d691f2035618c65306d01fbbbe; flrbgmrp=1650957728-f76f23244b398fd9b613017c63a8708c12ea93c0; \
    flrbgrp=1650957728-c89eb58bd2f767c5a4a771db32004fbd67b8b42e; flrbp=1650957728-1a9f54fc132efa65f082d5ed570c0dbf33cb7d07;\
    flrbrp=1650957728-291c9cd7bbba51fc1185ddc257daade108e21b0f; \
    flrbrst=1650957728-b10ab1ff5728d8cdd1c2c56985bffe78ecdb4e44; flrtags=1650957728-cecbd31883d4235109d5f40060eaab118ff24150; localization=en-us%3Bus%3Bus; xb=840952'
}

response = requests.request("GET", url, headers=headers, data=payload)

resp = response.json()
print(resp)

if resp["message"] == "Invalid auth token":
    print("Authentication fail")
else:
    print("Authentication Pass")