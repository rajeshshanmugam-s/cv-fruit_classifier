import hug
import giver

@hug.get('/')
def test():
    '''Hello'''
    return {'Hello'}

@hug.post("/upload")
def solver(image_url : hug.types.text):
    result = giver.predictor(image_url)
    return result