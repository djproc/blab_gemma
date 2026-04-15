#!/usr/bin/env bash
# install_gemma_core.sh
# Bootstraps the blab_gemma agentic framework into the current directory.

set -e

SOURCE_DIR="$(dirname "$(dirname "$(readlink -f "$0")")")"
TARGET_DIR=$(pwd)

echo "💎 Bootstrapping blab_gemma Agentic OS into $TARGET_DIR"

if [ "$SOURCE_DIR" = "$TARGET_DIR" ]; then
    echo "❌ Error: Cannot install into the source directory itself."
    exit 1
fi

echo "-> Copying GEMINI.md (Core Mandates)..."
cp "$SOURCE_DIR/GEMINI.md" "$TARGET_DIR/GEMINI.md"

echo "-> Copying Standard Operating Procedures (SOPs)..."
mkdir -p "$TARGET_DIR/SOPs"
cp -r "$SOURCE_DIR/SOPs/"* "$TARGET_DIR/SOPs/"

echo "-> Linking Skills to Gemini CLI..."
if command -v gemini &> /dev/null; then
    echo "   Linking extension: blab-gemma-skills"
    gemini extensions link "$SOURCE_DIR/gemini_extension" || echo "   ⚠️ Failed to link blab-gemma-skills"
else
    echo "⚠️ Gemini CLI not found in PATH. Skipping skill linking."
fi

echo "✅ Bootstrapping complete! Your repository is now Gemma 4 ready."
