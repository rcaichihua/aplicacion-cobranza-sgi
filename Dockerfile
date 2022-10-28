FROM alpine:3.16

RUN apk add --no-cache python3 \
  && pip3 install --upgrade pip && pip install -r requirements.txt