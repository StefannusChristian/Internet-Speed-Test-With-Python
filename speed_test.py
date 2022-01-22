import speedtest
from prettytable import PrettyTable

test = speedtest.Speedtest()
print('Getting Server List...')
test.get_servers()
print('Choosing Server...')

best_server = test.get_best_server()
cols = best_server.keys()
vals = best_server.values()
best_server_table = PrettyTable(cols)

print('Server Found!')
print(f'Server Host: {best_server["host"]}')
print(f'Server Location: {best_server["country"]}')
print('Server Detail')
best_server_table.add_row(vals)
print(best_server_table)

print('Performing Download Test...')
download_result = test.download()
print('Download Test Completed!')
print(f'Download Speed = {round((download_result/1024/1024),2)} Mbps')
print()

print('Performing Upload Test...')
upload_result = test.upload()
print('Upload Test Completed!')
print(f'Upload Speed = {round((upload_result/1024/1024),2)} Mbps')
print()

print('Performing Ping Test')
ping_result = test.results.ping
print('Ping Test Completed!')
print(f'Ping = {round((ping_result),2)} ms')
