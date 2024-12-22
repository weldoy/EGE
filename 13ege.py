from ipaddress import ip_network

net = ip_network('69.121.128.142/255.255.252.0', 0)
for ip in net:
    print(ip)

# НЕ БРАТЬ! (ЗАРЕЗЕРВИРОВАННЫЕ)

# Первый ip - ip сети
# Последний - ip сети широковещательный 

# Ответ >>>

# От второго и до предпоследнего
# Или for ip in net.hosts(): - ip адреса компьютеров
