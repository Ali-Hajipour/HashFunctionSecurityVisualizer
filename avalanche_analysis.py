from hash_visualizer import compute_hash , hex_to_bin

def avalanche_score (message1 , message2 , algorithm = "sha256"):
    hash1 = hex_to_bin(compute_hash(message1 , algorithm))
    hash2 = hex_to_bin(compute_hash(message2 , algorithm))


    bits_difference = sum(b2 != b1 for b1 , b2 in zip(hash1 , hash2))
    total_bits = len(hash1)

    return (bits_difference/total_bits) * 100



test = avalanche_score("Ali Hajipour" , "Ali Hajipounn")
print(test)
#asdsadsad