#Python version
FROM python:3.9

#Datein hinzufügen
ADD config.json .
ADD main.py .

#command der beim bauen gestartet wird
RUN pip install asyncio datetime discord youtube_dl

#Startup command
CMD [ "python", "./main.py" ]
