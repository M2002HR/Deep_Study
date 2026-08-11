# Deep Study - Docker Mastery Syllabus v1.1.0

سیلابس جامع تسلط عمیق بر Docker، Linux Containers، OCI، containerd، runc و پیاده‌سازی

**Version:** 1.1.0  
**Research cutoff:** 2026-08-11  
**Status:** Canonical foundation release - before first instructional PDF

## هدف سند

- این سند ستون فقرات مسیر Deep Study برای Docker است. هدف آن «تمام کردن Docker» نیست؛ هدف ساختن مدلی است که از usage تا implementation و contribution امتداد دارد.
- هر module در آینده می‌تواند به یک Study PDF مستقل (و در صورت نیاز Workbook جدا) تبدیل شود. هیچ PDF نباید بدون Scope Contract، منابع canonical و Definition of Done ساخته شود.
- این نسخه آگاهانه Docker را در دو سطح می‌بیند: (۱) container/Engine/open-source stack که باید بسیار عمیق شود؛ (۲) product ecosystem شرکت Docker که باید گسترده و version-sensitive شناخته شود.

## اصل بنیادی: PDF خروجی مطالعه است، نه Source of Truth

- در repository، نسخه Markdown/structured text منبع قابل version-control است و PDF artifact نهایی مطالعه. اصلاحات ابتدا در source انجام می‌شوند و سپس PDF دوباره ساخته می‌شود.
- برای هر PDF metadata شامل Document ID، version، last reviewed، research cutoff، scope، prerequisites و source baseline ثبت می‌شود.
- PDF باید synthesis باشد: concepts + internals + source/spec provenance + labs + failure modes + assessment؛ نه بازنویسی طولانی documentation.

## قرارداد یکپارچگی PDF و Knowledge Base

- فونت canonical همه PDFهای فارسی پروژه **Vazirmatn** است. Body، headings، tables، boxes، footer/page numbers و اعداد فارسی باید با Vazirmatn تولید شوند؛ وجود واقعی و embedding فونت با PDF preflight کنترل می‌شود.
- Master prompt پروژه در `meta/prompts/MASTER_PDF_PROMPT.md` قرار دارد و برای **هر** PDF آینده mandatory است. prompt اصلی کاربر بدون حذف در repository نگه‌داری می‌شود و master prompt لایه‌های Deep Study را به آن اضافه می‌کند.
- هر Study PDF یک Scope Contract دارد: In Scope، Out of Scope، Prerequisites، Assumed Knowledge، Upstream/Downstream Dependencies، Version-sensitive Areas، Source Baseline و Required Mastery Evidence.
- قبل از نوشتن هر PDF، syllabus فعلی + owner/upstream/downstream documents + terminology registry + source policy باید consistency-audit شوند.
- بعد از تولید PDF، preflight ماشینی کافی نیست: PDF باید به تصاویر render شود و **تمام صفحات** از نظر RTL/LTR، فونت، glyph، cover، TOC، borders، page numbers، headings، tables، boxes، code blocks، citations و page breaks بررسی شوند. هر defect باید در source اصلاح و PDF از نو ساخته/بازبینی شود.
- هیچ PDF با status `canonical` بدون ثبت Visual QA status/date و matching source version معتبر نیست.

## Baseline پژوهش این نسخه

- Research cutoff: 2026-08-11. قبل از اجرای هر module version-sensitive باید canonical page و release notes فعلی دوباره باز و verify شوند؛ search snippets به‌تنهایی معیار «latest» نیستند.
- Docker Engine: شاخه 29؛ آخرین release مشاهده و مستقیماً روی صفحه رسمی release notes بررسی‌شده در این سند **29.7.2 (2026-08-05)** است. 29.7.2 BuildKit را به v0.32.2 به‌روزرسانی می‌کند؛ release 29.7.0 نیز containerd v2.3.3 و runc v1.4.3 را برای static binaries گزارش می‌کند. component baseline باید هنگام هر module دوباره با packaging واقعی همان environment تطبیق داده شود.
- Docker Engine 29.0+ در fresh installations از containerd image store به‌عنوان storage backend پیش‌فرض استفاده می‌کند؛ upgradeهای قدیمی ممکن است همچنان classic graph driver داشته باشند.
- OCI snapshot بررسی‌شده: Runtime Spec v1.3.0؛ Image Spec v1.1.1؛ Distribution Spec v1.1.1. این نسخه‌ها برای pin کردن reading استفاده می‌شوند ولی syllabus به یک version محدود نیست.

### Deltaهای مهم current baseline که باید در moduleهای مربوط دیده شوند

- Engine 29.0+ در fresh install به containerd image store مهاجرت کرده؛ تفاوت upgrade install و userns-remap caveat در DKR.22/DKR.31 بررسی می‌شود.
- Engine 29.7.0 یک feature آزمایشی `embedded-containerd` اضافه کرده که topology سنتی dockerd -> external managed containerd را optional می‌کند؛ DKR.03/DKR.22 باید logical contract را از deployment topology جدا آموزش دهند.
- mount type `image` در 29.7.0 از experimental خارج شده و باید در storage/mount coverage ثبت شود.
- `default-stop-timeout` در 29.7.0 به daemon configuration اضافه شده؛ lifecycle/daemon administration باید version caveat آن را بشناسد.
- cgroup v1 در Engine 29 deprecated است؛ مسیر عمیق پروژه بر cgroup v2 متمرکز است و legacy فقط برای migration/debug awareness نگه‌داری می‌شود.
- rootless networking defaults در شاخه 29 تغییر کرده‌اند؛ هر rootless module باید implementation/default واقعی release مورد مطالعه را دوباره verify کند.
- از Docker v29، Go module قدیمی `github.com/docker/docker` deprecated است؛ source/contributor path باید public modules جدید Moby client/api و root module binary-oriented را بشناسد.

## هر Module چه خروجی‌ای دارد؟

- Core Study PDF: متن آموزشی canonical برای scope همان module.
- Scope Contract: In Scope / Out of Scope / Prerequisites / Downstream Dependencies / Version-sensitive areas.
- Labs: آزمایش‌های سالم و experiments برای مشاهده mechanism.
- Failure Pack: خطاهای عمدی و debugging checklist.
- Source/Spec Reading Tasks: دقیقاً کدام specification section یا code path باید خوانده شود.
- Assessment: teach-back، interview ladder، diagrams-from-memory و mastery checklist.

## نردبان تسلط

- **L1 - User:** عملیات اصلی را انجام می‌دهد و terminology را می‌شناسد.
- **L2 - Power User:** reference را سریع پیدا می‌کند، edge cases و configuration surface را می‌شناسد.
- **L3 - Production Operator:** امن و قابل‌اعتماد deploy/upgrade/observe می‌کند و failureهای رایج را حل می‌کند.
- **L4 - Troubleshooter/Architect:** مشکل را cross-layer debug می‌کند و trade-offهای architecture را توضیح می‌دهد.
- **L5 - Internals Expert:** Docker abstraction را تا OCI/containerd/runc/Linux primitives می‌شکند و source را trace می‌کند.
- **L6 - Contributor:** issue واقعی را reproduce، test/patch تولید و در review فنی مشارکت می‌کند.

## Dependency chains کلیدی

- `Docker run -> CLI -> Engine API -> dockerd/Moby -> containerd -> shim -> runc -> OCI config -> Linux syscalls/namespaces/cgroups/mounts`
- `Image build -> Dockerfile frontend -> LLB -> BuildKit solver -> worker/executor/snapshotter -> OCI image/index -> registry`
- `Image pull -> OCI Distribution -> descriptor graph -> content store -> unpack -> snapshots -> active rootfs -> runtime bundle`
- `Bridge network -> net namespace -> veth -> Linux bridge -> route/IP forwarding -> netfilter NAT/conntrack -> host NIC`
- `Resource limit -> Docker run config -> OCI Linux resources -> runc/libcontainer -> cgroup v2 controller files -> kernel scheduler/memory/IO`
- `Rootless Docker -> user namespace -> subuid/subgid -> rootless networking/storage/cgroup delegation -> daemon + containers without host root`
- `Compose -> Compose model/spec -> effective project config -> Docker Engine API objects -> networks/volumes/containers`
- `Swarm service -> desired state -> manager/Raft -> scheduler/task -> overlay/service discovery/routing mesh -> worker containers`

## فهرست فازها و ماژول‌ها

### P0 - قرارداد پروژه، روش مطالعه و آزمایشگاه
- **META.DKR.01** - قرارداد تسلط Docker و Scope کل برنامه (Meta)
- **META.DKR.02** - محیط آزمایش و ابزارهای مشاهده سیستم (Foundation)
- **META.DKR.03** - سیستم Coverage و Snapshot کامل Reference (Meta)
### P1 - Docker به‌عنوان محصول و runtime روزمره
- **DKR.01** - تاریخچه و مدل ذهنی Container (Core)
- **DKR.02** - نصب، Editions، Platforms و Distribution (Core)
- **DKR.03** - معماری Docker Engine: CLI -> API -> dockerd -> runtime stack (Core)
- **DKR.04** - Docker Object Model و Inspectability (Core)
- **DKR.05** - Container Lifecycle کامل (Core)
- **DKR.06** - Process Model، PID 1، Signals، TTY و I/O (Deep Core)
- **DKR.07** - Resource Constraints، OOM، PIDs، Devices و Accelerators (Core+Internals)
- **DKR.08** - Filesystem view و Container Mutation Operations (Core)
### P2 - Images، Dockerfile، BuildKit و Distribution
- **DKR.09** - Image Mental Model: layers, config, manifest, digest (Core)
- **DKR.10** - Naming، Tags، Digests، Content Addressability و Image Lifecycle (Core)
- **DKR.11** - Dockerfile: Semantics کامل دستورات (Core)
- **DKR.12** - Build Context، .dockerignore و Context Types (Core)
- **DKR.13** - Layering، Cache و Reproducible Builds (Core)
- **DKR.14** - BuildKit Architecture و LLB (Deep Core)
- **DKR.15** - Buildx، Builder Instances، Drivers و Bake (Core+Advanced)
- **DKR.16** - Multi-platform Images و Cross Building (Advanced)
- **DKR.17** - Advanced Build Mounts، Secrets، SSH، Devices و Entitlements (Advanced)
- **DKR.18** - Exporters، Cache Backends، SBOM و Provenance Attestations (Advanced)
- **DKR.19** - Registries، OCI Distribution، Docker Hub و Authentication (Core+Spec)
### P3 - Storage و Networking از Docker تا Linux boundary
- **DKR.20** - Persistence Model: Volumes، Bind Mounts، tmpfs (Core)
- **DKR.21** - Storage Drivers، Copy-on-Write و Overlay Concepts (Deep Core)
- **DKR.22** - containerd Image Store، Content Store و Snapshotters در Docker Engine (Advanced)
- **DKR.23** - Docker Networking Model و Network Drivers (Core)
- **DKR.24** - Bridge Networking Deep Dive: veth -> bridge -> routing -> NAT (Internals)
- **DKR.25** - Advanced Network Drivers: host/none/macvlan/ipvlan/IPv6 (Advanced)
- **DKR.26** - Overlay Networking و Swarm Data Plane (Advanced)
- **DKR.27** - Networking Troubleshooting Playbook (Production)
### P4 - Compose، Engine Administration، Observability، Security و Swarm
- **DKR.28** - Compose Application Model و Specification (Core)
- **DKR.29** - Compose Advanced: Merge، Include، Profiles، Watch و Reuse (Advanced)
- **DKR.30** - dockerd Administration و Host Integration (Production)
- **DKR.31** - Versioning، API Compatibility، Deprecations و Upgrades (Production)
- **DKR.32** - Logs، Events، Metrics و Diagnostics (Production)
- **DKR.33** - Container/Daemon Security Model (Deep Core)
- **DKR.34** - User Namespaces، userns-remap و Rootless Docker (Deep Core)
- **DKR.35** - Image و Software Supply Chain Security (Security)
- **DKR.36** - Credentials، Secrets و Trust Boundaries (Security)
- **DKR.37** - Swarm Architecture: Nodes، Services، Tasks، Raft و PKI (Advanced)
- **DKR.38** - Swarm Operations: Overlay، Routing Mesh، Updates، Secrets و DR (Advanced)
- **DKR.39** - Docker Engine Plugin System و Extension APIs (Advanced+Contributor)
### P5 - Linux internals زیر Container
- **LNX.01** - Linux Process Model، syscalls، /proc و file descriptors (Internals)
- **LNX.02** - Linux Namespaces: همه انواع و API (Internals)
- **LNX.03** - User Namespace و ID Mapping Internals (Internals)
- **LNX.04** - cgroup v2: hierarchy، controllers و delegation (Internals)
- **LNX.05** - Mounts، VFS، rootfs، chroot و pivot_root (Internals)
- **LNX.06** - OverlayFS Internals (Internals)
- **LNX.07** - Linux Networking Fundamentals برای Containers (Foundation->Internals)
- **LNX.08** - veth، Linux Bridge، NAT، conntrack و nftables/iptables (Internals)
- **LNX.09** - Linux Security: capabilities، seccomp، LSM و devices (Internals)
- **LNX.10** - systemd، cgroups و Container Host Integration (Internals+Ops)
### P6 - OCI، containerd و runc
- **OCI.01** - OCI Image Specification (Spec)
- **OCI.02** - OCI Runtime Specification (Spec)
- **OCI.03** - OCI Distribution Specification (Spec)
- **OCI.04** - OCI Artifacts، Referrers و Non-image Content (Spec+Ecosystem)
- **CTR.01** - containerd Architecture و Plugin/Service Model (Internals)
- **CTR.02** - containerd Content Flow، Images، Snapshots، Leases و GC (Internals)
- **CTR.03** - containerd Containers vs Tasks، Runtime v2 و Shim (Internals)
- **RNC.01** - runc CLI، OCI Bundle و Runtime Lifecycle (Internals)
- **RNC.02** - libcontainer Internals، Bootstrap/Init و CRIU (Implementation)
### P7 - Source Code Reading و ساخت اجزای مشابه
- **SRC.MOB.01** - Moby Repository Architecture، Build و Test (Contributor)
- **SRC.MOB.02** - Trace کردن Code Paths واقعی در Moby (Contributor)
- **SRC.CLI.01** - Docker CLI Source و API Mapping (Contributor)
- **SRC.BLD.01** - BuildKit Source: Solver، Worker، Cache، Executor و Frontend (Contributor)
- **SRC.CMP.01** - Compose Specification و Compose Implementation Source (Contributor/Ecosystem)
- **LAB.01** - ساخت Mini Container Runtime (Capstone)
- **LAB.02** - ساخت Mini OCI Image/Registry Explorer (Capstone)
- **LAB.03** - بازسازی Docker Bridge Networking بدون Docker (Capstone)
### P8 - Cross-platform، Docker Product Ecosystem و قابلیت‌های جدید
- **PLT.01** - Docker Desktop Architecture و Host Integration (Product)
- **PLT.02** - Windows: WSL2، Hyper-V و Windows Containers (Product)
- **PLT.03** - Docker Hub، Scout و Hardened Images به‌عنوان Product Surface (Product)
- **PLT.04** - Emerging Docker AI/Agent Surface: Model Runner، Sandboxes، MCP Toolkit (Awareness)
### P9 - Production، Failure Engineering، Ecosystem، Contribution و Interview
- **OPS.01** - Production Engineering و Lifecycle Management (Production)
- **OPS.02** - Performance Engineering (Production)
- **OPS.03** - Failure Engineering و Troubleshooting Matrix (Production)
- **OPS.04** - Ecosystem Comparison و Boundary Reasoning (Advanced)
- **CONTRIB.01** - Contribution Workflow: از Issue تا Merged PR (Contributor)
- **INT.01** - Interview Mastery: 30 seconds / 3 minutes / 30 minutes (Interview)
- **INT.02** - Adversarial Interview و Production Scenario Drills (Interview)
- **CAP.01** - Final Docker Mastery Capstone و Re-certification (Capstone)

