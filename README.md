# Gitea Mirror

Automatically creates mirrored repos (migrations) from your repos on GitHub.
The mirrored repos will be created in a dedicated organization.

# Usage

## Install package requirements

```bash
pipenv install --deploy
```

## Define the required environment variables:

| Environment Variable | Description                               | Example                  |
|----------------------|-------------------------------------------|--------------------------|
| GITEA_URL            | The URL of your Gitea Instance            | https://teahub.com       |
| GITEA_TOKEN          | The access token you generate for Gitea   | rgjkrehg4289th894hgrueig |
| GITHUB_TOKEN         | GitHub access token with repo scope       | reiugnu834g8h48gw8g838gr |
| GITEA_ORG            | The name of the organization to mirror to | mirror                   |

## Run the script

```bash
pipenv run migrate
```
