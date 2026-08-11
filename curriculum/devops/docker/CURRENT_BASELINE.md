# Docker Curriculum Current Baseline

**Verified:** 2026-08-11

- Docker Engine branch: 29
- Latest release directly verified on official v29 release-note page: **29.7.2 (2026-08-05)**
- Docker Engine 29 fresh-install default: containerd image store (subject to documented exceptions/configuration)
- OCI Runtime Specification: **v1.3.0**
- OCI Image Specification: **v1.1.1**
- OCI Distribution Specification: **v1.1.1**
- Vazirmatn PDF font dependency: **v33.003**, pinned by CI workflow; font binary not committed

## Current caveats

- Never infer `latest` from a search snippet; open the canonical release page.
- Docker packaging can differ by distribution/install method; component versions for BuildKit/containerd/runc must be verified per module/environment.
- Experimental/default features are rechecked at module build time.
