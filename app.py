from fastapi import FastAPI, Header, HTTPException, status

app = FastAPI()

API_KEY = "my-secret-key"  # replace with your key

@app.get("/validate_user")
def validate_user(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    return {"message": "Access granted"}
