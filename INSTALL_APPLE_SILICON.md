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

## 2. Local LLM Engine (Ollama / MLX)

To run Gemma locally on your Mac, you have two primary options:

### Option A: Ollama (Recommended for ease of use)
Ollama natively supports Apple Silicon GPU acceleration.

```bash
# Install Ollama via Homebrew
brew install --cask ollama

# Start the Ollama application from your Applications folder, then pull Gemma:
# (Note: Replace with the specific gemma4 tag when available)
ollama run gemma:7b 
```

### Option B: Apple MLX (Recommended for maximum performance/customization)
If you want to run Gemma directly in Python using Apple's MLX framework (which is heavily optimized for Apple Silicon):

```bash
# First, ensure you are in an initialized uv project:
uv init
# Then add the MLX dependencies:
uv add mlx mlx-lm
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
