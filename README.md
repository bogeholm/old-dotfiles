# Bootstrapping

1. Install [XCode Command Line Tools](https://developer.apple.com/xcode/features/):
```bash
xcode-select --install
```

2. Install [Pipenv](https://pypi.org/project/pipenv/):
```bash
pip3 install pipenv
```

3. Clone this repo:
```bash
git clone git@github.com:bogeholm/dotfiles.git
```

4. Sync dotfiles
```bash
cd dotfiles/sync
pipenv install && pipenv shell
python sync.py --dotfile-list "dotfiles.toml"
```

# `dotfiles` overview

## `bash`
- [`~/.bash_profile`](bash/bash_profile)
- [`~/.profile`](bash/profile)

# `git`
[`~/.gitconfig`](git/gitconfig)

## `nix`
 - [`~/.nixpkgs/darwin-configuration.nix`](nix/darwin-configuration.nix)

## `ssh`
- [`~/.ssh/config`](ssh/config)

## `starship`
- [`~/.config/starship.toml`](starship/starship.toml)

## `zsh`
- [`~/.zprofile`](zsh/zprofile)
- [`~/.zshrc`](zsh/zshrc)

# Acknowledgements
- [@necolas](https://github.com/necolas/dotfiles) | [dotfiles](https://github.com/necolas/dotfiles)