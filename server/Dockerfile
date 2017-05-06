FROM python:2.7.11-onbuild

EXPOSE 5000

ADD ./ /opt/server
ADD config/boot.sh /

CMD ["/bin/bash","/boot.sh"]

WORKDIR "/opt/server"

CMD [ "gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "api:app" ]
