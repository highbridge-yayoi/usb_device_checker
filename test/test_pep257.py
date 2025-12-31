# Copyright (c) 2025, highbridge-yayoi
# All rights reserved.
#
# This software is released under the BSD 3-Clause License.
# https://opensource.org/licenses/BSD-3-Clause


from ament_pep257.main import main
import pytest


@pytest.mark.linter
@pytest.mark.pep257
def test_pep257():
    rc = main(argv=['.', 'test'])
    assert rc == 0, 'Found code style errors / warnings'
