from fastapi import APIRouter
from typing import List

from service.product_service import (
    build_product_response,
    get_all_products,
    get_product,
    get_products_from_seller,
    get_related_products
)
from schemas.schemas import ProductResponse
from utils.logger import logger

router = APIRouter(prefix="/product", tags=["product"])

@router.get("/")
def get_products():
    logger.info(f"Get all products")
    return get_all_products()

@router.get("/{product_id}", response_model=ProductResponse, responses={
    404: {"description": "Product not found"},
})
def get_product_by_id(product_id: int):
    logger.info(f"Get product by ID: {product_id}")
    product = get_product(product_id)
    return build_product_response(product)

@router.get("/{product_id}/{seller_id}/from-seller", response_model=List[ProductResponse])
def products_from_seller(seller_id: int, product_id: int = 0):
    logger.info(f"Get products from seller: {seller_id}")
    products = get_products_from_seller(seller_id, product_id)
    return [build_product_response(p) for p in products]

@router.get("/{product_id}/related", response_model=List[ProductResponse])
def related_products(product_id: int):
    products = get_related_products(product_id)
    return [build_product_response(p) for p in products]
