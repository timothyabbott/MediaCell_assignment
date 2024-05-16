from typing import Annotated

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
                "codeword": 5000,
                "id": "alert"},
            {
                "codeword": 5001,
                "id": "alert"},
            {
                "codeword": 5002,
                "id": "thanks"}
        ]
    }


# this could be a list
@app.get('/actions/id/{codeword}', status_code=status.HTTP_200_OK)
def id_from_codeword(codeword: Annotated[int, Path(title="The codeword of the action")]):
    for item in data['actions']:
        codeword = int(codeword)
        if int(codeword) in item.values():
            return item.get('id')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Action not found")


@app.get('/actions/codeword/{id}', status_code=status.HTTP_200_OK)
def codewords_from_id(id: Annotated[str, Path(title="The id(s) of the action")]):
    ids = []

    for item in data['actions']:
        if id in item.values():
            ids.append(item.get('codeword'))
    if ids:
        return ids
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Action not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
