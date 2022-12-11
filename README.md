# Pull Request Comment 

A GitHub action which adds comments on PRs based on templates.

## Usage Example

[`.github/workflows/example.yml`](.github/workflows/example.yml)
 
```yml
name: Example 
on:
  pull_request:
    branches: [ "main"]

jobs:
  comment:
    permissions:
      pull-requests: write
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Add a comment to the PR
        uses: Correlatio-company/Pull-Request-Comments@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          filename: template.md
```
 
The worflow above will comment the content of the template. As of now the worflow does not format template.
Depending on the configuration of your repositories you might not need to explicitly set the permitions.
