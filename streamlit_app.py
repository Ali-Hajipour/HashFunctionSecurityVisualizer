import streamlit as st
from hash_visualizer import compute_hash
from avalanche_analysis import avalanche_score


st.set_page_config(page_title="Hash Function Security Visualizer" , layout="centered")
st.title("Hash Function Security Visualizer")
st.subheader("In this Project we will check the avalanche effect on hash functions | Ali Hajipour")
st.markdown("Ali Hajipour")

url = "https://github.com/Ali-Hajipour"
st.write("My  [Github](%s)" % url)

#inputs
msg1 = st.text_input("The First Message")
msg2 = st.text_input("The Second Message")

algorithm = st.selectbox("Hashing Algorithm" ,  ["sha1", "sha256", "sha512", "sha3_512"])

if st.button("Compute Avalanche Effect"):
    h1 = compute_hash(msg1, algorithm)
    h2 = compute_hash(msg2, algorithm)

    st.write(f"**{algorithm.upper()} Digest of Message 1:** `{h1}`")
    st.write(f"**{algorithm.upper()} Digest of Message 2:** `{h2}`")

    # --- Avalanche Analysis ---
    score = avalanche_score(msg1, msg2, algorithm)
    st.success(f" Avalanche Score: {score:.2f}% of bits differ")

    st.caption("Expected ≈ 50 % for a good cryptographic hash.")

    st.subheader("Visual Bit Difference Map")
    fig = show_diff_plot(msg1, msg2, algorithm)
    st.pyplot(fig)