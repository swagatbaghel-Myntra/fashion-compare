from .models import MatchCandidate

def match_confidence(c: MatchCandidate) -> float:
    if c.exact_identifier_score >= 0.99:
        return 1.0
    # Conservative weighted prototype. Production weights must be validated.
    score = (
        c.structured_score * 0.45
        + c.semantic_score * 0.30
        + c.image_score * 0.25
    )
    return round(max(0.0, min(1.0, score)), 4)

def match_decision(score: float) -> str:
    if score >= 0.92:
        return "auto_accept"
    if score >= 0.70:
        return "manual_review"
    return "do_not_merge"
