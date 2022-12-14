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
        uses: Correlatio-company/Pull-Request-Comments@1.0
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          filename: templates/template.md
```
 
The worflow above will comment the content of the template. As of now the worflow does not format template.
Depending on the configuration of your repositories you might not need to explicitly set the permitions.


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
        uses: Correlatio-company/Pull-Request-Comments@1.1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          filename: templates/template.md
          tag: template

      - name: create a new template
        run: echo "This is a generated text" > templates/temp.md

      - name: Try to add another comment to the PR
        uses: Correlatio-company/Pull-Request-Comments@1.1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          filename: templates/temp.md
          tag: template
```

The workflow above will comment the content of the template `template.md` then, create a new file and will try to comment it. As we are using the same tag for both comment, the second won't be added unless we specify `override: true` as another parameter. If `override` is set top true, the action will edit the previous comment and change its content. This is handy if you want to comment coverage on PR but do not want the PR to be spammed with comments or to have the coverage not up to date.
The `tag` and `override` arguments are both optional and if omitted the behavior of the action will be the same as in the 1.0. 