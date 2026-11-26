# Colosseum in Tokyo S.E.T.I

A semantic technique engine by A Elite Estrangeira: fourteen system-hardening techniques, searchable through Oracle's own augmented embedding models, locally or inside the database.

## The engine

The engine is Oracle's own: their prebuilt **augmented** ONNX embedding models, run unchanged. The tokenizer and the pre/post-processing are baked into each model file by Oracle, so the input is raw text and the output is a 384-dimension embedding. Ranking is cosine similarity between the query embedding and each technique's embedding.

Two entry points share the same corpus and the same models:

- `engine.py` — local search over `corpus.json` with an ONNX session.
- `db_engine.py` — the database engine: the corpus as the `TECHNIQUES` table, both vector columns populated inside the database by `VECTOR_EMBEDDING`, with six search modes (exact, approximate over HNSW/IVF indexes, hybrid vector+text, Private AI provider, RAG retrieval with chunking, and ORDS REST).

## The techniques

The corpus holds fourteen hardening techniques, each a short card: default deny, per-request authorization, least privilege, contested network assumption, resource inventory, categorization by criticality, enforcement point coverage, compensating controls, bounded input handling, origin and host validation, monitor and assess loop, release authorization, fail-closed automation, and tailoring to what exists.

The techniques live in `corpus.json`; for the database, `data/techniques.dmp` is the Data Pump export of the `TECHNIQUES` table (round-trip verified), defined by `data/techniques_schema.sql`.

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
