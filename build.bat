if exist Config.txt (
for /f "delims== tokens=1,2" %%G in (Config.txt) do set %%G=%%H
cls
docker build -t discordbot .

docker run -d --name discordbot --env PREFIX=%Discord_prefix% --env TOKEN=%Discord_token% discordbot
pause
) else (

cls
echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
echo YOU DONT HAVE THE CONFIG.TXT FILE IN THE CURRENT DIRECTORY!
echo TO DOWNLOAD THEM GO TO https://raw.githubusercontent.com/Benegamer/PyBot-Discord/master/Config.txt
pause

)
