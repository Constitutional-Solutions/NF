{
  description = "The Legion Sovereign Stack: A Bio-Quantum AI Environment";

  # 1. INPUTS: Where do we get our 'Matter' (Software)?
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    # Rust overlay for bleeding-edge performance
    rust-overlay.url = "github:oxalica/rust-overlay";
  };

  # 2. OUTPUTS: What do we build?
  outputs = { self, nixpkgs, flake-utils, rust-overlay, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        overlays = [ (import rust-overlay) ];
        pkgs = import nixpkgs {
          inherit system overlays;
          config.allowUnfree = true; # Allow NVIDIA drivers if present
        };

        # The Rust Toolchain (The Forge)
        rustToolchain = pkgs.rust-bin.stable.latest.default.override {
          extensions = [ "rust-src" "rust-analyzer" ];
        };

        # Python Environment (The Nervous System)
        pythonEnv = pkgs.python311.withPackages (ps: with ps; [
          numpy
          scipy
          networkx
          torch
          requests
          fastapi
          uvicorn
          pydantic
          maturin # Essential: Builds Rust for Python
        ]);

      in
      {
        # A. DEVELOPMENT SHELL (For You)
        # Run `nix develop` to enter this space.
        devShells.default = pkgs.mkShell {
          buildInputs = [
            rustToolchain
            pythonEnv
            pkgs.pkg-config
            pkgs.openssl
            pkgs.sccache # Caching for faster builds
          ];

          # Environment Variables
          shellHook = ''
            echo "🏛️  LEGION SOVEREIGN SHELL ACTIVATED"
            echo "   - Python: 3.11 (Bio-Math Ready)"
            echo "   - Rust: Stable (Quantum-Math Ready)"
            echo "   - System: ${system}"
            
            # Auto-activate Python venv if you prefer it
            # source .venv/bin/activate
          '';
        };

        # B. THE PACKAGE (For The Community)
        # Run `nix build` to compile the sovereign binary.
        packages.default = pkgs.python311Packages.buildPythonPackage {
          pname = "legion-genesis";
          version = "2.0.0";
          src = ./.; # Use current directory

          # Build inputs
          nativeBuildInputs = [
            pkgs.maturin
            rustToolchain
          ];

          # How to build the hybrid Python/Rust code
          format = "pyproject";
          
          meta = with pkgs.lib; {
            description = "Synthetic Sentience Kernel v2.0";
            homepage = "https://github.com/constitutional-solutions/nf";
            license = licenses.agpl3Only;
          };
        };
      }
    );
}
