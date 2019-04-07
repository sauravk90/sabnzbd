#!/usr/bin/python3 -OO
# Copyright 2007-2019 The SABnzbd-Team <team@sabnzbd.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""
tests.test_utils.test_internetspeed- Testing sabnzdb internetspeed
"""

from sabnzbd.utils.internetspeed import internetspeed, measurespeed

class TestInternetSpeed:
    """ This class contains tests to measure internet speed with an active and inactive connection """
    def test_measurespeed_invalid_url(self):
        speed = measurespeed("www.fake-url-9999999.xyz")

        assert isinstance(speed, float)
        assert speed == 0.0

    def test_measurespeed_valid_url(self):
        speed = measurespeed("https://sabnzbd.org/tests/internetspeed/5MB.bin")

        assert isinstance(speed, float)
        assert speed > 0

    def test_internet_speed(self):
        curr_speed_MBps = internetspeed()

        assert isinstance(curr_speed_MBps, float)
        assert curr_speed_MBps > 0



