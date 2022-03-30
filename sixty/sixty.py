# -*- coding: utf-8 -*-
"""
Simple python inteface for SIXTE/SIMPUT

@author: A. Ruiz
"""
import logging
import os
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)


if "SIXTE" not in os.environ:
    raise ImportError("SIXTE has not been initialized in your system!")

# We have to redirect the HEADAS output, otherwise SIXTE tasks fail
os.environ["HEADASPROMPT"] = "/dev/null"

_sixte_dir = Path(os.environ["SIXTE"])
_simput_dir = Path(os.environ["SIMPUT"])

_sixte_bin_dir = _sixte_dir.joinpath("bin")
_simput_bin_dir = _simput_dir.joinpath("bin")

_sixte_binaries = [f.name for f in _sixte_bin_dir.glob("*")]
_sixte_binaries += [f.name for f in _simput_bin_dir.glob("*")]


class SixtyError(RuntimeError):
    pass


def _check_task(task):
    if task not in _sixte_binaries:
        raise ValueError(f"Unknown task: {task}")


def _parse_arguments(kwargs):
    return [f'{key}={value}' for key, value in kwargs.items()]
    
    
def _run_command(task, args):
    try:
        logger.info(f"Running {task} {' '.join(args)}")
        output = subprocess.check_output([task] + args, stderr=subprocess.STDOUT)
        logger.info(output.decode())

    except subprocess.CalledProcessError as e:
        logger.error(f"Task {task} failed with status {e.returncode}")
        logger.error(e.output.decode())
        raise SixtyError("Error running SIXTE. Check log for details.")


def run(task, **kwargs):
    _check_task(task)
    args = _parse_arguments(kwargs)
    _run_command(task, args)
