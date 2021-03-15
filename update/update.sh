#! /usr/bin/env zsh
source logging.sh

# Conda
info "Updating Anaconda"
conda update -n base -c defaults conda --yes
conda update anaconda --yes

# Rust
info "Updating Rust"
rustup self update
rustup update stable

# Nix
# https://github.com/LnL7/nix-darwin#updating
# darwin-rebuild switch <- requires password, but is required when new packages are added
info "Updating Nix"
nix-channel --update darwin
darwin-rebuild changelog
nix-store --gc

ok "Update complete"
info "Remember to run 'darwin-rebuild switch' if you have added Nix packages"
