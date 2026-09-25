"""
Run the whole pipeline in order:

    python scripts/pipeline.py              # everything after extraction
    python scripts/pipeline.py --extract    # also rebuild dataset.json
    python scripts/pipeline.py --skip-solve # reuse data/optimization.json

extract -> optimize -> orders -> benchmarks -> sensitivity -> pro rank -> findings -> docs -> web -> verify
"""

import argparse
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(*args):
    t0 = time.time()
    print(f"\n$ python {' '.join(args)}", flush=True)
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)
    print(f"  done in {time.time() - t0:.0f}s", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--extract", action="store_true")
    parser.add_argument("--skip-solve", action="store_true")
    parser.add_argument("--iterations", default="24")
    args = parser.parse_args()
    if args.extract:
        run("scripts/extract.py")
    if not args.skip_solve:
        run("scripts/optimize.py", "--iterations", args.iterations)
    run("scripts/order_all.py")
    run("scripts/benchmarks.py")
    run("scripts/sensitivity.py")
    run("scripts/pro_rank.py")
    run("scripts/findings.py")
    run("scripts/docs_gen.py")
    run("scripts/export_web.py")
    run("verify/test_model.py")
    run("verify/check_outputs.py", "--deep")


if __name__ == "__main__":
    main()
