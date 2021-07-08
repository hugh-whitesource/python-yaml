#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Read Employee data to return turnover information.
This is a example Python program to read and process YAML files.
"""

import argparse
import logging
import os.path
import sys

from employees.employees import Employees
from utils.report import dump_employees, show_employees

if __name__ == "__main__":

    __version__ = Employees.__version__
    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        usage="%(prog)s [options] infile",
        description="a Python example program to show YAML processing",
        epilog="© 2014-2021 Frank H Jung mailto:frankhjung@linux.com",
    )
    parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType("r"),
        default="tests/test.yaml",
        help="alternate YAML file to test",
    )
    parser.add_argument("-v", "--verbose", help="show verbose output")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )

    # process command line arguments
    args = parser.parse_args()
    program = parser.prog
    infile = args.infile
    verbose = args.verbose

    # set logger
    logging.basicConfig(
        format="%(asctime)s %(message)s",
        level=logging.DEBUG if verbose else logging.INFO,
    )
    logger = logging.getLogger(__name__)

    # show command parameters
    logger.debug("infile ......................: %s", infile.name)
    logger.debug("prog ........................: %s", program)
    logger.debug("verbose .....................: %s", verbose)
    logger.debug("version .....................: %s", __version__)

    # call helper function to log file contents
    show_employees(infile)
    dump_employees(infile.name)

    sys.exit(0)
