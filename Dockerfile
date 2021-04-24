#Python version
FROM python:3.9

#Install discord extensions
RUN pip install asyncio datetime pytz discord youtube_dl PyNaCl

#Credit to SoftwareStep
#####
RUN apt-get update ; apt-get install -y git build-essential gcc make yasm autoconf automake cmake libtool  libmp3lame-dev pkg-config libunwind-dev zlib1g-dev libssl-dev libopus0 opus-tools

RUN apt-get update \
    && apt-get clean \
    && apt-get install -y --no-install-recommends libc6-dev libgdiplus wget software-properties-common

RUN wget https://www.ffmpeg.org/releases/ffmpeg-4.0.2.tar.gz
RUN tar -xzf ffmpeg-4.0.2.tar.gz; rm -r ffmpeg-4.0.2.tar.gz
RUN cd ./ffmpeg-4.0.2; ./configure --enable-gpl --enable-libmp3lame --enable-decoder=mjpeg,png --enable-encoder=png --enable-openssl --enable-nonfree

#                            v: Thanks SoftwareStep
RUN cd ./ffmpeg-4.0.2; make -j 4
RUN  cd ./ffmpeg-4.0.2; make install

#####

RUN wget https://raw.githubusercontent.com/Benegamer/PyBot-Discord/master/main2.0.py

####

#Startup command
CMD [ "python", "./main2.0.py" ]