import requests
import os
import github
import json
from loguru import logger


gitea_token = os.getenv("GITEA_TOKEN")
gitea_url = os.getenv("GITEA_URL")
mirror_org = os.getenv("MIRROR_ORG")
github_token = os.getenv("GITHUB_TOKEN")

gitea_api_url = f"{gitea_url}/api/v1"


def migrate(repo, headers, org_id):
    body = {
        "clone_addr": repo.clone_url,
        "description": repo.description,
        "mirror": True,
        "private": False,
        "repo_name": repo.name,
        "uid": org_id,
    }
    r = requests.post(f"{gitea_api_url}/repos/migrate", json=body, headers=headers)
    if r.status_code == 201:
        logger.info(f"Created {repo.name} mirror from GitHub")
    else:
        logger.error(f"Could not create {repo.name}. Skipping.")

def main():
    headers = {
        "accept": "application/json",
        "Authorization": f"token {gitea_token}",
        "Content-Type": "application/json",
    }

    gh = github.Github(github_token)
    repos = gh.get_user().get_repos(affiliation="owner", visibility="public")
    org_id = json.loads(requests.get(
        f"{gitea_api_url}/orgs/{mirror_org}",
        headers=headers
    ).text)["id"]

    for repo in repos:
        if not repo.fork:
            migrate(repo, headers, org_id)


if __name__ == "__main__":
    main()
