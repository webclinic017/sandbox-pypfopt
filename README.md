# Sandbox

Sandbox for random scripts and notebooks.

## Navigation

- YouTube downloader: [link](scripts/2023_06_16-youtube.py)
- ZAR/USD calendar year moves: [link](scripts/2023_06_16-zarusd.py)

## Development

### Dependencies

> Optional group dependencies will still be resolved alongside other dependencies, ensure they are compatible with each other.

```shell
# define which python version to use for the current project
poetry env use $(py -3.10 -c 'import sys; print(sys.executable)')

# install all required dependencies, synchronize environment
poetry install --sync

# ignore all dependencies besides runtime
poetry install --only main

# ignore all dependencies besides group_1
poetry install --only group_1

# ignore all dependencies besides project root
poetry install --only-root

# without (for required groups), with (for optional groups)
poetry install --without group_1,group_2 --with group_3,group_4

# add dependencies
poetry add pytest --group group_1

# remove dependencies
poetry remove pytest --group group_1

# update dependencies (and lock file), use --lock to only update lock file
poetry update --lock
```
