# DECISION_LOG.md

### System Memory & Architectural Audit Trail

This file records every significant architectural and operational decision made for this project. It ensures that the project does not depend on ephemeral chat memory and provides a source of truth for AI agents to understand the "Why" behind the "What".

---

## 🏗️ 1. Decision Template

Every entry in this log must follow this format to ensure clarity and auditability:

### [Decision Title]
**Date**: YYYY-MM-DD
**Decision**:
* [Explicit statement of the choice made]
**Why**:
* [The data-backed rationale]
* [The risk being mitigated]
* [The counter-perspective considered]

---

## 🛡️ 2. Baseline Architectural Decisions

### Use a "Reliability Stack" for Agent Steering
**Date**: [Current Date]
**Decision**:
* All agentic behavior must be governed by the Five Steering Files: `AGENTS.md`, `CONSTRAINTS.md`, `DECISION_LOG.md`, `SKILL.md`, and `PROGRESS.txt`.
**Why**:
* Probabilistic "vibing" is insufficient for high-stakes automation.
* Standardized steering files provide deterministic guardrails that an LLM cannot easily ignore.

### Prioritize Auditability Over Raw Reasoning
**Date**: [Current Date]
**Decision**:
* Store structured summaries, scores, and rule checks in the operations store rather than raw "chain-of-thought" text.
**Why**:
* Structured data is easier to query and review for performance audits.
* It avoids the operational risk of over-collecting low-value or sensitive reasoning text.

### Require PostgreSQL for Operations
**Date**: [Current Date]
**Decision**:
* All live operational data must be persisted in PostgreSQL; SQLite is for local bootstrap only.
**Why**:
* Provides a central, durable source of truth for multi-agent environments.
* Prevents "stale state" issues common with ephemeral or file-based fallbacks.

---

## 📝 3. Maintenance Rule

When a major project decision is made—especially one that overrides a "vibe" or introduces a new constraint—it must be recorded here immediately. This ensures the "AI Bloom" is always pruned according to the Architect's intent.