# P0 - قرارداد پروژه، روش مطالعه و آزمایشگاه

این فاز مشخص می‌کند «تسلط» در این پروژه دقیقاً چه معنی دارد، چگونه version drift کنترل می‌شود و محیطی می‌سازیم که بتوان عمداً آن را خراب کرد.

## META.DKR.01 - قرارداد تسلط Docker و Scope کل برنامه

**Depth:** Meta  
**Prerequisites:** None / baseline

### پوشش اجباری
- تعریف شش سطح: User -> Power User -> Production Operator -> Troubleshooter -> Internals Expert -> Contributor.
- تفکیک «دانستن operation» از «حفظ syntax»؛ هدف: شناخت تمام capabilityها و توانایی پیدا کردن reference دقیق.
- تعریف Core / Deep Internals / Product Ecosystem / Historical-Legacy tracks تا breadth باعث قربانی شدن depth نشود.
- اصل spiral learning و just-in-time prerequisites؛ Linux و networking هنگام نیاز باز می‌شوند و بعد عمیق‌تر بازگشت می‌کنیم.
- تعریف خروجی هر module: Study PDF، Scope Contract، lab، failure scenarios، source/spec reading و mastery evidence.

### منابع canonical
- [DOCS] Docker Documentation - https://docs.docker.com/
- [ENGINE] Docker Engine manual - https://docs.docker.com/engine/
- [BOOK_UR] Docker: Up & Running, 3rd ed. - Sean P. Kane, Karl Matthias - https://www.oreilly.com/library/view/docker-up/9781098131814/
- [BOOK_DD] Docker Deep Dive, 4th ed. - Nigel Poulton - https://www.packtpub.com/en-us/product/docker-deep-dive-9781837028344

### Evidence خاص این module
- نوشتن تعریف شخصی از «Docker expert» و معیارهای رد/قبول هر سطح.

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## META.DKR.02 - محیط آزمایش و ابزارهای مشاهده سیستم

**Depth:** Foundation  
**Prerequisites:** None / baseline

### پوشش اجباری
- حداقل یک Linux VM disposable، ترجیحاً دو VM برای شبکه و registry/Swarm؛ snapshot/restore برای بازگشت سریع.
- ابزارها: docker, dockerd, ctr, nerdctl(optional), runc, buildctl/buildx, ip, ss, nsenter, unshare, lsns, mount/findmnt, strace, lsof, tcpdump, iptables/nft, systemctl/journalctl, jq, curl.
- ثبت baseline سخت‌افزار، kernel، cgroup mode، filesystem، firewall backend، Docker/BuildKit/containerd/runc versions.
- ساخت lab journal: برای هر آزمایش فرضیه، command، observation، explanation و cleanup ثبت شود.
- قاعده امنیتی: آزمایش‌های privileged/network/firewall فقط روی VM یا محیط disposable.

### Labs / Experiments
- ایجاد snapshot اولیه VM و ثبت خروجی uname, docker info, docker version, mount, lsns و cgroup.controllers.

### منابع canonical
- [ENGINE] Docker Engine manual - https://docs.docker.com/engine/
- [RELEASE29] Docker Engine v29 release notes - https://docs.docker.com/engine/release-notes/29/
- [LNX_NS] Linux namespaces(7) - https://man7.org/linux/man-pages/man7/namespaces.7.html
- [LNX_CGROUP] Linux kernel - Control Group v2 - https://docs.kernel.org/admin-guide/cgroup-v2.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## META.DKR.03 - سیستم Coverage و Snapshot کامل Reference

**Depth:** Meta  
**Prerequisites:** META.DKR.02

### پوشش اجباری
- در هر baseline نسخه، خروجی docker help، docker <object> --help، docker compose --help، docker buildx --help و dockerd --help snapshot شود.
- CLI commands بر اساس object و operation دسته‌بندی شوند: create/read/update/delete, lifecycle, transfer, inspect, debug, orchestration, build, security.
- Engine API endpoints و API version history به عنوان inventory مستقل ثبت شود؛ لازم نیست همه endpointها حفظ شوند اما هیچ capability ناشناخته نماند.
- Reference audit باید deprecated/experimental/hidden-behind-feature-flag capabilities را جدا علامت بزند.
- در هر ارتقای major/minor، coverage matrix با docs و release notes دوباره diff شود.

### Labs / Experiments
- تولید machine-readable command inventory از help output و مقایسه آن با CLI reference.

### منابع canonical
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/
- [DOCKERD] dockerd CLI reference - https://docs.docker.com/reference/cli/dockerd/
- [API] Docker Engine API reference - https://docs.docker.com/reference/api/engine/
- [RELEASE29] Docker Engine v29 release notes - https://docs.docker.com/engine/release-notes/29/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## P0 Gate
- Gate P0: محیط قابل خراب‌کردن آماده است؛ baseline نسخه و command/API inventory ثبت شده؛ Definition of Done پذیرفته شده است.

# P1 - Docker به‌عنوان محصول و runtime روزمره

از مدل ذهنی container تا معماری Engine، object model و lifecycle؛ این فاز باید تو را از کاربر معمولی به operator قابل اتکا برساند.

## DKR.01 - تاریخچه و مدل ذهنی Container

**Depth:** Core  
**Prerequisites:** META.DKR.01

### پوشش اجباری
- مسئله‌ای که containers حل می‌کنند: packaging، isolation، reproducibility، density و delivery؛ محدودیت‌های portability.
- مقایسه process/container/VM/system container؛ تفاوت virtualization در سطح OS با hypervisor.
- Container یک kernel primitive منفرد نیست؛ مجموعه‌ای از process + namespaces + cgroups + mounts + credentials + security policy است.
- فرق Docker company/product، Docker Engine، Moby، OCI، containerd، runc، Compose و Kubernetes.
- Linux containers در برابر Windows containers؛ چیزهایی که shared kernel بودن تضمین نمی‌کند.

### Labs / Experiments
- مقایسه process tree و namespaceهای یک process معمولی با container.

### Failure scenarios
- توضیح false assumptionهای «container = lightweight VM» و «image = zip file».

### منابع canonical
- [DOCS] Docker Documentation - https://docs.docker.com/
- [ENGINE] Docker Engine manual - https://docs.docker.com/engine/
- [OCI_RUNTIME] OCI Runtime Specification - https://specs.opencontainers.org/runtime-spec/
- [BOOK_UR] Docker: Up & Running, 3rd ed. - Sean P. Kane, Karl Matthias - https://www.oreilly.com/library/view/docker-up/9781098131814/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.02 - نصب، Editions، Platforms و Distribution

**Depth:** Core  
**Prerequisites:** DKR.01, META.DKR.02

### پوشش اجباری
- Docker Engine packages و install methods؛ Docker Desktop در برابر Engine؛ Linux/Windows/macOS operational differences.
- docker context، DOCKER_HOST، local Unix socket، TCP/SSH remote access و client/daemon version differences.
- rootful vs rootless deployment shape؛ package-managed vs static binaries و implications برای bundled components.
- نسخه‌ها، release channels، compatibility و pinning؛ تشخیص Engine، CLI، API، Compose، Buildx، BuildKit، containerd و runc versions.
- Baseline فعلی سند: Engine 29.x؛ اما هر lab باید version واقعی محیط را ثبت کند.

### Labs / Experiments
- نصب روی Linux VM؛ ساخت یک context دوم برای daemon remote آزمایشی.

### Failure scenarios
- client/daemon version mismatch
- permission denied روی docker.sock
- remote daemon ناامن روی TCP.

### منابع canonical
- [ENGINE] Docker Engine manual - https://docs.docker.com/engine/
- [RELEASE29] Docker Engine v29 release notes - https://docs.docker.com/engine/release-notes/29/
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/
- [ROOTLESS] Docker rootless mode - https://docs.docker.com/engine/security/rootless/
- [DESKTOP] Docker Desktop manual - https://docs.docker.com/desktop/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.03 - معماری Docker Engine: CLI -> API -> dockerd -> runtime stack

**Depth:** Core  
**Prerequisites:** DKR.01, DKR.02

### پوشش اجباری
- Client-server architecture، dockerd responsibilities و Docker objects.
- Unix socket/TCP، REST Engine API، version negotiation، request/response/error model؛ Docker contexts، DOCKER_HOST/DOCKER_CONTEXT و endpoint/TLS selection precedence.
- جایگاه Moby، containerd، shim و runc در path اجرای Linux container؛ تمایز logical architecture و packaging؛ و topologyهای version-sensitive مانند experimental embedded-containerd را بدون قاطی کردن logical contract با deployment topology تحلیل کن.
- Events و state transitions؛ daemon responsibilities در network/volume/image/runtime orchestration.
- مرزهایی که Docker به kernel delegation می‌دهد و چیزهایی که خودش implement می‌کند.

### Labs / Experiments
- با curl روی /var/run/docker.sock version/info/containers endpoints را صدا بزن؛ یک container را بدون docker CLI create/start/delete کن.

### Failure scenarios
- API version mismatch
- daemon unavailable
- stale state after daemon restart.

### منابع canonical
- [ENGINE] Docker Engine manual - https://docs.docker.com/engine/
- [API] Docker Engine API reference - https://docs.docker.com/reference/api/engine/
- [CONTAINERD_RUNTIME] containerd runtime v2 architecture - https://github.com/containerd/containerd/blob/main/docs/runtime-v2.md
- [MOBY] Moby repository - https://github.com/moby/moby

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.04 - Docker Object Model و Inspectability

**Depth:** Core  
**Prerequisites:** DKR.03

### پوشش اجباری
- Objects: containers, images, networks, volumes, plugins, contexts, services, nodes, secrets, configs, builders؛ object-specific prune/system-df/system-prune lifecycle awareness.
- Names/IDs/digests/labels/annotations و lifecycle متفاوت هر object.
- docker inspect، Go templates، filtering، formatting، labels و object metadata.
- فرق desired configuration، runtime state و derived status؛ operations مکمل مانند diff/cp/export/import/save/load/commit/top/stats/wait/update و boundary دقیق object mutation/transfer.
- قاعده operational: قبل از mutation state را inspect و evidence جمع کن.

### Labs / Experiments
- برای container/image/network/volume خروجی inspect را map و فیلدهای مهم را مستند کن.

### منابع canonical
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/
- [API] Docker Engine API reference - https://docs.docker.com/reference/api/engine/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.05 - Container Lifecycle کامل

**Depth:** Core  
**Prerequisites:** DKR.04

### پوشش اجباری
- create, start, run, exec, attach, detach, pause/unpause, stop, kill, restart, wait, rename, remove.
- export/import/commit/cp و تفاوتشان با image build/registry workflows؛ موارد مناسب و anti-patternها.
- AutoRemove، restart policy، container state machine، exit status، health status و ordering.
- فرق stop timeout و kill signal؛ STOPSIGNAL و custom stop signal.
- تفاوت docker exec با شروع process اولیه و اثر namespace/cgroup membership.

### Labs / Experiments
- lifecycle یک container را با events و inspect همزمان trace کن.

### Failure scenarios
- container stuck stopping
- exec fails when init exited
- restart loop
- paused container behavior.

### منابع canonical
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/
- [ENGINE] Docker Engine manual - https://docs.docker.com/engine/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.06 - Process Model، PID 1، Signals، TTY و I/O

**Depth:** Deep Core  
**Prerequisites:** DKR.05

### پوشش اجباری
- PID 1 semantics در namespace، signal handling، zombie reaping و init helperها.
- ENTRYPOINT/CMD در runtime؛ exec form vs shell form و اثر shell بر signal propagation.
- process groups/sessions، stdin/stdout/stderr، pseudo-TTY، attach vs logs و detach keys.
- graceful shutdown و application contracts؛ stop signal/timeouts و orchestrator expectations.
- چرا daemonizing داخل container معمولاً anti-pattern است؛ one-process guideline و استثناها.

### Labs / Experiments
- برنامه کوچک بساز که SIGTERM را log کند؛ تفاوت shell-form و exec-form را اندازه بگیر.

### Failure scenarios
- SIGTERM به app نمی‌رسد
- zombie accumulation
- interactive container hang.

### منابع canonical
- [ENGINE] Docker Engine manual - https://docs.docker.com/engine/
- [DOCKERFILE] Dockerfile reference - https://docs.docker.com/reference/dockerfile/
- [OCI_RUNTIME] OCI Runtime Specification - https://specs.opencontainers.org/runtime-spec/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.07 - Resource Constraints، OOM، PIDs، Devices و Accelerators

**Depth:** Core+Internals  
**Prerequisites:** DKR.05

### پوشش اجباری
- Memory hard/soft limits، swap semantics، OOM killer، oom score، memory pressure و failure interpretation.
- CPU shares/weight، quota/period، cpuset، realtime concepts و تفاوت limit/weight/reservation.
- PIDs limits، ulimits، blkio/IO controls و device access.
- GPU access، NVIDIA Container Toolkit awareness و relationship با device injection.
- CDI concept برای declarative device exposure؛ build-time CDI awareness و security implications.

### Labs / Experiments
- container را memory limit کن و OOM ایجاد کن؛ CPU throttling را مشاهده کن؛ pids limit بشکن.

### Failure scenarios
- host OOM vs container OOM
- swap misunderstanding
- resource flag unsupported by host kernel.

### منابع canonical
- [RESOURCE] Docker container resource constraints - https://docs.docker.com/engine/containers/resource_constraints/
- [GPU] Docker Engine GPU access - https://docs.docker.com/engine/containers/gpu/
- [CDI] Docker Build CDI - https://docs.docker.com/build/building/cdi/
- [LNX_CGROUP] Linux kernel - Control Group v2 - https://docs.kernel.org/admin-guide/cgroup-v2.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.08 - Filesystem view و Container Mutation Operations

