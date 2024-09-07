from auth.databases import SessionLocal


def get_session():
    session = SessionLocal()
    try:
        yield session
    except Exception as exc:
        session.rollback()
        raise exc
    finally:
        session.commit()
        session.close()
