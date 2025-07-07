# Mercado Libre - Technical Challenge

## 🛠 Tecnologías utilizadas

- **Backend:** FastAPI
- **Frontend:** React (CDN con Babel)
- **Contenedores:** Docker + Docker Compose
- **Testing:** Pytest + Coverage
- **Logging:** Rotación de logs por archivo, excluidos del control de versiones

## 📂 Estructura del proyecto

ml-challenge/
├── app/
│ ├── routes/ # Endpoints de la API
│ ├── service/ # Lógica
│ ├── utils/ # Funciones reutilizables
│ ├── schemas/ # Esquemas Pydantic
│ ├── frontend/ # HTML + JS React desde CDN
│ ├── static/ # Imagenes e iconos
│ └── main.py # App principal de FastAPI
├── tests/ # Tests automatizados
├── docker-compose.yml
├── requirementes.txt
└── Dockerfile

## 🚀 Cómo ejecutarlo

Ver el archivo [`run.md`] para instrucciones completas de instalación, ejecución y pruebas.


## 📄 Documentación técnica

El documento de decisiones, diseño y desafíos enfrentados se encuentra aparte en formato PDF.
