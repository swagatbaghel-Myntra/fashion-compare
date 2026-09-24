from fastapi import FastAPI, HTTPException, Query
from .demo_data import PRODUCTS, PRICE_HISTORY
from .models import MatchCandidate
from .matching import match_confidence, match_decision

app = FastAPI(title="Threadly API", version="0.2.0", description="Fashion comparison API. Current bundled catalog is synthetic.")

@app.get("/health")
def health():
    return {"status":"ok","data_mode":"synthetic_demo"}

@app.get("/search")
def search(q: str = "", article_type: str | None = None, max_price: int | None = Query(None, ge=0)):
    terms = q.lower().split()
    result = []
    for p in PRODUCTS:
        haystack = " ".join([p.brand,p.title,p.gender,p.category,p.article_type,p.colour,p.fit or "",p.fabric or ""]).lower()
        if terms and not all(t in haystack for t in terms):
            continue
        if article_type and p.article_type.lower() != article_type.lower():
            continue
        lowest = min(x.price for x in p.offers)
        if max_price is not None and lowest > max_price:
            continue
        result.append({"product":p,"lowest_price":lowest,"retailer_count":len(p.offers)})
    return {"data_mode":"synthetic_demo","count":len(result),"results":result}

@app.get("/products/{product_id}")
def product(product_id: str):
    p = next((x for x in PRODUCTS if x.id == product_id), None)
    if not p:
        raise HTTPException(404, "Product not found")
    return {"data_mode":"synthetic_demo","product":p}

@app.get("/products/{product_id}/offers")
def offers(product_id: str):
    p = next((x for x in PRODUCTS if x.id == product_id), None)
    if not p:
        raise HTTPException(404, "Product not found")
    return {"data_mode":"synthetic_demo","offers":sorted(p.offers,key=lambda x:x.price)}

@app.get("/products/{product_id}/price-history")
def price_history(product_id: str):
    if product_id not in PRICE_HISTORY:
        raise HTTPException(404, "Product not found")
    values=PRICE_HISTORY[product_id]
    return {"data_mode":"synthetic_demo","current":values[-1],"low":min(values),"high":max(values),"snapshots":values}

@app.get("/products/{product_id}/similar")
def similar(product_id: str):
    p = next((x for x in PRODUCTS if x.id == product_id), None)
    if not p:
        raise HTTPException(404, "Product not found")
    return {"data_mode":"synthetic_demo","results":[x for x in PRODUCTS if x.id in p.similar_product_ids]}

@app.post("/matching/evaluate")
def evaluate(candidate: MatchCandidate):
    score=match_confidence(candidate)
    return {"confidence":score,"decision":match_decision(score),"note":"Prototype scoring; production thresholds require validation."}

@app.get("/intelligence/assortment")
def assortment():
    types={}
    for p in PRODUCTS:
        types[p.article_type]=types.get(p.article_type,0)+1
    return {"data_mode":"synthetic_demo","canonical_products":len(PRODUCTS),"article_type_depth":types}
