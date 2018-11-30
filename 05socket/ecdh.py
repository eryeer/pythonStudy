import coincurve

key = coincurve.PrivateKey()
print(key.secret)
print(key.public_key.public_key)
