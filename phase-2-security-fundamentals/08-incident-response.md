# Incident Response

**Date started:** 2026-10-13
**Source:** Professor Messer Security+ SY0-701

## What Incident Response Is

The structured process of handling a security incident — from the moment it's detected to full recovery. Prevents panic, ensures evidence is preserved, and minimizes damage.

**Based on the NIST Incident Response Lifecycle.**

---

## The NIST 6-Step Lifecycle

| Step | What Happens |
|------|--------------|
| **1. Preparation** | Build policies, tools, teams, playbooks BEFORE incidents happen |
| **2. Detection & Analysis** | Identify the incident, assess scope, determine severity |
| **3. Containment** | Stop the spread — isolate affected systems |
| **4. Eradication** | Remove the threat — delete malware, patch vulnerabilities |
| **5. Recovery** | Restore systems to normal operation |
| **6. Lessons Learned** | Review what happened, improve for next time |

**Memory trick:** "Prepare, Detect, Contain, Eradicate, Recover, Learn" → **PDCERL**

---

## Key Roles

| Role | What They Do |
|------|--------------|
| **Incident Responder** | Leads the investigation and response |
| **SOC Analyst** | Detects and triages the alert |
| **Forensics Analyst** | Collects and preserves evidence |
| **IT Admin** | Restores systems |
| **Management** | Handles communication and decisions |
| **Legal / PR** | Handles disclosure and media |

---

## Digital Forensics — Evidence Handling

| Term | Meaning |
|------|---------|
| **Order of Volatility** | Collect the most volatile evidence first (RAM → disk → backups) |
| **Chain of Custody** | Documented record of who handled evidence and when |
| **Hashing** | SHA-256 hash of evidence to prove it wasn't modified |
| **Write Blocker** | Hardware that prevents modification of evidence during analysis |
| **Legal Hold** | Preserve evidence for legal proceedings |

**Order of Volatility (most to least volatile):**
1. RAM (lost on reboot)
2. Running processes
3. Network connections
4. Temporary files
5. Disk storage
6. Backups and archives

---

## Playbooks

Pre-written response guides for specific incidents:

| Playbook | When Used |
|----------|-----------|
| **Ransomware Playbook** | Files encrypted, ransom note found |
| **Phishing Playbook** | User reports suspicious email |
| **Data Breach Playbook** | Customer data exposed |
| **DDoS Playbook** | Service under attack |
| **Insider Threat Playbook** | Employee suspected |

Playbooks save time and prevent panic during a real incident.

---

## Key Metrics

| Metric | What It Measures |
|--------|------------------|
| **MTTD** (Mean Time to Detect) | How fast you notice incidents |
| **MTTR** (Mean Time to Respond) | How fast you contain them |
| **MTBF** (Mean Time Between Failures) | Time between incidents |

Lower MTTD and MTTR = better security posture.

---

## Cybersecurity Application

- **SOC Analyst** — detects and triages, escalates to IR
- **IR Team** — contains, eradicates, recovers
- **Forensics** — preserves evidence for legal action
- **Management** — communicates with stakeholders
- **AI Security** — applies the same process to AI-specific incidents (model poisoning, prompt injection)

---

## Key Takeaways

1. IR = NIST lifecycle: Prepare → Detect → Contain → Eradicate → Recover → Learn
2. Order of Volatility: RAM first, backups last
3. Chain of custody + hashing = legal-grade evidence
4. Playbooks = pre-written responses for common incidents
5. Lessons learned is the most skipped and most important step

---

## Phase 2.1 Summary

You've now completed the 8 foundations of Security Fundamentals:
1. CIA Triad
2. Risk Management
3. Threats & Vulnerabilities
4. Security Controls
5. Cryptography Basics
6. Authentication & Authorization
7. Malware Types
8. Incident Response

These map directly to the CompTIA Security+ exam objectives. You now understand the vocabulary and concepts for Phase 2.2 (Blue Team Hands-On).

---

*Last updated: October 2026*
