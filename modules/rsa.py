from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse, long_to_bytes
from factordb.factordb import FactorDB

try:
    import gmpy2
    HAS_GMPY2 = True
except ImportError:
    HAS_GMPY2 = False
    print("Warning: gmpy2 not installed. Small exponent attack (rsa_e) will not work.")

def factor_n(n):
    f = FactorDB(n)
    f.connect()
    factors = f.get_factor_list()
    return factors

def rsa_pem(s):
    with open(s , "rb") as f:
        key = RSA.import_key(f.read())

    n = key.n
    e = key.e
    print(f"Extracted n: {n}")
    print(f"Extracted e: {e}")

    factors = factor_n(n)
    print(f"Factors from FactorDB: {factors}")

    if len(factors) != 2:
        print("Warning: n does not factor into exactly two primes!")
        return

    p, q = factors

    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)

    private_key = RSA.construct((n, e, d, p, q))

    with open("private.pem", "wb") as f:
        f.write(private_key.export_key())

    print("Private key saved to private.pem")

def rsa_fact(n, e, c):
    """
    Factor n using FactorDB, then decrypt ciphertext c.
    """
    print(f"Attempting to factor n: {n}")
    factors = factor_n(n)
    print(f"Factors from FactorDB: {factors}")

    if len(factors) != 2:
        print("Warning: n does not factor into exactly two primes!")
        return

    p, q = factors
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    
    m = pow(c, d, n)
    plaintext = long_to_bytes(m)
    
    print(f"Private exponent d: {d}")
    print(f"Plaintext (hex): {plaintext.hex()}")
    print(f"Plaintext (bytes): {plaintext}")
    
    try:
        print(f"Plaintext (decoded): {plaintext.decode()}")
    except:
        print("Could not decode plaintext as UTF-8")
    
    return plaintext

def rsa(p, q, e, c):
    """
    Decrypt RSA ciphertext given p, q, e, c.
    """
    print(f"Using provided primes p={p}, q={q}")
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    
    m = pow(c, d, n)
    plaintext = long_to_bytes(m)
    
    print(f"Modulus n: {n}")
    print(f"Private exponent d: {d}")
    print(f"Plaintext (hex): {plaintext.hex()}")
    print(f"Plaintext (bytes): {plaintext}")
    
    try:
        print(f"Plaintext (decoded): {plaintext.decode()}")
    except:
        print("Could not decode plaintext as UTF-8")
    
    return plaintext

def rsa_e(c, e):
    """
    Small exponent attack (e.g., e=3).
    If c^(1/e) is small enough, we can compute the eth root directly.
    """
    if not HAS_GMPY2:
        print("Error: gmpy2 is required for small exponent attack")
        print("Install with: pip install gmpy2 or sudo pacman -S python-gmpy2")
        return None
    
    print(f"Attempting small exponent attack with e={e}")
    
    # Try to compute the eth root of c
    k = 0
    while True:
        # m^e = c + k*n, but we don't know n, so we try m^e = c directly
        m_test = gmpy2.iroot(c + k, e)
        if m_test[1]:  # if exact root found
            m = int(m_test[0])
            plaintext = long_to_bytes(m)
            print(f"Found plaintext after {k} iterations")
            print(f"Plaintext (hex): {plaintext.hex()}")
            print(f"Plaintext (bytes): {plaintext}")
            try:
                print(f"Plaintext (decoded): {plaintext.decode()}")
            except:
                print("Could not decode plaintext as UTF-8")
            return plaintext
        k += 1
        if k > 1000:
            print("Could not find plaintext with small exponent attack (tried 1000 iterations)")
            return None

if __name__ == "__main__":
    rsa_pem()

