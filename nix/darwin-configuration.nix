{ pkgs, ... }:
{
  # List packages installed in system profile. To search by name, run:
  # $ nix-env -qaP | grep wget
  environment.systemPackages =
    [ pkgs.exa
      pkgs.fd
    ];

  # Auto upgrade nix package and the daemon service.
  services.nix-daemon.enable = false;
  nix.package = pkgs.nix;

  # Enable zsh 
  # https://github.com/LnL7/nix-darwin/blob/56f01699fbe462ae9f361ff08d2dbb9e898b9439/tests/programs-zsh.nix
  programs.zsh.enable = true;
  programs.zsh.enableCompletion = true;
}