**Depth:** Core  
**Prerequisites:** DKR.05

### پوشش اجباری
- container writable layer، copy-on-write در سطح concept، docker diff و mutation visibility.
- docker cp semantics، ownership/path/symlink considerations و security edge cases.
- export/import در برابر save/load در برابر commit؛ چه metadataهایی حفظ یا از دست می‌روند.
- read-only root filesystem، tmpfs paths و ephemeral state.
- Operational rule: runtime mutation را با immutable build pipeline مقایسه و anti-patternها را تشخیص بده.

### Labs / Experiments
- یک image را mutate کن؛ diff/export/commit را مقایسه و metadata تفاوت را ثبت کن.

### منابع canonical
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/
- [STORAGE] Docker Engine storage - https://docs.docker.com/engine/storage/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## P1 Gate
- Gate P1: باید بتوانی یک container را بدون CLI از API بسازی، lifecycle و signal path را توضیح بدهی، resource failureها را diagnose کنی و object state را دقیق inspect کنی.

# P2 - Images، Dockerfile، BuildKit و Distribution

از image به‌عنوان artifact روزمره تا OCI graph، LLB، cache، multi-platform، attestations و registry protocol.

## DKR.09 - Image Mental Model: layers, config, manifest, digest

**Depth:** Core  
**Prerequisites:** DKR.04

### پوشش اجباری
- image vs container، repository/tag/digest و mutable naming در برابر immutable content identity.
- layer changesets، image config، history، rootfs ordering و platform metadata.
- manifest vs image index/manifest list؛ multi-platform selection.
- compressed blob digest، uncompressed DiffID و chain relationships در سطح مفهومی.
- docker image inspect/history/save/load و mapping به OCI concepts.

### Labs / Experiments
- docker save یک image را باز کن و manifest/config/layers را با jq/tar بررسی کن.

### Failure scenarios
- tag drift
- wrong platform image
- digest mismatch mental model.

### منابع canonical
- [OCI_IMAGE] OCI Image Specification - https://specs.opencontainers.org/image-spec/
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.10 - Naming، Tags، Digests، Content Addressability و Image Lifecycle

**Depth:** Core  
**Prerequisites:** DKR.09

### پوشش اجباری
- image reference grammar: registry/namespace/repository:tag@digest.
- pull policies، local cache، dangling/unused images و garbage collection/prune.
- content-addressable identity، deduplication و implications برای trust/reproducibility.
- platform-aware pulls و pinning by digest؛ tag immutability policies در registryها.
- image import/export/save/load/pull/push/remove/prune semantics.

### Labs / Experiments
- همان image را با tag و digest pull کن و identity را مقایسه کن.

### منابع canonical
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/
- [OCI_IMAGE] OCI Image Specification - https://specs.opencontainers.org/image-spec/
- [OCI_DIST] OCI Distribution Specification - https://specs.opencontainers.org/distribution-spec/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.11 - Dockerfile: Semantics کامل دستورات

**Depth:** Core  
**Prerequisites:** DKR.09

### پوشش اجباری
- FROM, ARG, ENV, RUN, COPY, ADD, WORKDIR, USER, EXPOSE, VOLUME, LABEL, SHELL, STOPSIGNAL, HEALTHCHECK, ONBUILD, CMD, ENTRYPOINT.
- parser directives و syntax directive؛ shell vs exec forms؛ variable replacement و scope.
- COPY/ADD source semantics، ownership/permissions، --link/advanced features مطابق syntax version.
- USER و UID/GID portability؛ EXPOSE documentation vs port publishing.
- CMD/ENTRYPOINT composition و override behavior در docker run/Compose.

### Labs / Experiments
- برای هر instruction حداقل یک minimal Dockerfile و inspect/history evidence بساز.

### Failure scenarios
- ARG/ENV scope surprise
- COPY path/permission errors
- CMD/ENTRYPOINT override confusion.

### منابع canonical
- [DOCKERFILE] Dockerfile reference - https://docs.docker.com/reference/dockerfile/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.12 - Build Context، .dockerignore و Context Types

**Depth:** Core  
**Prerequisites:** DKR.11

### پوشش اجباری
- local directory/tar/stdin/Git/remote contexts؛ context transfer و security boundary.
- .dockerignore matching semantics و Dockerfile-specific ignore files.
- named contexts و cross-context COPY/mount patterns.
- چرا secrets نباید داخل context بیایند؛ accidental leakage و cache retention.
- context size/performance و reproducibility implications.

### Labs / Experiments
- یک secret را عمداً وارد context کن و سپس با .dockerignore و secret mount اصلاح کن.

### Failure scenarios
- unexpected cache invalidation
- huge context transfer
- secret leaked into layer.

### منابع canonical
- [BUILD] Docker Build manual - https://docs.docker.com/build/
- [DOCKERFILE] Dockerfile reference - https://docs.docker.com/reference/dockerfile/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.13 - Layering، Cache و Reproducible Builds

**Depth:** Core  
**Prerequisites:** DKR.11, DKR.12

### پوشش اجباری
- cache keys، invalidation، instruction ordering و package-manager patterns.
- multi-stage builds، target stages، scratch/distroless/minimal bases.
- determinism/reproducibility: pin dependencies، timestamps، external downloads، digest pinning.
- cache mounts و external cache strategies؛ inline/registry/local/GHA awareness.
- image size vs attack surface vs debuggability trade-offs.

### Labs / Experiments
- یک build کند را profile و با cache/multi-stage بهینه کن؛ reproducibility را با دو build مقایسه کن.

### Failure scenarios
- stale package cache
- non-reproducible download
- cache poisoning assumptions.

### منابع canonical
- [BUILD] Docker Build manual - https://docs.docker.com/build/
- [BUILDKIT] Docker BuildKit manual - https://docs.docker.com/build/buildkit/
- [DOCKERFILE] Dockerfile reference - https://docs.docker.com/reference/dockerfile/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.14 - BuildKit Architecture و LLB

**Depth:** Deep Core  
**Prerequisites:** DKR.13

### پوشش اجباری
- BuildKit daemon، frontends، solver، workers، executors، snapshotters، cache manager، exporters/importers.
- LLB به‌عنوان content-addressable dependency graph؛ operation DAG و parallelism.
- Dockerfile frontend -> LLB -> solver -> worker -> result/export pipeline؛ BuildKit sessions، sources، workers/executors/snapshotters و GC policy boundaries.
- entitlements، sandboxing و network/security modes در build execution.
- تفاوت legacy builder architecture با BuildKit و دلیل performance/extensibility improvements.

### Labs / Experiments
- LLB یک build را dump/inspect کن؛ independent stages را طوری بساز که parallel execution قابل مشاهده باشد.

### Failure scenarios
- builder unavailable
- frontend version incompatibility
- cache miss unexplained.

### منابع canonical
- [BUILDKIT] Docker BuildKit manual - https://docs.docker.com/build/buildkit/
- [BUILDKIT_REPO] BuildKit repository - https://github.com/moby/buildkit

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.15 - Buildx، Builder Instances، Drivers و Bake

**Depth:** Core+Advanced  
**Prerequisites:** DKR.14

### پوشش اجباری
- Buildx CLI plugin و relation با BuildKit؛ builder instances/nodes/platforms.
- drivers: docker, docker-container, remote, kubernetes awareness؛ capability differences.
- builder creation/inspection/bootstrap/use/stop/remove و resource configuration.
- Bake/HCL/Compose-derived build definitions؛ target groups، matrices/variables و CI reuse.
- cache/exporter behavior differences based on driver and image store.

### Labs / Experiments
- docker-container builder مستقل بساز، inspect کن و با default docker driver مقایسه کن.

### منابع canonical
- [BUILD] Docker Build manual - https://docs.docker.com/build/
- [BUILDKIT] Docker BuildKit manual - https://docs.docker.com/build/buildkit/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.16 - Multi-platform Images و Cross Building

**Depth:** Advanced  
**Prerequisites:** DKR.09, DKR.15

### پوشش اجباری
- platform tuple: OS/architecture/variant؛ image index و manifest selection.
- QEMU/binfmt emulation، native multi-node builders و cross-compilation strategies.
- BUILDPLATFORM/TARGETPLATFORM args و platform-aware Dockerfiles.
- performance/correctness trade-offs و architecture-specific dependencies.
- local image store limitations/behavior و push/load output choices.

### Labs / Experiments
- amd64+arm64 image بساز و index/manifests را inspect کن.

### Failure scenarios
- exec format error
- wrong platform selected
- emulation-only failure.

### منابع canonical
- [BUILD] Docker Build manual - https://docs.docker.com/build/
- [OCI_IMAGE] OCI Image Specification - https://specs.opencontainers.org/image-spec/
- [CONTAINERD_STORE] containerd image store with Docker Engine - https://docs.docker.com/engine/storage/containerd/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.17 - Advanced Build Mounts، Secrets، SSH، Devices و Entitlements

**Depth:** Advanced  
**Prerequisites:** DKR.14

### پوشش اجباری
- RUN --mount types: cache, secret, ssh, bind, tmpfs و lifetime/security semantics.
- secret values در layer/history/cache نباید persist شوند؛ verification techniques.
- SSH forwarding برای private source access بدون key baking.
- build network modes، insecure/security entitlements و threat model.
- CDI devices/GPU during build و labs-only/feature-gated syntax awareness.

### Labs / Experiments
- private dependency pattern را با secret/ssh mount بساز و ثابت کن secret در image نیست.

### Failure scenarios
- secret persisted accidentally
- SSH agent unavailable
- insecure entitlement unintentionally enabled.

### منابع canonical
- [BUILD] Docker Build manual - https://docs.docker.com/build/
- [CDI] Docker Build CDI - https://docs.docker.com/build/building/cdi/
- [BUILDKIT] Docker BuildKit manual - https://docs.docker.com/build/buildkit/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.18 - Exporters، Cache Backends، SBOM و Provenance Attestations

**Depth:** Advanced  
**Prerequisites:** DKR.14, DKR.16

### پوشش اجباری
- exporters: image/registry/local/tar/OCI/docker و تفاوت artifact outputs.
- cache import/export backends و cache portability.
- provenance و SBOM attestations؛ in-toto/SLSA awareness و attachment to image index.
- provenance modes، reproducibility metadata و CI policy consumption.
- relation با Scout policies، registry support و containerd image store.

### Labs / Experiments
- image را با SBOM/provenance بساز، push و attestations را inspect/extract کن.

### Failure scenarios
- attestation lost on incompatible output
- no base-image provenance data
- registry feature mismatch.

### منابع canonical
- [BUILD_ATTEST] Docker build attestations - https://docs.docker.com/build/metadata/attestations/
- [SCOUT] Docker Scout manual - https://docs.docker.com/scout/
- [OCI_IMAGE] OCI Image Specification - https://specs.opencontainers.org/image-spec/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.19 - Registries، OCI Distribution، Docker Hub و Authentication

**Depth:** Core+Spec  
**Prerequisites:** DKR.09, DKR.10

### پوشش اجباری
- registry/repository/blob/manifest/index vocabulary و Registry HTTP API v2 concepts.
- pull/push workflow، HEAD/GET/POST/PATCH/PUT، resumable blobs، deduplication و error codes.
- auth challenges/tokens، docker login/logout، credential stores/helpers، PATs، device-code/browser flows در صورت platform relevance، registry mirrors/insecure registry trust و least privilege.
- Docker Hub repositories/tags/access/webhooks/trusted content/API؛ rate/usage limits awareness.
- OCI artifacts/referrers و non-image artifacts؛ registry interoperability.

### Labs / Experiments
- local registry راه بینداز؛ manifest و blob را با HTTP مستقیم بگیر؛ یک blob digest را verify کن.

### Failure scenarios
- 401 challenge
- manifest unknown
- blob upload interrupted
- rate limit.

### منابع canonical
- [OCI_DIST] OCI Distribution Specification - https://specs.opencontainers.org/distribution-spec/
- [HUB] Docker Hub manual - https://docs.docker.com/docker-hub/
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## P2 Gate
- Gate P2: باید یک OCI image را دستی تشریح کنی، Dockerfile semantics را دفاع کنی، Dockerfile->LLB flow را توضیح بدهی، multi-platform image و attestations بسازی و registry را بدون docker pull با HTTP بررسی کنی.

# P3 - Storage و Networking از Docker تا Linux boundary

این فاز دو حوزه‌ای را عمیق می‌کند که بیشترین production incidentها را می‌سازند: persistence و packet path.

## DKR.20 - Persistence Model: Volumes، Bind Mounts، tmpfs

**Depth:** Core  
**Prerequisites:** DKR.08

### پوشش اجباری
- فرق writable layer، named/anonymous volumes، bind mounts، tmpfs و storage plugins.
- --mount vs -v semantics؛ subpaths، readonly، ownership، SELinux labeling و propagation awareness.
- volume lifecycle مستقل از container؛ backup/restore/migration patterns.
- bind mounts host coupling/security risks و path portability.
- tmpfs memory-backed behavior و secrets/ephemeral data patterns.

### Labs / Experiments
- برای یک DB volume backup/restore انجام بده؛ bind/volume/tmpfs behavior را مقایسه کن.

### Failure scenarios
- permission mismatch UID/GID
- mount obscures existing files
- volume deleted/misidentified.

### منابع canonical
- [STORAGE] Docker Engine storage - https://docs.docker.com/engine/storage/
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.21 - Storage Drivers، Copy-on-Write و Overlay Concepts

**Depth:** Deep Core  
**Prerequisites:** DKR.09, DKR.20

### پوشش اجباری
- classic graph/storage-driver model و overlay2، vfs، btrfs/zfs awareness.
- copy-on-write، lower/upper/merged/work concepts و performance implications.
- container writable layer vs persistent data؛ write amplification و copy-up.
- backing filesystem requirements و migration between storage backends.
- docker system df/prune و disk accounting pitfalls.

### Labs / Experiments
- overlay2 directory layout را روی test host inspect کن؛ file modification و copy-up را observe کن.

### Failure scenarios
- disk full
- inode exhaustion
- storage driver switch hides old data.

### منابع canonical
- [STORAGE] Docker Engine storage - https://docs.docker.com/engine/storage/
- [LNX_OVERLAY] Linux kernel - OverlayFS - https://docs.kernel.org/filesystems/overlayfs.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.22 - containerd Image Store، Content Store و Snapshotters در Docker Engine

**Depth:** Advanced  
**Prerequisites:** DKR.21, DKR.14

### پوشش اجباری
- containerd image store در fresh Engine 29+؛ تفاوت با classic graph drivers.
- compressed content store در برابر unpacked snapshots؛ why disk usage differs.
- snapshotter plugin model و overlayfs default؛ advanced lazy/p2p snapshotter awareness.
- multi-platform images و attestations support؛ data roots و migration/visibility behavior.
- relation Docker image metadata <-> containerd content/images/snapshots.

