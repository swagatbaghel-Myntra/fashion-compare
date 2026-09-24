# Architecture

Threadly is a fashion-first comparison platform built around a canonical catalog rather than independent retailer cards.

## Core flow

Retailer feed -> validate -> normalize -> taxonomy map -> deduplicate -> match -> canonical product -> price/inventory snapshots -> search/vector indexes -> consumer and intelligence applications.

## Domain model

- canonical_product: the fashion item identity shared across retailers.
- product_variant: colour/size variants.
- retailer_listing: one retailer's listing of a canonical product.
- listing_variant: retailer-specific variant availability.
- price_snapshot: immutable historical price observation.
- inventory_snapshot: immutable availability observation.
- product_match: accepted exact match.
- match_candidate: uncertain match awaiting review.
- alert: price or size condition.
- retailer_connector: approved source integration configuration.

## Matching stages

1. Exact identifiers: GTIN/EAN/UPC/manufacturer SKU/style ID.
2. Structured similarity: brand, category, colour, material, attributes.
3. Semantic title/attribute similarity.
4. Image similarity.
5. Confidence and review policy.

Similar products are never represented as exact matches.

## Data access policy

Production connectors must use official APIs, affiliate/merchant feeds, licensed datasets, partner integrations, or other explicitly permitted sources. Demo adapters are synthetic.
