#Python version
FROM python:3.9                

#command der beim bauen gestartet wird
#install discord extensions
RUN pip install asyncio datetime discord youtube_dl PyNaCl     

RUN apt-get update ; apt-get install -y git build-essential gcc make yasm autoconf automake cmake libtool  libmp3lame-dev pkg-config libunwind-dev zlib1g-dev libssl-dev libopus0 opus-tools
#credit to SoftwareStep

RUN apt-get update \
    && apt-get clean \
    && apt-get install -y --no-install-recommends libc6-dev libgdiplus wget software-properties-common

#RUN RUN apt-add-repository ppa:git-core/ppa && apt-get update && apt-get install -y git

RUN wget https://www.ffmpeg.org/releases/ffmpeg-4.0.2.tar.gz
RUN tar -xzf ffmpeg-4.0.2.tar.gz; rm -r ffmpeg-4.0.2.tar.gz
RUN cd ./ffmpeg-4.0.2; ./configure --enable-gpl --enable-libmp3lame --enable-decoder=mjpeg,png --enable-encoder=png --enable-openssl --enable-nonfree

RUN cd ./ffmpeg-4.0.2; make
RUN  cd ./ffmpeg-4.0.2; make install
#####

RUN echo "git clone https://raw.githubusercontent.com/Benegamer/PyBot-Discord/master/main2.0.py"
ADD config.json . 

#Startup command
CMD [ "python", "./main.py" ]
