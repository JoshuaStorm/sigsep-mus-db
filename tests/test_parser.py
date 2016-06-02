import pytest
import dsd100


def user_function1(track):
    '''Should work'''

    # return any number of targets
    estimates = {
        'vocals': track.audio,
        'accompaniment': track.audio,
    }
    return estimates


def user_function2(track):
    '''wrong shape'''

    # return any number of targets
    estimates = {
        'vocals': track.audio[:-1],
        'accompaniment': track.audio,
    }
    return estimates


def test_fileloading():
    # initiate dsd100

    dsd = dsd100.DB(root_dir="data/DSD100subset")
    tracks = dsd.load_dsd_tracks()

    assert len(tracks) == 4


@pytest.mark.parametrize(
    "func",
    [
        user_function1,
        pytest.mark.xfail(user_function2, raises=ValueError),
    ]
)
def test_user_functions(func):
    dsd = dsd100.DB(root_dir="data/DSD100subset")

    assert dsd.test(user_function=func)