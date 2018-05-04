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
			made by Boat on Boat
				ver 1.0
""")
c = None
while 1:
        c = input('\033[1m\033[32m(I P E R):\033[0m\033[37m')
        if c.startswith('ipw'):
                c = c.replace('ipw ','')
                try:
                        print(socket.gethostbyname(c))
                except:
                        print('URL 가 유효하지 않습니다')
        elif c.startswith('help'):
            print("\033[1m\033[36m                   --------------------------------------")
            print("                   ip [IP] Get ip information")
            print("                   ipw[Domain]Get domain Ip")
            print("                   --------------------------------------\033[0m\033[37m")
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
        
