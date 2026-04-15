# 🍏 Apple Silicon (M1/M2/M3/M4) Installation Guide

Running `blab_gemma` and local LLMs (like Gemma 4) on Apple Silicon requires specific setups to leverage the unified memory and Metal Performance Shaders (MPS) of the M-series chips.

## 1. System Prerequisites

We use **Homebrew** as the base package manager and **uv** for blazing-fast Python environments.

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install uv (Python package manager) and git
brew install uv git
```

## 2. Local LLM Engine Options

To run Gemma on your Mac and leverage the **Agentic OS**, you have three primary paths:

### Path A: The Easiest Way (Ollama)
Ollama is a lightweight engine that manages model weights and automatically uses your Mac's GPU.

```bash
# Install Ollama via Homebrew
brew install --cask ollama

# Start the Ollama application, then pull and run Gemma 4:
ollama run gemma4
```

### Path B: The Performance Way (Apple MLX)
Since you already ran `uv add mlx mlx-lm`, you can run Gemma directly from your terminal using Apple's high-performance framework.

```bash
# Run a quick generation:
uv run python -m mlx_lm.generate --model google/gemma-4-it --prompt "Hello, I am running on Apple Silicon. Who are you?"
```
*Note: The first time you run this, it will download several GBs of weights from Hugging Face into your `~/.cache/huggingface` folder.*

### Path C: The "Agentic" Way (Gemini CLI Bridge)
To make your local Gemma instance "aware" of the **`GEMINI.md`** mandates and skills we just installed, you need to point the Gemini CLI at your local model using a proxy like **LiteLLM**.

```bash
# 1. Install the bridge
uv add litellm

# 2. Start the bridge (in a separate terminal pane)
uv run litellm --model ollama/gemma4
# This creates a "fake" Google Gemini API at http://0.0.0.0:4000

# 3. Point the Gemini CLI at your Mac
export GEMINI_API_BASE="http://0.0.0.0:4000"

# 4. Now run your commands! The CLI will use your local Gemma.
gemini "Review the current directory and check for SOP compliance."
```

## 3. Bootstrapping the Agentic OS

Navigate to your target project folder and run the bootstrap script. `uv` natively handles downloading the correct `arm64` wheels for Mac (so libraries like `pandas` and `pymupdf` will run natively, not via Rosetta).

```bash
# 1. Clone the core
git clone https://github.com/djproc/blab_gemma /tmp/blab_gemma

# 2. Run the bootstrap
/tmp/blab_gemma/scripts/install_gemma_core.sh
```

## 4. Mac-Specific Environment Variables (Optional)

If your Dagster pipelines or testing scripts utilize **PyTorch** for local ML inference, you should enable the Metal (MPS) backend to use the Mac's GPU.

Add these to your `~/.zshrc`:
```bash
# Enable PyTorch Metal Performance Shaders (MPS) fallback for missing ops
export PYTORCH_ENABLE_MPS_FALLBACK=1

# Optional: Limit thread count for Polars/Pandas to prevent CPU thrashing on Apple Silicon
export POLARS_MAX_THREADS=$(sysctl -n hw.ncpu)
```

Apply the changes:
```bash
source ~/.zshrc
```

## 5. Verifying the Setup

To verify everything is running natively on Apple Silicon:
1. Run `uv run python -c "import platform; print(platform.machine())"`. It should output `arm64` (not `x86_64`).
2. Open **Activity Monitor**, run your local LLM or Dagster pipeline, and check the "Kind" column. It should say "Apple" (native), not "Intel" (Rosetta translation).
