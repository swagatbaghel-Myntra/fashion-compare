-- Threadly PostgreSQL foundation
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE brands (
 id BIGSERIAL PRIMARY KEY,
 name TEXT NOT NULL UNIQUE,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE canonical_products (
 id UUID PRIMARY KEY,
 brand_id BIGINT REFERENCES brands(id),
 title TEXT NOT NULL,
 gender TEXT,
 category TEXT NOT NULL,
 article_type TEXT NOT NULL,
 attributes JSONB NOT NULL DEFAULT '{}',
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_product_article_type ON canonical_products(article_type);
CREATE INDEX idx_product_attributes_gin ON canonical_products USING GIN(attributes);

CREATE TABLE product_variants (
 id UUID PRIMARY KEY,
 product_id UUID NOT NULL REFERENCES canonical_products(id) ON DELETE CASCADE,
 colour TEXT,
 size_system TEXT,
 attributes JSONB NOT NULL DEFAULT '{}'
);
CREATE TABLE retailers (
 id BIGSERIAL PRIMARY KEY,
 name TEXT NOT NULL UNIQUE,
 base_url TEXT,
 active BOOLEAN NOT NULL DEFAULT true
);
CREATE TABLE retailer_listings (
 id UUID PRIMARY KEY,
 retailer_id BIGINT NOT NULL REFERENCES retailers(id),
 canonical_product_id UUID REFERENCES canonical_products(id),
 external_id TEXT NOT NULL,
 external_url TEXT,
 title TEXT NOT NULL,
 raw_payload JSONB,
 last_seen_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 UNIQUE(retailer_id,external_id)
);
CREATE INDEX idx_listing_canonical ON retailer_listings(canonical_product_id);

CREATE TABLE listing_variants (
 id UUID PRIMARY KEY,
 listing_id UUID NOT NULL REFERENCES retailer_listings(id) ON DELETE CASCADE,
 retailer_size TEXT,
 normalized_size TEXT,
 available BOOLEAN NOT NULL DEFAULT false,
 UNIQUE(listing_id,retailer_size)
);
CREATE TABLE price_snapshots (
 id BIGSERIAL PRIMARY KEY,
 listing_id UUID NOT NULL REFERENCES retailer_listings(id) ON DELETE CASCADE,
 captured_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 mrp NUMERIC(12,2),
 selling_price NUMERIC(12,2) NOT NULL CHECK(selling_price >= 0),
 effective_price NUMERIC(12,2),
 currency CHAR(3) NOT NULL DEFAULT 'INR'
);
CREATE INDEX idx_price_listing_time ON price_snapshots(listing_id,captured_at DESC);
CREATE TABLE inventory_snapshots (
 id BIGSERIAL PRIMARY KEY,
 listing_variant_id UUID NOT NULL REFERENCES listing_variants(id) ON DELETE CASCADE,
 captured_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 available BOOLEAN NOT NULL
);
CREATE TABLE match_candidates (
 id UUID PRIMARY KEY,
 left_listing_id UUID NOT NULL REFERENCES retailer_listings(id),
 right_listing_id UUID NOT NULL REFERENCES retailer_listings(id),
 confidence NUMERIC(5,4) CHECK(confidence BETWEEN 0 AND 1),
 status TEXT NOT NULL CHECK(status IN ('pending','accepted','rejected')),
 evidence JSONB NOT NULL DEFAULT '{}',
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE product_embeddings (
 product_id UUID PRIMARY KEY REFERENCES canonical_products(id) ON DELETE CASCADE,
 text_embedding vector(384),
 image_embedding vector(512),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE alerts (
 id UUID PRIMARY KEY,
 user_ref TEXT NOT NULL,
 canonical_product_id UUID NOT NULL REFERENCES canonical_products(id),
 alert_type TEXT NOT NULL CHECK(alert_type IN ('target_price','price_drop','percentage_drop','size_restock')),
 target JSONB NOT NULL,
 active BOOLEAN NOT NULL DEFAULT true,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
