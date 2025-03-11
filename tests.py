import requests

if __name__ == "__main__":
  r = requests.post("http://127.0.0.1:5000/messages/", json={"content":"howtot", "user_id":123})
  r = requests.get("http://127.0.0.1:5000/messages")
  r = requests.get("http://127.0.0.1:5000/messages/1")
  r = requests.put("http://127.0.0.1:5000/messages/1", json={"content":"anothermsg", "user_id":123})
  r = requests.delete("http://127.0.0.1:5000/messages/1")

  r = requests.post("http://127.0.0.1:5000/chat/", json={"content":"howtot", "user_id":123})