import os
import sys

def create_blueprint(project_name):
    # 1. Create the Directory
    if os.path.exists(project_name):
        print(f"🛑 Error: Directory '{project_name}' already exists.")
        sys.exit(1)
    
    os.makedirs(project_name)
    os.chdir(project_name)

    # 2. Define the Reliability Stack Templates
    files = {
        "README.md": """# {project_name}

### A Standard for Auditable Agentic Systems
This project uses the **agentic-blueprint** framework and **Documentation-Driven Orchestration (DDO)** to ensure deterministic AI behavior.

## 🛡️ The Reliability Stack
* **AGENTS.md**: System Identity & Roles.
* **CONSTRAINTS.md**: Hard Guardrails & CFO Gates.
* **DECISION_LOG.md**: Architectural Memory.
* **SKILL.md**: Verified Capability Playbooks.
* **PROGRESS.txt**: Atomic State Tracking.
""",
        "AGENTS.md": """# AGENTS.md
### System Identity & Orchestration
* **Architect (Human)**: Primary Authority.
* **Lead Junior (AI)**: Implementation & Initial Auditing.

**Persona**: Senior Developer Lead.
**Tone**: Grounded, data-backed, brutally honest.
**Directive**: Challenge the Architect if premises lack data or violate constraints.
""",
        "CONSTRAINTS.md": """# CONSTRAINTS.md
### The Hard Guardrails
* **No Stealth Execution**: All state-modifying calls require a safety gate.
* **No Credential Exposure**: Use environment variables only.
* **CFO Gate**: 
    * Notional Limit: [Define e.g., $10.00]
    * Concurrency Limit: [Define e.g., 1 slot]
* **Postgres-First**: SQLite is for local bootstrap only.
""",
        "SKILL.md": """# SKILL.md
### Verified Capability Playbook
* **Template**: 
    * Goal | Inputs | Deterministic Logic | Safety Checks | Logging
* **Verified Skills**:
    * [List verified skills here]
""",
        "DECISION_LOG.md": """# DECISION_LOG.md
### System Memory & Audit Trail
* **[YYYY-MM-DD] Initialized Reliability Stack**: 
    * **Decision**: Use agentic-blueprint standard for all development.
    * **Why**: To move from probabilistic vibes to deterministic engineering.
""",
        "PROGRESS.txt": "STATUS: Project Initialized. Waiting for first tick."
    }

    # 3. Write the Files
    for filename, content in files.items():
        with open(filename, "w") as f:
            f.write(content.format(project_name=project_name))
    
    print(f"✅ Success: '{project_name}' initialized with the Reliability Stack.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python init_blueprint.py <project_name>")
    else:
        create_blueprint(sys.argv[1])
