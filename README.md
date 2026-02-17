Control de versiones y resolución de conflictos en Git

**Objetivo:** 
Simular un escenario real de desarrollo en equipo donde dos personas trabajan simultáneamente en el mismo archivo de una aplicación Streamlit, provocando un "Merge Conflict" que deberán resolver.

**Entrega:** 
La entrega será a través del campus, compartiendo el enlace del repositorio en donde trabajaron.

**Importante:**
En este taller ejecutará varios comandos en la terminal. **No se limite a copiar y pegar.** Parte fundamental del proceso de desarrollo de aplicaciones de datos es comprender lo que sucede internamente en cada proceso.

Si en algún momento no tiene certeza sobre la función de una "bandera" (como `-b`, `-u` o `-m`) o el significado de parámetros como `origin`, **utilice** el siguiente prompt en su asistente de IA de preferencia (ChatGPT, Gemini o Claude) para recibir una explicación detallada:

> **Prompt:**
> 
> "Actúe como un experto en programación y explíqueme detalladamente el siguiente comando:
> 
> `[PEGUE AQUÍ EL COMANDO]`
> 
> Por favor, desglose la explicación en los siguientes puntos:
> 
> 1.  Cuál es la función principal del comando.
>     
> 2.  Qué significa cada **bandera** (flag) o parámetro específico incluido (por ejemplo: `-u`, `-m`, `origin`, etc.).
>     
> 3.  Qué sucedería si ejecuto el comando **sin** esos parámetros específicos."
>     

**Ejemplo de uso:** Si proporciona el comando `git push -u origin feature/mi-rama`, la IA le explicará que el parámetro `-u` configura el "upstream" para facilitar futuras subidas de código. **Inténtelo con cada comando nuevo que encuentre**

## Instrucciones:

### Fase 1: Configuración del Proyecto (Solo uno por equipo)

Uno de los dos integrantes debe iniciar el proyecto:

1.  Crear un repositorio en Github.
    
2.  Crear la carpeta `data/` y agregar el archivo `ventas.csv`:
    
    **`data/ventas.csv`**
    ```
    fecha,sucursal,producto,unidades,ingreso
    2024-01-01,Norte,Laptop,5,5000
    2024-01-02,Sur,Mouse,10,200
    2024-01-03,Norte,Teclado,8,400
    2024-01-04,Este,Monitor,3,900
    2024-01-05,Sur,Laptop,2,2000
    2024-01-06,Oeste,Mouse,15,300
    2024-01-07,Este,Teclado,5,250
    2024-01-08,Norte,Monitor,2,600
    2024-01-09,Sur,Monitor,4,1200
    2024-01-10,Oeste,Laptop,1,1000
    ```
    
3.  Crear el archivo base de la aplicación:
    
    **`app.py`**
    ```python
    import streamlit as st
    import pandas as pd
    
    # Configuración básica
    st.set_page_config(page_title="Dashboard Ventas", layout="wide")
    
    # Función de carga de datos
    @st.cache_data
    def load_data():
        return pd.read_csv('data/ventas.csv')
    
    df = load_data()
    
    st.title("Reporte de Ventas")
    st.write("Datos cargados exitosamente:")
    st.dataframe(df.head())
    
    st.markdown("---")
    
    # ==========================================
    # ZONA DE TRABAJO
    # ==========================================
    
    # Espacio reservado para nuevas funcionalidades
    ```
    
4.  Subir todo a `main` en GitHub y compartir el repositorio con su compañero/a.
    
5.  **La segunda persona:** Clonar el repositorio en su codespace.
	   ```bash
	git clone <URL>
	   ```
7.  Ambos deberán instalar streamlit, dado que es un entorno nuevo:
	   ```bash
	pip install streamlit
	   ```
	   
### Fase 2: Desarrollo Paralelo 

Ahora, trabajando cada uno en su propio codespace al mismo tiempo:

#### Rol A:  Visualización

La tarea es agregar un filtro interactivo por sucursal.

1.  Crear rama:
    También se puede utilizar la UI para esto. 
    ```bash
    git checkout -b feature/filtro-sucursal
    ```
    
2.  En `app.py`, **borrar** el comentario "Espacio reservado..." y agregar este código:
    ```python
    # Funcionalidad A: Filtros por Sucursal
    st.sidebar.header("Filtros")
    sucursal = st.sidebar.selectbox("Seleccionar Sucursal", df['sucursal'].unique())
    
    df_filtered = df[df['sucursal'] == sucursal]
    st.subheader(f"Ventas de la sucursal: {sucursal}")
    st.bar_chart(df_filtered.set_index('producto')['ingreso'])
    ```
    
