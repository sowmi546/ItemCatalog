from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, CatalogItem, Base

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#Items for Soccer
category1 = Category(name = "Soccer")

session.add(category1)
session.commit()


catalogItem1 = CatalogItem(name = "Soccer1", description = "soccer1", category = category1)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name = "Soccer2", description = "soccer2", category = category1)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name = "Soccer3", description = "soccer3", category = category1)
session.add(catalogItem3)
session.commit()


#Items for Basketball
category2 = Category(name = "Basketball")
session.add(category2)
session.commit()


catalogItem1 = CatalogItem(name = "Basketball1", description = "basketball1", category = category2)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name = "Basketball2", description = "basketball2", category = category2)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name = "Basketball3", description = "basketball3", category = category2)
session.add(catalogItem3)
session.commit()



#Items for Baseball
category3 = Category(name = "Baseball")
session.add(category3)
session.commit()


catalogItem1 = CatalogItem(name = "Baseball1", description = "baseball1", category = category3)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name = "Baseball2", description = "baseball2", category = category3)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name = "Baseball3", description = "baseball3", category = category3)
session.add(catalogItem3)
session.commit()


#Items for frisbee

category4 = Category(name = "Frisbee")
session.add(category4)
session.commit()


catalogItem1 = CatalogItem(name = "Frisbee1", description = "frisbee1", category = category4)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name = "Frisbee2", description = "frisbee2", category = category4)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name = "Frisbee3", description = "frisbee3", category = category4)
session.add(catalogItem3)
session.commit()

#Items for snowboarding

category5 = Category(name = "Snowboarding")
session.add(category5)
session.commit()


catalogItem1 = CatalogItem(name = "Snowboarding1", description = "snowboarding1", category = category5)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name = "Snowboarding2", description = "snowboarding2", category = category5)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name = "Snowboarding3", description = "snowboarding3", category = category5)
session.add(catalogItem3)
session.commit()



#Items for rockclimbing
category6 = Category(name = "Rockclimbing")
session.add(category6)
session.commit()


catalogItem1 = CatalogItem(name = "Rockclimbing1", description = "rockclimbing1", category = category6)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name = "Rockclimbing2", description = "rockclimbing2", category = category6)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name = "Rockclimbing3", description = "rockclimbing3", category = category6)
session.add(catalogItem3)
session.commit()


#Items for foosball
category7 = Category(name = "Foosball")
session.add(category7)
session.commit()


catalogItem1 = CatalogItem(name = "Foosball1", description = "foosball1", category = category7)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name = "Foosball2", description = "foosball2", category = category7)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name = "Foosball3", description = "foosball3", category = category7)
session.add(catalogItem3)
session.commit()


#Items for skating

#Items for Basketball
category8 = Category(name = "Skating")
session.add(category8)
session.commit()


catalogItem1 = CatalogItem(name = "Skating1", description = "skating1", category = category8)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name = "Skating2", description = "skating2", category = category8)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name = "Skating3", description = "skating3", category = category8)
session.add(catalogItem3)
session.commit()

#Items for hockey

category9 = Category(name = "Hockey")
session.add(category9)
session.commit()


catalogItem1 = CatalogItem(name = "Hockey1", description = "hockey1", category = category9)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name = "Hockey2", description = "hockey2", category = category9)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name = "Hockey3", description = "hockey3", category = category9)
session.add(catalogItem3)
session.commit()


print "added category and items!"
