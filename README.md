# Testing

# Python environment

* Version 3.12.1
* Using [PDM](https://pdm-project.org)
* Check pyproject.toml if you want to run the tests

# Create the presentation

## Install [Marp](https://www.npmjs.com/package/@marp-team/marp-cli)

```sh
npm install --save-dev @marp-team/marp-cli
```

## Create the presentation PDF
```sh
./node_modules/.bin/marp --pdf presentation.md
```

