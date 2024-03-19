from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from conftest import SQLITE_URL
from models import Company, Freebie, Dev


# engine = create_engine(SQLITE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

class TestFreebie:
  def test_returns_dev_instance(self):


    engine = create_engine(SQLITE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    freebie = Freebie( 
      item_name="earl",
      value=150,
      company_id=3,
      dev_id=4,

    )



    session.add(freebie)
    session.commit()

    assert isinstance(freebie.dev, Dev)
    assert isinstance(freebie.company, Company)
    session.query(Freebie).delete()
    session.commit()


class TestCompany:
  def test_returns_dev_instance(self):


    engine = create_engine(SQLITE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    freebie = Freebie( 
      item_name="earl",
      value=150,
      company_id=3,
      dev_id=4,

    )

    session.add(freebie)
    session.commit()

    assert isinstance(freebie.dev, Dev)
    session.query(Freebie).delete()
    session.commit()

