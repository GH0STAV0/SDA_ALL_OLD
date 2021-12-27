
#!/bin/bash

mkdir -p /dev/net
mknod /dev/net/tun c 10 200
chmod 600 /dev/net/tun

/etc/init.d/openvpn restart
openvpn --mktun --dev tun0
openvpn --mktap --dev tap0
