# Cross-Document Consistency Contract

Deep Study will eventually contain hundreds of PDFs. Consistency is therefore a first-class data problem, not a stylistic preference.

## Ownership

Every concept that can create conflicting definitions should have an owner document. A downstream PDF may summarize it, but must link to the owner and must not silently fork the definition.

Examples for the Docker track:

- OCI runtime lifecycle -> `OCI.02`
- cgroup v2 mechanics -> `LNX.04`
- Docker bridge packet path -> `DKR.24` with Linux primitives owned by `LNX.07/LNX.08`
- containerd shim/runtime v2 -> `CTR.03`

## Before writing a PDF

The author/agent must inspect:

1. current syllabus node;
2. prerequisite owner documents;
3. upstream/downstream references;
4. terminology registry;
5. current baseline and source registry;
6. existing PDFs that overlap the Scope Contract.

## Duplicate content

Duplication is allowed only for orientation. Deep mechanics should have one canonical owner. Repeated material must either:

- be a short recap with a cross-reference; or
- be explicitly specialized for a different context and state how it differs.

## Version drift

When a foundational owner changes, list potentially affected downstream Document IDs. Re-review them before claiming they remain canonical.

## Terminology

Use stable project terminology. When upstream projects use ambiguous or historically overloaded terms, state the exact layer/context instead of normalizing away the distinction.

## Release gate

A PDF cannot become `canonical` while it has an unresolved contradiction with another canonical owner document.
