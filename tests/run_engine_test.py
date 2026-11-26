"""End-to-end check: known questions must rank their technique first.

Runs engine.py's ranking in-process for both models and asserts the
expected top-1 technique for each question. Exit code 0 means every
question ranked correctly.
"""

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine import MODELS, embed, load_session  # noqa: E402

CASES = [
    ("how do I refuse unknown routes by default", "zt-01"),
    ("should a previous approval carry trust to the next request", "zt-02"),
    ("how do I limit a component to only the permissions it needs", "zt-03"),
    ("is being inside the network enough to trust a request", "zt-04"),
    ("what do I need to list before I can protect a system", "zt-05"),
    ("how do I classify resources by the damage a compromise would cause", "zt-06"),
    ("how do I make sure no path reaches a resource unchecked", "zt-07"),
    ("what if a resource cannot carry a strong control itself", "zt-08"),
    ("how do I stop one slow client from blocking the others", "zt-09"),
    ("how do I validate the host a request claims to come from", "zt-10"),
    ("is protection a one-time setup or a continuous loop", "zt-11"),
    ("what must be checked before a release ships", "zt-12"),
    ("should a script continue after a failed verification", "zt-13"),
    ("should I invent identities to satisfy a security model", "zt-14"),
]


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "corpus.json"), encoding="utf-8") as f:
        corpus = json.load(f)
    failures = 0
    for name in ("e5", "minilm"):
        session = load_session(MODELS[name])
        docs = [f"{item['title']}. {item['text']}" for item in corpus]
        doc_vecs = embed(session, docs)
        doc_vecs = doc_vecs / np.linalg.norm(doc_vecs, axis=1, keepdims=True)
        for question, expected in CASES:
            qv = embed(session, [question])[0]
            qv = qv / np.linalg.norm(qv)
            top = corpus[int(np.argmax(doc_vecs @ qv))]["id"]
            ok = top == expected
            failures += 0 if ok else 1
            print(f"{name} {'PASS' if ok else 'FAIL'} {expected} -> {top} | {question}")
    total = len(CASES) * 2
    print(f"{total - failures}/{total} top-1 correct")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
