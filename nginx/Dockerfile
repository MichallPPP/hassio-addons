ARG BUILD_FROM=ghcr.io/hassio-addons/base/amd64:10.0.1
FROM ${BUILD_FROM}

# Setup base
RUN apk add --no-cache nginx>1.20.1

# Copy data
COPY data/run.sh /
COPY data/nginx.conf /etc/

CMD [ "/run.sh" ]
