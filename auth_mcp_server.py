from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import JWTVerifier
from fastmcp.server.dependencies import get_access_token

from config import setting

verifier = JWTVerifier(
    public_key=setting.JWT_SECRET,
    algorithm=setting.JWT_ALGORITHM,
    issuer=setting.JWT_ISSUER,
    audience=setting.JWT_AUDIENCE
)

mcp = FastMCP("Secure MCP Server..", auth=verifier)

@mcp.tool
def whoami() -> dict:
    """Return the userid of the current authenticated user"""
    token = get_access_token()
    
    print("\n\n",token,"\n\n")
    
    return {
        "client_id" : token.client_id,
        # "email": token.claims.get("email","")
    }
    
mcp.run(transport="streamable-http")