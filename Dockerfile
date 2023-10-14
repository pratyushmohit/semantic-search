# Build stage
FROM python:3.11-slim

RUN apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y bash && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /usr/src/app

# Install dependencies
COPY . ./
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "semantic_search.main:app", "--host=0.0.0.0", "--port=8000"]