FROM python:3.7

WORKDIR /opt/gitea-mirror
COPY Pipfile Pipfile.lock ./

RUN pip3 install pipenv && \
      pipenv install --deploy

COPY . .

ENTRYPOINT ["pipenv", "run"]
CMD ["migrate"]
