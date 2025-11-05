import hashlib

def compute_hash( message , algorithm = "sha256"):
    h = hashlib.new( algorithm )
    h.update(message.encode("utf-8"))
    return h.hexdigest()




def hex_to_bin (hex_str):
    # transform the hex to binary
    return bin(int (hex_str, 16))[2:].zfill(len(hex_str)*4)


if __name__ == "__main__":
    msg = "AliHajipour"
    for alg in ['sha1', 'sha256', 'sha3_512']:
        print(f"{alg.upper()}: {compute_hash(msg, alg)}")



