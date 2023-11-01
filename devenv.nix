{ pkgs, ... }:

{
  packages = [
    pkgs.just
    pkgs.git
    pkgs.shellcheck
  ];

  enterShell = ''
    git --version
    poetry install
  '';

  languages.python = {
    enable = true;
    package = pkgs.python311;
    poetry.enable = true;
    poetry.package = pkgs.poetry;
    venv.enable = true;
  };

}
