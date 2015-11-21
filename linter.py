#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ulrich Eck
# Copyright (c) 2015 Ulrich Eck
#
# License: MIT
#

"""This module exports the Awchecker plugin class."""

from io import StringIO
from SublimeLinter.lint import PythonLinter, util


class Awchecker(PythonLinter):
    """Provides an interface to awchecker."""

    syntax = ('latex', 'latexing', )
    selectors = {}

    cmd = 'awchecker'
    error_stream = util.STREAM_STDOUT
    regex = (
        r'^(?P<line>\d+):(?P<col>\d+) '
        r'(?:(?P<error>Error)|(?P<warning>Warning)) '
        r'(?P<message>.+)'
    )

    line_col_base = (1, 0)
    config_file = ()
    defaults = {}
    inline_overrides = ('nowarn', 'erroron')
    comment_re = r'\s*%'