3.  Guardar, commit y push:
    ```bash
    git commit -am "feat: agrega filtro por sucursal"
    git push origin feature/filtro-sucursal
    ```
    O bien, también se puede ejecutar:
    
	```bash
    git add .
    git commit -m "feat: agrega filtro por sucursal"
    git push origin feature/filtro-sucursal
    ```

#### Rol B: KPIs

La tarea es agregar métricas generales (KPIs) al inicio del dashboard.

1.  Crear rama:
También se puede utilizar la UI para esto. 
    ```bash
    git checkout -b feature/kpis-metricas
    ```
  
2.  En `app.py`, **borrar** el comentario "Espacio reservado..." (la misma línea que el rol A) y agregar este código:
    ```python
    # Funcionalidad B: KPIs Generales
    total_ingresos = df['ingreso'].sum()
    total_unidades = df['unidades'].sum()
    
    col1, col2 = st.columns(2)
    col1.metric("Ingresos Totales", f"${total_ingresos}")
    col2.metric("Unidades Vendidas", f"{total_unidades}")
    ```
    
3.  Guardar, commit y push:
4. 
    ```bash
    git commit -am "feat: agrega kpis generales"
    git push origin feature/kpis-metricas
    ```
    O bien, también se puede ejecutar:
    
	```bash
    git add .
    git commit -m "feat: agrega kpis generales"
    git push origin feature/kpis-metricas
    ```

### Fase 3: Conflicto

1.  **Rol A:** En GitHub, crear un **Pull Request** de su rama hacia `main` y hacer **Merge**. (Debería ser exitoso).
    
2.  **Rol B:** Intentar hacer lo mismo (Pull Request y Merge).
    
    -   **ERROR:** GitHub va a decir: _"Can’t automatically merge"_.
        
    -   Esto sucede porque ambos editaron las mismas líneas de código.

### Fase 4: Resolución 

El **Rol B** debe resolver esto localmente:

1.  Volver a la terminal y asegurarse de estar en su rama.
    
2.  Traer los cambios que el Rol B ya fusionó en `main`:
    ```bash
    git pull origin main
    ```
    
    Va a salir un mensaje: `CONFLICT (content): Merge conflict in app.py`._
    
3.  Abrir `app.py` en VS Code. Se verá algo así:

    ```python
    <<<<<<< HEAD
    # Funcionalidad B: KPIs Generales
    total_ingresos = df['ingreso'].sum()
    ...
    =======
    # Funcionalidad A: Filtros por Sucursal
    st.sidebar.header("Filtros")
    ...
    >>>>>>> main (o hash del commit)
    ```
    
4.  **Decisión para el manejo de conflictos:** No queremos borrar el trabajo de nadie. Queremos **ambas** cosas.
    
    -   Organizar el código lógicamente: Poner los KPIs primero (arriba) y los gráficos después (abajo).
        
    -   Borrar las marcas de conflicto (`<<<<`, `====`, `>>>>`).
        
    
    **El código final debe quedar limpio:**
    
    ```python
    # ... imports y carga de datos ...
    
    st.markdown("---")
    
    # 1. KPIs Generales (Lo que hizo B)
    total_ingresos = df['ingreso'].sum()
    col1, col2 = st.columns(2)
    col1.metric("Ingresos Totales", f"${total_ingresos}")
    col2.metric("Unidades Vendidas", f"{total_unidades}")
    
    st.markdown("---")
    
    # 2. Filtros (Lo que hizo A)
    st.sidebar.header("Filtros")
    sucursal = st.sidebar.selectbox("Seleccionar Sucursal", df['sucursal'].unique())
    # ... resto del código de A ...
    ```
    
5.  Finalizar la fusión:
    ```
    git add app.py
    git commit -m "fix: resolviendo conflicto, integrando KPIs y Filtros"
    git push origin feature/kpis-metricas
    ```
    
6.  Volver a GitHub y en el pull request va a decir ahora sí se puede hacer el **Merge**.

### Cierre

Ejecuten la aplicación final para asegurar que no hay errores de sintaxis.

De no estar en la rama main, deberán cambiar a esa rama previo al siguiente paso:
```bash
git switch main
```

Ir a la terminal del codespace, y actualizar la rama main:
```bash
git pull
```

Ejecutar la aplicación para comprobar que todo está corriendo bien.
```bash
streamlit run app.py
```
