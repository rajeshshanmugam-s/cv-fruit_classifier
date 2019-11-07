from fastapi import FastAPI
import giver


app = FastAPI()


@app.get("/test")
def read_root():
    return {"Hello": "World"}

@app.get("/predict")
def solver():
    print('1')
    result = giver.predictor(image_url='https://images.agoramedia.com/everydayhealth/gcms/All-About-Bananas-Nutrition-Facts-Health-Benefits-Recipes-and-More-RM-722x406.jpg')
    print(result)
    return result