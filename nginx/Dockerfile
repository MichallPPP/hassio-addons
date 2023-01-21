ARG BUILD_FROM
FROM ${BUILD_FROM}

# Setup base
RUN apk add --no-cache nginx>1.23.3

# Copy data
COPY data/run.sh /
COPY data/nginx.conf /etc/

CMD [ "/run.sh" ]
