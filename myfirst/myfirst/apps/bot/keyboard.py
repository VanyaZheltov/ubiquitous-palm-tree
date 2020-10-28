import json

cancelkeyboard = {
  "one_time": True,
  "buttons": [
    [{
      "action": {
        "type": "text",
        "label": "Отмена"
      },
      "color": "negative"
    }]
  ]
}
cancelkeyboard = json.dumps(cancelkeyboard, ensure_ascii=False).encode('utf-8')
cancelkeyboard = str(cancelkeyboard.decode('utf-8'))