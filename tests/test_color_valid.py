from app.models import Color


def test():
    assert Color.valid("000000")
    assert Color.valid("#000000")
    assert Color.valid("#1234fd")
    assert Color.valid("#abcdef")
    assert Color.valid("#123456")
    assert Color.valid("#789abc")

    assert not Color.valid("##000000")
    assert not Color.valid("00000")
    assert not Color.valid("00000y")
