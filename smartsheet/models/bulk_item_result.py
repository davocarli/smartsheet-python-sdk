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

from .row import Row
from .bulk_item_failure import BulkItemFailure
from ..types import TypedList
from ..util import serialize
from ..util import deserialize


class BulkItemResult(object):

    """Smartsheet BulkItemResult data model."""

    def __init__(self, props=None, dynamic_result_type=None, base_obj=None):
        """Initialize the BulkItemResult model."""
        self._base = None
        if base_obj is not None:
            self._base = base_obj

        self._dynamic_result_type = None
        if dynamic_result_type is not None:
            self._dynamic_result_type = dynamic_result_type

        self._failed_items = TypedList(BulkItemFailure)
        self._message = None
        self._result = TypedList(object)
        self._result_code = None
        self._version = None

        if props:
            deserialize(self, props)

        self.__initialized = True

    @property
    def failed_items(self):
        return self._failed_items

    @failed_items.setter
    def failed_items(self, value):
        if isinstance(value, list):
            self._failed_items = [BulkItemFailure(x, self._base) for x in value]
        else:
            self._failed_items = BulkItemFailure(value, self._base)

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if isinstance(value, six.string_types):
            self._message = value

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if self._dynamic_result_type == 'Row':
            if isinstance(value, list):
                self._result = [Row(x, self._base) for x in value]
            else:
                self._result = Row(value, self._base)

    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        if isinstance(value, six.integer_types):
            self._result_code = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        if isinstance(value, six.integer_types):
            self._version = value

    @property
    def data(self):
        """Simplify difference between Result and IndexResult"""
        return self._result

    def to_dict(self):
        return serialize(self)

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.to_json()