### Labs / Experiments
- فعال بودن containerd image store را verify کن؛ content/snapshot state را با ctr و docker مقایسه کن.

### Failure scenarios
- backend switch makes objects invisible
- containerd root partition fills
- snapshotter failure.

### منابع canonical
- [CONTAINERD_STORE] containerd image store with Docker Engine - https://docs.docker.com/engine/storage/containerd/
- [CONTAINERD_FLOW] containerd content flow - https://github.com/containerd/containerd/blob/main/docs/content-flow.md

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.23 - Docker Networking Model و Network Drivers

**Depth:** Core  
**Prerequisites:** DKR.04

### پوشش اجباری
- CNM-style object concepts در Docker implementation: network, endpoint, sandbox; IPAM concepts.
- default bridge vs user-defined bridge؛ embedded DNS و name resolution.
- drivers: bridge, host, none, overlay, macvlan, ipvlan؛ internal/attachable/IPv4/IPv6/IPAM/default-address-pools/MTU options و plugin-driver boundary.
- container interfaces/routes/gateway و multi-network attachment.
- EXPOSE در برابر publish؛ port mapping syntax، host IP binding، ephemeral host ports، userland-proxy awareness، port-allocation conflicts و interaction با host firewall.

### Labs / Experiments
- چند network بساز و route/DNS/interface changes را داخل container inspect کن.

### Failure scenarios
- wrong network attachment
- name resolution unexpected
- published port bound to wrong interface.

### منابع canonical
- [NETWORK] Docker Engine networking - https://docs.docker.com/engine/network/
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.24 - Bridge Networking Deep Dive: veth -> bridge -> routing -> NAT

**Depth:** Internals  
**Prerequisites:** DKR.23

### پوشش اجباری
- network namespace، veth pair، Linux bridge، L2/L3 boundaries و default gateway path.
- IP forwarding، NAT/masquerade، DNAT/SNAT و port publishing packet path.
- iptables/nftables backend و Docker-created rules؛ DOCKER chains/history awareness.
- hairpin/local host-to-container/container-to-internet flows و conntrack role.
- DNS forwarding/internal resolver behavior در user-defined bridge.

### Labs / Experiments
- packet path یک curl از host به published port و از container به Internet را با tcpdump/rules trace کن.

### Failure scenarios
- IP forwarding disabled
- NAT rule missing
- host firewall conflict
- hairpin edge case.

### منابع canonical
- [NETWORK] Docker Engine networking - https://docs.docker.com/engine/network/
- [FIREWALL] Docker packet filtering and firewalls - https://docs.docker.com/engine/network/packet-filtering-firewalls/
- [LNX_NS] Linux namespaces(7) - https://man7.org/linux/man-pages/man7/namespaces.7.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.25 - Advanced Network Drivers: host/none/macvlan/ipvlan/IPv6

**Depth:** Advanced  
**Prerequisites:** DKR.23, DKR.24

### پوشش اجباری
- host networking isolation trade-off؛ none network و manual plumbing.
- macvlan modes، parent interface، L2 identity و host communication caveat.
- ipvlan L2/L3 modes و routing implications.
- IPv6 addressing، forwarding، NAT differences و dual-stack considerations.
- internal networks، multi-homing و route selection.

### Labs / Experiments
- macvlan یا ipvlan در VM lab بساز؛ none container را دستی network کن.

### Failure scenarios
- host cannot reach macvlan child
- upstream switch limitations
- IPv6 forwarding/DNS issues.

### منابع canonical
- [NETWORK] Docker Engine networking - https://docs.docker.com/engine/network/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.26 - Overlay Networking و Swarm Data Plane

**Depth:** Advanced  
**Prerequisites:** DKR.23

### پوشش اجباری
- overlay network purpose برای multi-host connectivity؛ VXLAN concept.
- control-plane membership/service discovery در برابر data-plane packet encapsulation.
- ingress/routing mesh concepts و published ports در Swarm.
- attachable overlay و standalone containers؛ encryption option و overhead.
- network MTU، underlay dependence و troubleshooting boundaries.

### Labs / Experiments
- دو node Swarm lab و overlay بساز؛ VXLAN traffic را capture کن.

### Failure scenarios
- overlay packets blocked
- MTU fragmentation
- routing mesh confusion.

### منابع canonical
- [NETWORK] Docker Engine networking - https://docs.docker.com/engine/network/
- [SWARM] Docker Swarm mode - https://docs.docker.com/engine/swarm/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.27 - Networking Troubleshooting Playbook

**Depth:** Production  
**Prerequisites:** DKR.24, DKR.25

### پوشش اجباری
- decision tree: process/listen socket -> namespace/interface -> route -> DNS -> firewall/NAT -> remote network -> application protocol.
- ابزارها: ss, ip addr/route/link/neigh, nsenter, tcpdump, dig/getent, curl/nc, conntrack, iptables-save/nft list ruleset.
- container DNS و /etc/resolv.conf behavior، host resolvers و DNS failure classification.
- MTU/MSS، asymmetric routing، conntrack exhaustion و ephemeral ports awareness.
- firewalld/ufw integration pitfalls و why published ports may bypass expected host firewall policy.

### Labs / Experiments
- پنج failure سناریو بساز: DNS، wrong bind address، missing route، firewall، MTU.

### Failure scenarios
- DNS timeout
- connection refused vs timeout
- conntrack full
- ufw assumption.

### منابع canonical
- [FIREWALL] Docker packet filtering and firewalls - https://docs.docker.com/engine/network/packet-filtering-firewalls/
- [NETWORK] Docker Engine networking - https://docs.docker.com/engine/network/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## P3 Gate
- Gate P3: باید bridge networking را بدون Docker بازسازی کنی، packet path را trace کنی، storage backendها را توضیح بدهی و permission/disk/network incidents را به‌صورت systematic debug کنی.

# P4 - Compose، Engine Administration، Observability، Security و Swarm

از یک host و container منفرد به application model، daemon operations، production security و orchestration داخلی Docker.

## DKR.28 - Compose Application Model و Specification

**Depth:** Core  
**Prerequisites:** DKR.05, DKR.20, DKR.23

### پوشش اجباری
- Compose application model: services, networks, volumes, configs, secrets و project identity.
- Compose Specification current model و legacy 2.x/3.x history؛ schema validation و canonical config.
- build/image, command/entrypoint, environment/env_file, ports/expose, volumes, networks, healthcheck, restart/deploy distinctions.
- depends_on semantics و readiness vs startup ordering.
- Compose CLI lifecycle: up/down/create/start/stop/restart/exec/run/logs/ps/pull/push/build/config/events.

### Labs / Experiments
- یک سه‌سرویس app با healthcheck/network/volume بساز و docker compose config را canonicalize کن.

### Failure scenarios
- depends_on mistaken for readiness
- env interpolation mismatch
- orphan resources.

### منابع canonical
- [COMPOSE] Compose file reference / Compose Specification implementation - https://docs.docker.com/reference/compose-file/
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.29 - Compose Advanced: Merge، Include، Profiles، Watch و Reuse

**Depth:** Advanced  
**Prerequisites:** DKR.28

### پوشش اجباری
- multiple files و merge rules؛ overrides و environment-specific composition.
- profiles، fragments/extensions، anchors vs spec-level reuse، include و model normalization.
- variable interpolation precedence، .env/env_file/process environment و debugging effective config.
- one-off jobs، scale، lifecycle hooks/health/dependencies، develop/watch، dry-run و conversion/bridge/provider-style integration awareness؛ هر feature جدید Compose باید در META.DKR.03 current inventory شود.
- secrets/configs semantics و portability gap با orchestrators.

### Labs / Experiments
- base+dev+prod compose layers بساز و final config را diff کن؛ profile و watch استفاده کن.

### Failure scenarios
- unexpected merge
- wrong env precedence
- bind mount performance on Desktop.

### منابع canonical
- [COMPOSE] Compose file reference / Compose Specification implementation - https://docs.docker.com/reference/compose-file/
- [DESKTOP] Docker Desktop manual - https://docs.docker.com/desktop/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.30 - dockerd Administration و Host Integration

**Depth:** Production  
**Prerequisites:** DKR.03, META.DKR.02

### پوشش اجباری
- daemon startup، systemd units/socket activation، daemon.json vs flags و conflict rules.
- Unix/TCP sockets، TLS mutual auth، SSH contexts و remote daemon security.
- data-root و containerd data location؛ proxies، DNS defaults، registry mirrors/insecure registries.
- live-restore، default runtimes، log defaults، iptables/nftables settings، shutdown/restart behavior، stop-timeout defaults و daemon-wide transfer/concurrency controls.
- multiple daemons/test daemons، debug mode، system logs و config validation.

### Labs / Experiments
- daemon config را تغییر و validate کن؛ TLS-protected remote daemon بساز.

### Failure scenarios
- daemon won’t start due config conflict
- data root full
- remote socket exposed unauthenticated.

### منابع canonical
- [DOCKERD] dockerd CLI reference - https://docs.docker.com/reference/cli/dockerd/
- [ENGINE] Docker Engine manual - https://docs.docker.com/engine/
- [CONTAINERD_STORE] containerd image store with Docker Engine - https://docs.docker.com/engine/storage/containerd/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.31 - Versioning، API Compatibility، Deprecations و Upgrades

**Depth:** Production  
**Prerequisites:** DKR.30, META.DKR.03

### پوشش اجباری
- Engine/CLI/API version relationships و API version negotiation/history.
- deprecated/removed features؛ release-note-driven migration و behavior changes.
- bundled component versions (BuildKit/containerd/runc) در packages/static binaries و why source debugging needs exact versions.
- upgrade/downgrade planning، rollback constraints، storage/network compatibility.
- feature flags/experimental features و policy برای استفاده production؛ deprecation examples مثل cgroup v1 و legacy links فقط با release-specific verification.

### Labs / Experiments
- دو release note متوالی را diff و breaking/deprecation checklist تولید کن.

### Failure scenarios
- deprecated feature breaks upgrade
- API client hardcodes newer endpoint.

### منابع canonical
- [RELEASE29] Docker Engine v29 release notes - https://docs.docker.com/engine/release-notes/29/
- [API] Docker Engine API reference - https://docs.docker.com/reference/api/engine/
- [ENGINE] Docker Engine manual - https://docs.docker.com/engine/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.32 - Logs، Events، Metrics و Diagnostics

**Depth:** Production  
**Prerequisites:** DKR.05, DKR.30

### پوشش اجباری
- container stdout/stderr و logging drivers؛ json-file/local/syslog/journald/fluentd/gelf/awslogs/splunk awareness.
- log rotation، blocking/non-blocking modes و loss/backpressure trade-offs.
- docker events event stream و correlation با lifecycle incidents.
- docker stats و cgroup metrics؛ daemon metrics/Prometheus exposure awareness.
- daemon logs، inspect، system df/info و OS-level telemetry integration.

### Labs / Experiments
- یک logging driver alternative آزمایش کن؛ event stream و stats را با incident timeline correlate کن.

### Failure scenarios
- disk filled by logs
- logging driver blocks app
- missing logs after crash.

### منابع canonical
- [ENGINE] Docker Engine manual - https://docs.docker.com/engine/
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/
- [LNX_CGROUP] Linux kernel - Control Group v2 - https://docs.kernel.org/admin-guide/cgroup-v2.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.33 - Container/Daemon Security Model

**Depth:** Deep Core  
**Prerequisites:** DKR.06, DKR.07

### پوشش اجباری
- Docker daemon/root authority و خطر docker.sock؛ access to daemon ~= host root در rootful model.
- privileged containers، device mounts، host namespaces، bind mounts و breakout risk amplification.
- Linux capabilities default set/drop/add؛ no-new-privileges.
- seccomp default profile و syscall filtering؛ AppArmor/SELinux LSM integration.
- read-only FS، user selection، masked/readonly paths، kernel attack surface و host patching؛ archive/copy/extraction paths و historical security failures به‌عنوان reminder برای trust-boundary analysis.

### Labs / Experiments
- capabilities را drop/add کن و behavior را مشاهده کن؛ seccomp-denied syscall demo بساز.

### Failure scenarios
- container works only privileged
- socket mounted into untrusted container
- LSM policy denial.

### منابع canonical
- [LNX_CAP] Linux capabilities(7) - https://man7.org/linux/man-pages/man7/capabilities.7.html
- [LNX_SECCOMP] Linux seccomp(2) - https://man7.org/linux/man-pages/man2/seccomp.2.html
- [ROOTLESS] Docker rootless mode - https://docs.docker.com/engine/security/rootless/
- [USERNS] Docker user namespace remapping - https://docs.docker.com/engine/security/userns-remap/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.34 - User Namespaces، userns-remap و Rootless Docker

**Depth:** Deep Core  
**Prerequisites:** DKR.33

### پوشش اجباری
- user namespace UID/GID mappings، subordinate IDs و ownership translation.
- userns-remap: daemon rootful ولی containers remapped؛ storage/mount limitations.
- rootless: daemon و containers داخل user namespace؛ rootlesskit/network/storage implications.
- rootless networking evolution و version-sensitive drivers؛ cgroup delegation/systemd considerations.
- فرق rootless با “USER non-root داخل container” و با Desktop isolation.

### Labs / Experiments
- rootless daemon نصب کن؛ host/container UID mapping را با files و /proc بررسی کن.

### Failure scenarios
- subuid/subgid missing
- privileged port/device limitations
- bind mount ownership confusion.

### منابع canonical
- [ROOTLESS] Docker rootless mode - https://docs.docker.com/engine/security/rootless/
- [USERNS] Docker user namespace remapping - https://docs.docker.com/engine/security/userns-remap/
- [LNX_NS] Linux namespaces(7) - https://man7.org/linux/man-pages/man7/namespaces.7.html
- [LNX_CGROUP] Linux kernel - Control Group v2 - https://docs.kernel.org/admin-guide/cgroup-v2.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.35 - Image و Software Supply Chain Security

**Depth:** Security  
**Prerequisites:** DKR.18, DKR.19, DKR.33

### پوشش اجباری
- base-image trust، digest pinning، minimal/distroless images و patch cadence.
- SBOM، provenance، attestations، signatures/VEX concepts و policy enforcement.
- Docker Scout CVE analysis، policy evaluation، base-image freshness و license checks.
- Docker Hardened Images concepts، signed metadata، SLSA/VEX و shared responsibility.
- secret scanning، dependency lifecycle و CI admission gates.

### Labs / Experiments
- یک image آسیب‌پذیر scan کن؛ policy برای non-root/SBOM/provenance اجرا و remediate کن.

### Failure scenarios
- false confidence from “0 CVE”
- stale base digest
- missing provenance.

