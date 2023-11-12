import socket,re

# Adres i port, na którym działa serwer na drugim komputerze
remote_address = ('192.168.68.129', 7489)

# Tworzenie gniazda (socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def parser(data):
    # Konwertowanie danych na tekst
    data = data.decode('utf-8')

    # Wyrażenie regularne do wydobycia liczb z tekstu
    pattern = r'Ch1="(\d+\.\d+)" Ch2="(\d+\.\d+)"'

    match = re.search(pattern, data)
    if match:
        liczba1 = float(match.group(1))
        liczba2 = float(match.group(2))
        return [liczba1, liczba2]
    else:
        return None

try:
    sock.connect(remote_address)

    while True:
        data = sock.recv(128)
        if not data:
            break
        #value = parser(data)
        #if value != None:
         #   print(value)

        print(f'Odebrano: {data.decode()}')

finally:
    sock.close()
