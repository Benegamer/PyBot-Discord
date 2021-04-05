if test -f "config.json"; then
    docker build -t discordbot .     

    docker run -d --name discordbot --restart unless-stopped redis discordbot
else
    echo YOU DONT HAVE THE CONFIG.JSON FILE IN THE CURRENT DIRECTORY!
    echo YOU DONT HAVE THE CONFIG.JSON FILE IN THE CURRENT DIRECTORY!
    echo YOU DONT HAVE THE CONFIG.JSON FILE IN THE CURRENT DIRECTORY!
    echo YOU DONT HAVE THE CONFIG.JSON FILE IN THE CURRENT DIRECTORY!
    echo YOU DONT HAVE THE CONFIG.JSON FILE IN THE CURRENT DIRECTORY!
    echo YOU DONT HAVE THE CONFIG.JSON FILE IN THE CURRENT DIRECTORY!
    echo TO DOWNLOAD THEM GO TO https://raw.githubusercontent.com/Benegamer/PyBot-Discord/master/config.json
fi


