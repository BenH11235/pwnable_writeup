#stdio
echo "00 00 0a 00 ff" | xxd -r > /tmp/bh/stdio.dat;
echo "00 00 0a 02 ff" | xxd -r > /tmp/bh/stderr.dat;

#netcat
echo "00 de ad be ef" | xxd -r > /tmp/bh/netcat.dat;

#file
echo "00 00 00 00 00" | xxd -r > $'\x0a';

env $'\xde\xad\xbe\xef'=$'\xca\xfe\xba\xbe' ./input A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A $'\0' $' \n\r' 29001 A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A  0< /tmp/bh/stdio.dat 2< /tmp/bh/stderr.dat > readable_flag.dat&

nc localhost 29001 < /tmp/bh/netcat.dat > /tmp/bh/netcat.out;

