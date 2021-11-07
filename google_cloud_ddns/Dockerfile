ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Copy data for add-on
COPY . /

# Install requirements for add-on
RUN apk add --no-cache python3>3.8.10
RUN apk add py3-pip>20.3.4-r1
RUN pip3 install gcloud>=0.18.3
RUN pip3 install requests>=2.26.0

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]