# flask_send_file
Sample for sending audio file using Flask API

* server.py
```
Flask를 통해 REST API를 구성하였고, 서버에 있는 파일을 client에게 전송하는 예제 입니다.
```

* client.py
```
client는 requests 를 통해 서버로부터 오디오 파일을 streaming으로 수신 받고 이를 파일로 저장하는 예제 입니다.
```

### Installation

```
pip install -r requirements.txt
```


### How to test?

* 1. Run API server
```
python3 server.py
```

* 2. Run client
```
python3 client.py
```

* 3. Check new audio file `copied.wav` is in `./data_to/`

* If you want `curl` instead of `client.py`, then you can use curl command as below
```
curl -X GET http://127.0.0.1:8877/wav --output ./data_to/copied.wav
```
