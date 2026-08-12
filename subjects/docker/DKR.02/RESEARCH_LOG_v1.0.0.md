# Research Log - DS-DKR-02 v1.0.0

**Date / cutoff:** 2026-08-12

## Research questions

1. Docker Engine، Desktop و CLI از نظر install/deployment چه مرزی دارند؟
2. package-managed، manual package، convenience script و static binaries چه trade-offی دارند؟
3. current Engine 29 baseline و API compatibility امروز چیست؟
4. context، `DOCKER_HOST`، `DOCKER_CONTEXT` و remote access چه precedence/security boundary دارند؟
5. rootful/rootless در حد DKR.02 چه install/connection surfaceی دارند؟
6. Linux، macOS و Windows از نظر محل daemon/kernel چه تفاوت عملیاتی دارند؟
7. کدام failureها باید در Core module قابل reproduce/debug باشند؟

## Evidence summary

- Release notes page directly opened: latest listed Engine 29 release = 29.7.2 / 2026-08-05; BuildKit v0.32.2.
- 29.7.0 packaging notes: containerd v2.3.3 and runc v1.4.3 specifically for static binaries.
- Engine API page: 29.7 max API 1.55, minimum 1.40; normal CLI negotiates highest mutually supported API; `DOCKER_API_VERSION` disables negotiation.
- Ubuntu docs: official repo, conflict package inventory, package set, exact version installation, manual package and convenience-script caveats.
- Context docs: named endpoint/TLS state; default local Unix socket; environment/global flag overrides.
- Protect socket docs: SSH context and TLS/mTLS; possession of client keys is effectively high privilege; secure Docker TLS convention port 2376.
- Current Engine security/deprecation docs: unauthenticated remote TCP is not treated as a supported normal deployment path in current Engine; plain remote HTTP must not be taught as an acceptable lab endpoint.
- Rootless docs: daemon and containers non-root in user namespace; subordinate IDs and `newuidmap`/`newgidmap`; setup tool creates rootless context/user service.
- Desktop Linux: VM + `desktop-linux` context; state separate from host native Engine.
- Desktop Windows: per-user/all-users modes, WSL2/Hyper-V differences and Windows-container restrictions are current/version-sensitive.
- Desktop Mac: Linux VM powered by a VMM; static Mac binary is client-only.

## Scope / owner decisions

- No deep `dockerd -> containerd -> runc` architecture: DKR.03.
- No full daemon configuration or production upgrade playbook: DKR.30/DKR.31.
- No rootless internals: DKR.34.
- No detailed Desktop architecture: PLT.01/PLT.02.

## Unresolved by design

- Real learner environment versions, distribution repository contents and remote policy cannot be known from the PDF. The Lab Journal explicitly requires environment evidence.
