import requests
import os
import github


gitea_token = os.getenv("GITEA_TOKEN")
gitea_url = os.getenv("GITEA_URL")
github_token = os.getenv("GITHUB_TOKEN")
api_url = f"{gitea_url}/api/v1"


def migrate(repo, headers):
    body = {
        "clone_addr": repo.clone_url,
        "description": repo.description,
        "mirror": True,
        "private": False,
        "repo_name": repo.name,
        "uid": 3,
    }
    r = requests.post(f"{api_url}/repos/migrate", json=body, headers=headers)
    print(r.text)


def fetch_repos(token):
    gh = github.Github(token)
    return gh.get_user().get_repos(affiliation="owner")


def main():
    repos = fetch_repos(github_token)
    headers = {
        "accept": "application/json",
        "Authorization": f"token {gitea_token}",
        "Content-Type": "application/json",
    }
    for repo in repos:
        migrate(repo, headers)


if __name__ == "__main__":
    main()
