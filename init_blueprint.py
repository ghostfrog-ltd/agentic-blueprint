import os
import sys

def create_blueprint(project_name):
    # 1. Create the Directory Structure
    paths = [
        project_name,
        os.path.join(project_name, ".github", "workflows")
    ]
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
    
    os.chdir(project_name)

    # 2. Define the Reliability Stack Templates
    files = {
        "README.md": """# {project_name}
### A Standard for Auditable Agentic Systems
Built using **Documentation-Driven Orchestration (DDO)** to ensure deterministic AI behavior.

## 🛡️ The Reliability Stack
* **AGENTS.md**: System Identity & Roles.
* **CONSTRAINTS.md**: Hard Guardrails & CFO Gates.
* **DECISION_LOG.md**: System Memory.
* **SKILL.md**: Verified Capability Playbooks.
* **PROGRESS.txt**: Atomic State Tracking.
""",
        "AGENTS.md": """# AGENTS.md
### System Identity & Orchestration
* **Architect (Human)**: Primary Authority.
* **Lead Junior (AI)**: Implementation & Cost Monitoring.

**Persona**: Senior Developer Lead.
**Tone**: Grounded, data-backed, brutally honest.
**Directive**: Challenge the Architect if a "vibe" is inefficient or violates **CONSTRAINTS.md**.
""",
        "CONSTRAINTS.md": """# CONSTRAINTS.md
### The Hard Guardrails
* **No Stealth Execution**: All state-modifying calls require a safety gate.
* **Vibe Budget**: Max $1.00 USD per individual research/execution loop.
* **CFO Gate Rules**: 
    - Max Notional: $10.00 (or project equivalent)
    - Max Slots: 1 active execution at a time.
* **Persistence**: PostgreSQL is the mandatory source of truth.
""",
        "DECISION_LOG.md": """# DECISION_LOG.md
### System Memory & Audit Trail
* **[2026-03-28] Infrastructure Setup**: 
    - **Decision**: Implemented Workflow-Based Cost Accounting via SKILL.md.
    - **Why**: To prevent "AI Bloom" from generating unmonitored API expenses.
""",
        "SKILL.md": """# SKILL.md
### Verified Capability Playbook

**Skill: Cost-Aware Inference**
* **Goal**: Track token consumption and USD spend per "vibe" (workflow).
* **Logic**: 
    1. Intercept LLM API response metadata (`usage` block).
    2. Extract `input_tokens`, `output_tokens`, and `model_id`.
    3. Calculate cost using current provider rate-cards stored in `cost_ledger`.
* **Persistence**: Log `(workflow_id, model, tokens, estimated_cost_usd)` to **PostgreSQL**.
* **Safety Check**: If cumulative workflow cost > $1.00, trigger **HALT** in `PROGRESS.txt`.

**Skill: Agentic Audit**
* **Goal**: Verify code changes against `CONSTRAINTS.md`.
* **Logic**: Automated scan of PR diffs for "Hard No" patterns (e.g., unauthorized API calls).
""",
        "PROGRESS.txt": "STATUS: Project Initialized. Current Session Cost: $0.00.",
        ".github/workflows/agentic-audit.yml": """name: Agentic Constraint Audit
on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Reliability Stack Audit
        uses: github/agentic-audit-action@v1 # 2026 DDO Standard
        with:
          agents_file: 'AGENTS.md'
          constraints_file: 'CONSTRAINTS.md'
          decision_log: 'DECISION_LOG.md'
          fail_on_violation: true
"""
    }

    # 3. Write the Files
    for filename, content in files.items():
        with open(filename, "w") as f:
            f.write(content.format(project_name=project_name))
    
    print(f"✅ Success: '{project_name}' initialized with the full Reliability Stack.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        create_blueprint("agentic-blueprint-repo")
    else:
        create_blueprint(sys.argv[1])
