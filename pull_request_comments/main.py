#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module contains the main function of the repository.

@author: Cyril Obrecht
@license: MIT
@date: 2022-11-02
@version: 1.0
"""

# MIT LicenseCorrelatio
#
# Copyright (c) 2022 Correlatio
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys

from github import Github, PullRequest

gh = Github(os.getenv("GITHUB_TOKEN"))

repo = gh.get_repo(os.getenv("GITHUB_REPOSITORY"))
pr: PullRequest.PullRequest = repo.get_pulls(state="open", sort="created", head=os.getenv("GITHUB_HEAD_REF"))[0]

f_name = os.getenv("INPUT_FILENAME")

with open(f_name, "r", encoding="utf-8") as f:
    comment = f.read()

for existing in pr.get_comments():
    if existing.body == comment:
        print("The comment has been already added to the pull request.")
        sys.exit(0)

pr.create_issue_comment(comment)
