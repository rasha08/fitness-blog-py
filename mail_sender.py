import requests

def sendMessageFromContactPage(data):
    formData = data.to_dict();

    if not data['email'] or not data['message'] or not data['first_name']:
        return None

    data = {
        'email': data['email'],
        'subject': 'Poruka sa sajta',
        'fblink': data['fb'],
        'user': data['first_name'] + ' ' + data['last_name'],
        'message': data['message']

    }
    return sendMessage(data)
        

def sendMessage(data):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox0910a7251b2247bc8a91ca0f0686a2d5.mailgun.org/messages",
        auth=("api", "key-74d69a614db62f11c9459f6627c9fe43"),
        data = {
            "from": data['email'],
            "to": "rasha08@gmail.com",
            "subject": data['subject'],
            "text": data['message'],
            "html": '<!DOCTYPE html> <html> <head> <meta charset="UTF-8"> <title>'+ data['subject'] +'</title> </head> <body> <h2> '+ data['subject'] +' </h2> <table style="width:450px;text-align:center !important"> <tr> <th style="width:150px;">Korisnik</th> <th style="width:150px;">Korisnikov email</th> <th style="width:150px;">facebook / telefon</th> </tr><tr> <td style="width:150px;">'+ data['user'] +'</td><td style="width:150px;">'+ data['email'] +'</td><td style="width:150px;">'+ data['fblink'] +'</td></tr></table><br><br> <h3><small><b>PORUKA:</b></small> '+ data['message'] +'</h3></body> </html>s'
        }
    )

