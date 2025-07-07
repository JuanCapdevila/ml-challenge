from typing import List, Optional
from fastapi import HTTPException

from schemas.schemas import (
    Product,
    Seller,
    PaymentMethod,
    ProductPaymentMethods,
    ProductResponse
)
from utils.utils import (
    load_json_with_model,
    load_products,
    get_product_by_id
)

def get_all_products() -> List[Product]:
    return load_products()

def get_product(product_id: int) -> Product:
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def get_products_from_seller(seller_id: int, exclude_product_id: Optional[int] = None) -> List[Product]:
    products = load_products()
    return [
        p for p in products 
        if p.seller and p.seller == seller_id and p.id != exclude_product_id
    ]

def get_related_products(product_id: int) -> List[Product]:
    products = load_products()
    main_product = next((p for p in products if p.id == product_id), None)
    if not main_product:
        return []

    related = [
        p for p in products 
        if p.id != product_id and (p.category == main_product.category)
    ]
    return related[:3]

def build_product_response(product_raw: Product) -> ProductResponse:
    sellers = load_json_with_model("sellers.json", Seller)
    payment_methods = load_json_with_model("payment_methods.json", PaymentMethod)
    product_payment_methods = load_json_with_model("product_payment_methods.json", ProductPaymentMethods)

    seller_id = product_raw.seller
    seller = next((s for s in sellers if s.id == seller_id), None)

    products_payment_methods = next((method for method in product_payment_methods if method.product_id == product_raw.id), None)
    method_ids = products_payment_methods.payment_method_ids if products_payment_methods else []
    methods = [method for method in payment_methods if method.id in method_ids]

    characteristics = product_raw.characteristics

    return ProductResponse(
        id=product_raw.id,
        title=product_raw.title,
        description=product_raw.description,
        price=product_raw.price,
        currency=product_raw.currency,
        images=product_raw.images,
        stock=product_raw.stock,
        model=product_raw.model,
        brand=product_raw.brand,
        color=product_raw.color,
        year=product_raw.year,
        included_accessories=product_raw.included_accessories,
        head_shape=product_raw.head_shape,
        characteristics=characteristics,
        seller=seller,
        payment_methods=methods
    )
