# Analisis-de-Alquileres

## README: Proyecto ETL - Idealista a AWS Redshift

### Descripción del Proyecto

Este proyecto forma parte del curso de Data Engineering de CoderHouse y tiene como objetivo crear un pipeline ETL para extraer datos de alquileres de la plataforma Idealista, transformarlos y cargarlos en un data warehouse en AWS Redshift, accesible a través de DBeaver.

### Flujo ETL

1. **Extracción:**
   * **Herramienta:** Request (Python)
   * **Fuente de datos:** Anuncios de alquiler en Idealista
   * **Datos extraídos:** Precio, ubicación, características, etc.
   * **Formato:** JSON (o CSV, según preferencia)
2. **Transformación:**
   * **Limpieza:** Eliminación de valores nulos, duplicados y outliers.
   * **Normalización:** Conversión de tipos de datos, unificación de formatos.
   * **Enriquecimiento:** (Opcional) Incorporación de datos externos (e.g., índices de precios, datos demográficos).
   * **Estructuración:** Creación de un esquema coherente para la carga en Redshift.
3. **Carga:**
   * **Destino:** AWS Redshift
   * **Herramienta:** COPY command (o herramientas de carga de AWS)
   * **Formato:** CSV (o formato compatible con Redshift)

### Tecnologías Utilizadas

* **Lenguajes:** Python
* **Librerías:** Beautiful Soup, Pandas, NumPy
* **Herramientas:** Jupyter Notebook, AWS CLI, DBeaver
* **Cloud:** AWS (EC2, S3, Redshift)

### Estructura del Proyecto

* `scripts/`: Scripts de Python para extracción, transformación y carga.
* `data/`: Datos crudos, transformados y archivos de configuración.
* `notebooks/`: Jupyter Notebooks para análisis exploratorio y visualización.
* `aws/`: Scripts y archivos de configuración para AWS (e.g., IAM roles).

### Cómo Ejecutar el Proyecto

1. **Configuración de AWS:** Crear una instancia EC2, un bucket S3 y un cluster Redshift.
2. **Configuración del entorno:** Crear un entorno virtual y instalar las dependencias.
3. **Ejecución:** Ejecutar secuencialmente los scripts de extracción, transformación y carga.
4. **Validación:** Verificar los datos cargados en Redshift utilizando DBeaver.

### Consideraciones Importantes

* **Rendimiento:** Optimizar los queries SQL en Redshift para mejorar el rendimiento.
* **Escalabilidad:** Diseñar el pipeline para manejar grandes volúmenes de datos.
* **Seguridad:** Implementar medidas de seguridad para proteger los datos (e.g., encriptación).
* **Mantenimiento:** Establecer un cron job para automatizar la ejecución del pipeline.

### Próximos Pasos

* **Exploración de datos:** Realizar análisis más profundos utilizando herramientas de BI.
* **Modelado:** Crear modelos predictivos para estimar precios o clasificar propiedades.
* **Visualización:** Desarrollar dashboards interactivos para comunicar los resultados.

**Aspectos a Considerar para una Mayor Complejidad:**

* **Orquestación:** Utilizar herramientas como Airflow o Luigi para orquestar el flujo ETL.
* **Testing:** Implementar pruebas unitarias y de integración para garantizar la calidad del código.
* **Documentación:** Documentar el proceso ETL de manera detallada.

**Personalización:**

* **Aprofundar en cada etapa:** Detallar los pasos específicos de extracción, transformación y carga.
* **Incluir diagramas:** Utilizar diagramas de flujo para visualizar el proceso ETL.
* **Agregar métricas:** Definir métricas para evaluar el rendimiento del pipeline.
* **Mencionar desafíos:** Describir los desafíos enfrentados y cómo fueron superados.
