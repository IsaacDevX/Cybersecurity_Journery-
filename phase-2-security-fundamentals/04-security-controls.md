# Security Controls

**Date started:** [today]
**Source:** Professor Messer Security+ SY0-701

## What Security Controls Are

Any measure put in place to reduce risk. Every firewall, password, guard, backup, or policy is a control.

---

## The 4 Categories (How They Work)

| Category | What It Means | Examples |
|----------|---------------|----------|
| **Technical** | Implemented in technology | Firewalls, encryption, antivirus, MFA |
| **Managerial** | Policies and procedures | Risk assessments, security policies |
| **Operational** | Day-to-day human actions | Security guards, awareness training |
| **Physical** | Physical barriers | Locks, fences, CCTV, badges |

---

## The 6 Types (What They Do)

| Type | What It Does | Example |
|------|--------------|---------|
| **Preventive** | Stops the attack before it happens | Firewall, MFA, door lock |
| **Detective** | Finds the attack when it happens | IDS, CCTV, log monitoring |
| **Corrective** | Fixes damage after an attack | Backups, patching |
| **Deterrent** | Discourages attackers | Warning signs, visible cameras |
| **Compensating** | An alternative when the main control isn't possible | Extra monitoring when MFA isn't available |
| **Recovery** | Restores systems after an incident | Backup restoration, DR plan |

---

## Defense in Depth

Using **multiple layers** of controls so if one fails, another catches it.

**Example layers:**
1. Physical — locked server room
2. Network — firewall
3. Endpoint — antivirus
4. Application — input validation
5. Data — encryption
6. User — security awareness training

**Why it matters:** No single control is perfect. Layers give you time to respond.

---

## Key Takeaways

1. Every control fits into one of 4 categories AND one of 6 types
2. Controls can overlap categories (e.g., a firewall is technical + preventive)
3. Defense in depth = layers. Assume each layer will fail eventually.
4. Compensating controls are used when the ideal control isn't possible

---

## Cybersecurity Application

When a SOC analyst investigates an incident:
- Which control **should** have stopped it?
- Did that control **fail**?
- What **compensating** control could have caught it?
- What **corrective** action restores the system?

---

*Last updated: October 2026*
