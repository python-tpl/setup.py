# -*- coding:utf-8 -*-

import os

import delegator
from candy_prompt.prompt import *


def construct():
    history = os.path.join(os.path.expanduser('~'), '.templates', 'tpl.history')
    git_remote_url = delegator.run("git remote -v | head -n 1 | awk '{{print $2}}'").out.strip()
    git_last_tag = delegator.run("git describe --abbrev=0 --tags| xargs echo").out.strip()
    git_tags = [tag.strip() for tag in delegator.run("git tag -l").out.split('\n') if tag.strip()]
    git_last_commit_author = delegator.run("git log -1 --pretty=tformat:%aN").out.strip()
    git_commit_authors = [author.strip() for author in
                          delegator.run("git log --pretty=tformat:%aN | sort -u").out.split('\n') if author.strip()]
    requirements_file = open(os.path.join(os.getcwd(), 'requirements.txt'))
    requirements = [r.strip() for r in requirements_file if r.strip()]
    readme = open(os.path.join(os.getcwd(), 'README.md')).read()
    licenses = ['Apache License 2.0',
                'MIT License',
                'BSD 2-clause "Simplified" License',
                'BSD 3-clause "New" or "Revised" License',
                'Eclipse Public License 1.0',
                'GNU General Public License v2.0',
                'GNU Lesser General Public License v2.1',
                'GUN General Public License V3.0',
                'GNU Affero General Public License v3.0',
                'GNU Lesser General Public License v3.0',
                'Mozilla Public License 2.0']
    classifiers_file = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'classifiers'))
    classifier_options = [c.strip() for c in classifiers_file if c.strip()]
    res = {
        'name': prompt('Name: ', default=os.getcwd().split('/')[-1], history=history),
        'version': prompt_list('Version: ', default=git_last_tag, completions=git_tags, history=history),
        'description': prompt('Description: ', history=history),
        'readme': readme,
        'author': prompt_list('Author: ', default=git_last_commit_author, completions=git_commit_authors,
                              history=history),
        'url': prompt('Project URL: ', default=git_remote_url, history=history),
        'requirements': requirements,
        'console_scripts': prompt('Console Scripts: ', type='LIST', history=history),
        'license': prompt_list('License: ', default='MIT License', completions=licenses, history=history)
    }
    classifiers = []
    while True:
        input = prompt_list('Classifier: ', completions=classifier_options)
        if input == 'q':
            break
        classifiers.append(input)
    res.update({'classifiers': classifiers})
    return res
