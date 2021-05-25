FROM ubuntu:latest

    RUN apt-get update && apt-get -y upgrade

    # Install iozone and iperf
    RUN apt-get install -y iozone3 iperf3

    # Copy benchmark files to container
    VOLUME /docker_benchmark 
    COPY ./benchmarks /docker_benchmark

    # Set docker_benchmark as starting directory
    WORKDIR /docker_benchmark

    # Install geekbench dependencies
    RUN dpkg --add-architecture i386 \
    && apt-get install --no-install-recommends -y wget libc6:i386 libstdc++6:i386 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

    # Set geekbench version
    ENV GEEKBENCHVERSION Geekbench-5.4.1-Linux
    ENV GEEKBENCHPACKAGE $GEEKBENCHVERSION.tar.gz

    # Download and install geekbench
    RUN wget --quiet --no-check-certificate https://cdn.geekbench.com/$GEEKBENCHPACKAGE -O /tmp/$GEEKBENCHPACKAGE \
        && mkdir -p /opt/geekbench \
        && tar xzf /tmp/$GEEKBENCHPACKAGE -C /opt/geekbench \
        && rm -rf /tmp/$GEEKBENCHPACKAGE

    # Run all tests
    #ENTRYPOINT ["bash", "./run.sh"]
