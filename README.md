# agentic-blueprint

### A Standard for Auditable Agentic Systems

`agentic-blueprint` is a boilerplate designed to move AI-assisted development from "probabilistic vibing" to "deterministic engineering". It provides a structured framework for managing AI agents through a set of steering files known as the **Reliability Stack**.

By using this blueprint, you ensure that AI agents (like Codex or Copilot) operate as high-speed "Junior Devs" under the strict architectural oversight of a "Senior Architect".

---

## 🛡️ The Reliability Stack (AGENTS.md Standard)

This repository enforces the 2026 industry standard for agentic steering. These files act as the **Control Plane** for the repository:

* **`AGENTS.md` (The Identity)**: Defines the specific roles, tools, and permissions for every agent in the pipeline.
* **`CONSTRAINTS.md` (The Guardrails)**: Lists the "Hard Nos" that the AI cannot override (e.g., resource limits, safety gates, or unauthorized execution).
* **`DECISION_LOG.md` (The Memory)**: Tracks *why* architectural changes were made, preventing the AI from repeating old mistakes or "hallucinating" away project requirements.
* **`SKILL.md` (The Capability)**: Contains standardized, verified implementations of specific tasks that can be loaded into the AI's context on-demand.
* **`PROGRESS.txt` (The State)**: A lightweight log that tracks the current state of execution to prevent loops and ensure atomic task completion.

---

## 🎯 Prime Directives

All development within this blueprint must adhere to these core principles:

1.  **Preserve System Integrity First**: Safety and resource management are the primary features, not afterthoughts.
2.  **Measurable & Auditable**: Every automated decision must be recorded in a persistent operations store (e.g., PostgreSQL).
3.  **Documentation as Logic**: The Markdown files in the Reliability Stack are the "Source of Truth." If it isn't documented in the stack, the AI shouldn't build it.
4.  **Deterministic Backbones**: Use LLMs for interpretation and commentary, but keep core execution logic rule-based and auditable.

---

## 🚀 Getting Started

To use this blueprint with an AI agent:

1.  **Initialize the Stack**: Create the five core MD files in your repository root.
2.  **Set the Persona**: Define your role (e.g., Architect) and the AI's role (e.g., Senior Dev Lead) in `AGENTS.md`.
3.  **Define Guardrails**: Explicitly state your "Hard Nos" in `CONSTRAINTS.md`.
4.  **Audit the Bloom**: When the AI generates code, verify it against the `DECISION_LOG.md` before committing.

---

## 🛠️ Infrastructure Defaults

* **Database**: PostgreSQL for all operational data (SQLite for fallback/local testing only).
* **Orchestration**: Pipeline-first control flow (e.g., LangGraph compatibility).
* **Scheduler**: Native system schedulers (e.g., `launchd`) for reliable unattended execution.

---

**Disclaimer**: This is a framework for high-stakes automation. Reliability is unproven until it survives rigorous testing against the constraints defined in the Reliability Stack.
