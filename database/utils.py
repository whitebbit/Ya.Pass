from database.models import Pass
from database import session


def add(service, token):
    item = Pass(service=service, token=token)

    session.add(item)
    session.commit()


def delete(service):
    item = session.query(Pass).filter(Pass.service == service).first()

    session.delete(item)
    session.commit()


def edit(service, token):
    item = session.query(Pass).filter(Pass.service == service).first()
    item.token = token


def get(service):
    item = session.query(Pass).filter(Pass.service == service).first()
    return item


def service_exist(service):
    return get(service.title()) is not None


def get_similar(service):
    item = session.query(Pass).where(Pass.service.startswith(service)).all()
    return item


def all_items():
    for item in session.query(Pass).all():
        yield item
