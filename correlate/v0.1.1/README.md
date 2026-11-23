# correlate-app 0.1.1

Installers for correlate-app 0.1.1. The Sump it provisions is
`ghcr.io/cantica-tech/correlate-sump:0.1.1`, for amd64 and arm64. Each file's SHA-256 is in
[`manifest.json`](manifest.json).

| System | Architecture | Installer | Size |
| ------ | ------------ | --------- | ---- |
| Linux | `x86_64` | [`correlate-app-0.1.1-linux-x86_64.AppImage`](https://github.com/cantica-tech/cantica-tech/releases/download/correlate-v0.1.1/correlate-app-0.1.1-linux-x86_64.AppImage) | 122 MB |
| Windows | `x64` | [`correlate-app-0.1.1-win-x64.exe`](https://github.com/cantica-tech/cantica-tech/releases/download/correlate-v0.1.1/correlate-app-0.1.1-win-x64.exe) | 106 MB |
| macOS | `arm64` | [`correlate-app-0.1.1-mac-arm64.dmg`](https://github.com/cantica-tech/cantica-tech/releases/download/correlate-v0.1.1/correlate-app-0.1.1-mac-arm64.dmg) | 127 MB |
| macOS | `x64` | [`correlate-app-0.1.1-mac-x64.dmg`](https://github.com/cantica-tech/cantica-tech/releases/download/correlate-v0.1.1/correlate-app-0.1.1-mac-x64.dmg) | 130 MB |

The Sump image, saved per architecture, to load where the registry cannot be
reached (`docker load -i <file>`; then the app provisions it as usual):

| System | Architecture | Image | Size |
| ------ | ------------ | ----- | ---- |
| Linux (Docker) | `amd64` | [`correlate-sump-0.1.1-linux-amd64.tar`](https://github.com/cantica-tech/cantica-tech/releases/download/correlate-v0.1.1/correlate-sump-0.1.1-linux-amd64.tar) | 147 MB |
| Linux (Docker) | `arm64` | [`correlate-sump-0.1.1-linux-arm64.tar`](https://github.com/cantica-tech/cantica-tech/releases/download/correlate-v0.1.1/correlate-sump-0.1.1-linux-arm64.tar) | 143 MB |

The installers may be unsigned; the system then asks before opening them.
On macOS, right-click the app and choose Open (or allow it in System
Settings, Privacy & Security). On Windows, choose More info, then Run anyway.
On Linux, make the AppImage executable (`chmod +x`) and run it.

## The zips in this folder

Each file above, zipped; a zip over 95 MB is cut into numbered pieces
(`.001`, `.002`, ...). Download every piece of one file into one folder,
then open its `.001` with 7-Zip, which joins them; or join them and unzip:
`cat <name>.zip.0* > <name>.zip && unzip <name>.zip` (macOS, Linux), or
`copy /b <name>.zip.001+<name>.zip.002 <name>.zip` (Windows, every piece in
order).

| File | Pieces |
| ---- | ----- |
| `correlate-app-0.1.1-linux-x86_64.AppImage` | [`correlate-app-0.1.1-linux-x86_64.AppImage.zip.001`](correlate-app-0.1.1-linux-x86_64.AppImage.zip.001), [`correlate-app-0.1.1-linux-x86_64.AppImage.zip.002`](correlate-app-0.1.1-linux-x86_64.AppImage.zip.002) |
| `correlate-app-0.1.1-mac-arm64.dmg` | [`correlate-app-0.1.1-mac-arm64.dmg.zip.001`](correlate-app-0.1.1-mac-arm64.dmg.zip.001), [`correlate-app-0.1.1-mac-arm64.dmg.zip.002`](correlate-app-0.1.1-mac-arm64.dmg.zip.002) |
| `correlate-app-0.1.1-mac-x64.dmg` | [`correlate-app-0.1.1-mac-x64.dmg.zip.001`](correlate-app-0.1.1-mac-x64.dmg.zip.001), [`correlate-app-0.1.1-mac-x64.dmg.zip.002`](correlate-app-0.1.1-mac-x64.dmg.zip.002) |
| `correlate-app-0.1.1-win-x64.exe` | [`correlate-app-0.1.1-win-x64.exe.zip.001`](correlate-app-0.1.1-win-x64.exe.zip.001), [`correlate-app-0.1.1-win-x64.exe.zip.002`](correlate-app-0.1.1-win-x64.exe.zip.002) |
| `correlate-sump-0.1.1-linux-amd64.tar` | [`correlate-sump-0.1.1-linux-amd64.tar.zip.001`](correlate-sump-0.1.1-linux-amd64.tar.zip.001), [`correlate-sump-0.1.1-linux-amd64.tar.zip.002`](correlate-sump-0.1.1-linux-amd64.tar.zip.002) |
| `correlate-sump-0.1.1-linux-arm64.tar` | [`correlate-sump-0.1.1-linux-arm64.tar.zip.001`](correlate-sump-0.1.1-linux-arm64.tar.zip.001), [`correlate-sump-0.1.1-linux-arm64.tar.zip.002`](correlate-sump-0.1.1-linux-arm64.tar.zip.002) |
