-- TECHNIQUES table for the database engine (db_engine.py).
-- The corpus of record is corpus.json; load its rows into this table,
-- populate both vector columns with VECTOR_EMBEDDING, then export with
-- Data Pump to produce data/techniques.dmp.

CREATE TABLE techniques (
    id          VARCHAR2(16) PRIMARY KEY,
    title       VARCHAR2(200) NOT NULL,
    text        VARCHAR2(4000) NOT NULL,
    minilm_vector VECTOR(384, FLOAT32),
    e5_vector     VECTOR(384, FLOAT32)
);

-- After loading the rows and the in-database models:
--   UPDATE techniques SET minilm_vector = VECTOR_EMBEDDING(minilm_l12_v2 USING title || '. ' || text AS data);
--   UPDATE techniques SET e5_vector     = VECTOR_EMBEDDING(e5_small     USING title || '. ' || text AS data);
--   CREATE VECTOR INDEX tech_hnsw_idx ON techniques (e5_vector) ORGANIZATION NEIGHBOR PARTITIONS DISTANCE COSINE;
--   CREATE VECTOR INDEX tech_ivf_idx  ON techniques (minilm_vector) ORGANIZATION CENTROID PARTITIONS DISTANCE COSINE;
