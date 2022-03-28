# -*- coding: utf-8 -*-
"""
Simple python inteface for SIXTE/SIMPUT

@author: A. Ruiz
"""
import os
import subprocess
from pathlib import Path

from astropy import log


# We have to redirect the HEADAS output, otherwise SIXTE tasks fail
os.environ["HEADASPROMPT"] = "/dev/null"

_sixte_dir = Path(os.environ["SIXTE"])
_simput_dir = Path(os.environ["SIMPUT"])

_sixte_bin_dir = _sixte_dir.joinpath("bin")
_simput_bin_dir = _simput_dir.joinpath("bin")

_sixte_binaries = [f.name for f in _sixte_bin_dir.glob("*")]
_sixte_binaries += [f.name for f in _simput_bin_dir.glob("*")]


def _check_task(task):
    if task not in _sixte_binaries:
        raise ValueError(f"Unknown task: {task}")


def _parse_arguments(kwargs):
    return [f'{key}={value}' for key, value in kwargs.items()]
    
    
def _run_command(task, args):
    try:
        log.info(f"Running {task} {' '.join(args)}")
        output = subprocess.check_output([task] + args, stderr=subprocess.STDOUT)
        log.info(output.decode())

    except subprocess.CalledProcessError as e:
        log.error(f"Task {task} failed with status {e.returncode}")
        log.error(e.output.decode())


def run(task, **kwargs):
    _check_task(task)
    args = _parse_arguments(kwargs)
    _run_command(task, args)
