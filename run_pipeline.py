"""Standalone runner for the document analysis pipeline."""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional

from backend.services.pipeline_service import analyze_document
from backend.services.speech_service import read_text_document
from utils.file_utils import ensure_directory


LOGGER = logging.getLogger("document_review_pipeline")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the document analysis pipeline on raw text or a .txt file.",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", type=str, help="Business document text input to process.")
    group.add_argument("--file", type=Path, help="Path to a .txt document.")

    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to write the JSON result. Defaults to stdout only.",
    )
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Print compact JSON instead of pretty-formatted JSON.",
    )
    return parser


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def _validate_file_path(file_path: Path) -> Path:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    if not file_path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    if file_path.suffix.lower() != ".txt":
        raise ValueError("Only .txt files are supported.")
    return file_path


def _run_pipeline(text: Optional[str] = None, file_path: Optional[Path] = None) -> Dict[str, Any]:
    if text is not None:
        LOGGER.info("Running text analysis")
        return analyze_document(text)

    if file_path is not None:
        validated_path = _validate_file_path(file_path)
        LOGGER.info("Running document analysis for %s", validated_path)
        document_text = read_text_document(str(validated_path))
        return analyze_document(document_text)

    raise ValueError("Either text or file input must be provided.")


def _write_output(output_path: Path, payload: Dict[str, Any]) -> None:
    ensure_directory(output_path.parent)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> int:
    _configure_logging()
    parser = _build_parser()
    args = parser.parse_args()

    try:
        result = _run_pipeline(text=args.text, file_path=args.file)
    except Exception as exc:
        LOGGER.error("Pipeline failed: %s", exc)
        return 1

    json_kwargs = {"ensure_ascii": False}
    if not args.compact:
        json_kwargs["indent"] = 2

    rendered = json.dumps(result, **json_kwargs)
    print(rendered)

    if args.output:
        try:
            _write_output(args.output, result)
            LOGGER.info("Saved output to %s", args.output)
        except Exception as exc:
            LOGGER.error("Failed to write output file: %s", exc)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
