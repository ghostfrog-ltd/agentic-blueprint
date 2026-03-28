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
This project uses **Documentation-Driven Orchestration (DDO)** to ensure deterministic AI behavior.

## 🛡️ The Reliability Stack
* **AGENTS.md**: System Identity & Roles.
* **CONSTRAINTS.md**: Hard Guardrails & CFO Gates.
* **DECISION_LOG.md**: Architectural Memory.
* **SKILL.md**: Verified Capability Playbooks.
* **PROGRESS.txt**: Atomic State Tracking.
""",
        "AGENTS.md": """# AGENTS.md
### System Identity & Orchestration Standard
* **Architect (Human)**: Primary Authority.
* **Lead Junior (AI)**: Implementation & Initial Auditing.

**Persona**: Senior Developer Lead.
**Tone**: Grounded, data-backed, brutally honest.
**Directive**: Challenge the Architect if premises lack data or violate **CONSTRAINTS.md**.
""",
        "CONSTRAINTS.md": """# CONSTRAINTS.md
### The Hard Guardrails
* **No Stealth Execution**: All state-modifying calls require a deterministic safety gate.
* **No Credential Exposure**: Use environment variables only.
* **CFO Gate Rules**: 
    - Max Notional: $10.00
    - Max Slots: 1
* **Postgres-First**: SQLite is prohibited for live operations.
""",
        "DECISION_LOG.md": """# DECISION_LOG.md
### System Memory & Audit Trail
* **[2026-03-28] Initialized Blueprint**: 
    - **Decision**: Adopted the AGENTS.md standard for all automated steering.
    - **Why**: To prevent "AI Bloom" and ensure auditable results.
""",
        "SKILL.md": """# SKILL.md
### Verified Capability Playbook
* **Skill: Agentic Audit**:
    - **Goal**: Verify that new code does not violate `CONSTRAINTS.md`.
    - **Safety Check**: Compare PR diff against the "Hard Nos" list.
""",
        "PROGRESS.txt": "STATUS: Project Initialized. Waiting for first tick.",
        ".github/workflows/agentic-audit.yml": """name: Agentic Constraint Audit
on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Reliability Stack Audit
        uses: github/agentic-audit-action@v1 # 2026 Industry Standard for DDO
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
    
    print(f"✅ Success: '{project_name}' scaffolded with the Reliability Stack and Agentic Audit.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        create_blueprint("my-agentic-project")
    else:
        create_blueprint(sys.argv[1])
