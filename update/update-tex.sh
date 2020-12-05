#! /bin/zsh
set -x

# LaTeX - requires sudo
# https://tex.stackexchange.com/questions/55437/how-do-i-update-my-tex-distribution
tlmgr update --self
tlmgr update --all
