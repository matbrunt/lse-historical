FROM honir/prophet:latest

ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install --upgrade beautifulsoup4 requests

RUN mkdir -p /usr/src

ENV PYTHONPATH /usr/src:$PYTHONPATH

EXPOSE 8888

WORKDIR /usr/src
