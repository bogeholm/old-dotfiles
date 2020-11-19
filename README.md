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
python sync.py --config "dotfiles.toml"
```

# `dotfiles` overview

## `bash`
- `~/.bash_profile`
- `~/.profile`

## `nix`
 - `~/.nixpkgs/darwin-configuration.nix`
 - `/etc/static/bashrc`

## `ssh`
- `~/.ssh/config`

## `starship`
- `~/.config/starship.toml`


## `zsh`
- `~/.zprofile`
- `~/.zshrc`

# Acknowledgements
- [@necolas](https://github.com/necolas/dotfiles) | [dotfiles](https://github.com/necolas/dotfiles)