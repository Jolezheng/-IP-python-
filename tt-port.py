import telnetlib as tel
import time
#import socket

def test(host, port):
  try:
    tel.Telnet(host=host, port=port, timeout=2)
    print(port, "port was opening")
  except:
    print(port, "port not opening")

if __name__ == '__main__':
  test(host='10.118.230.69', port=12580)
