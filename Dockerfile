FROM nvidia/cuda:12.2.0-runtime-ubuntu20.04

# Set non-interactive environment variable to prevent prompts
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y bash 

# Install Python 3.9 and pip
RUN apt-get install -y bash python3.9 python3-pip

# Set Python 3.9 as the default Python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

WORKDIR /usr/src/app

# Install dependencies
COPY . ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "semantic_search.main:app", "--host=0.0.0.0", "--port=8000"]