# agentic-blueprint

### The Reliability Stack for Auditable Agentic Systems

`agentic-blueprint` is a professional-grade boilerplate for building and deploying agentic systems that require strict risk management and deterministic execution. 

While many AI projects rely on "probabilistic vibes," this blueprint uses **Documentation-Driven Orchestration (DDO)** to ensure that AI agents operate within human-defined guardrails. It is the foundation for **Project Centaur**, a trading research and automation system.

---

## 🛡️ The Reliability Stack (AGENTS.md Standard)

This repository follows the 2026 industry standard for agentic steering. The following "Steering Files" act as the Control Plane for all AI interactions:

* **`AGENTS.md`**: Defines the identities, roles, and repo-level configurations for all agents in the pipeline.
* **`CONSTRAINTS.md`**: The "Hard Guardrails" (including the **CFO Gate**) that no agent is permitted to override.
* **`DECISION_LOG.md`**: The durable memory of architectural choices (e.g., **Postgres-only**, **launchd** scheduler) to prevent "AI Bloom" from repeating mistakes.
* **`SKILL.md`**: Standardized playbooks for complex tasks, such as Alpaca broker execution and internal managed exits.
* **`PROGRESS.txt`**: A lightweight state log used to prevent loops and ensure atomic task completion during automated ticks.

---

## 🎯 Prime Directives

Every contribution to this blueprint must align with these core principles:
* **Preserve Capital First**: Risk management is not an afterthought; it is the primary feature.
* **Safe & Repeatable**: Growth must be achieved legally and through a verifiable edge, not luck.
* **Measurable & Auditable**: Every decision, from a "Shadow Proposal" to a "Paper Order," must be recorded in the **PostgreSQL** operations store.
* **Deterministic Logic**: The AI layer is used for interpretation and commentary, while the core trading engine remains rule-based.

---

## 🚀 Current Implementation: Project Centaur

The primary reference implementation for this blueprint is a trading automation system capable of:
* **Multi-Market Data Collection**: Equity and crypto data gathered 24/7.
* **Shadow Learning**: Generating and scoring "pretend" trades to establish strategy fitness before risking capital.
* **Micro Paper Execution**: A tightly constrained path for Alpaca Paper orders ($10 limit, one slot at a time).
* **Managed Exits**: Internal tracking of stops and targets to bypass broker-native fractional limitations.

---

## 🛠️ Infrastructure Requirements

* **Runtime**: Python 3.11+
* **Orchestration**: LangGraph-compatible pipeline control flow.
* **Database**: PostgreSQL (Required for live operations; SQLite is legacy fallback only).
* **Scheduler**: `launchd` (macOS native) for unattended reliable execution.
* **Monitoring**: Integrated Tkinter desktop dashboard for real-time status.

---

## ⚠️ Disclaimer

This is a research and automation framework. Profitability is unproven until it survives exhaustive testing. Small capital means small absolute returns; this system is designed for discipline and proof-of-concept first.
