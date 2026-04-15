# 💎 blab_gemma: The Universal Agentic OS

`blab_gemma` is a portable, high-discipline framework designed to turn any LLM (local or cloud) into a senior-level software engineer and data scientist. It provides the **Core Mandates**, **SOPs**, and **Specialized Skills** required for reproducible, asset-based development.

## 🚀 Quick Start: Bootstrapping a New Repo

> 🍏 **Mac Users:** If you are running this on a Mac with an M-series chip, please see the [Apple Silicon Installation Guide](INSTALL_APPLE_SILICON.md) for local LLM and environment optimizations.

To "install" the Agentic OS into a new project directory, run the following from the root of your target repository:

```bash
# 1. Clone the core into a temporary location
git clone https://github.com/djproc/blab_gemma /tmp/blab_gemma

# 2. Copy the Universal Core and SOPs
cp /tmp/blab_gemma/GEMINI.md .
cp -r /tmp/blab_gemma/SOPs/ .

# 3. Link the specialized skills to your Gemini CLI
# (Requires Gemini CLI v0.6.0+)
gemini extensions link /tmp/blab_gemma/skills/visual-verification
```

## 🧠 Core Components

### 1. The Universal Core (`GEMINI.md`)
The "Constitution" of the agent. It defines:
- **Security Protocols:** Credential protection and financial awareness.
- **Context Efficiency:** Turn minimization and surgical editing.
- **Execution Loops:** The mandatory Research -> Strategy -> Execution cycle.

### 2. Standard Operating Procedures (`SOPs/`)
Deterministic guides for complex tools:
- **SOP-DAGSTER-01:** Software-Defined Assets (SDA) and IO management.
- **SOP-DVC-01:** Large artifact management and GCS Data Lake integration.
- **SOP-VIZ-01:** Automated Visual QC and zero-overlap layouts.
- **SOP-PROVENANCE-01:** Broadstore `bs://` URI tracking for the scientific method.

### 3. Specialized Skills (`skills/`)
Markdown-based expert instructions that can be "activated" during a session:
- **Visual Verification:** Native multimodal inspection of generated figures.
- **Literature Search:** Graph RAG-based literature summaries.
- **Code Review:** senior-level PR analysis and diff auditing.

### 4. Core Libraries (`lib/`)
Reusable Python modules for complex logic:
- **bcite_core:** Essential methods for DOI resolution (Unpaywall), metadata fetching (Crossref), and PDF parsing (PyMuPDF).
- **broadstore_core:** Provenance engine for generating `bs://` URIs and standardized scientific markdown blocks.

## 🛠 Engineering Standards

- **Runtime:** Always use `uv` for Python environments.
- **Orchestration:** Prefer Dagster Assets over monolithic scripts.
- **Data:** Treat the local workspace as an ephemeral cache; use GCS/DVC for persistence.
- **Audit:** Every major action is logged to the central `blab-midas` infrastructure.

---
*Developed by: djproc*
*Targeted Runtimes: Gemma 4, Gemini 2.0+, Claude 3.5 Sonnet*
