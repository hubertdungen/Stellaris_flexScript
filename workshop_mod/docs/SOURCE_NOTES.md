# Workshop mod source notes

This folder contains the Git-tracked Steam Workshop content for **More Picks &
Points: Traits|Civics|Ethics [FLEX EDITION]** (`3038118849`). It is intentionally
separate from `flexScript.py` so the mod content itself can be edited, reviewed,
and uploaded from the repository.

## Sources used

- Steam Workshop item `3038118849` for the published title, App ID, supported
  feature description, and default FLEX preset values.
- Public Stellaris modding examples for the standard `common/defines` and
  `common/species_archetypes` folder layout.

## Environment note

The original Workshop payload could not be fetched directly in this environment:
SteamCMD installed, but the bundled 32-bit client could not execute here; a
DepotDownloader attempt was also unable to connect to Steam anonymously. Because
of that, this folder recreates the small editable mod source from the public
Workshop values rather than claiming to be a byte-for-byte export of the current
Workshop download.

## Uploading

Copy `workshop_item.vdf.example` to a private `.vdf` file, replace the placeholder
paths with absolute local paths, and run SteamCMD with an account that owns the
Workshop item:

```bash
steamcmd +login <steam-user> +workshop_build_item /absolute/path/to/workshop_item.vdf +quit
```
