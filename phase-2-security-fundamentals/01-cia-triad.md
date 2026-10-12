# CIA Triad

**Date started:** 2026-10-12
**Source:** Professor Messer Security+ SY0-701

## What It Is

The CIA Triad is the foundational model for all cybersecurity. Every security decision, tool, and policy exists to protect one or more of these three principles:

- **Confidentiality** — keeping data secret
- **Integrity** — keeping data unchanged
- **Availability** — keeping data accessible

If any of the three is broken, security has failed.

---

## Confidentiality

- **What it means:** Information should only be known to authorized people. Prevent disclosure to unauthorized systems or individuals.

- **Examples:**
  - Encryption (encrypting messages so only the right people can read them)
  - Two-factor authentication (additional confirmation before information is disclosed)
  - Access control lists (only certain users can view certain files)
  - Password protection on medical records, bank accounts, corporate documents

- **What violates it:**
  - A doctor accessing another doctor's patient files
  - Data leaks / breaches
  - Shoulder surfing
  - Stolen credentials
  - Unencrypted data sent over the internet

---

## Integrity

- **What it means:** Data is stored and transferred exactly as intended. Any modification must be detected.

- **Examples:**
  - Hashing (SHA-256, MD5) — any change to the file produces a different hash
  - Digital signatures — prove the data is genuine and untampered
  - Checksums on downloads
  - Blockchain (hash chains)

- **What violates it:**
  - Man-in-the-middle attacks (attacker modifies data in transit)
  - Malware modifying system files
  - Unauthorized database edits
  - Ransomware altering file contents

---

## Availability

- **What it means:** Information and systems must be accessible to authorized users whenever needed. Systems must stay up and running.

- **Examples:**
  - Backups (if one server dies, data isn't lost)
  - Redundancy / Failover (if one server dies, another takes over instantly)
  - Load balancing (traffic distributed so no single point fails)
  - Fault tolerance (system continues operating through failures)
  - DDoS protection
  - Closing security holes that cause crashes

- **What violates it:**
  - DDoS attacks (flooding a server until it goes down)
  - Ransomware (encrypts files — you can't access them)
  - Physical destruction (fire, flood, power failure)
  - Hardware failure
  - Insider sabotage

---

## Cybersecurity Application

Every security tool, policy, and incident response maps back to one or more of these pillars:

| Tool / Concept | Protects |
|----------------|----------|
| Encryption | Confidentiality |
| Hashing, Digital Signatures | Integrity |
| Backups, Redundancy | Availability |
| Firewalls | All three |
| Multi-factor Authentication | Confidentiality + Integrity |
| Incident Response | Depends on attack (each pillar has different playbooks) |

**Why it matters:** When analyzing an incident, the first question is *"which pillar was attacked?"* — because the response is different for each.

**Example:**
- **Confidentiality attack** → rotate credentials, notify affected users, patch leak
- **Integrity attack** → restore from clean backup, verify hashes
- **Availability attack** → restore service, block the attack source, scale up

---

## Key Takeaways

1. **CIA Triad = Confidentiality, Integrity, Availability** — every security decision maps back to one or more.

2. **Ransomware attacks Availability**, not Confidentiality. The files still exist; they're just inaccessible.

3. **Different pillars require different responses.** Knowing which was attacked determines the playbook.

4. **Real-world tools:**
   - Confidentiality → Encryption, 2FA, access controls
   - Integrity → Hashing, Digital Signatures, checksums
   - Availability → Backups, redundancy, load balancing

---

## Quiz Notes

**Q1:** A doctor accesses another doctor's patient files → **Confidentiality** violated.

**Q2:** Availability is protected by **Backups, Redundancy, and Load Balancing**.

**Q3:** Ransomware attacks **Availability** — the files are still there but inaccessible. It is NOT a confidentiality attack.

---

*Last updated: October 2026*
