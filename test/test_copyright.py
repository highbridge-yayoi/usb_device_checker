# Copyright (c) 2025, highbridge-yayoi
# All rights reserved.
#
# This software is released under the BSD 3-Clause License.
# https://opensource.org/licenses/BSD-3-Clause

from ament_copyright.main import main
import pytest


# Remove the `skip` decorator once the source file(s) have a copyright header
@pytest.mark.skip(reason='No copyright header has been placed in the generated source file.')
@pytest.mark.copyright
@pytest.mark.linter
def test_copyright():
    rc = main(argv=['.', 'test'])
    assert rc == 0, 'Found errors'
