from sentence_transformers import SentenceTransformer

# 1. Load a small, fast AI model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Define the sentences you want to turn into numbers
sentences = [
    "end subscription",
    "cancel subscription"
]

# 3. Tell the model to convert the text into vectors
vectors = model.encode(sentences)

# 4. Print out the raw numbers
for i, vector in enumerate(vectors):
    print(f"\nSentence: '{sentences[i]}'")
    print(f"Vector Shape (Total numbers): {vector.shape}")
    print(f"First 5 raw numbers: {vector[:5]}...") 
