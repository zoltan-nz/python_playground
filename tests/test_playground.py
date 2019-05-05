from playground import generate_random, download_example_com


def test_generate_random_with_monkeypatch(monkeypatch):
    monkeypatch.setattr("playground.randint", lambda x, y: 5)
    assert generate_random() == 5


def test_generate_random_with_mocker(mocker):
    mocker.patch("playground.randint", return_value=6)
    assert generate_random() == 6


def test_download_example_com(mocker):
    mocker.patch("urllib.request.urlretrieve", return_value=(1, 2))
    assert download_example_com() == (1, 2)
