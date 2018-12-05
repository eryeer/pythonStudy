import coincurve

if __name__ == '__main__':
    privkey1 = coincurve.PrivateKey(b'\x01')
    privkey2 = coincurve.PrivateKey(b'\x01')
    print(privkey1 == privkey2)
    ecdh = privkey1.ecdh(privkey2.public_key.format())
    ecdh2 = privkey2.ecdh(privkey1.public_key.format())
    print(ecdh == ecdh2)
    print(ecdh2)
    print(len(ecdh2))

    print(ecdh2.hex())
    print(bytes.fromhex(ecdh2.hex()))
