from hash_visualizer import compute_hash, hex_to_bin
import numpy as np
import matplotlib.pyplot as plt

def avalanche_score(msg1: str, msg2: str, algorithm: str) -> float:

    h1 = hex_to_bin(compute_hash(msg1, algorithm))
    h2 = hex_to_bin(compute_hash(msg2, algorithm))

    # Count differing bits
    diff_bits = sum(b1 != b2 for b1, b2 in zip(h1, h2))
    total_bits = len(h1)
    return (diff_bits / total_bits) * 100.0


def show_diff_plot(msg1: str, msg2: str, algorithm: str):

    # --- Step 1: Compute both hashes ---
    h1 = compute_hash(msg1, algorithm)
    h2 = compute_hash(msg2, algorithm)

    # --- Step 2: Convert to binary arrays ---
    b1 = np.array(list(hex_to_bin(h1)), dtype=int)
    b2 = np.array(list(hex_to_bin(h2)), dtype=int)

    # --- Step 3: Logical XOR → 1 if bits differ ---
    diff = np.logical_xor(b1, b2).astype(int)

    # --- Step 4: Matplotlib visualization ---
    fig, ax = plt.subplots(figsize=(10, 1))
    ax.imshow(diff.reshape(1, -1), cmap='coolwarm', aspect='auto')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Bit Differences for {algorithm.upper()} ({sum(diff)} flipped bits)",
                 fontsize=10)
    plt.tight_layout()
    return fig
