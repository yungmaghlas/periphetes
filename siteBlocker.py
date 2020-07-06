
host_path = "/etc/hosts" #locationtranslates urls to ip addresses
redirect = "127.0.0.1" #local host 
block_list = ["www.youtube.com","youtube.com","www.reddit.com","reddit.com","www.imgur.com","imgur.com"]

while True:

	with open (host_path, "r+") as file:
		text = file.read()
		for site in block_list:
			if site in text:
				pass
			else:
				file.write(redirect + " " + site + "\n")