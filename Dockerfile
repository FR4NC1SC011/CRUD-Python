FROM alpine

RUN apk update

# RUN apk add --no-cache python3-dev && pip install --upgrade pip
RUN apk add --update python3 py3-pip

# # Defining working directory
WORKDIR /application

# # Copy everything which is present in my docker directory to working (/app)
# COPY /requirements.txt /application
COPY . /application

RUN pip install -r requirements.txt

# COPY ["app.py, /app", "/application"]
# COPY . .

# Exposing an internal port
EXPOSE 5001


# Step 4 set default commands
# These are permanent commands i.e even if user will provide come commands those will be considered as argunemts of this command
ENTRYPOINT [ "python3" ]

# These commands will be replaced if user provides any command by himself
CMD ["app.py"]