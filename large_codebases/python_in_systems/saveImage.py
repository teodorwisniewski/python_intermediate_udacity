import requests
import random
import os

image_url = 'https://images.ctfassets.net/2y9b3o528xhq/4swf2qhcelEUWzKHaKne6C/d890de3220ea332fb42e9b8e5f7848fd/real-world-projects.png'
r = requests.get(image_url, allow_redirects=True)
if not os.path.exists('./tmp'):
    os.mkdir('./tmp')

tmp = f'./tmp/{random.randint(0, 100000000)}.png'
open(tmp, 'wb').write(r.content)

print(tmp)