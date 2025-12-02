FROM ubuntu:14.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openssl=1.0.1f-1ubuntu2 \
        wget \
        curl && \
    rm -rf /var/lib/apt/lists/*

CMD ["bash"]
