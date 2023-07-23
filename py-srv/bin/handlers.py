from tornado.web import RequestHandler

from db.setup import get_db

from strategy.cls_raw import Raw
# from strategy.cls_chained import Chained

def get_strategy():
    db = next(get_db())
    return Raw(db)

class SmokeTestHandler(RequestHandler):
    def get(self):
        self.write({"hello": "world"})

class GetHandler(RequestHandler):
    def get(self):
        results = get_strategy().all()
        self.write(results)
 
    def delete(self, dog_id):
        results = get_strategy().delete_by(int(dog_id))
        self.write(results)

class GetByFilterHandler(RequestHandler):
    def get(self, dog_id):
        results = get_strategy().filter_by(dog_id)
        self.write(results)

class InsertHandler(RequestHandler):
    def put(self, dog_breed, dog_color):
        results = get_strategy().insert_entry(dog_breed, dog_color)
        self.write(results)

class UpdateHandler(RequestHandler):
    def post(self, dog_id, dog_breed, dog_color):
        results = get_strategy().update_entry(dog_id, dog_breed, dog_color)
        self.write(results)
