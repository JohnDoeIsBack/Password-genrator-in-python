import hashlib
import os

password = 'password123'  # This should be replaced with the user's password

# Generate a random salt
salt = os.urandom(16)

# Combine the salt and password
salted_password = salt + password.encode()

# Hash the salted password
hashed_password = hashlib.sha256(salted_password).hexdigest()

# Now you can store the salt and hashed_password in your database
