from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

def test_insert_attendee():
    event_id = "meu-uuid"
    attendeesInfo = {
        "uuid": "meu_uuid_attendee2",
        "name": "meu name2",
        "email": "email2@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendeesInfo)
    print(response)

@pytest.mark.skip(reason="nao precisa")
def test_get_attendee_badge_by_id():
    attendee_id = "meu_uuid_attendeea"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendee_id)

    print(attendee)