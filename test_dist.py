# ------------------------------------------------------------------------------
# Unit tests for the 'dist' module. Run using pytest.
# ------------------------------------------------------------------------------

import dist


def test_dublin_london():
    dublin = dist.Pos(53.33306, -6.24889)
    london = dist.Pos(51.50853, -0.12574)
    distance = dist.distance(dublin, london)
    assert abs(distance - 462) < 1


def test_dublin_dundalk():
    dublin = dist.Pos(53.33306, -6.24889)
    dundalk = dist.Pos(53.9979451, -6.405957)
    distance = dist.distance(dublin, dundalk)
    assert abs(distance - 75) < 1


def test_bray_howth():
    bray = dist.Pos(53.2044, -6.1092)
    howth = dist.Pos(53.3858, -6.0647)
    distance = dist.distance(bray, howth)
    assert abs(distance - 20) < 1
