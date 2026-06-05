import hashlib
import random
import time


def create_system_entropy():
    """Generates a dynamic sequence of binary points to act as a unique system signature."""
    # Customization tip: You can change the range from 128 to 64 or 256
    binary_stream = [str(random.choice([0, 1])) for _ in range(128)]
    return "".join(binary_stream)


def initialize_canary_trap():
    """Sets up the fake configuration file and locks in its initial integrity hash."""
    secret_key = create_system_entropy()

    # Generate the baseline SHA-256 hash representing the secure state
    baseline_hash = hashlib.sha256(secret_key.encode()).hexdigest()

    print("--- DECEPTION NODE ACTIVATED ---")
    print("[INFO] Fake Database Credentials Generated.")
    print(f"[INFO] Secure State Hash: {baseline_hash}\n")

    return baseline_hash


def verify_system_integrity(secure_hash):
    """Monitors the token file.

    If an intruder reads or alters it, the hash state breaks.
    """
    print("[RUNNING] Monitoring canary token for unauthorized access...")
    time.sleep(2)

    # Simulating a realistic network check
    is_compromised = random.choice([True, False])

    if is_compromised:
        # The intruder alters the file, generating a completely different hash
        current_hash = hashlib.sha256(b"file_accessed_by_unauthorized_user").hexdigest()
    else:
        current_hash = secure_hash

    # Check if the states match
    if current_hash != secure_hash:
        print("\n[!] SECURITY INCIDENT DETECTED [!]")
        print("[ALERT] Canary token integrity has collapsed!")
        print(f"[TIME] Event recorded at: {time.ctime()}")
        print("[RESPONDING] Flagging local ip address and updating logs.")
    else:
        print("\n[STATUS] System clean. No unauthorized file access detected.")


if __name__ == "__main__":
    active_trap = initialize_canary_trap()
    verify_system_integrity(active_trap)
