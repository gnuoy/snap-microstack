# Copyright (c) 2022 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from snaphelpers import Snap

LOG = logging.getLogger(__name__)


class Check:
    """Base class for Pre-flight checks.

    Check performs a verification step to determine
    to proceed further or not.
    """

    def __init__(self, name: str, description: str = ""):
        """Initialise the Check.

        :param name: the name of the check
        """
        self.name = name
        self.description = description
        self.message = None

    def run(self) -> bool:
        """Run the check logic here.

        Return True if check is Ok.
        Otherwise update self.message and return False.
        """

        return True


class JujuSnapCheck(Check):
    """Check if juju snap is installed or not."""

    def __init__(self):
        super().__init__(
            "Check for juju snap",
            "Checking for presence of Juju",
        )

    def run(self) -> bool:
        """Check for juju-bin content."""

        snap = Snap()
        juju_content = snap.paths.snap / "juju"
        if not juju_content.exists():
            self.message = "Juju not detected: please install snap"

            return False

        return True


class Microk8sSnapCheck(Check):
    """Check if microk8s snap is installed or not."""

    def __init__(self):
        super().__init__(
            "Check for microk8s snap",
            "Checking for presence of microk8s",
        )

    def run(self) -> bool:
        """Check for microk8s content."""

        snap = Snap()
        microk8s_content = snap.paths.data / "microk8s"
        if not microk8s_content.exists():
            self.message = "microk8s not detected: please install snap"

            return False

        return True


class OpenStackHypervisorSnapCheck(Check):
    """Check if openStack-hypervisor snap is installed or not."""

    def __init__(self):
        super().__init__(
            "Check for openstack-hypervisor snap",
            "Checking for presence of openstack-hypervisor",
        )

    def run(self) -> bool:
        """Check for openstack-hypervisor content."""

        snap = Snap()
        ohv_content = snap.paths.data / "hypervisor-config"
        if not ohv_content.exists():
            self.message = "openstack-hypervisor not detected: please install snap"

            return False

        return True
