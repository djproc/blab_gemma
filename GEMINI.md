# Agentic Core Mandates

This file defines the foundational mandates, operational protocols, and engineering standards. It is designed to ensure safe, efficient, and reproducible operations for local and cloud-native LLMs.

## 📚 1. Context Hierarchy

Agents must synchronize with the following hierarchy before executing modifications:
1.  **.cursorrules (The Guardrails):** Strict security, tooling, and safety constraints.
2.  **AGENTS.md (The Manual):** Architectural overview of the current workspace.
3.  **GEMINI.md (This File):** Global agentic policies and mandated operational loops.

## 🛡️ 2. Core Mandates

### Security & Integrity
- **Credential Zero-Tolerance:** Never log, print, or commit secrets, API keys, or `.env` files.
- **Source Control:** Do not stage or commit changes unless explicitly requested. Always review `git diff` before proposing a commit.
- **Financial Awareness:** Proactively warn the user before launching high-cost resources (GPUs, massive batch arrays).

### Context Efficiency
- **Turn Minimization:** Accomplish tasks in the fewest possible turns by parallelizing tool calls (searching, reading, and executing).
- **Surgical Edits:** Use targeted `replace` calls. Do not rewrite files unless they require full refactoring.

## ⚙️ 3. Tooling & Environment Standards

- **Runtime Management:** Always use `uv` for Python virtual environments. 
- **Shell Safety:** Explain the purpose and impact of any file-system modifying command before execution.
- **Visual Verification:** For any visual artifact generation, the agent MUST use multimodal capabilities to verify output quality before completion.

## 🔄 4. The Execution Lifecycle

### Phase 1: Research
- Validate all assumptions using `grep_search` and `read_file`.
- **Empirical Reproduction:** For bug fixes, create a reproduction script to confirm the failure state before applying a fix.

### Phase 2: Strategy & Finality
- Propose a concise plan.
- **Validation is the only path to finality.** A task is not complete until behavioral correctness is verified via automated tests or materialization checks.

## 📜 5. Standard Operating Procedures (SOPs)

### SOP-DAGSTER-01: Asset-Based Orchestration
When using Dagster to orchestrate workflows, adhere to the "Software-Defined Asset" (SDA) philosophy:

1.  **Define Assets, Not Tasks:** Focus on the *data result* (@asset) rather than the *process* (@op). Every script should represent a state in the data lifecycle.
2.  **IO Management:** Use Dagster IO Managers (e.g., GCS/S3/Parquet) to decouple business logic from storage. Assets should return objects (DataFrames, Arrays), not write to hardcoded paths.
3.  **Atomic Materialization:** 
    - Use `AssetSelection` to run specific sub-graphs. 
    - Verify successful materialization via the Dagster UI/CLI before reporting a step as finished.
4.  **Metadata Tracking:** Always attach metadata to asset materializations (e.g., `metadata={"row_count": len(df), "preview": df.head().to_html()}`).
5.  **Local Development:** Run `dagster dev` to test assets locally. Ensure `DAGSTER_HOME` is set and `workspace.yaml` is correctly configured before execution.

### SOP-DATA-01: Large Artifact Management (DVC)
- **Files >100MB:** NEVER commit to Git.
- **Protocol:** Use `dvc add` for local outputs and `dvc import-url` for cloud-native assets.
- **Synchronization:** Always `dvc push` after a successful pipeline run to ensure the remote "Data Lake" is the source of truth.

### SOP-VIZ-01: Automated Visual QC
- **Zero-Overlap Policy:** Figures must be designed for clarity.
- **Verification:** Use the agent's vision capabilities to "look" at generated images. Check for:
    - Legend-to-Plot collision.
    - Cut-off axis labels.
    - Data density issues (over-plotting).

---
*Status: Initialized for Universal Portability*
