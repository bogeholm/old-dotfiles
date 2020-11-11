# Installation

## Install `Nix` on macOS

Courtesy of [@garyverhaegen-da](https://github.com/garyverhaegen-da) on [NixOS/nix/issues/2925](https://github.com/NixOS/nix/issues/2925#issuecomment-604501661)

These instructions are for macOS El Capitan and up, on machines with no T2 chip. 

Nix wants to install itself in `/nix` but writing to `/` is disabled by [System Integrity Protection](https://support.apple.com/en-us/HT204899). On machines _with_ a T2 chip, passing `--darwin-use-unencrypted-nix-store-volume` to the Nix installer [may denecessitate](https://wickedchicken.github.io/post/macos-nix-setup/) creating a `Nix` volume and mounting that at `/nix` as a workaround, as is done in steps 1-2 below.

### Step 1
```bash
sudo bash -c "echo nix >> /etc/synthetic.conf"

sudo reboot # Or use the Apple menu
```

### Step 2
```bash
sudo diskutil apfs addVolume disk1 APFSX Nix -mountpoint /nix

sudo bash -c 'echo "LABEL=Nix /nix apfs rw" >> /etc/fstab'

diskutil ap encryptVolume Nix -user disk # Choose a password - optionally, store in Keychain

sudo reboot # Or use the Apple menu
```

### Step 3
_See [1](https://unix.stackexchange.com/questions/339237/whats-the-difference-between-curl-sh-and-sh-c-curl) and [2](https://www.rust-lang.org/tools/install) for thoughts on piping to shell_.
```bash
zsh <(curl --proto '=https' --tlsv1.2 -sSfL https://nixos.org/nix/install)
```


## Install [`nix-darwin`](https://github.com/LnL7/nix-darwin)

```bash
nix-build https://github.com/LnL7/nix-darwin/archive/master.tar.gz -A installer

./result/bin/darwin-installer
```

# Background
- [MacOS Nix setup](https://wickedchicken.github.io/post/macos-nix-setup/)
- [The Manual](https://daiderd.com/nix-darwin/manual/index.html)

# Troubleshooting
## `zsh` cannot find executables
**Problem**: `darwin-rebuild switch` asks you to source `/etc/static/bashrc`, but this file is not sourceable by `zsh`

**Solution**: as described in [nix-darwin/tests/programs-zsh.nix](https://github.com/LnL7/nix-darwin/blob/master/tests/programs-zsh.nix), put the following lines in [`darwin-configuration.nix`](`darwin-configuration.nix`):

```bash
  programs.zsh.enable = true;
  programs.zsh.enableCompletion = true;
```