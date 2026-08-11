# Source Baseline - DS-DKR-01 v1.0.0

**Research cutoff:** 2026-08-11

این درس فقط برای current behavior یا تعریف‌های فنی به منابع primary/official تکیه می‌کند. کتاب‌ها می‌توانند برای ترتیب آموزشی مکمل باشند، اما Source of Truth رفتار فعلی نیستند.

## Docker / OCI / Runtime stack

- Docker Docs - What is a container?  
  `https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/`
- Docker Docs - What is Docker?  
  `https://docs.docker.com/get-started/docker-overview/`
- Docker Docs - What is an image?  
  `https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/`
- Docker Docs - Docker Engine  
  `https://docs.docker.com/engine/`
- Docker Engine 29 release notes  
  `https://docs.docker.com/engine/release-notes/29/`
- Open Container Initiative  
  `https://opencontainers.org/`
- OCI Runtime Specification  
  `https://specs.opencontainers.org/runtime-spec/`
- Moby Project  
  `https://github.com/moby/moby`
- runc  
  `https://github.com/opencontainers/runc`
- containerd  
  `https://github.com/containerd/containerd`

## Linux primitives

- `namespaces(7)`  
  `https://man7.org/linux/man-pages/man7/namespaces.7.html`
- Linux kernel - cgroup v2  
  `https://docs.kernel.org/admin-guide/cgroup-v2.html`
- OCI runtime Linux configuration  
  `https://github.com/opencontainers/runtime-spec/blob/main/config-linux.md`

## Orchestration / system containers / Windows

- Kubernetes - Containers  
  `https://kubernetes.io/docs/concepts/containers/`
- Kubernetes - Container Runtimes  
  `https://kubernetes.io/docs/setup/production-environment/container-runtimes/`
- Incus - Containers and VMs  
  `https://linuxcontainers.org/incus/docs/main/explanation/containers_and_vms/`
- Microsoft Learn - Containers vs Virtual Machines  
  `https://learn.microsoft.com/en-us/virtualization/windowscontainers/about/containers-vs-vm`
- Microsoft Learn - Windows container isolation modes  
  `https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container`
- Microsoft Learn - Secure Windows containers  
  `https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/container-security`

## Currentness notes

- Docker Engine 29 release notes were opened directly on the research date; the lesson records the checked 29.7.2 baseline only where needed for ecosystem-topology awareness.
- Deep implementation details intentionally belong to later owner modules (`DKR.03`, `LNX.02`, `LNX.04`, `RUN.*`) and are not duplicated here.
