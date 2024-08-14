from auth.databases import SessionLocal


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
