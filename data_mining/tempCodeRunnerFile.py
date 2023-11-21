engine = create_engine('sqlite:///mining.db', echo = True )
    Base.metadata.create_all(engine)
    print('Database created')
