#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Freebie, Dev


if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Company).delete()
    session.query(Dev).delete()
    session.query(Freebie).delete()

    fake = Faker()

    devs = []
    for i in range(20):
      dev = Dev(
        name=fake.name())

      session.add(dev)
      session.commit()   
      devs.append(dev)
    

    companies = []
    for i in range(10):
      company = Company(
        name=fake.company(),
        founding_year=fake.date())

      session.add(company)
      session.commit()  
      companies.append(company)


    


    freebies = []
    for company in companies:
        for i in range(random.randint(1,5)):
            dev = random.choice(devs)
            if company not in dev.companies:
                dev.companies.append(company)
                session.add(dev)
                session.commit()
            
            freebie = Freebie( 
                item_name=fake.job(),
                value=random.randint(100,200),
                company_id=company.id,
                dev_id=dev.id,

            )

  

            freebies.append(freebie)
    
    session.add_all(freebies)
    session.commit()
    session.close()
    