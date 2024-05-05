from typing import  Annotated

import uvicorn
from fastapi import FastAPI, Path, HTTPException, status

app = FastAPI()

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


@app.get('/actions/codeword/{code}', status_code=status.HTTP_200_OK)
def action_from_code(code: Annotated[int, Path(title="The ID of the action")]):
    for item in data['actions']:
        if code in item.values():
            return item.get('codeword')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Action not found")


@app.get('/actions/code/{action}', status_code=status.HTTP_200_OK)
def code_from_action(action: Annotated[str, Path(title="The title of the action")]):
    for item in data['actions']:
        if action in item.values():
            return item.get('id')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Action not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
