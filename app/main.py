from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from pydantic import BaseModel
from app.api.v1.endpoints import health,auth,secure_endpoint,query,leave,user
from app.core import bedrock_agent_client
from app.core.database import db_manager


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Include the API router
app.include_router(health.router)
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(secure_endpoint.router, prefix="/secure", tags=["secure"])
app.include_router(query.router)
app.include_router(leave.router)
app.include_router(user.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/static/{path}")
async def serve_static_file(path: str):
    response = FileResponse(f"static/{path}")
    response.headers["Cache-Control"] = "public, max-age=31536000"  # Cache for 1 year
    return response

# Initialize Bedrock client at startup
@app.on_event("startup")
async def startup_event():
    print("Initializing Bedrock client...")
    bedrock_agent_client.init_bedrock_client()
    if bedrock_agent_client.bedrock_client:
        print("Bedrock client successfully initialized.")
    else:
        print("Bedrock client initialization failed.")
    db_manager.Base.metadata.create_all(bind=db_manager.engine)

@app.get("/", response_class=HTMLResponse)
async def get_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class Message(BaseModel):
    message: str

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
