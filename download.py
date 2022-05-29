import requests

url = input("URL : ")
# url = "https://ipaudio6.com/wp-content/uploads/BOOKAUDIO/Da%20Vinci%20Code/01.mp3"

response = requests.get(url)

n = url[::-1].find("/")
n = len(url) - n - 1
# print(n)
# print(url[len(url) - n - 1])
# print(url[n])
# print(url[n + 1 :])

file = open(url[n + 1 :], "wb")
file.write(response.content)
file.close()