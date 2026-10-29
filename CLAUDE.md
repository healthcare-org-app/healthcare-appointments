# Working on this repo

Contract-first Flask API: `openapi.yaml` at the root, code in `app/`, pytest in `tests/`, Postman collection in `postman/`. CI checks: `ci` (pytest) and `quality-gate` (config `quality-gate.yml`). Service facts (name, port, dependencies) are in `service.yaml` and `.postman/resources.yaml`.

For any change to the contract, the code or the Postman objects, follow the `healthcare-api-quality-gate:gate-loop` skill: work on a branch, your session codes, `gate-verdict` reviews, the gate decides.

## Local commands

- `pytest -q`
- `npx github:healthcare-org-app/healthcare-api-quality-gate#v1 run` (after `postman login`)

## Service-specific rules

- Never call `https://myhealthcare.dev` (production). The collection's `baseUrl` stays `http://localhost:8600`.