### منابع canonical
- [SCOUT] Docker Scout manual - https://docs.docker.com/scout/
- [DHI] Docker Hardened Images - https://docs.docker.com/dhi/
- [BUILD_ATTEST] Docker build attestations - https://docs.docker.com/build/metadata/attestations/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.36 - Credentials، Secrets و Trust Boundaries

**Depth:** Security  
**Prerequisites:** DKR.19, DKR.35

### پوشش اجباری
- docker login credential storage و credential helpers/stores؛ tokens vs passwords.
- Build secrets/SSH در برابر runtime secrets و environment-variable leakage.
- Swarm secrets/configs encryption-at-rest model و access lifecycle.
- TLS certs برای daemon/registry و trust store management.
- CI credentials scope، short-lived tokens و avoiding docker.sock exposure.

### Labs / Experiments
- credential helper configure کن؛ secret را در env/history/logs leak و سپس اصلاح کن.

### Failure scenarios
- plaintext credentials in config
- secret baked in image
- overprivileged registry token.

### منابع canonical
- [CLI] Docker CLI reference - https://docs.docker.com/reference/cli/docker/
- [SWARM] Docker Swarm mode - https://docs.docker.com/engine/swarm/
- [BUILD] Docker Build manual - https://docs.docker.com/build/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.37 - Swarm Architecture: Nodes، Services، Tasks، Raft و PKI

**Depth:** Advanced  
**Prerequisites:** DKR.23, DKR.30

### پوشش اجباری
- Swarm init/join، managers/workers، desired state، services/tasks و replicated/global modes.
- scheduler constraints/preferences/resources و placement.
- Raft consensus/quorum، manager fault tolerance و state storage.
- mutual TLS/CA rotation، node certificates و join tokens.
- service discovery/VIP/DNSRR و control-plane vs data-plane.

### Labs / Experiments
- ۳-node swarm آزمایشی بساز؛ manager loss/quorum را simulate کن.

### Failure scenarios
- lost quorum
- bad placement constraints
- cert/join problems.

### منابع canonical
- [SWARM] Docker Swarm mode - https://docs.docker.com/engine/swarm/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.38 - Swarm Operations: Overlay، Routing Mesh، Updates، Secrets و DR

**Depth:** Advanced  
**Prerequisites:** DKR.37, DKR.26

### پوشش اجباری
- ingress/routing mesh، overlay networks، published ports و endpoint modes.
- rolling updates/rollback، health/failure handling و update config.
- stacks، Compose compatibility limits، configs/secrets.
- backup/restore manager state و disaster recovery.
- when NOT to use Swarm؛ relation to Kubernetes learning path.

### Labs / Experiments
- service rolling update و rollback؛ manager backup/restore lab.

### Failure scenarios
- routing mesh unreachable
- update stuck
- quorum recovery.

### منابع canonical
- [SWARM] Docker Swarm mode - https://docs.docker.com/engine/swarm/
- [COMPOSE] Compose file reference / Compose Specification implementation - https://docs.docker.com/reference/compose-file/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## DKR.39 - Docker Engine Plugin System و Extension APIs

**Depth:** Advanced+Contributor  
**Prerequisites:** DKR.03, DKR.30, DKR.33

### پوشش اجباری
- managed plugin lifecycle: install/create/enable/disable/inspect/set/upgrade/remove/push؛ distribution به‌صورت image-like artifact و permission grant model.
- plugin `config.json`، rootfs، declared interfaces، mounts/devices/network/capabilities و Engine-managed isolation.
- extension interfaces و use cases: volume، network، logging و authorization؛ تفاوت plugin interface با built-in driver.
- legacy out-of-process Plugin API: discovery، activation handshake، socket/systemd activation، retry/error semantics و migration/history.
- plugin debugging، dockerd log correlation، privilege/security review، availability/failure blast radius و platform limitations.
- developing a minimal plugin و تشخیص اینکه چه زمانی plugin مناسب است و چه زمانی external service/CSI/CNI/other extension model بهتر است.

### Labs / Experiments
- یک managed plugin موجود را install/inspect/disable/enable کن و permission surface آن را تحلیل کن؛ سپس یک minimal test plugin یا mock Plugin API handshake بساز.

### Failure scenarios
- plugin permission mismatch
- plugin fails activation
- volume/network depends on unavailable plugin
- unsafe privilege request
- legacy discovery/socket failure.

### منابع canonical
- Docker Engine managed plugin system - https://docs.docker.com/engine/extend/
- Docker Plugin API - https://docs.docker.com/engine/extend/plugin_api/
- Docker legacy plugins - https://docs.docker.com/engine/extend/legacy_plugins/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## P4 Gate
- Gate P4: باید بتوانی Compose app پیچیده را reason کنی، daemon را امن اداره کنی، observability و security controls را دفاع کنی و Swarm failure/quorum/update را توضیح بدهی.

# P5 - Linux internals زیر Container

اینجا abstraction Docker را می‌شکنیم. هدف این است که container را بدون Docker از primitives سیستم عامل بازسازی کنی.

## LNX.01 - Linux Process Model، syscalls، /proc و file descriptors

**Depth:** Internals  
**Prerequisites:** DKR.06

### پوشش اجباری
- process/thread distinction، PID/TID، parent/child، fork/clone/clone3، execve، wait و exit.
- credentials، environment، cwd/root، file descriptor table، pipes/sockets/TTY.
- signals، process groups/sessions و PID 1 special behavior.
- /proc process introspection: status, cmdline, fd, ns, cgroup, mounts, limits.
- strace/lsof/pstree/ps به‌عنوان ابزار reasoning نه صرفاً troubleshooting.

### Labs / Experiments
- یک docker run/exec را با strace سطح مناسب روی runtime/child process مشاهده کن.

### منابع canonical
- [LNX_NS] Linux namespaces(7) - https://man7.org/linux/man-pages/man7/namespaces.7.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LNX.02 - Linux Namespaces: همه انواع و API

**Depth:** Internals  
**Prerequisites:** LNX.01

