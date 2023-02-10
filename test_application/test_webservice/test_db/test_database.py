from pytest_mock_resources import create_mongo_fixture
from application.webservice.db.database import insert_doc

mongo = create_mongo_fixture()

def test_insert_doc(mongo):
    json={"name": "vélo après les cours", "distance": "20"}
    collection=mongo['user_activities']
    insert_doc(collection,json)

    returned = collection.find_one()
    returned.pop("_id",None)

    assert returned == {"name": "vélo après les cours", "distance": "20"}