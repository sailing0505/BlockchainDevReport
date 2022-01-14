#!/usr/bin/env python
#-*-coding=utf-8-*-

from github import Github
PAT = "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"
gh = Github(PAT)
# repo = gh.get_repo('commons-stack/voteable-issues')
repo = gh.get_repo('dappnode/DAppNodePackage-grin')

bs = repo.get_branches()
print(bs.totalCount)
# print(repo.get_branch('master'))