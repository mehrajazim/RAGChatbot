# app.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from controllers import pdf_controller
from controllers import chat_controller

app = FastAPI()

# Set up template directory for our HTML views
templates = Jinja2Templates(directory="templates")
# If you have static files (CSS/JS), mount them here
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the controllers' routes
app.include_router(pdf_controller.router)
app.include_router(chat_controller.router)

@app.get("/")
async def home(request: Request):
    """
    Home page that renders the HTML UI.
    """
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
