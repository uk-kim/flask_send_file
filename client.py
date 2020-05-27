import shutil
import requests
import json

API_HOST = 'http://127.0.0.1:8877/wav'
dst_file = './data_to/copied.wav'

def main():
    resp = requests.get(API_HOST, stream=True)

    with open(dst_file, 'wb') as f:
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, f)
    print("Donload done")

if __name__ == "__main__":
    main()
