# pylint: disable=C0111,R0902,R0904,R0912,R0913,R0915,E1101
# Smartsheet Python SDK.
#
# Copyright 2017 Smartsheet.com, Inc.
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
from ..types import TypedList
from datetime import date
from dateutil.parser import parse


class ProjectSettings(object):
    """Smartsheet ProjectSettings data model."""

    def __init__(self, props=None, base_obj=None):
        """Initialize the ProjectSettings model."""
        self._base = None
        if base_obj is not None:
            self._base = base_obj

        self._length_of_day = None
        self._non_working_days = TypedList(date)
        self._working_days = TypedList(six.string_types)

        if props:
            deserialize(self, props)

        self.__initialized = True

    @property
    def length_of_day(self):
        return self._length_of_day

    @length_of_day.setter
    def length_of_day(self, value):
        if isinstance(value, (six.integer_types, float)):
            self._length_of_day = value

    @property
    def non_working_days(self):
        return self._non_working_days

    @non_working_days.setter
    def non_working_days(self, value):
        if isinstance(value, list):
            self._non_working_days.purge()
            for x in value:
                if isinstance(x, six.string_types):
                    x = parse(x).date()
                if isinstance(x, date):
                    self._non_working_days.extend([x])
        elif isinstance(value, TypedList):
            self._non_working_days.purge()
            self._non_working_days = value.to_list()
        elif isinstance(value, date):
            self._non_working_days.purge()
            self._non_working_days.append(value)
        elif isinstance(value, six.string_types):
            value = parse(value).date()
            self._non_working_days.purge()
            self._non_working_days.append(value)

    @property
    def working_days(self):
        return self._working_days

    @working_days.setter
    def working_days(self, value):
        if isinstance(value, list):
            self._working_days.purge()
            self._working_days.extend([
                 (six.string_types(x, self._base)
                  if not isinstance(x, six.string_types) else x) for x in value
             ])
        elif isinstance(value, TypedList):
            self._working_days.purge()
            self._working_days = value.to_list()
        elif isinstance(value, six.string_types):
            self._working_days.purge()
            self._working_days.append(value)

    def to_dict(self):
        return serialize(self)

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_json()
