import numpy as np
from sympy import Matrix
import rsa
from fermat import fermat


def get_inverse(key, M):
    return int(np.array(Matrix(*key.shape, key.reshape(-1)).inv_mod(M)))


# Test part
# print(fermat(5, 100))

# tmp = 9
# key = np.array([[pow(tmp, 65537)]])
# print(get_inverse(key, 324408067905331294061961362648401604850041094409525393))

# print(pow(3, 618970019642690137449562110, 618970019642690137449562111))

key_len = 512
(public_key, private_key) = rsa.newkeys(key_len)
# (public_key, private_key) = (rsa.key.PublicKey(33233, 65537), rsa.key.PrivateKey(33233, 65537, 31877, 199, 167)) # Small
# (public_key, private_key) = (rsa.key.PublicKey(324408067905331294061961362648401604850041094409525393, 65537),
#                              rsa.key.PrivateKey(324408067905331294061961362648401604850041094409525393, 65537, 261053033937948972126275498807071761584832756042575305, 18527606826476548858471694039, 17509442581744647239696087)) # Normal

message = b'ARTISTICALLY'

encrypted = rsa.encrypt(message, public_key)  # Шифрование
print(encrypted)
message = rsa.decrypt(encrypted, private_key)  # Расшифрование
print(message)
