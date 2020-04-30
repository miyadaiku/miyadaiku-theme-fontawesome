#!/usr/bin/env python3

import pathlib
from miyadaiku import setuputils

DIR = pathlib.Path(__file__).resolve().parent


srcdir = DIR / 'node_modules/@fortawesome/fontawesome-free'
destdir = DIR / 'miyadaiku_theme_fontawesome/externals'
copy_files = [
    [srcdir / 'js', ['all.js', 'all.min.js'], destdir / 'js/'],
]

setuputils.copyfiles(copy_files)
