import uvicorn
if __name__ == '__main__':
    uvicorn.run('image_tags_web:app', host='127.0.0.1', port=33341, log_level="info")
    exit()

from os import listdir,getcwd,path,chdir
old_cwd=getcwd()
chdir(path.join(getcwd(),"modules"))
from modules.img_tag_module import tag
chdir(old_cwd)
from fastapi import FastAPI, File,HTTPException
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/get_tags")
async def get_tags_handler(image: bytes = File(...)):
    try:
        return {"tags":tag(image)}
    except:
        raise HTTPException(status_code=500, detail="Can't get image tags")
