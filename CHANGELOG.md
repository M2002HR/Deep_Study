# Changelog

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
