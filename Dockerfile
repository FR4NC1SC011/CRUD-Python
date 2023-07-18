FROM alpine

RUN apk update

# RUN apk add --no-cache python3-dev && pip install --upgrade pip
RUN apk add --update python3 py3-pip

WORKDIR /application

COPY . /application

RUN pip install -r requirements.txt

EXPOSE 5001

ENTRYPOINT [ "python3" ]

CMD ["app.py"]