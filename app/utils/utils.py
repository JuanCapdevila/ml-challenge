from typing import List, Optional, Type, TypeVar
from pydantic import BaseModel
from pathlib import Path
import json

from schemas.schemas import Product

T = TypeVar("T", bound=BaseModel)

DATA_DIR = Path(__file__).parent.parent.parent / "data"

def load_json_with_model(file_path: str, model: Optional[Type[T]] = None) -> list:
    with open(DATA_DIR / file_path, encoding="utf-8") as f:
        data = json.load(f)
    if model:
        return [model(**item) for item in data]
    return data

def load_products() -> List[Product]:
    return load_json_with_model("products.json", Product)

def get_product_by_id(product_id: int) -> Optional[Product]:
    products = load_products()
    product = next((product for product in products if product.id == product_id), None)
    return product

