from transformers import pipeline

model_id = "openai-community/gpt2"
generator = pipeline("text-generation", model=model_id)

prompt ="The dog chased the"

outputs= generator(prompt, max_new_tokens=15, num_return_sequences=1)

print("\n--- Model Output ---")
print(outputs[0]["generated_text"])
