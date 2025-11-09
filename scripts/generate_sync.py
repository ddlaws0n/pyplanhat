#!/usr/bin/env python3
"""Generate synchronous code from async source using unasync."""

import subprocess
import sys
from pathlib import Path


def main() -> None:
    """Run unasync to generate sync code from async source."""

    project_root = Path(__file__).parent.parent

    # Transformation rules for unasync
    rules = [
        ("/_async/", "/_sync/"),
        ("async def ", "def "),
        ("await ", ""),
        ("AsyncClient", "Client"),
        ("AsyncPyPlanhat", "PyPlanhat"),
        ("@pytest.mark.asyncio", ""),
        ("__aenter__", "__enter__"),
        ("__aexit__", "__exit__"),
        ("aclose", "close"),
    ]

    # Build unasync command for source code
    src_cmd = [
        "python",
        "-m",
        "unasync",
        str(project_root / "src" / "pyplanhat" / "_async"),
        "--outdir",
        str(project_root / "src" / "pyplanhat" / "_sync"),
    ]

    for old, new in rules:
        src_cmd.extend(["--replace", f"{old}:{new}"])

    print("Generating sync source code...")
    result = subprocess.run(src_cmd)

    if result.returncode != 0:
        print("Failed to generate sync source code", file=sys.stderr)
        sys.exit(1)

    # Build unasync command for tests (if they exist)
    tests_async = project_root / "tests" / "_async"
    if tests_async.exists():
        tests_cmd = [
            "python",
            "-m",
            "unasync",
            str(tests_async),
            "--outdir",
            str(project_root / "tests" / "_sync"),
        ]

        for old, new in rules:
            tests_cmd.extend(["--replace", f"{old}:{new}"])

        print("Generating sync tests...")
        result = subprocess.run(tests_cmd)

        if result.returncode != 0:
            print("Failed to generate sync tests", file=sys.stderr)
            sys.exit(1)

    print("✓ Sync code generation complete!")
    print("\nNext steps:")
    print("  1. Run: uv run ruff format src/pyplanhat/_sync/ tests/_sync/")
    print("  2. Run: uv run ruff check src/pyplanhat/_sync/ tests/_sync/ --fix")
    print("  3. Run: uv run pytest tests/_sync/ -v")


if __name__ == "__main__":
    main()
