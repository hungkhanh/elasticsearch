f = open("account.json", "r")
d = open("data.json", "w")
buffer = f.read()

for x in range(1024):
  d.write(buffer)

f.close()
d.close()