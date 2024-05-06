from typing import  Annotated

import uvicorn
from fastapi import FastAPI, Path, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = \
    {
        "actions": [
            {
                "codeword": "alert",
                "id": 5001},
            {
                "codeword": "thanks",
                "id": 5002}
        ]
    }


@app.get('/actions/codeword/{id}', status_code=status.HTTP_200_OK)
def action_from_code(id: Annotated[int, Path(title="The ID of the action")]):
    for item in data['actions']:
        if id in item.values():
            return item.get('codeword')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Action not found")


@app.get('/actions/id/{codeword}', status_code=status.HTTP_200_OK)
def code_from_action(codeword: Annotated[str, Path(title="The title of the action")]):
    for item in data['actions']:
        if codeword in item.values():
            return item.get('id')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Action not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
