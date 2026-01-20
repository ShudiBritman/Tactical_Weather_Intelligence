from fastapi import FastAPI
import uvicorn



app = FastAPI()


app.include_router(

)



if __name__ == "__main__":
    uvicorn.run(app, "127.0.0.1", 8080)