#! /bin/zsh
set -x

# Conda
conda update -n base -c defaults conda --yes
conda update anaconda --yes

# Rust
rustup self update
rustup update stable

# Nix
# https://github.com/LnL7/nix-darwin#updating
nix-channel --update darwin
darwin-rebuild changelog # Verbose

# LaTeX
# https://tex.stackexchange.com/questions/55437/how-do-i-update-my-tex-distribution
tlmgr update --self --all --reinstall-forcibly-removed
