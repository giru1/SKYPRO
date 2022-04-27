import pytest

from service.director import DirectorNotFound


@pytest.mark.parametrize(
    'data',
    (
        {
            'id': 1,
            'name': 'test',
        },
        {
            'id': 3,
            'name': 'test3',
        },
    )
)
def test_get_one(director_service, data):
    director_service.dao.get_one.return_value = data

    assert director_service.get_one(data['id']) == data


def test_get_one_with_error(director_service):
    director_service.dao.get_one.side_effect = DirectorNotFound

    with pytest.raises(DirectorNotFound):
        director_service.get_one(0)


@pytest.mark.parametrize(
    'length, data',
    (
        (
            2,
            [
                {
                    'id': 1,
                    'name': 'test',
                },
                {
                    'id': 3,
                    'name': 'test3',
                },
            ],
        ),
    ),
)
def test_get_all(director_service, length, data):
    director_service.dao.get_all.return_value = data
    test_result = director_service.get_all()

    assert isinstance(test_result, list)
    assert len(test_result) == length
    assert test_result == data


@pytest.mark.parametrize(
    'origin_data, modified_data',
    (
        (
            {
                'id': 1,
                'name': 'test',
            },
            {
                'id': 1,
                'name': 'tesdgdgdfgdft3',
            },
        ),
    ),
)
def test_partially_update(director_service, origin_data, modified_data):
    director_service.dao.get_one.return_value = origin_data
    director_service.partially_update(modified_data)

    director_service.dao.get_one.assert_called_once_with(origin_data['id'])  # assert под капотом
    director_service.dao.update.assert_called_once_with(modified_data)  # assert под капотом


@pytest.mark.parametrize(
    'origin_data, modified_data',
    (
        (
            {
                'id': 1,
                'name': 'test',
            },
            {
                'id': 12,
                'jghjghj': 'tesdgdgdfgdft3',
            },
        ),
    ),
)
def test_partially_update_wrong(director_service, origin_data, modified_data):
    director_service.dao.get_one.return_value = origin_data
    director_service.partially_update(modified_data)

    director_service.dao.update.assert_called_once_with(origin_data)  # assert под капотом


def test_delete(director_service):
    director_service.delete(1)
    director_service.dao.delete.assert_called_once_with(1)


def test_update(director_service):
    director_service.update({})
    director_service.dao.update.assert_called_once_with({})
