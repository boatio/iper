import json
import socket
from urllib.request import urlopen
print("""
                     .####.########..########.########.
                     ..##..##.....##.##.......##.....##
                     ..##..##.....##.##.......##.....##
                     ..##..########..######...########.
                     ..##..##........##.......##...##..
                     ..##..##........##.......##....##.
                     .####.##........########.##.....##
""")
c = None
while 1:
        c = input('(I P E R):')
        if c.startswith('ipw'):
                c = c.replace('ipw ','')
                try:
                        print(socket.gethostbyname(c))
                except:
                        print('URL 가 유효하지 않습니다')
        elif c.startswith('ip'):
                c = c.replace('ip ','')
                try:
                        url = 'https://ipinfo.io/'+str(c)+'/json'
                        data = urlopen(url).read().decode('utf-8')
                        data = json.loads(data)
                        print('--------------------------------')
                        print('ip: '+data["ip"])
                        print('Country: '+data["country"])
                        print('City: '+data["city"])
                        print('loc: '+data["loc"])
                        print('org '+data["org"])
                        print('--------------------------------')
                except:
                        print('IP가 유효하지 않습니다')
        
