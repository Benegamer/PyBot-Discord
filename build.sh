docker build -t discordbot .     

docker run -d --name discordbot --restart unless-stopped redis discordbot