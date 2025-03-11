import requests

if __name__ == "__main__":
  endpoint = "http://172.23.63.100:5000"
  r = requests.post(f"{endpoint}/messages/", json={"content":"howtot", "user_id":123})
  print(r.text);
  r = requests.get(f"{endpoint}/messages")
  print(r.text);
  r = requests.put(f"{endpoint}/messages/1", json={"content":"anothermsg", "user_id":123})
  print(r.text);
  r = requests.delete(f"{endpoint}/messages/1")
  print(r.text);
  r = requests.post(f"{endpoint}/chat/", json={"content":"howtot", "user_id":123})
  print('done');