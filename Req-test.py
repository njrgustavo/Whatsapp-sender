import requests

url = "http://localhost:8081/message/sendText/Test1"

payload = {
    "number": "5513997537748",
    "text": "sdadasdas",
    "delay": 123,
    "linkPreview": True,
    "mentionsEveryOne": True,
    "mentioned": ["5513997537748"], 
    "quoted": {
        "key": {"id": "BC2285612233-4F70-9F01-13BA796ACEB9"},
        "message": {"conversation": "alo"}
    }
}
headers = {
    "apikey": "429683C4C977415CAAFAAGG0F7D57E11",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)