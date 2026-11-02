# python/Makefile — the Python SDK lane of the kion-sdk monorepo.
#
# Consumes the shared, language-agnostic spec at $(SPEC_DIR)/<v>/openapi3.json
# (produced by ../preprocess, driven by the root Makefile) and generates the
# typed Python client per Kion version into src/kion_sdk/<v>/.
#
# openapi-python-client emits packages with relative imports, so each version's
# generated code drops straight in as the kion_sdk.<v> sub-package — the Python
# analogue of the go lane's generated/<v>. The hand-written wrapper lives in
# src/kion_sdk/ (version-agnostic: client factory, query-string transport, auth,
# options, errors). Generation is normally driven by the root orchestrator
# (`make gen LANG=python VERSION=<v>`).

.PHONY: help install-python generate scaffold-version build test lint fmt clean

.DEFAULT_GOAL := help

# Shared spec directory, produced by ../preprocess.
SPEC_DIR ?= ../spec

# Pinned generator version (analogue of the go lane's OGEN_VERSION).
OPC_VERSION := 0.29.0

PKG_DIR := src/kion_sdk

## help: Show this help.
help:
	@echo "kion-sdk python lane — typed Python SDK for the Kion API"
	@echo ""
	@echo "  make generate-<v>   regenerate one version from \$$(SPEC_DIR)/<v>/openapi3.json"
	@echo "                      into src/kion_sdk/<v>/ (importable as kion_sdk.<v>)"
	@echo "  make build          build wheel + sdist (uv build)"
	@echo "  make test           run unit tests (pytest)"
	@echo "  make lint / fmt     ruff check / format"
	@echo ""
	@echo "  SPEC_DIR=$(SPEC_DIR)  OPC_VERSION=$(OPC_VERSION)"

## install-python: no-op placeholder (generator is fetched on demand via uvx).
install-python:
	@echo "python lane uses uvx to fetch openapi-python-client@$(OPC_VERSION) on demand; nothing to install."

## scaffold-version: no-op. openapi-python-client --meta none generates the
##                   whole per-version package, and the client factory is the
##                   version-agnostic _wrapper — nothing to hand-write. Defined
##                   so the root scaffold-version, which loops every lane, does
##                   not die here.
scaffold-version:
	@echo "python lane needs no per-version scaffolding (the _wrapper takes the version as an argument)."

# Regenerate ONE version's client from the shared spec into src/kion_sdk/<v>/.
# openapi-python-client requires the parent dir to exist and the target NOT to
# pre-exist, so we rm the target and mkdir the parent. --meta none = no
# per-version project scaffolding; the lane's top-level pyproject packages every
# version + the wrapper together. The .ruff_cache the generator drops is removed.
# Usage: make generate-v3_16   (or via root: make gen LANG=python VERSION=v3_16)
generate-%:
	rm -rf $(PKG_DIR)/$*
	mkdir -p $(PKG_DIR)
	uvx --from openapi-python-client==$(OPC_VERSION) openapi-python-client generate \
	  --path $(SPEC_DIR)/$*/openapi3.json --meta none --output-path $(PKG_DIR)/$*
	rm -rf $(PKG_DIR)/$*/.ruff_cache

## build: Build wheel + sdist.
build:
	uv build

## test: Run unit tests.
test:
	uv run --extra dev pytest -q

# ruff comes from uv.lock (the dev extra), the same version CI runs. This was
# `uvx ruff`, which resolves the NEWEST ruff on every call: local lint then
# disagreed with CI whenever ruff shipped a rule or formatter change (RUF022
# fired locally, never in CI).
RUFF := uv run --extra dev ruff
RUFF_PATHS := src/kion_sdk/_wrapper tests

## lint: Lint + format-check the hand-written wrapper (generated code is
##       excluded in pyproject). Matches the test:python CI job.
lint:
	$(RUFF) check $(RUFF_PATHS)
	$(RUFF) format --check $(RUFF_PATHS)

## fmt: Format the hand-written wrapper.
fmt:
	$(RUFF) format $(RUFF_PATHS)

## clean: Remove build artifacts.
clean:
	rm -rf dist build .ruff_cache
