# Authentication & Authorization

**Date started:** 2026-10-13
**Source:** Professor Messer Security+ SY0-701

## The Core Difference

- **Authentication (AuthN)** — WHO you are (proving your identity)
- **Authorization (AuthZ)** — WHAT you can do (your permissions)

**Example:** You log into your bank (authentication). You can see your own account but not someone else's (authorization).

---

## Authentication Methods

| Method | Examples |
|--------|----------|
| **Something you know** | Password, PIN, security question |
| **Something you have** | Phone, hardware token, smart card |
| **Something you are** | Fingerprint, face, iris scan |
| **Somewhere you are** | GPS location, IP address |
| **Something you do** | Typing pattern, walking gait |

**Real-world auth = combining two or more = MFA (Multi-Factor Authentication).**

---

## Authentication Factors

| Term | Meaning |
|------|---------|
| **MFA (Multi-Factor Auth)** | 2+ different factors (password + phone) |
| **2FA (Two-Factor Auth)** | Exactly 2 factors |
| **TOTP** | Time-based One-Time Password (Google Authenticator) |
| **HOTP** | HMAC-based One-Time Password (counter-based) |
| **FIDO2 / WebAuthn** | Passwordless authentication (hardware keys) |
| **SSO** | Single Sign-On — one login for multiple services |
| **Biometrics** | Fingerprint, face, iris — something you are |

---

## Authorization Models

| Model | What It Means |
|-------|---------------|
| **RBAC** (Role-Based Access Control) | Permissions based on role (Admin, User, Guest) |
| **ABAC** (Attribute-Based Access Control) | Permissions based on attributes (department, location, time) |
| **MAC** (Mandatory Access Control) | System enforces rules (military, government) |
| **DAC** (Discretionary Access Control) | Owner decides who has access |

**RBAC example:**
- Admin → can do everything
- Manager → can approve expenses
- Employee → can submit expenses
- Guest → can only view

---

## Key Principles

| Principle | Meaning |
|-----------|---------|
| **Least Privilege** | Give users the MINIMUM access needed to do their job |
| **Separation of Duties** | No single person can complete a critical task alone |
| **Zero Trust** | Trust nobody, verify everything |
| **Defense in Depth** | Multiple layers of access controls |

---

## Comparison

| Concept | Example |
|---------|---------|
| Authentication | Logging in with password + 2FA |
| Authorization | Once logged in, you can only view — not delete |
| Least Privilege | Intern doesn't get admin access |
| RBAC | "Manager" role gets manager permissions |

---

## Cybersecurity Application

- **SOC Analyst** — sees failed authentication attempts, privilege escalation
- **Red Teamer** — tries to bypass authentication or escalate privileges
- **AI Security** — protects AI system access (who can query the model?)
- **Incident Response** — revokes compromised credentials

---

## Key Takeaways

1. Authentication = identity. Authorization = permissions.
2. MFA = 2+ different factor types (not just two passwords)
3. RBAC = most common authorization model in companies
4. Least privilege = the golden rule of access control
5. Zero Trust = assume breach, verify everything

---

*Last updated: October 2026*
