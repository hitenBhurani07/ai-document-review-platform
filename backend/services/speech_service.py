"""Minimal helpers for loading uploaded document text."""

from __future__ import annotations

from pathlib import Path


def read_text_document(file_path: str) -> str:
    """Read a text document from disk.

    Args:
        file_path: Path to a .txt file.

    Returns:
        Decoded text content.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    if path.suffix.lower() != ".txt":
        raise ValueError("Only .txt files are supported")
    return path.read_text(encoding="utf-8", errors="ignore").strip()
