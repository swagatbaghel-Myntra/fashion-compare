from app.matching import match_confidence, match_decision
from app.models import MatchCandidate

def test_exact_identifier_accepts():
    c=MatchCandidate(left_listing_id="a",right_listing_id="b",exact_identifier_score=.99)
    assert match_confidence(c)==1.0
    assert match_decision(1.0)=="auto_accept"

def test_uncertain_goes_to_review():
    c=MatchCandidate(left_listing_id="a",right_listing_id="b",structured_score=.85,semantic_score=.8,image_score=.75)
    score=match_confidence(c)
    assert 0.70 <= score < 0.92
    assert match_decision(score)=="manual_review"
