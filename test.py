#!/usr/bin/env python
#-*-coding=utf-8-*-

from github import Github
PAT = "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"
gh = Github(PAT)
# repo = gh.get_repo('commons-stack/voteable-issues')
repo = gh.get_repo('commons-stack/comms')

bs = repo.get_branches()
print(bs.totalCount)
# print(repo.get_branch('master'))