### پوشش اجباری
- namespace abstraction و lifetime/pinning در /proc/*/ns.
- PID, mount, network, UTS, IPC, user, cgroup, time namespaces؛ scope و چیزهایی که isolate می‌کنند/نمی‌کنند.
- clone/clone3 flags، unshare، setns و permission model.
- nested namespaces و parent relationships؛ visibility rules.
- nsenter/lsns و namespace debugging.

### Labs / Experiments
- با unshare چند namespace بساز و با nsenter واردشان شو؛ بدون Docker hostname/PID/mount isolation بساز.

### Failure scenarios
- CAP_SYS_ADMIN requirement
- mount propagation surprises.

### منابع canonical
- [LNX_NS] Linux namespaces(7) - https://man7.org/linux/man-pages/man7/namespaces.7.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LNX.03 - User Namespace و ID Mapping Internals

**Depth:** Internals  
**Prerequisites:** LNX.02

### پوشش اجباری
- uid_map/gid_map، setgroups restrictions، subordinate IDs و newuidmap/newgidmap.
- capabilities inside user namespace و scope آنها.
- idmapped mounts awareness و ownership problems در container storage.
- rootless networking/storage limitations از دید kernel privilege.
- security boundary caveats و kernel dependency.

### Labs / Experiments
- user namespace بدون root بساز؛ UID 0 داخل را با host UID map کن.

### منابع canonical
- [LNX_NS] Linux namespaces(7) - https://man7.org/linux/man-pages/man7/namespaces.7.html
- [LNX_CAP] Linux capabilities(7) - https://man7.org/linux/man-pages/man7/capabilities.7.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LNX.04 - cgroup v2: hierarchy، controllers و delegation

**Depth:** Internals  
**Prerequisites:** LNX.01

### پوشش اجباری
- single unified hierarchy، cgroup.procs، subtree_control، no-internal-process rule concepts.
- controllers: cpu, memory, io, pids, cpuset و metrics/events.
- limits/weights/protections، OOM/memory events و PSI awareness.
- delegation model، cgroup namespaces و systemd integration.
- mapping Docker resource flags to cgroup v2 files.

### Labs / Experiments
- بدون Docker cgroup بساز و memory/CPU/PIDs limits اعمال کن؛ OOM event را ثبت کن.

### منابع canonical
- [LNX_CGROUP] Linux kernel - Control Group v2 - https://docs.kernel.org/admin-guide/cgroup-v2.html
- [RESOURCE] Docker container resource constraints - https://docs.docker.com/engine/containers/resource_constraints/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LNX.05 - Mounts، VFS، rootfs، chroot و pivot_root

**Depth:** Internals  
**Prerequisites:** LNX.01, LNX.02

### پوشش اجباری
- VFS و mount tree؛ mount namespace و bind mounts.
- mount propagation: shared/slave/private/unbindable و container implications.
- root filesystem assembly، chroot limitation و pivot_root semantics.
- proc/sys/dev mounts و pseudo-filesystems داخل container.
- masked/readonly paths و device nodes basics.

### Labs / Experiments
- mount namespace بساز و rootfs را با pivot_root/chroot مقایسه کن.

### Failure scenarios
- mount leak due propagation
- missing /proc breaks tools.

### منابع canonical
- [LNX_NS] Linux namespaces(7) - https://man7.org/linux/man-pages/man7/namespaces.7.html
- [OCI_RUNTIME] OCI Runtime Specification - https://specs.opencontainers.org/runtime-spec/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LNX.06 - OverlayFS Internals

**Depth:** Internals  
**Prerequisites:** LNX.05, DKR.21

### پوشش اجباری
- lowerdir/upperdir/workdir/merged و layer stacking.
- copy-up، whiteouts، opaque directories، rename/hardlink/xattr caveats.
- page cache/inode behavior و performance impact awareness.
- OverlayFS در classic Docker vs containerd overlayfs snapshotter conceptual mapping.
- failure modes روی backing filesystems و disk/inode pressure.

### Labs / Experiments
- manual overlay mount بساز؛ delete/modify/rename را انجام بده و upper whiteouts/copy-up را inspect کن.

### منابع canonical
- [LNX_OVERLAY] Linux kernel - OverlayFS - https://docs.kernel.org/filesystems/overlayfs.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LNX.07 - Linux Networking Fundamentals برای Containers

**Depth:** Foundation->Internals  
**Prerequisites:** LNX.01

### پوشش اجباری
- Ethernet/L2، IP/L3، ARP/NDP، routes، gateways، interfaces و MTU.
- sockets، TCP/UDP، listen/bind/connect و localhost/interface semantics.
- Linux routing tables/rules، IP forwarding و sysctl.
- DNS resolver path، /etc/resolv.conf/nsswitch و local stub resolvers.
- network diagnostic mental model: packet path before tools.

### Labs / Experiments
- بدون Docker دو network namespace را با veth متصل و ping/TCP service برقرار کن.

### منابع canonical
- [LNX_NS] Linux namespaces(7) - https://man7.org/linux/man-pages/man7/namespaces.7.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LNX.08 - veth، Linux Bridge، NAT، conntrack و nftables/iptables

**Depth:** Internals  
**Prerequisites:** LNX.07

### پوشش اجباری
- veth peer mechanics و moving endpoint into namespace.
- Linux bridge FDB/L2 switching، bridge ports و gateway interface.
- netfilter hooks/tables/chains، DNAT/SNAT/masquerade و stateful conntrack.
- iptables frontend/history vs nftables backend؛ rule inspection و packet counters.
- port publishing را کاملاً بدون Docker بازسازی کن.

### Labs / Experiments
- یک “mini docker bridge” دستی: namespace+veth+bridge+route+NAT+port forward.

### Failure scenarios
- wrong forward policy
- conntrack stale
- asymmetric route.

### منابع canonical
- [FIREWALL] Docker packet filtering and firewalls - https://docs.docker.com/engine/network/packet-filtering-firewalls/
- [LNX_NS] Linux namespaces(7) - https://man7.org/linux/man-pages/man7/namespaces.7.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LNX.09 - Linux Security: capabilities، seccomp، LSM و devices

**Depth:** Internals  
**Prerequisites:** LNX.01, LNX.03

### پوشش اجباری
- DAC UID/GID/mode bits و supplemental groups.
- capability sets: permitted/effective/inheritable/bounding/ambient و namespaced capabilities.
- seccomp filter model، syscall surface و default-deny/allow trade-offs.
- Linux Security Modules: AppArmor/SELinux concepts و labels/profiles.
- devices، /dev، cgroup/device access history و modern device control.

### Labs / Experiments
- minimal capability set برای یک task پیدا کن؛ seccomp profile سفارشی بساز.

### Failure scenarios
- CAP_SYS_ADMIN overuse
- LSM denial misdiagnosed as permission bit.

### منابع canonical
- [LNX_CAP] Linux capabilities(7) - https://man7.org/linux/man-pages/man7/capabilities.7.html
- [LNX_SECCOMP] Linux seccomp(2) - https://man7.org/linux/man-pages/man2/seccomp.2.html

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LNX.10 - systemd، cgroups و Container Host Integration

**Depth:** Internals+Ops  
**Prerequisites:** LNX.04, DKR.30

### پوشش اجباری
- systemd units/slices/scopes و cgroup ownership/delegation.
- docker.service/docker.socket و restart/order/dependency semantics.
- journal logging و daemon lifecycle during boot/shutdown.
- limits set by systemd vs Docker و nested resource control.
- host hardening، kernel/sysctl/module prerequisites و operational drift.

### Labs / Experiments
- dockerd unit overrides و cgroup placement را inspect کن.

### منابع canonical
- [LNX_CGROUP] Linux kernel - Control Group v2 - https://docs.kernel.org/admin-guide/cgroup-v2.html
- [DOCKERD] dockerd CLI reference - https://docs.docker.com/reference/cli/dockerd/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## P5 Gate
- Gate P5: باید بدون Docker یک container-like process با namespaces+cgroup+rootfs+network بسازی و دقیقاً بگویی هر primitive چه isolation/resource property ایجاد کرده است.

# P6 - OCI، containerd و runc

استاندارد و runtime stack را مستقیماً می‌خوانیم تا Docker دیگر جعبه سیاه نباشد.

## OCI.01 - OCI Image Specification

**Depth:** Spec  
**Prerequisites:** DKR.09, LNX.06

### پوشش اجباری
- Descriptor fields: mediaType, digest, size, annotations, platform/data/artifactType awareness.
- Image manifest، image index، image config، filesystem layers و image layout.
- layer changesets، whiteouts، DiffIDs و rootfs ordering.
- platform selection، annotations، conversion و canonicalization/extensibility.
- رابطه image artifact با runtime bundle.

### Labs / Experiments
- یک OCI layout دستی minimal بساز یا موجود را validate کن؛ descriptor graph را رسم کن.

### منابع canonical
- [OCI_IMAGE] OCI Image Specification - https://specs.opencontainers.org/image-spec/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## OCI.02 - OCI Runtime Specification

**Depth:** Spec  
**Prerequisites:** LNX.02, LNX.04, LNX.05, LNX.09

### پوشش اجباری
- filesystem bundle، config.json و process/root/mounts/hostname/user/env/cwd.
- Linux namespaces/resources/devices/capabilities/seccomp/sysctl/maskedPaths/readOnlyPaths.
- runtime state: creating/created/running/stopped و create/start/kill/delete lifecycle؛ platform-specific configuration sections (Linux و awareness نسبت به Windows/Solaris/FreeBSD additions در نسخه‌های جدید spec) بدون قاطی کردن semantics platformها.
- hooks و زمان/namespace اجرای آنها؛ annotations و features.
- compliance language MUST/SHOULD/MAY و distinction spec vs implementation.

### Labs / Experiments
- runc spec تولید و config.json را field-by-field به kernel mechanisms map کن.

### منابع canonical
- [OCI_RUNTIME] OCI Runtime Specification - https://specs.opencontainers.org/runtime-spec/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## OCI.03 - OCI Distribution Specification

**Depth:** Spec  
**Prerequisites:** DKR.19, OCI.01

### پوشش اجباری
- conformance، pull/push workflows، blobs/manifests و content discovery.
- HTTP endpoints، monolithic/chunked uploads، digest verification و error codes.
- referrers API و unavailable-referrers compatibility behavior.
- content management/delete behavior و registry-specific extensions boundaries.
- فرق Docker Hub product features با OCI distribution protocol.

### Labs / Experiments
- یک manifest/blob را فقط با curl pull کن؛ chunked upload کوچک اجرا کن.

### منابع canonical
- [OCI_DIST] OCI Distribution Specification - https://specs.opencontainers.org/distribution-spec/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## OCI.04 - OCI Artifacts، Referrers و Non-image Content

**Depth:** Spec+Ecosystem  
**Prerequisites:** OCI.01, OCI.03

### پوشش اجباری
- artifactType/subject/referrers و graph of related artifacts.
- SBOM/provenance/signature/model/chart artifacts بر روی OCI distribution.
- media type design و interoperability considerations.
- چرا image index و generic artifacts برای modern supply chain مهم‌اند.
- relation با Docker attestations، DHI، Helm/AI model packaging.

### Labs / Experiments
- referrers یک image دارای attestation را enumerate و graph کن.

### منابع canonical
- [OCI_IMAGE] OCI Image Specification - https://specs.opencontainers.org/image-spec/
- [OCI_DIST] OCI Distribution Specification - https://specs.opencontainers.org/distribution-spec/
- [BUILD_ATTEST] Docker build attestations - https://docs.docker.com/build/metadata/attestations/
- [DHI] Docker Hardened Images - https://docs.docker.com/dhi/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## CTR.01 - containerd Architecture و Plugin/Service Model

**Depth:** Internals  
**Prerequisites:** OCI.01, OCI.02

### پوشش اجباری
- containerd daemon، gRPC APIs، plugin architecture و namespaces (logical multi-tenancy).
- content, images, containers, tasks, snapshots, leases, events, introspection services.
- clients: ctr, nerdctl, Docker/Moby, Kubernetes CRI؛ ctr به‌عنوان debug client نه UX production.
- plugin discovery/configuration و runtime/snapshotter selection.
- مرز containerd با image distribution و low-level runtime.

### Labs / Experiments
- ctr namespaces/plugins/version را inspect کن و objects Docker را در namespace مربوطه پیدا کن.

### منابع canonical
- [CONTAINERD] containerd repository - https://github.com/containerd/containerd
- [CONTAINERD_FLOW] containerd content flow - https://github.com/containerd/containerd/blob/main/docs/content-flow.md

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## CTR.02 - containerd Content Flow، Images، Snapshots، Leases و GC

**Depth:** Internals  
**Prerequisites:** CTR.01

### پوشش اجباری
- registry descriptor -> content store -> image metadata -> unpack -> committed snapshots -> active snapshot.
- compressed blob vs uncompressed filesystem و labels linking them.
- snapshotter concepts، parent chains و mount preparation.
- leases و garbage collection reachability؛ why content may persist/disappear.
- Docker containerd image store mapping و disk usage reasoning.

### Labs / Experiments
- با ctr pull/unpack؛ content ls/snapshot ls/images را correlate کن.

### Failure scenarios
- orphaned content assumptions
- snapshot missing
- GC/lease surprises.

### منابع canonical
- [CONTAINERD_FLOW] containerd content flow - https://github.com/containerd/containerd/blob/main/docs/content-flow.md
- [CONTAINERD_STORE] containerd image store with Docker Engine - https://docs.docker.com/engine/storage/containerd/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## CTR.03 - containerd Containers vs Tasks، Runtime v2 و Shim

**Depth:** Internals  
**Prerequisites:** CTR.01, OCI.02

### پوشش اجباری
- container metadata object در برابر task = live runtime process.
- runtime v2 architecture، shim discovery/naming و ttRPC socket communication.
- 1:1 vs grouped shim patterns؛ lifecycle استقلال container processes از containerd daemon.
- shim -> runc create/start/kill/delete flow و stdio/reaping responsibilities.
- CRI boundary awareness و Kubernetes pod grouping labels بدون ورود کامل به Kubernetes.

### Labs / Experiments
- docker container را با ctr/shim processes و sockets correlate کن؛ containerd restart behavior را observe کن.

### Failure scenarios
- containerd restart vs running task
- shim crash
- runtime not found.

### منابع canonical
- [CONTAINERD_RUNTIME] containerd runtime v2 architecture - https://github.com/containerd/containerd/blob/main/docs/runtime-v2.md

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## RNC.01 - runc CLI، OCI Bundle و Runtime Lifecycle

**Depth:** Internals  
**Prerequisites:** OCI.02, CTR.03

### پوشش اجباری
- runc spec/run/create/start/state/list/exec/kill/delete/pause/resume/update/checkpoint/restore.
- bundle/rootfs/config.json و separation create vs start برای higher-level setup.
- rootless runc و user namespace requirements.
- systemd cgroup driver awareness و runtime feature reporting.
- why runc is low-level and not a full image/network manager.

### Labs / Experiments
- busybox rootfs + runc spec؛ lifecycle را بدون Docker/containerd اجرا کن.

### Failure scenarios
- invalid config
- cgroup permission
- rootfs/mount failure.

### منابع canonical
- [RUNC] runc repository / README - https://github.com/opencontainers/runc
- [OCI_RUNTIME] OCI Runtime Specification - https://specs.opencontainers.org/runtime-spec/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## RNC.02 - libcontainer Internals، Bootstrap/Init و CRIU

**Depth:** Implementation  
**Prerequisites:** RNC.01, LNX.02

### پوشش اجباری
- libcontainer factory/container/process abstractions و native Go implementation.
- دو مرحله bootstrap/init، /proc/self/exe، nsenter و setns/clone sequencing.
- rootfs setup/mounts، namespaces، cgroups، capabilities، seccomp application ordering.
- console/stdio و sync protocol between parent/init.
- checkpoint/restore با CRIU و state transfer limitations.

### Labs / Experiments
- libcontainer code path create/start را trace کن؛ در صورت پشتیبانی checkpoint/restore آزمایشی.

### منابع canonical
- [LIBCONTAINER] runc libcontainer README - https://github.com/opencontainers/runc/blob/main/libcontainer/README.md
- [RUNC] runc repository / README - https://github.com/opencontainers/runc

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## P6 Gate
- Gate P6: باید OCI bundle را دستی اجرا کنی، containerd content/task model را توضیح بدهی و path shim->runc->kernel را از روی docs و process tree دفاع کنی.

# P7 - Source Code Reading و ساخت اجزای مشابه

در این فاز هدف از «فهمیدن» به «توانایی دنبال کردن implementation و تغییر دادن آن» ارتقا پیدا می‌کند.

## SRC.MOB.01 - Moby Repository Architecture، Build و Test

**Depth:** Contributor  
**Prerequisites:** DKR.03, CTR.03, RNC.01

### پوشش اجباری
- repo map: api/client/cmd/daemon/container/containerd/libnetwork/volume/images/graphdriver/internal/integration و build tooling؛ از v29 به بعد تفاوت root module `github.com/moby/moby/v2` با public `github.com/moby/moby/client` و `github.com/moby/moby/api` و release tags مستقل آن‌ها.
- build Moby from source در محیط ایزوله؛ generated code/vendor/modules awareness.
- unit/integration test structure و test selection.
- daemon initialization/dependencies و subsystem ownership.
- contribution guidelines، issue reproduction و security boundaries.

### Labs / Experiments
- Moby را build و یک test کوچک اجرا کن؛ daemon dependency map اولیه بکش.

### منابع canonical
- [MOBY] Moby repository - https://github.com/moby/moby

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## SRC.MOB.02 - Trace کردن Code Paths واقعی در Moby

**Depth:** Contributor  
**Prerequisites:** SRC.MOB.01

### پوشش اجباری
- برای هر behavior مسیر را از CLI/API handler به daemon/service/storage/runtime دنبال کن.
- case studies اجباری: docker ps، docker run، docker exec، docker stop، docker logs، docker pull، docker network create، docker volume create.
- interface boundaries با containerd/libnetwork/volume/image services و error propagation.
- events/state persistence و locking/concurrency نقاط مهم.
- ثبت code map با file/function/commit hash؛ از line-by-line reading بی‌هدف اجتناب کن.

### Labs / Experiments
- حداقل ۸ code-path report مستقل، هرکدام با sequence diagram.

### منابع canonical
- [MOBY] Moby repository - https://github.com/moby/moby
- [API] Docker Engine API reference - https://docs.docker.com/reference/api/engine/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## SRC.CLI.01 - Docker CLI Source و API Mapping

**Depth:** Contributor  
**Prerequisites:** DKR.03, META.DKR.03

### پوشش اجباری
- command tree/Cobra-style command construction، contexts/config/credentials و API client creation.
- formatting/templates/progress streams و UX error handling.
- CLI command -> Engine API mapping و version negotiation.
- CLI plugins architecture برای Compose/Buildx/Model Runner و discovery boundaries.
- tests و backward compatibility behavior.

### Labs / Experiments
- یک command ساده را از parser تا API request trace کن.

### منابع canonical
- [DOCKER_CLI_REPO] Docker CLI repository - https://github.com/docker/cli
- [API] Docker Engine API reference - https://docs.docker.com/reference/api/engine/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## SRC.BLD.01 - BuildKit Source: Solver، Worker، Cache، Executor و Frontend

**Depth:** Contributor  
**Prerequisites:** DKR.14, CTR.02

### پوشش اجباری
- BuildKit repo map: solver, worker, executor, snapshot, cache, source, frontend, exporter, session, client/llb.
- LLB graph ingestion و solver scheduling/caching path.
- worker/executor/snapshotter interfaces و containerd/OCI reuse.
- frontend/gateway و Dockerfile frontend boundary.
- cache records/GC/export/import و content stores.

### Labs / Experiments
- یک Dockerfile build را تا LLB op و solver/worker execution در source trace کن.

### منابع canonical
- [BUILDKIT_REPO] BuildKit repository - https://github.com/moby/buildkit
- [BUILDKIT] Docker BuildKit manual - https://docs.docker.com/build/buildkit/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## SRC.CMP.01 - Compose Specification و Compose Implementation Source

**Depth:** Contributor/Ecosystem  
**Prerequisites:** DKR.28

### پوشش اجباری
- Compose Spec repository/model concepts و Docker Compose Go implementation awareness.
- parse -> interpolation -> normalization -> merge/include -> project model -> Engine API orchestration.
- CLI plugin integration و compatibility surface.
- تفاوت spec-defined behavior با implementation-specific extensions.
- انتخاب یک issue کوچک برای trace یا test.

### Labs / Experiments
- compose config path را در source trace کن.

### منابع canonical
- [COMPOSE_REPO] Docker Compose repository - https://github.com/docker/compose
- [COMPOSE] Compose file reference / Compose Specification implementation - https://docs.docker.com/reference/compose-file/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LAB.01 - ساخت Mini Container Runtime

**Depth:** Capstone  
**Prerequisites:** LNX.02, LNX.04, LNX.05, LNX.08, LNX.09

### پوشش اجباری
- نسخه ۱: process + chroot؛ نسخه ۲: mount/PID/UTS namespaces؛ نسخه ۳: cgroup limits؛ نسخه ۴: network namespace/veth/bridge؛ نسخه ۵: capabilities/seccomp.
- rootfs preparation و exec user process.
- parent-child synchronization و cleanup.
- CLI ساده run/exec/kill/state awareness؛ لزوماً OCI-compliant نیست در ابتدا.
- نسخه اختیاری Go با الهام از libcontainer، بدون copy کردن implementation.

### Labs / Experiments
- runtime خودت را برای busybox اجرا کن و با runc behavior مقایسه کن.

### Failure scenarios
- cleanup leaked namespaces/mounts
- PID1/signal issue
- cgroup permissions.

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LAB.02 - ساخت Mini OCI Image/Registry Explorer

**Depth:** Capstone  
**Prerequisites:** OCI.01, OCI.03, CTR.02

### پوشش اجباری
- HTTP registry client برای manifest/index/blob و digest verification.
- platform manifest selection، blob download/decompress و layer application.
- OCI image layout writer/reader minimal.
- whiteout handling در unpacker به‌عنوان advanced extension.
- attestation/referrer discovery optional.

### Labs / Experiments
- بدون Docker یک image کوچک را pull و rootfs materialize کن.

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## LAB.03 - بازسازی Docker Bridge Networking بدون Docker

**Depth:** Capstone  
**Prerequisites:** LNX.08

### پوشش اجباری
- namespace + veth + bridge + address + route + forwarding + NAT + DNS strategy.
- host port forwarding با netfilter.
- multiple containers و east-west communication.
- cleanup/idempotency script.
- مقایسه packet/rule state با Docker user-defined bridge.

### Labs / Experiments
- اسکریپت کامل create/run/destroy برای mini-network بنویس.

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## P7 Gate
- Gate P7: حداقل یک component را از source build کرده‌ای، چند code path را trace کرده‌ای و runtime/network/image mechanisms را خودت بازسازی کرده‌ای.

# P8 - Cross-platform، Docker Product Ecosystem و قابلیت‌های جدید

این فاز breadth محصولی را می‌دهد تا «Docker expert» فقط معادل Linux Engine expert نباشد؛ وزن این بخش کمتر از Core/Internals است و دائماً version-sensitive است.

## PLT.01 - Docker Desktop Architecture و Host Integration

**Depth:** Product  
**Prerequisites:** DKR.02, LNX.10

### پوشش اجباری
- چرا Linux containers روی macOS/Windows به Linux VM/kernel نیاز دارند؛ Desktop control plane و CLI integration.
- filesystem sharing، networking، DNS/localhost semantics و performance differences.
- VM resource allocation، proxy/cert integration و Kubernetes optional feature awareness.
- Enhanced Container Isolation concept و enterprise hardening boundaries.
- Desktop licensing/organization policy awareness بدون ورود business administration عمیق.

### Labs / Experiments
- روی Desktop در صورت دسترسی، host/container filesystem/network behavior را با native Linux مقایسه کن.

### منابع canonical
- [DESKTOP] Docker Desktop manual - https://docs.docker.com/desktop/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## PLT.02 - Windows: WSL2، Hyper-V و Windows Containers

**Depth:** Product  
**Prerequisites:** PLT.01

### پوشش اجباری
- WSL2 backend architecture و docker-desktop distribution، Linux filesystem performance best practices.
- Hyper-V backend concept و security/isolation trade-offs.
- Linux containers vs Windows containers و Windows kernel/image compatibility.
- Windows networking/storage/process differences و unsupported flags awareness.
- cross-platform Compose/build behavior و path/permission pitfalls.

### Labs / Experiments
- اگر Windows داری، WSL2 data location/performance و Linux-vs-Windows container mode را document کن.

### منابع canonical
- [DESKTOP_WSL] Docker Desktop WSL 2 backend - https://docs.docker.com/desktop/features/wsl/
- [DESKTOP] Docker Desktop manual - https://docs.docker.com/desktop/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## PLT.03 - Docker Hub، Scout و Hardened Images به‌عنوان Product Surface

**Depth:** Product  
**Prerequisites:** DKR.19, DKR.35

### پوشش اجباری
- Hub repositories/orgs/teams/access/tokens/webhooks/trusted content/API و lifecycle policies awareness.
- Scout SBOM/vulnerability/policy workflows و CI integration.
- DHI catalog/minimal images/provenance/VEX/signatures/compliance variants و shared responsibility.
- فرق open standards capabilities با Docker-hosted product features.
- deprecation/retirement tracking برای hosted features؛ docs/release notes source of truth.

### Labs / Experiments
- یک repo آزمایشی Hub + webhook یا Scout workflow در حد دسترسی موجود.

### منابع canonical
- [HUB] Docker Hub manual - https://docs.docker.com/docker-hub/
- [SCOUT] Docker Scout manual - https://docs.docker.com/scout/
- [DHI] Docker Hardened Images - https://docs.docker.com/dhi/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## PLT.04 - Emerging Docker AI/Agent Surface: Model Runner، Sandboxes، MCP Toolkit

**Depth:** Awareness  
**Prerequisites:** OCI.04, PLT.01

### پوشش اجباری
- Docker Model Runner: model artifacts via OCI، local inference engines، OpenAI/Ollama-compatible APIs و Compose integration.
- Docker Sandboxes: isolated microVM sandboxes برای coding agents، daemon/filesystem/network isolation.
- MCP Catalog/Toolkit/Gateway: containerized/remote MCP servers و policy-aware tool integration.
- این محصولات جزء core container runtime mastery نیستند؛ فقط architecture/use-case/security boundaries باید شناخته شوند.
- این module باید پیش از هر مطالعه دوباره against current docs audit شود چون surface سریع تغییر می‌کند.

### Labs / Experiments
- در صورت نیاز شخصی: یک model یا MCP server کوچک با Docker product workflow اجرا کن.

### منابع canonical
- [MODEL] Docker Model Runner - https://docs.docker.com/ai/model-runner/
- [SANDBOX] Docker Sandboxes - https://docs.docker.com/ai/sandboxes/
- [MCP] Docker MCP Catalog and Toolkit - https://docs.docker.com/ai/mcp-catalog-and-toolkit/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## P8 Gate
- Gate P8: می‌توانی توضیح بدهی کدام بخش Docker استاندارد/open-source core است و کدام بخش hosted/Desktop/product feature؛ platform differences را بدون قاطی کردن abstractionها بیان می‌کنی.

# P9 - Production، Failure Engineering، Ecosystem، Contribution و Interview

دانش را تحت فشار production، failure، design trade-offs و مصاحبه تثبیت می‌کند و آن را به contribution واقعی وصل می‌کند.

## OPS.01 - Production Engineering و Lifecycle Management

**Depth:** Production  
**Prerequisites:** DKR.30, DKR.32, DKR.35

### پوشش اجباری
- host provisioning/hardening، upgrade/rollback، capacity planning و resource governance.
- image lifecycle: base updates، rebuild cadence، registry retention، vulnerability response.
- data backup/restore، daemon/containerd data، volume DR و stateless/stateful design.
- logging/metrics/alerts، SLO-oriented observability و incident evidence preservation.
- CI/CD integration، immutable delivery، secrets، rollback و change management.

### Labs / Experiments
- یک production runbook برای host+registry+stateful app تهیه و disaster drill اجرا کن.

### منابع canonical
- [ENGINE] Docker Engine manual - https://docs.docker.com/engine/
- [RELEASE29] Docker Engine v29 release notes - https://docs.docker.com/engine/release-notes/29/
- [SCOUT] Docker Scout manual - https://docs.docker.com/scout/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## OPS.02 - Performance Engineering

**Depth:** Production  
**Prerequisites:** DKR.07, DKR.21, DKR.24

### پوشش اجباری
- CPU throttling/scheduling، memory pressure/page cache/OOM، PIDs و syscall overhead.
- storage CoW/copy-up، bind/volume/filesystem choices و IO benchmarks.
- network NAT/overlay/encryption/MTU overhead و connection scaling.
- image pull/decompression/startup latency؛ lazy snapshotter awareness.
- BuildKit parallelism/cache/context transfer و CI build optimization.

### Labs / Experiments
- baseline benchmark بساز و یک bottleneck CPU/memory/storage/network/build را isolate کن.

### Failure scenarios
- benchmark noise
- host contention misattributed to container.

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## OPS.03 - Failure Engineering و Troubleshooting Matrix

**Depth:** Production  
**Prerequisites:** OPS.01

### پوشش اجباری
- incident categories: daemon, image, pull/auth, build, process, signal, resource, storage, network, DNS, firewall, permissions, security policy, runtime/containerd/runc.
- فرضیه‌محور debugging: symptoms -> boundary -> evidence -> experiment -> root cause -> prevention.
- خطاها را عمداً بساز: disk full/inodes، OOM، DNS، MTU، bad routes، permission/UID، seccomp/capability، daemon config، registry auth، corrupt/unsupported images.
- postmortem format: trigger, contributing factors, detection gap, remediation و test to prevent regression.
- chaos فقط در lab؛ production safety rules.

### Labs / Experiments
- حداقل ۲۰ incident کارت با reproducible setup و expected diagnosis بساز.

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## OPS.04 - Ecosystem Comparison و Boundary Reasoning

**Depth:** Advanced  
**Prerequisites:** CTR.03, RNC.01

### پوشش اجباری
- Docker/Moby/containerd/runc/nerdctl و layers جایگزین‌شده توسط هرکدام.
- Podman/Buildah/Skopeo، CRI-O و daemonless/rootless trade-offs.
- Kubernetes CRI و جایگاه containerd/CRI-O؛ چرا Docker Engine مستقیماً Kubernetes runtime امروز نیست.
- gVisor/Kata/microVM sandbox concepts و stronger isolation trade-offs.
- Wasm/OCI artifacts و nontraditional workloads awareness؛ انتخاب tool بر اساس problem نه brand.

### Labs / Experiments
- یک جدول architecture replacement بساز و یک workload را با Docker و Podman/nerdctl مقایسه کن.

### منابع canonical
- [CONTAINERD] containerd repository - https://github.com/containerd/containerd
- [RUNC] runc repository / README - https://github.com/opencontainers/runc
- [OCI_RUNTIME] OCI Runtime Specification - https://specs.opencontainers.org/runtime-spec/

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## CONTRIB.01 - Contribution Workflow: از Issue تا Merged PR

**Depth:** Contributor  
**Prerequisites:** SRC.MOB.01, SRC.BLD.01

### پوشش اجباری
- انتخاب project: moby/moby, docker/cli, moby/buildkit, containerd/containerd, opencontainers/runc, OCI specs, docker/compose.
- issue triage، reproduction، minimal test case، reading contributing docs و maintainers expectations.
- شروع از docs/test/error-message/small bug؛ سپس behavior changes/features.
- commit hygiene، tests، CI، review iteration و backward compatibility.
- ثبت learning report: چه subsystemی را فهمیدی، چه assumptionsی غلط بود، چه code pathsی یاد گرفتی.

### Labs / Experiments
- حداقل یک issue reproduction عمومی و یک PR واقعی یا patch قابل ارسال.

### منابع canonical
- [MOBY] Moby repository - https://github.com/moby/moby
- [BUILDKIT_REPO] BuildKit repository - https://github.com/moby/buildkit
- [CONTAINERD] containerd repository - https://github.com/containerd/containerd
- [RUNC] runc repository / README - https://github.com/opencontainers/runc
- [COMPOSE_REPO] Docker Compose repository - https://github.com/docker/compose

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## INT.01 - Interview Mastery: 30 seconds / 3 minutes / 30 minutes

**Depth:** Interview  
**Prerequisites:** OPS.03

### پوشش اجباری
- برای هر concept سه depth پاسخ؛ شروع concise و deep dive فقط وقتی interviewer فضا می‌دهد.
- conceptual questions: container vs VM، image، namespaces/cgroups، networking، storage، BuildKit، OCI، containerd/runc.
- operational questions: outage/debugging، security، resource limits، deployment design و trade-offs.
- whiteboard architecture و packet/process/code-path drawing از حافظه.
- هدف: نشان دادن مدل ذهنی و reasoning، نه نمایش superiority نسبت به interviewer.

### Labs / Experiments
- بانک حداقل ۲۰۰ سؤال tiered؛ mock interview هفتگی با study partner.

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## INT.02 - Adversarial Interview و Production Scenario Drills

**Depth:** Interview  
**Prerequisites:** INT.01

### پوشش اجباری
- interviewer فقط symptom می‌دهد و candidate باید سؤال مناسب برای evidence بپرسد.
- cross-layer scenarios که root cause در Linux ولی symptom در Docker است.
- design trade-off: bind vs volume، rootless vs rootful، bridge vs host، Compose vs Swarm/Kubernetes، distroless vs debugability.
- false premise detection: سؤال مصاحبه‌ای که premise آن ناقص/غلط است را محترمانه اصلاح کن.
- post-answer self-review: چه assertionهایی بدون evidence یا version caveat بودند؟

### Labs / Experiments
- هر هفته roles را عوض کنید: interviewer/candidate/observer.

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## CAP.01 - Final Docker Mastery Capstone و Re-certification

**Depth:** Capstone  
**Prerequisites:** CONTRIB.01, INT.02

### پوشش اجباری
- از Docker CLI تا API/Moby/containerd/shim/runc/kernel یک docker run را از حافظه diagram کن و سپس source-verify.
- image را از registry protocol تا content store/snapshot/rootfs/runtime explain و manually inspect کن.
- bridge packet path و storage copy-up path را با kernel primitives explain و reproduce کن.
- یک incident ناشناخته را time-boxed debug کن؛ یک code change را locate و patch prototype کن.
- هر ۶-۱۲ ماه یا پس از major version، selected gates را re-run و syllabus coverage را re-audit کن.

### Labs / Experiments
- دو روز capstone: build+run+break+debug+source trace+teach-back+mock interview.

### Definition of Done مشترک
- توضیح بدون note + diagram از حافظه؛ اجرای lab؛ ایجاد حداقل یک failure؛ توضیح ارتباط با modules مجاور؛ پاسخ 30s/3m/30m؛ teach-back به study partner. برای Internals/Contributor: حداقل یک spec/source code path نیز trace شود.

## P9 Gate
- Gate P9 / Graduation: mastery evidence باید شامل labs، incident reports، code-path reports، حداقل یک contribution attempt و توانایی تدریس/مصاحبه در چند سطح باشد.

# قرارداد Master Prompt و Visual QA برای همه PDFها

- فایل canonical: `meta/prompts/MASTER_PDF_PROMPT.md`. نسخه اصلی ۶۴ بندی کاربر نیز بدون حذف در `meta/prompts/source/REPORT_GENERATION_PROMPT_ORIGINAL.md` نگه‌داری می‌شود.
- precedence: instruction همان document -> Deep Study overrides -> checklist اصلی. override اصلی این پروژه: **Vazirmatn** به‌جای مثال‌های فونت دیگر.
- هر candidate PDF باید structural preflight + font embedding check + render 180-220 DPI داشته باشد.
- **تمام صفحات** باید بصری بازبینی شوند؛ spot-check برای status نهایی پذیرفته نیست.
- defect workflow: `source fix -> rebuild -> rerender -> full review`. اصلاح مستقیم artifact بدون sync source ممنوع است.
- visual review شامل cover، TOC true-RTL، page numbers، borders/margins، headings/orphans، tables، boxes، code/Latin bidi، citations/URLs، glyphs و suspicious blank pages است.
- هر revision از آخرین canonical source ساخته می‌شود و regression fixes قبلی باید حفظ شوند.
- هر PDF باید matching source version، Document ID، research cutoff، source baseline و Visual QA status/date داشته باشد.

# استاندارد PDFهای بعدی

- 1. Document metadata و version baseline
- 2. Scope Contract: In Scope / Out of Scope / Prerequisites
- 3. Learning objectives و Definition of Done
- 4. Why this exists + historical context (فقط به اندازه فهم design)
- 5. Terminology و core mental model
- 6. Architecture / data flow / state machine diagrams
- 7. Detailed mechanics و configuration surface
- 8. Internals و underlying Linux/OCI mechanisms
- 9. Implementation/source-code path (اگر مربوط است)
- 10. Connections به modules دیگر و alternative tools
- 11. Hands-on labs و prediction-before-execution questions
- 12. Failure modes و troubleshooting decision tree
- 13. Production/security/performance considerations
- 14. Common misconceptions و version caveats
- 15. Interview ladder: 30s / 3m / 30m
- 16. Teach-back questions برای study partner
- 17. Mastery checklist و evidence required
- 18. References با provenance و source version/commit در صورت نیاز
- 19. Open questions و changelog
- 20. Typography/layout: Vazirmatn، RTL واقعی، LTR isolation برای code/IDs، A4، margins، border، footer و Persian prose numerals
- 21. Full visual QA report: همه صفحات render/inspect؛ defects و iterationها تا PASS کامل

# روش سیستماتیک استخراج Syllabus از منابع معتبر

## 1. Canonical documentation inventory
navigation رسمی docs را flatten کن و تمام manuals/reference/product sections را inventory کن. این inventory scope موجود را می‌گوید، نه ترتیب آموزش.

## 2. Book TOC extraction
TOC کتاب‌های معتبر را برای pedagogical ordering و مثال‌ها بگیر؛ کتاب به تنهایی معیار completeness یا currency نیست.

## 3. Standards/specifications
هر spec رسمی را section-by-section وارد union کن. موضوعی که در spec هست ولی کتاب ندارد = syllabus gap بالقوه.

## 4. Reference surface audit
CLI/API/file-format/daemon references را برای capability coverage بررسی کن؛ همه flags حفظ نمی‌شوند ولی وجود هر capability باید شناخته شود.

## 5. Source-tree audit
دایرکتوری‌ها/subsystems اصلی source را inventory کن. subsystem بزرگ بدون معادل در syllabus = gap یا deliberate out-of-scope که باید ثبت شود.

## 6. Dependency extraction
برای هر topic prerequisites مفهومی استخراج کن (مثلاً Docker bridge -> namespaces/veth/bridge/routing/NAT/firewall).

## 7. Release/deprecation audit
release notes، deprecated/removed/experimental features را بررسی کن تا syllabus با current behavior sync بماند.

## 8. Union + normalization
topicهای هم‌نام را merge کن ولی provenance را نگه دار؛ هیچ topic فقط چون یک منبع دیگر آن را ندارد حذف نشود.

## 9. Classification
هر topic را Foundation/Core/Production/Internals/Spec/Implementation/Product/Historical دسته‌بندی کن.

## 10. Dependency DAG -> Spiral Order
اول DAG بساز، سپس order آموزشی spiral طراحی کن؛ prerequisiteها را کامل و خطی قبل از موضوع اصلی تمام نکن.

## 11. Coverage Matrix
برای هر topic ستون‌های Book/Docs/Spec/Source/Lab/Failure/Interview/PDF/Done نگه دار.

## 12. Adversarial gap review
از AI و انسان بخواهند مشخصاً «چه چیز مهمی حذف شده؟ چه subsystemی source دارد ولی syllabus ندارد؟» نه اینکه roadmap جدید از حافظه بسازند.

# Protocol مطالعه دونفره

- Weekly Teach Without Notes: یک نفر ۲۰-۳۰ دقیقه موضوع را از حافظه روی تخته توضیح می‌دهد؛ نفر دوم فقط سؤال boundary و counterexample می‌پرسد.
- Attack/Defend: claimهایی مثل “containers are lightweight VMs” یا “namespaces provide security” را یکی دفاع و دیگری نقد می‌کند؛ سپس منبع canonical بررسی می‌شود.
- Mock Incident: interviewer فقط symptom و evidence را مرحله‌ای می‌دهد؛ debugger باید سؤال درست بپرسد، نه command تصادفی بزند.
- Role Rotation: teacher / interviewer / candidate / reviewer عوض شود تا skill توضیح دادن و skill کشف gap هر دو رشد کنند.
- Error Ledger: هر برداشت غلطی که کشف می‌شود با “I assumed X; actual model is Y; evidence: source/lab” ثبت شود.

# ساختار پیشنهادی Repository

- `deep-study/README.md - ورودی پروژه و هدف`
- `deep-study/PROJECT.md - mission و scope بلندمدت`
- `deep-study/STUDY_METHOD.md - روش spiral، labs، teach-back و AI usage`
- `deep-study/CONTENT_STANDARD.md - template اجباری PDFها`
- `deep-study/SOURCE_POLICY.md - hierarchy منابع و copyright policy`
- `deep-study/RESEARCH_METHOD.md - الگوریتم استخراج syllabus/module از منابع`
- `deep-study/MASTERY.md - Definition of Done و gates`
- `deep-study/AGENTS.md - دستورالعمل برای ChatGPT/Codex/agentهای آینده`
- `deep-study/meta/prompts/ - syllabus research, gap analysis, module research, source verification, PDF generation, interview, lab, code trace, update`
- `deep-study/curriculum/devops/docker/ - syllabus.md/pdf, coverage-matrix, dependency-map`
- `deep-study/subjects/docker/ - source Markdown هر module و supporting labs/diagrams`
- `deep-study/pdf/docker/ - PDFهای generated مطالعه`
- `deep-study/library/catalog.* - metadata و لینک/وضعیت ownership کتاب‌ها؛ فایل commercial book فقط اگر license/حق نگهداری اجازه دهد.`

# Source Policy و کتاب‌ها

- Source of Truth فنی: official docs/specs/source code. کتاب برای coherence و pedagogical order است، نه current truth.
- کتاب اصلی پیشنهادی: Docker: Up & Running, 3rd Edition؛ companion: Docker Deep Dive, 4th Edition. هر دو با docs/specs فعلی reconcile می‌شوند.
- فایل کتاب‌های تجاری داخل Git repo قرار نگیرد مگر license/حق استفاده صراحتاً اجازه دهد. در repo catalog metadata، ownership status، edition و لینک قانونی نگه‌داری شود.
- منابع open-source/specifications بر اساس license خودشان مدیریت و در صورت vendor کردن، license/commit/version ثبت شود.

# Coverage Matrix Schema

| Topic ID | Study PDF | Book | Docs | Spec | Source | Lab | Failure | Interview | Version reviewed | Mastered |
|---|---|---|---|---|---|---|---|---|---|---|
| DKR.09 | planned | بله | بله | as applicable | as applicable | بله | بله | بله | 2026-08-11 |  |
| DKR.24 | planned | بله | بله | as applicable | as applicable | بله | بله | بله | 2026-08-11 |  |
| LNX.04 | planned | بله | بله | as applicable | as applicable | بله | بله | بله | 2026-08-11 |  |
| OCI.02 | planned | بله | بله | as applicable | as applicable | بله | بله | بله | 2026-08-11 |  |
| CTR.03 | planned | بله | بله | as applicable | as applicable | بله | بله | بله | 2026-08-11 |  |
| RNC.02 | planned | بله | بله | as applicable | as applicable | بله | بله | بله | 2026-08-11 |  |
| SRC.MOB.02 | planned | بله | بله | as applicable | as applicable | بله | بله | بله | 2026-08-11 |  |
| OPS.03 | planned | بله | بله | as applicable | as applicable | بله | بله | بله | 2026-08-11 |  |

# Mastery Checklist عمومی

- می‌توانم مفهوم را بدون jargon اضافی در 30 ثانیه تعریف کنم.
- می‌توانم در 3 دقیقه mechanism و trade-off اصلی را توضیح بدهم.
- می‌توانم در 30 دقیقه internals، failure modes و connections را deep-dive کنم.
- می‌توانم architecture/state/data flow را از حافظه رسم کنم.
- می‌توانم capability یا flag دقیق را از reference پیدا کنم بدون تکیه به حفظ.
- حداقل یک happy-path lab و یک break/fix lab اجرا کرده‌ام.
- می‌توانم common misconceptions و version caveats را بگویم.
- اگر module internals است، spec/source code را مستقیم خوانده و evidence ثبت کرده‌ام.
- می‌توانم موضوع را به نفر دوم تدریس کنم و به counterexampleهای او پاسخ بدهم.
- Open questions باقی‌مانده صریحاً ثبت شده‌اند؛ “فهمیدم” جای سؤال حل‌نشده را نمی‌گیرد.

# Prompt pattern برای استخراج/به‌روزرسانی Syllabus

```text
I am maintaining an expert-level Docker syllabus.
Use ONLY the supplied canonical documentation inventory, specification TOCs, source-tree inventory, release/deprecation notes, and selected book TOCs as evidence.
1) Build the UNION of topics without dropping topics that appear in only one authoritative source.
2) Preserve provenance for every topic.
3) Classify each topic: Foundation / Core / Production / Internals / Spec / Implementation / Product / Historical.
4) Extract prerequisites and build a dependency DAG.
5) Identify gaps: docs-without-syllabus, spec-without-syllabus, major source subsystem-without-syllabus, reference capability-without-syllabus.
6) Mark version-sensitive, deprecated, experimental, and platform-specific topics.
7) Do NOT generate study order until the inventory and gap review are complete.
8) After approval, turn the DAG into a spiral study order and propose labs/failure/source-reading evidence for each module.
```

# Bibliography / Canonical Source Registry

- **DOCS** - Docker Documentation: https://docs.docker.com/
- **ENGINE** - Docker Engine manual: https://docs.docker.com/engine/
- **RELEASE29** - Docker Engine v29 release notes: https://docs.docker.com/engine/release-notes/29/
- **API** - Docker Engine API reference: https://docs.docker.com/reference/api/engine/
- **CLI** - Docker CLI reference: https://docs.docker.com/reference/cli/docker/
- **CONTEXTS** - Docker contexts: https://docs.docker.com/engine/manage-resources/contexts/
- **PLUGINS** - Docker Engine managed plugins: https://docs.docker.com/engine/extend/
- **PLUGIN_API** - Docker Plugin API: https://docs.docker.com/engine/extend/plugin_api/
- **DOCKERD** - dockerd CLI reference: https://docs.docker.com/reference/cli/dockerd/
- **DOCKERFILE** - Dockerfile reference: https://docs.docker.com/reference/dockerfile/
- **BUILD** - Docker Build manual: https://docs.docker.com/build/
- **BUILDKIT** - Docker BuildKit manual: https://docs.docker.com/build/buildkit/
- **BUILD_ATTEST** - Docker build attestations: https://docs.docker.com/build/metadata/attestations/
- **CDI** - Docker Build CDI: https://docs.docker.com/build/building/cdi/
- **COMPOSE** - Compose file reference / Compose Specification implementation: https://docs.docker.com/reference/compose-file/
- **STORAGE** - Docker Engine storage: https://docs.docker.com/engine/storage/
- **CONTAINERD_STORE** - containerd image store with Docker Engine: https://docs.docker.com/engine/storage/containerd/
- **NETWORK** - Docker Engine networking: https://docs.docker.com/engine/network/
- **FIREWALL** - Docker packet filtering and firewalls: https://docs.docker.com/engine/network/packet-filtering-firewalls/
- **RESOURCE** - Docker container resource constraints: https://docs.docker.com/engine/containers/resource_constraints/
- **GPU** - Docker Engine GPU access: https://docs.docker.com/engine/containers/gpu/
- **ROOTLESS** - Docker rootless mode: https://docs.docker.com/engine/security/rootless/
- **USERNS** - Docker user namespace remapping: https://docs.docker.com/engine/security/userns-remap/
- **SWARM** - Docker Swarm mode: https://docs.docker.com/engine/swarm/
- **DESKTOP** - Docker Desktop manual: https://docs.docker.com/desktop/
- **DESKTOP_WSL** - Docker Desktop WSL 2 backend: https://docs.docker.com/desktop/features/wsl/
- **HUB** - Docker Hub manual: https://docs.docker.com/docker-hub/
- **SCOUT** - Docker Scout manual: https://docs.docker.com/scout/
- **DHI** - Docker Hardened Images: https://docs.docker.com/dhi/
- **MODEL** - Docker Model Runner: https://docs.docker.com/ai/model-runner/
- **SANDBOX** - Docker Sandboxes: https://docs.docker.com/ai/sandboxes/
- **MCP** - Docker MCP Catalog and Toolkit: https://docs.docker.com/ai/mcp-catalog-and-toolkit/
- **OCI_IMAGE** - OCI Image Specification: https://specs.opencontainers.org/image-spec/
- **OCI_RUNTIME** - OCI Runtime Specification: https://specs.opencontainers.org/runtime-spec/
- **OCI_DIST** - OCI Distribution Specification: https://specs.opencontainers.org/distribution-spec/
- **LNX_NS** - Linux namespaces(7): https://man7.org/linux/man-pages/man7/namespaces.7.html
- **LNX_CGROUP** - Linux kernel - Control Group v2: https://docs.kernel.org/admin-guide/cgroup-v2.html
- **LNX_OVERLAY** - Linux kernel - OverlayFS: https://docs.kernel.org/filesystems/overlayfs.html
- **LNX_CAP** - Linux capabilities(7): https://man7.org/linux/man-pages/man7/capabilities.7.html
- **LNX_SECCOMP** - Linux seccomp(2): https://man7.org/linux/man-pages/man2/seccomp.2.html
- **CONTAINERD_RUNTIME** - containerd runtime v2 architecture: https://github.com/containerd/containerd/blob/main/docs/runtime-v2.md
- **CONTAINERD_FLOW** - containerd content flow: https://github.com/containerd/containerd/blob/main/docs/content-flow.md
- **CONTAINERD** - containerd repository: https://github.com/containerd/containerd
- **RUNC** - runc repository / README: https://github.com/opencontainers/runc
- **LIBCONTAINER** - runc libcontainer README: https://github.com/opencontainers/runc/blob/main/libcontainer/README.md
- **MOBY** - Moby repository: https://github.com/moby/moby
- **DOCKER_CLI_REPO** - Docker CLI repository: https://github.com/docker/cli
- **BUILDKIT_REPO** - BuildKit repository: https://github.com/moby/buildkit
- **COMPOSE_REPO** - Docker Compose repository: https://github.com/docker/compose
- **BOOK_UR** - Docker: Up & Running, 3rd ed. - Sean P. Kane, Karl Matthias: https://www.oreilly.com/library/view/docker-up/9781098131814/
- **BOOK_DD** - Docker Deep Dive, 4th ed. - Nigel Poulton: https://www.packtpub.com/en-us/product/docker-deep-dive-9781837028344

# Change Policy
- Document versioning: MAJOR برای scope-breaking، MINOR برای coverage/source-baseline مهم، PATCH برای factual/layout/citation fix محدود.
- هر تغییر foundational باید downstream impact list داشته باشد و PDFهای potentially invalidated را مشخص کند.
- هر تغییر syllabus باید دلیل، منبع، affected IDs و تاریخ review داشته باشد. حذف topic فقط با deliberate out-of-scope rationale مجاز است.
- قبل از ساخت PDF هر module، همان module دوباره current-audit می‌شود؛ این syllabus نقشه است، نه جایگزین verification نسخه فعلی.

# Changelog - v1.1.0

- Master PDF Prompt / Vazirmatn / full-page visual QA contract به syllabus اضافه شد.
- research cutoff به 2026-08-11 ارتقا یافت و latest verification rule از search snippet به canonical-page verification سخت‌گیرانه‌تر شد.
- current baseline روی Docker Engine 29.7.2 و OCI Runtime 1.3.0 / Image 1.1.1 / Distribution 1.1.1 تثبیت شد.
- version-sensitive deltaهای Engine 29.x (containerd image store، embedded-containerd experimental، image mounts، cgroup v1 deprecation، rootless default changes، Moby Go module changes) به map اضافه شدند.
- DKR.39 برای managed/legacy Docker Engine Plugin System و extension APIs اضافه شد.
- coverage موضوعات contexts، system maintenance/transfer operations، BuildKit GC/sessions، networking options، source-module versioning و platform-specific OCI runtime awareness تقویت شد.
