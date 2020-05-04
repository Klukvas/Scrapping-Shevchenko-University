from sqlalchemy.orm import sessionmaker
from abiturientsInfo.models import AbiturientRow, db_connect, create_table

class AbiturientsinfoPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        abitur = AbiturientRow()
        abitur.specialty = item["specialty"]
        abitur.faculty = item["faculty"]
        abitur.name = item["name"]
        abitur.mark = item["mark"]
        abitur.priority = item["priority"]
        abitur.status = item["status"]
        abitur.docs = item["docs"]
        try:
            session.add(abitur)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
