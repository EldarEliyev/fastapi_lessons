from fastapi import FastAPI

# Layihə haqqında məlumatları (Metadata) burada təyin edirik
app = FastAPI(
    title="My Backend Project",
    description="""
    The API created for to manage users.
    
    * **Users**: Create and read user.
    * **Items**: To manage items.
    """,
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Eldar Eliyev",
        "url": "https://github.com/eldareliyev",
        "email": "eldar@example.com",
    },
    license_info={
        "name": "MIT License",
    },
    # Swagger-in URL-ni (yolunu) belə dəyişə bilərsən:
    docs_url="/my-api-documents", 
    redoc_url=None 
)


@app.get("/",  tags=["Main"])
async def root():
    return {"message":  "Swagger metadata applied the successfully!"}



