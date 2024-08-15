import pyotp
import time

# Generate a random base32 secret
secret = pyotp.random_base32()

# Create a TOTP object with a time limit of 30 seconds
totp = pyotp.TOTP(secret, interval=30)

# Get the current OTP
otp = totp.now()

# Print the OTP
print("Your OTP:", otp)

# Wait for 30 seconds
time.sleep(30)

# Verify the OTP after the time limit
otp_verified = totp.verify(otp)

# Print whether the OTP was verified or not
if otp_verified:
    print("OTP verified successfully!")
else:
    print("OTP verification failed!")