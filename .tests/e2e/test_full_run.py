import csv
import os
import pytest
import shutil
import subprocess as sp
import tempfile
from pathlib import Path


@pytest.fixture
def setup():
    temp_dir = tempfile.mkdtemp()

    reads_fp = os.path.abspath(".tests/data/reads/")

    project_dir = os.path.join(temp_dir, "project/")

    sp.check_output(["sunbeam", "init", "--data_fp", reads_fp, project_dir])

    yield temp_dir, project_dir

    shutil.rmtree(temp_dir)


@pytest.fixture
def run_sunbeam(setup):
    temp_dir, project_dir = setup

    # Run the test job.
    sp.check_output(
        [
            "sunbeam",
            "run",
            "--profile",
            project_dir,
            "all_seeker",
            "--directory",
            temp_dir,
        ]
    )

    output_fp = os.path.join(project_dir, "sunbeam_output")

    bfrag_out_fp = os.path.join(output_fp, "virus/seeker/PCMP_dummybfragilis.tsv")

    benchmarks_fp = os.path.join(project_dir, "stats/")

    yield bfrag_out_fp, benchmarks_fp


def test_full_run(run_sunbeam):
    bfrag_out_fp, benchmarks_fp = run_sunbeam

    # Check output
    assert os.path.exists(bfrag_out_fp)

    with open(bfrag_out_fp, "r") as f:
        assert "" == f.readlines()
