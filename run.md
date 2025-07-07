# Cómo ejecutar la aplicación y tests

## Requisitos

- Tener **Docker** y **Docker Compose** instalados y funcionando.

---------------------------------------

**Ejecutar aplicacion**

1. Clonar el repositorio público:

```bash
git clone https://github.com/JuanCapdevila/ml-challenge.git
```

2. Crear el contenedor Docker y levantar la aplicación

```bash
cd ml-challenge
docker compose up --build
```

3. Abrir en el navegador

http://localhost:8000/

Esto redireccionará automáticamente al detalle del producto inicial:
http://localhost:8000/product.html?id=1

Desde ahí podrás navegar entre los distintos productos visibles (productos del vendedor, productos relacionados).

---------------------------------------

**Ejecutar tests y validar cobertura**

```bash
docker exec -it ml-challenge-web-1 python -m pytest /tests --cov=/app/service --cov=/app/routes --cov-report=term-missing
```

Este comando:
    Ejecuta los tests dentro de test_product
    Mide la cobertura dentro de service y routes.
    Muestra un reporte en consola con el % de cobertura.

---------------------------------------

**Documentacion de endpoints**

http://localhost:8000/docs