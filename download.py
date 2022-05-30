import requests
from sys import argv

# options = ["-o"]
# validating command-line input
if not (len(argv) == 2 or len(argv) == 4):
  print("The command line input is not correct.")
  exit()

# processing the comman-line input
url = argv[1]
n = url[::-1].find("/")
n = len(url) - n - 1
if len(argv) == 4 and argv[2] == "-o":
  output = argv[3]
else:
  output = url[n + 1 :]

# url = "https://ipaudio6.com/wp-content/uploads/BOOKAUDIO/Da%20Vinci%20Code/01.mp3"

response = requests.get(url)

# print(n)
# print(url[len(url) - n - 1])
# print(url[n])
# print(url[n + 1 :])

file = open(output, "wb")
file.write(response.content)
file.close()