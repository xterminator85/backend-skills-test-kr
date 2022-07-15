import pytest
from app import single_upload,bulk_upload


# def test_bulk_upload() -> None:
#     assert list(bulk_upload('')) == [
#     "Anna|true",
#     "Annie|false",
#     "Civic|true",
#     "Kayak|true",
#     "Levels|false",
#     "Madam|true",
#     "Mom|true",
#     "Noon|true",
#     "Racecar|true",
#     "Radar|true",
#     "Redder|true",
#     "Refer|true",
#     "Rotator|true",
#     "Rotor|true",
#     "Sagas|true",
#     "Solos|true",
#     "Stats|true",
#     "Tenet|true",
#     "Wow|true",
#     "Was it a cat I saw?|true",
#     "Eva, can I see bees in a cave?|true",
#     "A man, a plan, a canal. Panama!|true"
# ]
    

def test_single_upload() -> None:
    assert single_upload('test') == 'test|false'
    assert single_upload('otto') == 'otto|true'


pytest.main()
