# pylint: disable=C0111,R0902,R0904,R0912,R0913,R0915,E1101
# Smartsheet Python SDK.
#
# Copyright 2018 Smartsheet.com, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import absolute_import

import six
import json

from ..util import serialize
from ..util import deserialize


class FormatDetails(object):

    """Smartsheet FormatDetails data model."""

    def __init__(self, props=None, base_obj=None):
        """Initialize the FormatDetails model."""
        self._base = None
        if base_obj is not None:
            self._base = base_obj

        self.allowed_values = {
            'paper_size': [
                'LETTER',
                'LEGAL',
                'WIDE',
                'ARCHD',
                'A4',
                'A3',
                'A2',
                'A1',
                'A0']}

        self._paper_size = None

        if props:
            deserialize(self, props)

    @property
    def paper_size(self):
        return self._paper_size

    @paper_size.setter
    def paper_size(self, value):
        if isinstance(value, six.string_types):
            if value not in self.allowed_values['paper_size']:
                raise ValueError(
                    ("`{0}` is an invalid value for FormatDetails`paper_size`,"
                     " must be one of {1}").format(
                         value, self.allowed_values['paper_size']))
            self._paper_size = value

    def to_dict(self):
        return serialize(self)

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_json()
