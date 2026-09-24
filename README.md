# Threadly — Fashion Comparison & Intelligence

A fashion-first comparison prototype for Indian e-commerce.

**Demo data only.** Product, retailer, price, availability and price-history records are synthetic.

## MVP
- Fashion discovery homepage
- Search and category filters
- Cross-store offer comparison
- Synthetic price history and size availability
- Wishlist and alert interactions
- B2B fashion intelligence view
- Responsive static deployment

No unauthorized scraping or fabricated live retailer integrations are included.

## Run locally
```bash
python -m http.server 8000
```
Open http://localhost:8000.

## Deployment
GitHub Pages workflow is included in .github/workflows/pages.yml.

## Roadmap
Next.js + TypeScript, FastAPI, PostgreSQL/pgvector, approved retailer connectors, matching engine, authentication, visual search, admin review and production intelligence.

MIT licensed.