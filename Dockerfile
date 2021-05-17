FROM ubuntu:latest

    RUN apt-get -y update 
    RUN apt-get -y upgrade
    # install iozone and iperf
    RUN apt-get install -y iozone3 iperf3  
    # install dependencies
    RUN apt-get install -y libc6-i386 libstdc++6 wget build-essential gcc cpp make zip

    # copy benchmark files to container
    VOLUME /docker_benchmark 
    COPY ./benchmarks /docker_benchmark

    # set docker_benchmark as starting directory
    WORKDIR /docker_benchmark


    # setup and install geekbench
    RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install --no-install-recommends -y wget \
                                                  libc6:i386 \
                                                  libstdc++6:i386 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

    ENV GEEKBENCHVERSION Geekbench-5.4.1-Linux
    ENV GEEKBENCHPACKAGE $GEEKBENCHVERSION.tar.gz

    RUN wget --quiet --no-check-certificate https://cdn.geekbench.com/$GEEKBENCHPACKAGE -O /tmp/$GEEKBENCHPACKAGE \
        && mkdir -p /opt/geekbench \
        && tar xzf /tmp/$GEEKBENCHPACKAGE -C /opt/geekbench \
        && rm -rf /tmp/$GEEKBENCHPACKAGE

    # run all tests
    ENTRYPOINT ["bash", "./run.sh"]
