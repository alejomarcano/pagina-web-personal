import requests
payload = {"question":"que es una matriz origen destino"}
response = requests.post(f"https://urbot.azurewebsites.net/qnamaker/knowledgebases/801d369e-aac9-4252-90c5-79ce07207970/generateAnswer", json=payload,
 headers={
   "Authorization": "EndpointKey 1f73b6fa-5bbc-43d6-b973-13b8a0879e4b",
    "Content-Type": "application/json"
 }
)

resdic = response.json()
lista =resdic['answers'][0]
print (lista['questions'][0])
print (lista['answer'])
