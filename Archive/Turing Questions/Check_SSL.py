import ssl, socket
from asn1crypto import pem, x509

hostname = 'dev.temarico.com'
ctx = ssl.create_default_context()
s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
s.connect((hostname, 443))
der = s.getpeercert(binary_form=True)
cert = x509.Certificate.load(der)
pubkey = cert.public_key.unwrap()
print(pubkey)
print(pem.armor("PUBLIC KEY", pubkey.contents).decode("ASCII"))