#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from setuptools import setup, Extension


extra_link_args = []
if sys.platform == 'darwin':
    extra_link_args.extend([
        '-framework', 'CoreFoundation',
        '-framework', 'CoreGraphics',
        '-framework', 'CoreText',
        '-framework', 'CoreServices',
    ])


module = Extension(
    'emoji',
    sources=['src/emoji.c'],
    include_dirs = ['include'],
    library_dirs = ['lib'],
    libraries= ['z', 'skia', 'emoji'],
    extra_compile_args=[
        '-std=c11',
        '-Wall',
        '-Wextra',
    ],
    extra_link_args=extra_link_args,
    language='c11'
)

setup(
    name = 'libemoji',
    version = '1.0',
    description = '',
    test_suite = 'test.emoji',
    ext_modules = [module]
)
