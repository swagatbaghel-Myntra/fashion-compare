# Threadly

### Fashion discovery, comparison and commerce intelligence — built around a normalized product layer.

[Live Experience](https://swagatbaghel-myntra.github.io/fashion-compare/) · [API](https://fashion-compare.onrender.com/docs)

---

## Overview

Threadly is an experimental **fashion comparison and intelligence platform** designed to explore a simple question:

> What would fashion shopping look like if discovery, cross-store comparison, price context and affiliate commerce lived in one product?

The project combines a consumer-facing discovery experience with a backend architecture for product normalization, matching, retailer offers and affiliate attribution.

The current release is an **MVP / technical foundation**. Its bundled fashion catalog and price history are synthetic; they exist to validate the product experience and architecture while compliant retailer/catalog integrations are developed.

## Product Direction

Traditional comparison engines work well for products with standardized model numbers. Fashion is different: titles vary by retailer, attributes are inconsistent, variants matter, and visually similar products are often more useful than exact matches.

Threadly is being designed around four layers:

**Discover** → search and browse fashion across a normalized catalog  
**Compare** → evaluate retailer offers, sizes and price context  
**Match** → distinguish exact cross-retailer products from similar styles  
**Intelligence** → turn normalized catalog data into assortment and pricing signals

## Current Architecture

```text
GitHub Pages
     │
     │ HTTPS
     ▼
FastAPI API ──────────────── Synthetic Catalog
     │                             │
     │                             ├─ Products
     │                             ├─ Offers
     │                             └─ Price History
     │
     ▼
Cuelinks Affiliate Layer
     │
     ▼
Tracked Retailer Redirect
```

The frontend is deployed independently from the API. Affiliate credentials remain server-side and are never exposed in browser code or committed to the repository.

## What's Working

- Responsive fashion discovery interface
- Keyword search and category filtering
- Price and discount sorting
- Product detail experience
- Multi-store comparison UX
- Synthetic price-history visualization
- Size presentation
- Wishlist interactions
- Prototype product-match confidence scoring
- Fashion assortment intelligence view
- FastAPI service deployed on Render
- Server-side Cuelinks integration
- Affiliate URL conversion flow
- GitHub Pages continuous deployment
- Secret-safe environment configuration

## Data Status

| Layer | Current state |
| --- | --- |
| Product catalog | Synthetic demonstration dataset |
| Product prices | Synthetic |
| Price history | Synthetic |
| Size availability | Synthetic |
| Product matching | Prototype scoring engine |
| Affiliate infrastructure | Cuelinks server integration |
| Retailer product feeds | Not connected yet |
| Checkout | Redirects to external retailers; Threadly does not process checkout |

Synthetic information is intentionally labelled in the product experience. The project does not represent demo catalog values as live retailer data.

## Repository Structure

```text
fashion-compare/
├── index.html                 # Consumer web experience
├── styles.css                 # UI system
├── app.js                     # Discovery/comparison interactions
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI application
│   │   ├── models.py          # API/domain models
│   │   ├── matching.py        # Matching prototype
│   │   ├── demo_data.py       # Explicitly synthetic catalog
│   │   └── connectors/
│   │       └── cuelinks.py    # Server-side affiliate connector
│   ├── tests/
│   ├── requirements.txt
│   └── .env.example
├── database/
├── docs/
└── .github/workflows/
```

## API

The FastAPI service currently exposes endpoints across four areas.

**Catalog**
```
GET /search
GET /products/{product_id}
GET /products/{product_id}/offers
GET /products/{product_id}/price-history
GET /products/{product_id}/similar
```

**Matching**
```
POST /matching/evaluate
```

**Intelligence**
```
GET /intelligence/assortment
```

**Affiliate**
```
GET  /affiliate/campaigns
GET  /affiliate/offers
POST /affiliate/convert
GET  /affiliate/performance
```

Interactive API documentation is available through the deployed FastAPI service.

## Local Development

### Frontend

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

### API

```bash
cd backend
python -m venv .venv
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Create a local `.env` from `.env.example` when testing integrations.

Never commit API keys or production credentials.

## Deployment

| Component | Platform |
| --- | --- |
| Web experience | GitHub Pages |
| API | Render |
| Affiliate integration | Cuelinks |
| Source control / CI | GitHub |

Frontend: https://swagatbaghel-myntra.github.io/fashion-compare/

API documentation: https://fashion-compare.onrender.com/docs

## Engineering Principles

**Evidence over simulation.** Synthetic data is clearly identified until a legitimate live source exists.

**Canonical products over duplicated listings.** Retailer listings should ultimately map to normalized products rather than becoming independent catalog entities.

**Exact match ≠ similar style.** Product identity and fashion similarity are separate problems and should remain separate in the data model and interface.

**Secrets stay server-side.** Third-party credentials belong in deployment environment variables, never client JavaScript.

**Modular retailer integrations.** Future catalog providers should connect through adapters rather than retailer-specific logic leaking throughout the application.

## Roadmap

### Catalog Foundation
Connect compliant fashion product feeds and build retailer-specific normalization adapters.

### Product Graph
Introduce canonical products, variants, retailer listings and confidence-based cross-store matching.

### Price Intelligence
Persist price snapshots and calculate historical lows, price movement and retailer-level comparisons from observed data.

### Fashion Discovery
Add semantic search, image similarity, alternatives and "find this look for less."

### Consumer Utility
Add persistent accounts, wishlists, price alerts and size-restock alerts.

### Commerce Intelligence
Expand the B2B layer into assortment depth, price architecture, attribute trends and competitor comparison using observed catalog data.

---

## Status

**Active development.**

Threadly is currently an MVP demonstrating the product architecture and user experience. It is not presented as a production retailer-data service, and the bundled catalog should not be used for commercial analysis.

