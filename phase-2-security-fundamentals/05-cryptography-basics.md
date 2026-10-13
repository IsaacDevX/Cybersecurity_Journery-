# Cryptography Basics

**Date started:** 2026-10-13
**Source:** Professor Messer Security+ SY0-701

## What Cryptography Is

The science of protecting data using math. It provides:
- **Confidentiality** — only the right person can read it
- **Integrity** — nobody can change it undetected
- **Authentication** — proves who sent it
- **Non-repudiation** — sender can't deny sending it

---

## The 3 Core Concepts

### 1. Symmetric Encryption (One Key)
- **How it works:** Same key encrypts and decrypts
- **Speed:** Fast
- **Weakness:** Key must be shared securely
- **Examples:** AES-256, ChaCha20
- **Use case:** Encrypting files, VPN tunnels, disk encryption

### 2. Asymmetric Encryption (Two Keys)
- **How it works:** Public key encrypts, private key decrypts
- **Speed:** Slow
- **Strength:** No shared secret needed
- **Examples:** RSA, ECC
- **Use case:** HTTPS, SSH, digital signatures

### 3. Hashing (One-Way)
- **How it works:** Input → fixed-length output. Cannot be reversed
- **Purpose:** Verify integrity, store passwords
- **Examples:** SHA-256, SHA-512, bcrypt, Argon2
- **Use case:** File integrity, password storage, blockchain

---

## Comparison Table

| | Symmetric | Asymmetric | Hashing |
|--|-----------|------------|---------|
| Keys | 1 (shared) | 2 (public/private) | None |
| Speed | Fast | Slow | Fast |
| Reversible | Yes | Yes | No |
| Use | Bulk data encryption | Key exchange, signatures | Integrity, passwords |

---

## Digital Signatures

**What they are:** A way to prove a message came from a specific sender and wasn't modified.

**How they work:**
1. Sender hashes the message
2. Sender encrypts the hash with their PRIVATE key
3. That encrypted hash is the "signature"
4. Anyone can verify it using the sender's PUBLIC key

**Provides:**
- Integrity (message not modified)
- Authentication (message came from sender)
- Non-repudiation (sender can't deny it)

---

## PKI (Public Key Infrastructure)

The system that manages digital certificates.

**Key parts:**
| Component | Purpose |
|-----------|---------|
| **CA (Certificate Authority)** | Signs and issues certificates (Let's Encrypt, DigiCert) |
| **Certificate** | Proves a public key belongs to a specific entity |
| **CSR** | Certificate Signing Request — sent to CA to get a cert |
| **Trust Store** | List of CAs your system trusts |

**How HTTPS works (simplified):**
1. Website sends its certificate to your browser
2. Browser checks if the CA that signed it is trusted
3. If yes → encrypted connection starts

---

## Real-World Applications

| Technology | Cryptography Used |
|------------|-------------------|
| HTTPS (web) | Asymmetric (key exchange) + Symmetric (data) |
| SSH (remote login) | Asymmetric (auth) + Symmetric (session) |
| Password storage | Hashing (bcrypt, Argon2) |
| File integrity | Hashing (SHA-256) |
| VPN | Symmetric encryption |
| Blockchain | Hashing + Digital Signatures |
| Zcash (private crypto) | Zero-knowledge proofs |

---

## Key Takeaways

1. Symmetric = fast, one key. Asymmetric = slow, two keys. Hashing = one-way.
2. Hashing ≠ encryption. Hashing can't be reversed.
3. Digital signatures = integrity + authentication + non-repudiation
4. PKI = the system that manages certificates
5. HTTPS = asymmetric for the handshake, symmetric for the data

---

## Cybersecurity Application

- **SOC Analysts** verify file hashes to detect tampering
- **Red Teamers** attack weak crypto implementations
- **AI Security** uses hashing to detect model tampering
- **Incident Response** uses signatures to verify evidence

---

*Last updated: October 2026*
