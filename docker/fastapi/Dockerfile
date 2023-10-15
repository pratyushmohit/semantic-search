# BUILD STAGE
FROM python:3.11-slim AS build

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y bash && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /usr/src/app

# Create a virtual environment in the /venv directory
RUN python -m venv /venv

# Activate the virtual environment and install build dependencies
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt


# FINAL STAGE
FROM python:3.11-slim

WORKDIR /usr/src/app

# Copy the virtual environment from the build stage
COPY --from=build /venv /venv

# Set the PATH to include the virtual environment
ENV PATH="/venv/bin:$PATH"

# Copy only the necessary artifacts from the build stage
COPY . ./

EXPOSE 8000

CMD ["python", "-m", "semantic_search"]