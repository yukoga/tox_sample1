# -*- coding: utf-8 -*-

# Copyright 2018 yukoga. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import setuptools
import tox_sample1

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name=tox_sample1.__name__,
    version=tox_sample1.__version__,
    license='Apache License 2.0',
    author='Yutaka Koga',
    author_email='yukoga@gmail.com',
    description='Just sample project to try tox.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yukoga/tox_sample1',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: Apache License 2.0',
        'Operating System :: OS Independent',
    ],
)