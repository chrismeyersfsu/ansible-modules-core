#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# (c) 2016, Chris Meyers <cmeyers@ansible.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

DOCUMENTATION = '''
---
module: set_artifact
short_description: Save Ansible variables for use across playbook invocations
description:
    - Output user-specified facts to a file. Operates similar to set_fact with 
      variable merge and overwrite behavior. Operates similar to add_host in 
      this module is an action plugin and only runs once, on the first host, 
      for which it sets facts for.
version_added: "2.3"
options:
  dest:
    description:
      - File to output facts set via set_artifact. File will be created if it
        doesn't already exist and overwritten if does exist.
    required: false
    default: null

requirements: [ ]
author: Chris Meyers
'''

RETURN = """
artifact_data:
  description: The union of facts set by `set_artifact` invocations. Note that `artifact_data` is also returned via the magic key `ansible_facts`.
  type: dict
  returned: always
  sample: {
                "artifact_data": {
                   "foo": "bar",
                   "bool": true,
                   "array": [ "hello", "world" ],
                   "nested": {
                       "a": {
                           "b": {
                               "c": 3
                            }
                        }
                    }
                },
                "ansible_facts": {
                    "artifact_data": {
                       "foo": "bar",
                       "bool": true,
                       "array": [ "hello", "world" ],
                       "nested": {
                           "a": {
                               "b": {
                                   "c": 3
                                }
                            }
                        }
                    }
                }
           }
"""

EXAMPLES = '''
# Example fact output:
# Simple specifying of an artifact dictionary, will be passed on callback
- set_artifact:
    data:
        one_artifact: "{{ local_var * 2 }}"
        another_artifact: "{{ some_registered_var.results | map(attribute='ansible_facts.some_fact') | list }}"

# Init
- set_artifact:
    data:
        a: 7

# Overwrite a with 8 and add b, with a value of 9, to the artifact dictionary
- set_artifact:
    data:
        a: 8
        b: 9

# Specifying a local path to save the artifacts to
- set_artifact:
    data:
        one_artifact: "{{ local_var * 2 }}"
        another_artifact: "{{ some_registered_var.results | map(attribute='ansible_facts.some_fact') | list }}"
    dest=/tmp/prefix-{{ inventory_hostname }}
'''
