#!/usr/bin/env bash
set -euo pipefail

echo "Downloading SteamCMD..."
URL="https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz"
DIR="$(dirname "$0")/steamcmd"
mkdir -p "$DIR"
curl -L "$URL" | tar -xz -C "$DIR"

echo "Running SteamCMD first-time setup..."
"$DIR/steamcmd.sh" +quit

echo "SteamCMD installed in $DIR"
