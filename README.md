# Colosseum in Tokyo S.E.T.I

A semantic technique engine by A Elite Estrangeira: fourteen system-hardening techniques, searchable through Oracle's own augmented embedding models, locally or inside the database.

## The engine

The engine is Oracle's own: their prebuilt **augmented** ONNX embedding models, run unchanged. The tokenizer and the pre/post-processing are baked into each model file by Oracle, so the input is raw text and the output is a 384-dimension embedding. Ranking is cosine similarity between the query embedding and each technique's embedding.

Two entry points share the same corpus and the same models:

- `engine.py` — local search over `corpus.json` with an ONNX session.
- `db_engine.py` — the database engine: the corpus as the `TECHNIQUES` table, both vector columns populated inside the database by `VECTOR_EMBEDDING`, with six search modes (exact, approximate over HNSW/IVF indexes, hybrid vector+text, Private AI provider, RAG retrieval with chunking, and ORDS REST).

## How it maximizes a project

Think of the engine as a weapon aimed at a project: you fire a problem at it, and it returns the technique that solves that problem, ranked by relevance. The loop is always the same:

1. **Aim** — describe the project's weak point in plain words ("unknown routes reach the backend", "the release shipped without a signature check").
2. **Fire** — the engine embeds the problem and ranks every technique against it, locally or inside the database.
3. **Apply** — the top technique is applied only where it hardens code that already exists. Nothing is invented: no fake identities, no decorative panels.
4. **Verify** — tests, hashes, and the release checklist prove the improvement before it ships.

Today the magazine holds the techniques of **one book** — fourteen cards. The library behind it holds more than a thousand books. Each new book read page by page adds its cards to the same corpus, and every project the engine is aimed at gets stronger with each one.

## The techniques

Fourteen hardening techniques, organized by what they do:

**Decide** — who and what gets through:

- **Default Deny** (`zt-01`) — answer only what the system was built to answer; everything else is refused.
- **Per-Request Authorization** (`zt-02`) — every request is decided on its own merits; trust never carries forward.
- **Least Privilege** (`zt-03`) — each component holds only the permissions its job requires.

**Know** — what you actually have:

- **Resource Inventory** (`zt-05`) — a written list of services, ports, files, identities, and data flows.
- **Categorization by Criticality** (`zt-06`) — classify by damage, and let the class set the control level.

**Enforce** — checks in front of everything:

- **Contested Network Assumption** (`zt-04`) — every path, including loopback, is treated as hostile until proven otherwise.
- **Enforcement Point Coverage** (`zt-07`) — a check in front of every resource, with no unchecked path around it.
- **Compensating Controls** (`zt-08`) — surround a weak resource with bounds, validation, and logging it cannot carry itself.
- **Bounded Input Handling** (`zt-09`) — size, time, and concurrency limits; oversized and malformed input refused early.
- **Origin and Host Validation** (`zt-10`) — reject unexpected hosts so name confusion cannot redirect trust.

**Operate** — keep it true over time:

- **Monitor and Assess Loop** (`zt-11`) — log refusals and failures, reassess, adjust; protection is a loop, not a state.
- **Release Authorization** (`zt-12`) — every release earns approval against a written checklist.
- **Fail-Closed Automation** (`zt-13`) — scripts stop on the first failed check; a missing verification is a failure.
- **Tailoring to What Exists** (`zt-14`) — apply knowledge only where it hardens what the project really contains.

The techniques live in `corpus.json`; for the database, `data/techniques.dmp` is the Data Pump export of the `TECHNIQUES` table (round-trip verified), defined by `data/techniques_schema.sql`.

## Tested on Oracle AI Database 26ai

The database engine was exercised end to end on Oracle AI Database 26ai Free: both models loaded in-database, all 14 vector pairs populated by `VECTOR_EMBEDDING`, and `db_engine.py` search returns the correct technique first (for example, "how do I refuse unknown routes by default" → **Default Deny**, 0.8825), matching the local engine's top result.

## Usage

```bash
pip install -r requirements.txt
python engine.py "how do I refuse unknown routes by default"
python engine.py "como limitar permissoes" --model e5 --top 3
python db_engine.py "how do I refuse unknown routes by default"
python db_engine.py "least privilege" --mode hybrid
```

Models, in `models/` (Oracle's prebuilt augmented exports, via Git LFS):

- `all_MiniLM_L12_v2.onnx` — English-first, 384 dimensions
- `multilingual_e5_small.onnx` — 100 languages, 384 dimensions

## Tests

`tests/run_engine_test.py` runs fourteen known questions against both models and asserts the expected technique ranks first in every case (28/28).

## License

Copyright A Elite Estrangeira. Model attribution is in `models/LICENSE_ATTRIBUTION.txt`.
