import os
import sys

def create_blueprint(project_name):
    # Standard backtick placeholder to avoid breaking Markdown rendering
    bt = "```"
    
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
        "README.md": f"# {project_name}\n"
        "### A Standard for Auditable Agentic Systems\n"
        "Built using **Documentation-Driven Orchestration (DDO)**.\n\n"
        "## 🛡️ The Reliability Stack\n"
        "* **AGENTS.md**: System Identity & Roles.\n"
        "* **CONSTRAINTS.md**: Hard Guardrails & CFO Gates.\n"
        "* **DECISION_LOG.md**: System Memory.\n"
        "* **SKILL.md**: Verified Capability Playbooks.\n"
        "* **SCHEMA.md**: Persistence Contracts (PostgreSQL).\n"
        "* **PROGRESS.txt**: Atomic State Tracking.\n",

        "AGENTS.md": "# AGENTS.md\n"
        "### System Identity & Orchestration\n"
        "* **Architect (Human)**: Primary Authority.\n"
        "* **Lead Junior (AI)**: Implementation & Cost Monitoring.\n\n"
        "**Persona**: Senior Developer Lead.\n"
        "**Tone**: Grounded, data-backed, brutally honest.\n",

        "CONSTRAINTS.md": "# CONSTRAINTS.md\n"
        "### The Hard Guardrails\n"
        "* **No Stealth Execution**: All state-modifying calls require a safety gate.\n"
        "* **Vibe Budget**: Max $1.00 USD per individual research/execution loop.\n"
        "* **Persistence**: PostgreSQL is the mandatory source of truth.\n",

        "DECISION_LOG.md": f"# DECISION_LOG.md\n"
        "### System Memory & Audit Trail\n"
        "* **[2026-03-28] Infrastructure Setup**: \n"
        "    - **Decision**: Implemented PostgreSQL-first schema with automated cost-ledger.\n"
        "    - **Why**: To maintain professional-grade audit trails.\n",

        "SKILL.md": "# SKILL.md\n"
        "### Verified Capability Playbook\n\n"
        "**Skill: Cost-Aware Inference**\n"
        "* **Goal**: Track token consumption and USD spend per workflow.\n"
        "* **Logic**: Intercept LLM response metadata and calculate cost vs. budget.\n"
        "* **Persistence**: Write to `cost_ledger` table as defined in `SCHEMA.md`.\n",

        "SCHEMA.md": "# SCHEMA.md\n"
        "### Database Contract (PostgreSQL)\n\n"
        f"{bt}sql\n"
        "-- 1. Cost Ledger: Track every USD spent on inference\n"
        "CREATE TABLE IF NOT EXISTS cost_ledger (\n"
        "    id SERIAL PRIMARY KEY,\n"
        "    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,\n"
        "    workflow_id UUID NOT NULL,\n"
        "    agent_role VARCHAR(50),\n"
        "    model_id VARCHAR(100),\n"
        "    prompt_tokens INTEGER,\n"
        "    completion_tokens INTEGER,\n"
        "    estimated_cost_usd DECIMAL(10, 6),\n"
        "    metadata JSONB\n"
        ");\n\n"
        "-- 2. Audit Log: Track state-modifying decisions\n"
        "CREATE TABLE IF NOT EXISTS audit_log (\n"
        "    id SERIAL PRIMARY KEY,\n"
        "    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,\n"
        "    decision_type VARCHAR(50),\n"
        "    logic_source VARCHAR(100),\n"
        "    outcome VARCHAR(20),\n"
        "    summary TEXT,\n"
        "    payload JSONB\n"
        ");\n"
        f"{bt}\n",

        "PROGRESS.txt": "STATUS: Project Initialized. Current Session Cost: $0.00.",

        ".github/workflows/agentic-audit.yml": "name: Agentic Constraint Audit\n"
        "on: [push, pull_request]\n\n"
        "jobs:\n"
        "  audit:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - uses: actions/checkout@v4\n"
        "      - name: Run Reliability Stack Audit\n"
        "        uses: github/agentic-audit-action@v1\n"
        "        with:\n"
        "          agents_file: 'AGENTS.md'\n"
        "          constraints_file: 'CONSTRAINTS.md'\n"
        "          decision_log: 'DECISION_LOG.md'\n"
        "          fail_on_violation: true\n"
    }

    # 3. Write the Files
    for filename, content in files.items():
        with open(filename, "w") as f:
            f.write(content)
    
    print(f"✅ Success: '{project_name}' scaffolded with the Reliability Stack.")

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "agentic-blueprint-repo"
    create_blueprint(name)
