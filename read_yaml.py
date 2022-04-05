#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103
"""
Read Employee data to return turnover information.
This is an example Python program to read and process YAML files.
"""

import argparse
import logging.config
import os.path
import sys
from io import TextIOWrapper

from employees.employees import Employees
from utils.files import list_yamls
from utils.report import dump_employees, show_employees


def main() -> None:
    """ Example of YAML file processing. """

    __version__ = Employees.__version__
    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        usage="%(prog)s [options] path",
        description="a Python example program to show YAML processing",
        epilog="© 2014-2021 Frank H Jung mailto:frankhjung@linux.com",
    )
    parser.add_argument("-v",
                        "--verbose",
                        action="store_true",
                        help="show verbose output")
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "path",
        type=list_yamls,
        help="path to YAML files to test",
    )

    # process command line arguments
    args = parser.parse_args()
    program = parser.prog
    verbose = args.verbose
    path = args.path

    # set logger
    logging.config.fileConfig(fname="logger.properties",
                              defaults={"log_file_name": "read_yaml.log"})
    logger = logging.getLogger()

    # log at debug level if verbose flag given
    if verbose:
        logger.setLevel(logging.DEBUG)

    # show command parameters
    logger.debug("prog ........................: %s", program)
    logger.debug("verbose .....................: %s", verbose)
    logger.debug("version .....................: %s", __version__)

    # call helper function to show YAML file contents
    logger.debug("path ........................: %s", path)
    for f in path:
        with open(f, "r", encoding="UTF-8") as infile:
            logger.debug("processing file .............: %s", infile.name)
            assert isinstance(infile, TextIOWrapper)
            show_employees(infile)
            dump_employees(infile.name)


if __name__ == "__main__":
    main()
