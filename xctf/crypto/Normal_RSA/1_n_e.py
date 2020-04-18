import rsa

with open('pubkey.pem','rb') as f1:
    re = f1.read()

pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(re)
print(pubkey.e)
print(pubkey.n)