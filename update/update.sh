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
# darwin-rebuild switch <- requires password, but is required when new packages are added
nix-channel --update darwin
darwin-rebuild changelog # Verbose
