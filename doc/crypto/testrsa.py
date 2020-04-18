# -*- coding: utf-8 -*-
# by https://findneo.github.io/
# ref:
# https://crypto.stackexchange.com/questions/11053/rsa-least-significant-bit-oracle-attack
# https://ctf.rip/sharif-ctf-2016-lsb-oracle-crypto-challenge/
# https://introspelliam.github.io/2018/03/27/crypto/RSA-Least-Significant-Bit-Oracle-Attack/
import libnum, gmpy2, socket, time, decimal


def oracle(c1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = '47.96.239.28'
    port = 23333
    s.connect((hostname, port))
    s.recv(1024)
    s.send(hex(c1)[2:].strip("lL") + '\n')
    res = s.recv(1024).strip()
    s.close()
    if res == 'even': return 0
    if res == 'odd':
        return 1
    else:
        assert (0)


def partial(c, n):
    global c_of_2
    k = n.bit_length()
    decimal.getcontext().prec = k  # allows for 'precise enough' floats
    lower = decimal.Decimal(0)
    upper = decimal.Decimal(n)
    for i in range(k):
        possible_plaintext = (lower + upper) / 2
        # lower==0 when i<1809
        flag = oracle(c)
        if not flag:
            upper = possible_plaintext  # plaintext is in the lower half
        else:
            lower = possible_plaintext  # plaintext is in the upper half
        c = (c * c_of_2) % n  # multiply y by the encryption of 2 again
        print i, flag, int(upper - lower)
        # time.sleep(0.2)
    # By now, our plaintext is revealed!
    return int(upper)


def main():
    print "[*] Conducting Oracle attack..."
    return partial((c * c_of_2) % n, n)


if __name__ == '__main__':
    e = 0x10001
    n = 1606938044309278499168642398192229212629290234347717645487123

    c = 1206101155741464091016050901578054614292420649123909371122176
    c_of_2 = pow(2, e, n)
    m = main()
    # m = 560856645743734814774953158390773525781916094468093308691660509501812349
    print libnum.n2s(m)
    # QCTF{RSA_parity_oracle_is_fun}
