from app.services.tools import (
    rag_tool,
    sql_tool
)

from app.services.calculator_tool import (
    calculator_tool
)

TOOLS = {
    "RAG_TOOL": rag_tool,
    "SQL_TOOL": sql_tool,
    "CALCULATOR_TOOL": calculator_tool
}