# Data Compliance

**Effective date:** 2026-05-29
**Applies to:** the JustHireMe desktop application ("the Software") and the JustHireMe website ("the Site").

> **Note for the maintainer:** Complete the `[BRACKETED]` items (legal entity, representative, contact, processor regions). This document describes how JustHireMe's design maps to common data-protection regimes; it is not legal advice. Confirm obligations for your jurisdiction and deployment with a qualified advisor.

This document complements the [Privacy Policy](privacy-policy.md) with the compliance-specific details for GDPR/UK GDPR, CCPA/CPRA, and similar laws.

---

## 1. Roles and the local-first advantage

JustHireMe is **local-first**. The personal data that matters most — your resume/profile, job leads, generated documents, and API keys — is **created and stored on your own device** and is never transmitted to or controlled by the maintainer. For that data:

- **You are the controller** of your own local data. JustHireMe (running on your machine) is the tool you use to process it.
- The maintainer has **no access** to it and cannot retrieve, export, or delete it on your behalf.

For the limited Site processing (anonymized counters and the feedback channel), the **maintainer acts as controller**, with third-party **processors** (Section 6).

## 2. What personal data is involved, and where

| Data | Controller | Location | Notes |
| --- | --- | --- | --- |
| Profile, leads, generated docs, settings, API keys | You | Your device | Maintainer has no copy or access |
| Data sent to your chosen LLM provider | You + that provider | The provider | Governed by the provider's terms; use a local model (Ollama) to avoid this |
| Anonymous visit/download counts | Maintainer | Site infrastructure | Visitor IDs are salted-hashed; not used to identify you |
| Feedback submissions | Maintainer | GitHub issues | May contain personal data you include; auto-redaction attempts to strip PII/secrets |

## 3. GDPR / UK GDPR

**Lawful bases** (see Privacy Policy §6): legitimate interests (operating anonymized counters; running a feedback channel), consent (voluntary feedback/forms), and performing a requested action.

**Data minimization & purpose limitation:** the Site collects only what it needs to count downloads/visits and accept feedback. No profiles, no ad tracking, no sale of data.

**Data-subject rights.** You may request access, rectification, erasure, restriction, portability, and objection, and may withdraw consent at any time:

- **Local Software data:** exercise directly on your device — view, edit, export, or delete it yourself. The app provides profile management and an export of your identity graph.
- **Feedback / Site data:** contact us (Section 9). Because Site analytics are anonymized aggregates that cannot be tied to you, access/erasure typically applies to **feedback** content you submitted. We respond within **one month** (extendable as permitted by law).

**Automated decision-making:** JustHireMe's ranking/scoring runs locally and is advisory; it does not make legal or similarly significant decisions about you under Article 22. Generated documents are drafts for your review.

**International transfers:** Site processors may operate outside your country (Section 6); transfers rely on the safeguards those processors provide (e.g., Standard Contractual Clauses).

**EU/UK representative & DPO:** `[Appoint and list an Art. 27 representative and/or DPO here if required for your operation.]`

**Supervisory authority:** you have the right to lodge a complaint with your local data-protection authority.

## 4. CCPA / CPRA (California)

- **No sale or "sharing" of personal information.** We do not sell or share personal information as defined by the CCPA/CPRA, and we do not use it for cross-context behavioral advertising.
- **Categories collected by the Site:** internet/usage activity in the form of **anonymized, aggregated** counts (with salted-hashed de-dup keys) and any information you voluntarily include in feedback.
- **Your rights:** to know, access, delete, correct, and to opt out of sale/sharing (not applicable, since we do none). Exercise via Section 9. We will not discriminate against you for exercising rights.

## 5. Other regimes

The same minimal, transparent, local-first model is intended to align with laws such as Canada's PIPEDA, Brazil's LGPD, and similar frameworks. Where a specific obligation applies to your deployment, address it in this section.

## 6. Sub-processors

Depending on deployment, the Site may use: a static/edge host (e.g., Vercel), a key-value/counter store (e.g., Upstash Redis), and GitHub (release hosting + feedback issue tracker). Each processes data under its own terms and security program. `[Maintain an accurate, current list with regions and links to each processor's DPA.]`

## 7. Security measures

- HTTPS for Site traffic and Software downloads/updates.
- Salted **HMAC hashing** of visitor identifiers; raw IPs are not retained for analytics.
- **Redaction** on the public feedback path to reduce accidental exposure of PII/secrets.
- Local data is protected by your operating system's user account and device security; you control encryption (e.g., full-disk encryption) and backups.
- TLS certificate verification on the runtime-pack download path.

## 8. Data retention

- **Local Software data:** retained until you delete it; no server-side copy exists.
- **Site counters:** retained as aggregate counts / hashed de-dup keys for as long as the counters operate.
- **Feedback:** retained in the public issue tracker until removed on request or by maintainers.

## 9. Exercising your rights / contact

Email `[DATA / PRIVACY CONTACT EMAIL]`, or open a request at https://github.com/vasu-devs/JustHireMe (use `SECURITY.md` for anything sensitive). To protect you, we may need to verify your request. For most local data, the fastest path is to manage or delete it directly in the app on your device.

## 10. Breach handling

If a data breach affecting the limited Site-side personal data occurs and poses a risk to individuals, we will assess and, where legally required, notify the relevant supervisory authority and affected individuals within the applicable timeframe (e.g., 72 hours under GDPR).

## 11. Changes

We may update this document; the "Effective date" will be revised and material changes noted in release notes or the changelog.
