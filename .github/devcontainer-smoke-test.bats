#!/usr/bin/env bats
# Smoke test for the devcontainer environment.
# Verifies that caches, tools, and volumes are set up correctly
# after the template is ejected and the devcontainer is built.

@test "running as the vscode user" {
    [ "$(whoami)" = "vscode" ]
}

@test "working directory is the project root" {
    [ -f manage.py ]
}

@test "default shell is zsh" {
    [ "$SHELL" = "/usr/bin/zsh" ]
}

@test "package cache is a mounted volume (not container-local storage)" {
    mountpoint --quiet ~/pkg-cache
}

@test "package cache is owned by the devcontainer user (not root)" {
    test -O ~/pkg-cache
}

@test "uv populated its cache on the volume during onCreateCommand" {
    test -d ~/pkg-cache/uv
}

@test "expected CLI tools are available on PATH" {
    python --version
    uv --version
    npm --version
    node --version
    terraform --version
    aws --version
    gh --version
    heroku --version
    psql --version
}

@test "npm writes its cache to the volume (not the default location)" {
    local npm_cache_before
    npm_cache_before=$(find ~/pkg-cache/npm -type f 2>/dev/null | wc --lines)
    npx --yes semver --help
    local npm_cache_after
    npm_cache_after=$(find ~/pkg-cache/npm -type f 2>/dev/null | wc --lines)
    [ "$npm_cache_after" -gt "$npm_cache_before" ]
}

@test "Django is immediately runnable after container setup" {
    ./manage.py check
}

@test "Tox test suite passes" {
    tox
}

@test ".tox is not in the project directory" {
    ! test -e .tox
}

@test ".ruff_cache is not in the project directory" {
    ! test -e .ruff_cache
}

@test ".mypy_cache is not in the project directory" {
    ! test -e .mypy_cache
}

@test ".venv is not in the project directory" {
    ! test -e .venv
}
