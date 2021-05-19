import requests
import json

def sendFcm(fcmToken, object):
    url = "https://fcm.googleapis.com/fcm/send"
    data = {
        "title": "오브젝트 생성",
        "body": object
    }
    key = "key=AAAAUYSUHG4:APA91bFRwNfPCm04qtJyHhuWTDThEkf_XrivvkC1Js6FNR4FBa6U3Ch0pIXBN2iMJGednNt8PF-6CC-s55so0sZCGigZd-hFccCplKzC4deho1Ish7JlQ2nhrqLfXbTXQ4cgo5L7PJlQ"
    payload = {"to": fcmToken, "priority": "high", "data": data}
    headers = {
        "Content-Type": "application/json",
        "Authorization": key
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print(response.text)