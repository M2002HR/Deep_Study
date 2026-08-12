# Source Baseline - DS-DKR-02 v1.0.0

**Research cutoff:** 2026-08-12

این درس برای رفتار فعلی، نصب، compatibility و security فقط به documentation رسمی Docker و primary project material تکیه می‌کند. نسخه‌ها و defaultهای وابسته به release در روز research دوباره باز و verify شده‌اند.

## Engine / installation

- Docker Docs - Install Docker Engine  
  `https://docs.docker.com/engine/install/`
- Docker Docs - Install Docker Engine on Ubuntu  
  `https://docs.docker.com/engine/install/ubuntu/`
- Docker Docs - Linux post-installation steps  
  `https://docs.docker.com/engine/install/linux-postinstall/`
- Docker Docs - Install Docker Engine from binaries  
  `https://docs.docker.com/engine/install/binaries/`
- Docker Engine 29 release notes  
  `https://docs.docker.com/engine/release-notes/29/`

## Client / connection / API / security

- Docker Docs - Docker contexts  
  `https://docs.docker.com/engine/manage-resources/contexts/`
- Docker CLI - docker version  
  `https://docs.docker.com/reference/cli/docker/version/`
- Docker CLI base reference  
  `https://docs.docker.com/reference/cli/docker/`
- Docker Docs - Protect the Docker daemon socket  
  `https://docs.docker.com/engine/security/protect-access/`
- Docker Docs - Configure remote access  
  `https://docs.docker.com/engine/daemon/remote-access/`
- Docker Engine API reference  
  `https://docs.docker.com/reference/api/engine/`
- Docker Docs - Deprecated Docker Engine features / Unauthenticated TCP connections  
  `https://docs.docker.com/engine/deprecated/`

## Rootless

- Docker Docs - Rootless mode  
  `https://docs.docker.com/engine/security/rootless/`

## Desktop / platform

- Docker Docs - Install Docker Desktop on Linux  
  `https://docs.docker.com/desktop/setup/install/linux/`
- Docker Desktop for Linux FAQ  
  `https://docs.docker.com/desktop/troubleshoot-and-support/faqs/linuxfaqs/`
- Docker Docs - Install Docker Desktop on Windows  
  `https://docs.docker.com/desktop/setup/install/windows-install/`
- Docker Docs - Docker Desktop WSL 2 backend  
  `https://docs.docker.com/desktop/features/wsl/`
- Docker Docs - Virtual Machine Manager for Docker Desktop on Mac  
  `https://docs.docker.com/desktop/features/vmm/`

## Directly verified current baseline

- Docker Engine branch 29 release page was opened directly on 2026-08-12.
- Highest release shown on the official page: **29.7.2**, dated **2026-08-05**.
- 29.7.2 updates BuildKit to **v0.32.2**.
- 29.7.0 packaging notes report **containerd v2.3.3** and **runc v1.4.3** for **static binaries**; these values are not generalized to every package-managed installation.
- Docker Engine API page on 2026-08-12 reports Engine **29.7 -> API 1.55, minimum 1.40**.
- Ubuntu installation page on 2026-08-12 lists official package set `docker-ce`, `docker-ce-cli`, `containerd.io`, `docker-buildx-plugin`, `docker-compose-plugin` and provides version-specific install examples for 29.7.2.
- Current Engine security/deprecation documentation was checked before describing remote TCP: unauthenticated TCP is deprecated/removed from the supported path in current releases; secure remote use should be through SSH or TLS/mTLS rather than teaching plain TCP as a normal deployment pattern.

## Currentness rules for this module

- Never infer `latest` from search snippets; open the canonical release page.
- Package versions differ by distribution, repository state and install method; lab evidence must record the real host.
- Docker Desktop system requirements, Windows installation modes, licensing terms, backend defaults and rootless implementation details are version-sensitive and must be rechecked when this module is revised.
- DKR.03 owns runtime architecture internals; this module only inventories component versions and deployment boundaries.
