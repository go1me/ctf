import rsa
import gmpy2

with open('pubkey.pem','rb') as f1:
    re = f1.read()

pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(re)
p = 319576316814478949870590164193048041239
q = 275127860351348928173285174381581152299
fn = (p-1) * (q-1)

d = gmpy2.invert(pubkey.e,fn)
d = int(d)

with open('flag.enc','rb') as f2:
    flag = f2.read()

privatekey = rsa.PrivateKey(pubkey.n , pubkey.e , d , p , q)
print(rsa.decrypt(flag,privatekey))