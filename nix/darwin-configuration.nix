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
}