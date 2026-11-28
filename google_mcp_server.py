from config import setting

from fastmcp.server.auth.providers.google import GoogleProvider
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_access_token
from send_email_mcp_server import _send

verifier = GoogleProvider(
    client_id=setting.GOOGLE_CLIENT_ID,
    client_secret=setting.GOOGLE_CLIENT_SECRET,
    base_url=setting.MCP_SERVER_URL
)

mcp = FastMCP("Secure Google MCP Server..", auth=verifier)

@mcp.tool
def whoami() -> dict:
    """Return the userid of the current authenticated user"""
    token = get_access_token()
    
    print("\n\n",token,"\n\n")
    
    return {
        "client_id" : token.client_id,
        "email": token.claims.get("email","")
    }
    
@mcp.tool
def send_mail(email:str, subject:str, body:str) -> str:
    """Can end email to any email address, just required Email address, Subject and Body

    Args:
        email : email address
        subject : one line subject of email
        body : complete formated plain email

    """
    res = _send(email, subject, body)
    return f'Email sent to {email}'

mcp.run(transport="streamable-http")