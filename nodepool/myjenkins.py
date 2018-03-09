#!/usr/bin/env python
# Copyright 2011-2013 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import jenkins
import json

import six.moves.urllib.parse as urlparse
import six.moves.urllib.request as urlrequest

from jenkins import JenkinsException, NODE_TYPE, CREATE_NODE

TOGGLE_OFFLINE = '/computer/%(name)s/toggleOffline?offlineMessage=%(msg)s'
CONFIG_NODE = '/computer/%(name)s/config.xml'


class Jenkins(jenkins.Jenkins):
    pass
