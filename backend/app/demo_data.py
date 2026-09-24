from .models import Product, Offer

PRODUCTS = [
 Product(id="cp_tee_001",brand="Northline",title="Oversized Heavyweight Tee",gender="Men",category="Clothing",article_type="T-Shirts",colour="Black",fit="Oversized",fabric="Cotton",attributes={"neck":"Round Neck","sleeve":"Half Sleeve"},offers=[Offer(retailer="ModeMart",price=899,mrp=1499,sizes=["S","M","L","XL"]),Offer(retailer="StyleBay",price=949,mrp=1499,sizes=["M","L","XL"])],similar_product_ids=["cp_shirt_001"]),
 Product(id="cp_shirt_001",brand="Aster",title="Relaxed Linen Resort Shirt",gender="Men",category="Clothing",article_type="Shirts",colour="White",fit="Relaxed",fabric="Linen",attributes={"collar":"Spread","occasion":"Vacation"},offers=[Offer(retailer="StyleBay",price=1599,mrp=2499,sizes=["M","L","XL"]),Offer(retailer="ModeMart",price=1699,mrp=2499,sizes=["S","M","L"])],similar_product_ids=["cp_tee_001"]),
 Product(id="cp_sneaker_001",brand="Rove",title="Retro Court Sneakers",gender="Unisex",category="Footwear",article_type="Sneakers",colour="White",attributes={"style":"Retro Court"},offers=[Offer(retailer="ModeMart",price=2499,mrp=3999,sizes=["7","8","9","10"]),Offer(retailer="StyleBay",price=2699,mrp=3999,sizes=["8","9","10"])])
]
PRICE_HISTORY = {
 "cp_tee_001":[1199,1099,999,949,899],
 "cp_shirt_001":[1899,1799,1699,1599,1599],
 "cp_sneaker_001":[3199,2999,2799,2599,2499],
}
