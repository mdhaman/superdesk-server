# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license


import superdesk
from superdesk.resource import Resource

LINKED_IN_PACKAGES = 'linked_in_packages'
PACKAGE = 'package'

not_analyzed = {'type': 'string', 'index': 'not_analyzed'}

metadata_schema = {
    # Identifiers
    'guid': {
        'type': 'string',
        'unique': True,
        'mapping': not_analyzed
    },
    'unique_id': {
        'type': 'integer',
        'unique': True,
    },
    'unique_name': {
        'type': 'string',
        'unique': True,
        'mapping': not_analyzed
    },
    'parent_id': {
        'type': 'string',
        'unique': True,
        'mapping': not_analyzed
    },
    'version': {
        'type': 'integer'
    },
    'ingest_id': {
        'type': 'string',
        'mapping': not_analyzed
    },
    'family_id': {
        'type': 'string',
        'mapping': not_analyzed
    },

    # Audit Information
    'original_creator': Resource.rel('users'),
    'version_creator': Resource.rel('users'),
    'firstcreated': {
        'type': 'datetime'
    },
    'versioncreated': {
        'type': 'datetime'
    },

    # Ingest Details
    'ingest_provider': Resource.rel('ingest_providers'),
    'source': {     # The value is copied from the ingest_providers vocabulary
        'type': 'string',
        'mapping': not_analyzed
    },
    'original_source': {    # This value is extracted from the ingest
        'type': 'string',
        'mapping': not_analyzed
    },
    'ingest_provider_sequence': {
        'type': 'string',
        'mapping': not_analyzed
    },

    # Copyright Information
    'usageterms': {
        'type': 'string',
        'mapping': not_analyzed,
        'nullable': True,
    },

    # Category Details
    'anpa-category': {
        'type': 'dict',
        'mapping': {
            'type': 'object',
            'properties': {
                'qcode': not_analyzed,
                'name': not_analyzed,
            }
        }
    },

    'subject': {
        'type': 'list',
        'mapping': {
            'properties': {
                'qcode': not_analyzed,
                'name': not_analyzed
            }
        }
    },
    'genre': {
        'type': 'list',
        'mapping': {
            'properties': {
                'name': not_analyzed
            }
        }
    },

    # Story Metadata
    'type': {
        'type': 'string',
        'allowed': ['text', 'preformatted', 'audio', 'video', 'picture', 'graphic', 'composite'],
        'default': 'text',
        'mapping': not_analyzed
    },
    'language': {
        'type': 'string',
        'default': 'en',
        'mapping': not_analyzed,
        'nullable': True,
    },
    'abstract': {
        'type': 'string',
        'nullable': True,
    },
    'headline': {
        'type': 'string'
    },
    'slugline': {
        'type': 'string',
        'mapping': not_analyzed
    },
    'anpa_take_key': {
        'type': 'string',
        'nullable': True,
    },
    'keywords': {
        'type': 'list',
        'mapping': not_analyzed
    },
    'word_count': {
        'type': 'integer'
    },
    'priority': {
        'type': 'string',
        'mapping': not_analyzed,
        'nullable': True,
    },
    'urgency': {
        'type': 'integer',
        'nullable': True,
    },
    'state': {
        'type': 'string',
        'allowed': superdesk.allowed_workflow_states,
        'mapping': not_analyzed,
    },
    # The previous state the item was in before for example being spiked, when unspiked it will revert to this state
    'revert_state': {
        'type': 'string',
        'allowed': superdesk.allowed_workflow_states,
        'mapping': not_analyzed,
    },
    'pubstatus': {
        'type': 'string',
        'allowed': ['Usable', 'Withhold', 'Canceled'],
        'default': 'Usable',
        'mapping': not_analyzed
    },
    'signal': {
        'type': 'string',
        'mapping': not_analyzed
    },
    'byline': {
        'type': 'string',
        'nullable': True,
    },
    'ednote': {
        'type': 'string',
        'nullable': True,
    },
    'description': {
        'type': 'string',
        'nullable': True
    },
    'groups': {
        'type': 'list'
    },
    'body_html': {
        'type': 'string',
        'nullable': True,
    },
    'body_text': {
        'type': 'string',
        'nullable': True,
    },
    'dateline': {
        'type': 'string'
    },
    'expiry': {
        'type': 'datetime'
    },

    # Media Related
    'media': {
        'type': 'file'
    },
    'mimetype': {
        'type': 'string',
        'mapping': not_analyzed
    },
    'renditions': {
        'type': 'dict'
    },
    'filemeta': {
        'type': 'dict'
    },
    'media_file': {
        'type': 'string'
    },
    'contents': {
        'type': 'list'
    },

    # Not Categorized
    'place': {
        'type': 'list'
    },
    'located': {
        'type': 'string',
        'nullable': True,
    },
    'creditline': {
        'type': 'string'
    },
    'dateline': {
        'type': 'string',
        'nullable': True,
    },
    LINKED_IN_PACKAGES: {
        'type': 'list',
        'readonly': True,
        'schema': {
            'type': 'dict',
            'schema': {
                PACKAGE: Resource.rel('packages')
            }
        }
    },
    'highlight': Resource.rel('highlights'),

    # Task and Lock Details
    'task_id': {
        'type': 'string',
        'mapping': not_analyzed,
        'versioned': False
    },

    'lock_user': Resource.rel('users'),
    'lock_time': {
        'type': 'datetime',
        'versioned': False
    },
    'lock_session': Resource.rel('auth')
}

metadata_schema['lock_user']['versioned'] = False
metadata_schema['lock_session']['versioned'] = False
