import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers.router import router

app = FastAPI()

@app.get('/')
def root():
    return {"message": "An API to check the condition of the air we breathe in"}

app.include_router(router)
# This middleware enables allow all cross-domain requests to the API from a browser.
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)