import requests
resp=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
binfo=resp.json()
print('Bitcoin price as of:',binfo['time']['updated'])
print('1 bitcoin price =',binfo['bpi']['USD']['rate'])