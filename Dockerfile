FROM python:3.11

RUN apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y bash 

WORKDIR /usr/src/app

# Install dependencies
COPY . ./
RUN pip install --upgrade pip poetry
RUN poetry config virtualenvs.create false
RUN poetry install --without=dev

EXPOSE 8000

CMD ["uvicorn", "semantic_search.main:app", "--host=0.0.0.0", "--port=8000"]