if test -f "Config.txt"; then
    source Config.txt

    docker build -t discordbot .     

    docker run -d --name discordbot --env PREFIX=$PREFIX --env TOKEN=$TOKEN --restart unless-stopped redis discordbot
else
    echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
    echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
    echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
    echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
    echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
    echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
    echo TO DOWNLOAD THEM GO TO https://raw.githubusercontent.com/Benegamer/PyBot-Discord/master/Config.txt
fi


