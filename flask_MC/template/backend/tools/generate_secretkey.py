import secrets
import base64

def generate_secret_key(num_bytes):
    secret_key = secrets.token_bytes(num_bytes)
    return base64.b64encode(secret_key).decode('utf-8')

num_bytes = 64

generated_key = generate_secret_key(num_bytes)

file_name = "../app/environment/secret_key"
with open(file_name, "w") as file:
    file.write(generated_key)

print(f"Secret key generated and saved in {file_name}")
