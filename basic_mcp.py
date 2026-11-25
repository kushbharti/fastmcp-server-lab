from fastmcp import FastMCP

mcp = FastMCP(
    name='Simple MCP Server.'
)

@mcp.tool
def add(a:int, b:int) -> int:
    """Perform the addition of given two numbers."""
    return a + b

mcp.run(transport="streamable-http")