# SKILL.md

### The Capability Playbook: Verified Agentic Workflows

This file contains the "Gold Standard" implementations for specific tasks within this repository. Agents must follow these playbooks exactly to ensure consistency, safety, and auditability.

---

## 🛠️ 1. How to Define a Skill

Every skill added to this project must include the following sections to be considered "Verified":

* **Goal**: What does this skill achieve?
* **Inputs**: What data or credentials does it require?
* **Deterministic Logic**: The step-by-step code or process flow.
* **Safety Checks**: Which specific rules in `CONSTRAINTS.md` apply here?
* **Audit/Logging**: What specific data must be persisted to **PostgreSQL** after execution?

---

## 📋 2. Core Skill Template: [Skill Name]

### Goal
[Describe the specific outcome, e.g., "Persist Operational Summary to Database"]

### Pre-requisites
* [e.g., Verified PostgreSQL connection string]
* [e.g., Validated input schema]

### The Workflow (Step-by-Step)
1.  **Validation**: Check inputs against the expected schema.
2.  **Constraint Check**: Verify the action does not violate the "Hard Nos" in `CONSTRAINTS.md`.
3.  **Execution**: Perform the core logic (e.g., the SQL `INSERT` or the API `POST`).
4.  **Verification**: Confirm the external state changed as expected (e.g., check for a 200 OK or a successful DB commit).
5.  **Logging**: Write a **Structured Summary** of the outcome, including any error codes, to the audit table.

---

## 🚀 3. Verified Playbook: Standardized Data Persistence

**Goal**: Ensure all agentic decisions are recorded in a queryable, durable format.

**Logic**:
* **Step 1**: Extract the core "Score," "Decision," and "Timestamp" from the agent's output.
* **Step 2**: Use the `db_adapter` to open a session with the **Postgres** operations store.
* **Step 3**: Execute a parameterized query to prevent SQL injection.
* **Step 4**: Log the request count and estimated cost of the LLM call that generated this decision.

**Safety Gate**:
* If the database is unreachable, the agent must **Halt** and update `PROGRESS.txt` with a "Critical Persistence Failure" alert.
