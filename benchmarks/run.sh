    #!/bin/bash
    
    RAMSPEED_PATH='/docker_benchmark/ramsmp-3.5.0'
    GEEKBENCH_PATH='/opt/geekbench/Geekbench-5.4.1-Linux'
    RES_PATH='./results'

    #iozone -t 2 > $RES_PATH/iozone3

    #$RAMSPEED_PATH/ramsmp -b 3 > $RES_PATH/ramspeed3
    #$RAMSPEED_PATH/ramsmp -b 6 > $RES_PATH/ramspeed6
    #$GEEKBENCH_PATH/geekbench5   > $RES_PATH/geekbench

    iperf3 -s &
    iperf3 -c 127.0.0.1 -w 20K > $RES_PATH/iperf3_tcp
    iperf3 -u -c 127.0.0.1     > $RES_PATH/iperf3_udp
