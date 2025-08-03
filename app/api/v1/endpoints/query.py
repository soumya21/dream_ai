# app/api/v1/query.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core import bedrock_agent_client

router = APIRouter()


# Request model for user query
class QueryRequest(BaseModel):
    user_query: str


# API endpoint to invoke Bedrock agent
@router.post("/query")
async def query_bedrock(request: QueryRequest):
    if not bedrock_agent_client.bedrock_client:
        raise HTTPException(status_code=500, detail="Bedrock client not initialized")

    # Send user query to Bedrock
    response = bedrock_agent_client.bedrock_client.invoke_bedrock_agent(user_input=request.user_query)

    if not response:
        raise HTTPException(status_code=500, detail="Error invoking Bedrock agent")

    return {"response": response}

class Message(BaseModel):
    message: str

@router.post("/chat")
def chat(message: Message):
    if not bedrock_agent_client.bedrock_client:
        raise HTTPException(status_code=500, detail="Bedrock client not initialized")
    try:
        completion, traces = bedrock_agent_client.bedrock_client.invoke_bedrock_agent(user_input=message.message)
        return {"reply": completion}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error querying agent: {e}")