# -*- coding: utf-8 -*-
"""

    integration.reactor.reactor
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test Salt's reactor system
"""

from __future__ import absolute_import

import pytest
import salt.utils.event
from tests.support.case import ModuleCase
from tests.support.mixins import SaltMinionEventAssertsMixin


@pytest.mark.windows_whitelisted
class ReactorTest(SaltMinionEventAssertsMixin, ModuleCase):
    """
    Test Salt's reactor system
    """

    def test_ping_reaction(self):
        """
        Fire an event on the master and ensure
        that it pings the minion
        """
        # Create event bus connection
        e = salt.utils.event.get_event(
            "minion", sock_dir=self.minion_opts["sock_dir"], opts=self.minion_opts
        )

        e.fire_event({"a": "b"}, "/test_event")

        self.assertMinionEventReceived({"a": "b"}, timeout=30)
