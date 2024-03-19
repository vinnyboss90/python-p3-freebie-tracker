from sqlalchemy import ForeignKey, Column, Integer, String, MetaData,Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

company_dev = Table(
    'company_devs',
    Base.metadata,
    Column('company_id', ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', ForeignKey('devs.id'), primary_key=True),
    extend_existing=True,
)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', backref=backref('company'))
    devs = relationship('Dev', secondary=company_dev, back_populates='companies')


    def __repr__(self):
        return f'Company(id={self.id}, ' + \
               f' name={self. name}, ' + \
               f'founding_year={self.founding_year})'


    

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())


    freebies = relationship('Freebie', backref=backref('dev'))
    companies = relationship('Company', secondary=company_dev, back_populates='devs')


    def __repr__(self):
        return f'Dev(id={self.id}, ' + \
               f'name={self.name})'    

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    def print_details(self):
        name=session.query(Dev).filter(Dev.id==self.dev_id)
        # return f"{dev name} owns a {freebie item_name} from {company name}"

    def __repr__(self):
        return  f'Freebie(id={self.id}, ' + \
                f'item_name ={self.item_name }, ' + \
                f'value={self.value})'+ \
                f'dev_id={self.dev_id})'+ \
                f'company_id={self.company_id})'
                 

