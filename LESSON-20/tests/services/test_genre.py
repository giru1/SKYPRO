import pytest

from service.genre import GenreNotFound


@pytest.mark.parametrize(
    'data',
    (
            {
                'id': 1,
                'name': 'test1',
            },
            {
                'id': 3,
                'name': 'test3',
            },
    )
)
def test_get_one(genre_service, data):
    genre_service.dao.get_one.return_value = data

    assert genre_service.get_one(data['id']) == data


def test_get_one_with_error(genre_service):
    genre_service.dao.get_one.side_effect = GenreNotFound

    with pytest.raises(GenreNotFound):
        genre_service.get_one(0)


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
def test_get_all(genre_service, length, data):
    genre_service.dao.get_all.return_value = data
    test_result = genre_service.get_all()

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
def test_partially_update(genre_service, origin_data, modified_data):
    genre_service.dao.get_one.return_value = origin_data
    genre_service.partially_update(modified_data)

    genre_service.dao.get_one.assert_called_once_with(origin_data['id'])  # assert под капотом
    genre_service.dao.update.assert_called_once_with(modified_data)  # assert под капотом


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
def test_partially_update_wrong(genre_service, origin_data, modified_data):
    genre_service.dao.get_one.return_value = origin_data
    genre_service.partially_update(modified_data)

    genre_service.dao.update.assert_called_once_with(origin_data)  # assert под капотом


def test_delete(genre_service):
    genre_service.delete(1)
    genre_service.dao.delete.assert_called_once_with(1)


def test_update(genre_service):
    genre_service.update({})
    genre_service.dao.update.assert_called_once_with({})
