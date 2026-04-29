#!/usr/bin/env python
"""Quick test to verify document loader imports correctly."""

try:
    from backend.services.speech_service import read_text_document
    print("SUCCESS: document loader imports correctly")
except Exception as e:
    print(f"ERROR: {e}")
