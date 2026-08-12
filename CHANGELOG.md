# Changelog

## 2026-08-12 - DKR.02 v1.0.0 published

- Published `DS-DKR-02 / DKR.02 - نصب، Editions، Platforms و Distribution v1.0.0` as a 42-page canonical Study PDF.
- Reverified version-sensitive installation, API compatibility, contexts, rootless, remote access and Desktop/platform claims against official Docker sources with research cutoff `2026-08-12`.
- Candidate pass 1 was rejected after full visual QA because of Latin automatic page counters, mixed-direction cover subtitle ordering and font fallback; source/CSS were fixed and the PDF was rebuilt from scratch.
- Final exact candidate Run `31617684197` passed mechanical preflight and 42/42-page visual review at 180 DPI; cover, TOC, comparison table, labs/topology, evidence table, references and final page were checked at full size.
- Final PDF SHA256: `109e9d47c69cdecc33ab5e70be8e13baf7a224edc8a172b88fe33a69cadb0ab6`.
- Final font set is strictly embedded Vazirmatn Regular/Medium/Bold.
- Updated shared Study PDF CSS so table cells are centered/middle-aligned per the preserved 64-rule checklist and automatic footer/TOC counters render with Persian digits.
- `DKR.01` learner mastery remains `not assessed`; publication of DKR.02 does not advance learner progression.
- Next authoring target after publication is `DKR.03`.

## 2026-08-12 - DKR.02 preparation and state hardening

- Added `meta/standards/PROGRESSION_AND_PREREQUISITES.md` to separate authoring eligibility, publication, operational prerequisite readiness and learner mastery.
- Marked `DKR.02` as the next eligible authoring target without falsely marking `DKR.01` as mastered.
- Clarified `META.DKR.02` as an operational/environment prerequisite whose readiness evidence is required before the practical DKR.02 Lab.
- Synchronized `DKR.01` in the Docker coverage matrix from stale `planned/pending` to `published-canonical` with Visual QA PASS.
- Added generic validation for every `published-canonical` Study PDF through `scripts/check_published_study_docs.sh`.
- Replaced the document-contract DKR.01-only validation path with registry/manifest-driven published Study PDF validation.
- Added reusable Study PDF build and promotion workflows for modules after DKR.01.
- Added a generic exact-candidate visual-approval contract template.
- Updated continuation/bootstrap/agent instructions so future sessions can distinguish content authoring from learner progression.

## 2026-08-12 - Direct-to-main workflow

- Repository canonical/default branch is `main`.
- Normal project changes are committed directly to `main` without an automatic feature branch or Pull Request.
- Previous bootstrap PR was merged; later workflow/document updates and canonical PDF promotions were committed directly to `main`.

## 2026-08-11 - Docker foundation and first study document

- Canonical Docker Mastery Syllabus v1.1.0 published after full visual QA.
- First official Docker study document `DS-DKR-01 / DKR.01 - تاریخچه و مدل ذهنی کانتینر v1.0.0` published as a 37-page canonical Study PDF after full visual QA.
- Learner mastery remains separate from publication and was not automatically advanced.

## Repository bootstrap

- Canonical Deep Study governance documents.
- Enhanced master PDF prompt with preserved original 64-rule checklist.
- Vazirmatn-only Persian PDF standard and reproducible pinned font validation.
- Docker Mastery Syllabus v1.1.0 with corrected current baseline and coverage governance.
- Templates for scope, modules, research logs, incidents and coverage.
- Prompt library for research, gap analysis, source verification, labs, interviews, source tracing and updates.
