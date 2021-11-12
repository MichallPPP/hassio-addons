ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Copy data for add-on
COPY . /

RUN \
    apk update && \
    apk add python3-dev \
            py3-pip \
            gcc \
            musl-dev \
            libffi-dev \ 
            libressl-dev \
            make \
            cargo && \
    pip install azure-cli && \
    pip install azure-mgmt-dns && \
    pip install azure-identity && \
    chmod a+x /run.sh

CMD [ "/run.sh" ]