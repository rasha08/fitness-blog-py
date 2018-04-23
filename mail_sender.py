import requests

def sendMessageFromContactPage(data):
    print(data.to_dict())
    formData = data.to_dict();

def sendMessage(data):
    requests.post(
        "https://api.mailgun.net/v3/sandbox0910a7251b2247bc8a91ca0f0686a2d5.mailgun.org/messages",
        auth=("api", "key-74d69a614db62f11c9459f6627c9fe43"),
        data = {
            "from": data.email,
            "to": "rasha08@gmail.com",
            "subject": data.subject,
            "text": data.message
        }
    )