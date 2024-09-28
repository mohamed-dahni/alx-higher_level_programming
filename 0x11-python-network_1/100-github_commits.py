#!/usr/bin/python3
"""
Take two arguments - the repository name and the owner name, and uses the
GitHub API to fetch the latest 10 commits from the specified repository
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    params = {'per_page': 10}
    response = requests.get(url, params=params)

    try:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f'{sha}: {author}')
    except ValueError:
        print("Not a valid JSON response")
