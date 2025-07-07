from typing import List, Optional
from pydantic import BaseModel, Field

# --------------------------
# MÉTODOS DE PAGO
# --------------------------
class PaymentMethod(BaseModel):
    id: int = Field(..., description="ID")
    name: str = Field(..., description="Nombre")
    icon: Optional[str] = Field(None, description="Icono")
    category: Optional[str] = Field(None, description="Categoría")


class ProductPaymentMethods(BaseModel):
    id: int = Field(..., description="ID")
    product_id: int = Field(..., description="ID del producto")
    payment_method_ids: List[int] = Field(..., description="IDs de los métodos de pago")


# --------------------------
# SELLER
# --------------------------
class Seller(BaseModel):
    id: int = Field(..., description="ID")
    name: str = Field(..., description="Nombre")
    rating: float = Field(..., description="Calificación")


# --------------------------
# CARACTERÍSTICAS
# --------------------------
class Characteristics(BaseModel):
    nucleus_material: Optional[str] = Field(None, description="Material del núcleo")
    exterior_material: Optional[str] = Field(None, description="Material del exterior")
    profile_thickness: Optional[str] = Field(None, description="Espesor del perfil")
    weight: Optional[str] = Field(None, description="Peso")
    dimensions: Optional[str] = Field(None, description="Dimensiones")
    age_min: Optional[str] = Field(None, description="Edad mínima")
    length: Optional[str] = Field(None, description="Longitud")
    width: Optional[str] = Field(None, description="Ancho")
    safety_certificate: Optional[str] = Field(None, description="Certificado de seguridad")
    is_beach_paddle: Optional[str] = Field(None, description="Es una paleta de playa")
    gender: Optional[str] = Field(None, description="Género")
    target_group: Optional[str] = Field(None, description="Grupo objetivo")
    balance: Optional[str] = Field(None, description="Balance")

# --------------------------
# PRODUCTOS
# --------------------------
class Product(BaseModel):
    id: int = Field(..., description="ID")
    title: str = Field(..., description="Título")
    description: str = Field(..., description="Descripción")
    price: float = Field(..., description="Precio")
    currency: str = Field(..., description="Moneda")
    images: List[str] = Field(..., description="Imágenes")
    stock: int = Field(..., description="Stock")
    model: str = Field(..., description="Modelo")
    brand: str = Field(..., description="Marca")
    color: str = Field(..., description="Color")
    year: str = Field(..., description="Año")
    included_accessories: Optional[str] = Field(None, description="Accesorios incluidos")
    head_shape: Optional[str] = Field(None, description="Forma de la cabeza")
    seller: int = Field(..., description="ID del vendedor")
    characteristics: Optional[Characteristics] = Field(None, description="Características")
    category: Optional[str] = Field(None, description="Categoría")


# --------------------------
# RESPONSE
# --------------------------
class ProductResponse(BaseModel):
    id: int = Field(..., description="ID")
    title: str = Field(..., description="Título")
    description: str = Field(..., description="Descripción")
    price: float = Field(..., description="Precio")
    currency: str = Field(..., description="Moneda")
    images: List[str] = Field(..., description="Imágenes")
    stock: int = Field(..., description="Stock")
    model: str = Field(..., description="Modelo")
    brand: str = Field(..., description="Marca")
    color: str = Field(..., description="Color")
    year: str = Field(..., description="Año")
    included_accessories: Optional[str] = Field(None, description="Accesorios incluidos")
    head_shape: Optional[str] = Field(None, description="Forma de la cabeza")
    characteristics: Optional[Characteristics] = Field(None, description="Características")
    seller: Seller = Field(..., description="Vendedor")
    payment_methods: List[PaymentMethod] = Field(..., description="Métodos de pago")