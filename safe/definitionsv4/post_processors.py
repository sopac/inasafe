# coding=utf-8

"""Definitions relating to post-processing."""

from safe.utilities.i18n import tr
from safe.definitionsv4.fields import (
    female_ratio_field,
    population_count_field,
    women_count_field,
    youth_ratio_field,
    youth_count_field,
    adult_ratio_field,
    adult_count_field,
    elderly_ratio_field,
    elderly_count_field,
    feature_rate_field,
    feature_value_field
)

__copyright__ = "Copyright 2016, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'

post_processor_gender = {
    'key': 'post_processor_gender',
    'name': tr('Gender Post Processor'),
    'description': tr(
        'Post processor to calculate the number of affected woman'),
    'input': {
        'population': {
            'value': population_count_field,
            'type': 'field'
        },
        'gender_ratio': {
            'value': female_ratio_field,
            'type': 'field'
        }
    },
    'output': {
        'women': {
            'value': women_count_field,
            'formula': 'population * gender_ratio'
        }
    }
}
post_processor_youth = {
    'key': 'post_processor_youth',
    'name': tr('Youth Post Processor'),
    'description': tr(
        'Post processor to calculate the number of affected youth people'),
    'input': {
        'population': {
            'value': population_count_field,
            'type': 'field'
        },
        'youth_ratio': {
            'value': youth_ratio_field,
            'type': 'field'
        }
    },
    'output': {
        'youth': {
            'value': youth_count_field,
            'formula': 'population * youth_ratio'
        }
    }
}
post_processor_adult = {
    'key': 'post_processor_adult',
    'name': tr('Adult Post Processor'),
    'description': tr(
        'Post processor to calculate the number of affected adult people'),
    'input': {
        'population': {
            'value': population_count_field,
            'type': 'field'
        },
        'adult_ratio': {
            'value': adult_ratio_field,
            'type': 'field'
        }
    },
    'output': {
        'adult': {
            'value': adult_count_field,
            'formula': 'population * adult_ratio'
        }
    }
}
post_processor_elderly = {
    'key': 'post_processor_elderly',
    'name': tr('Elderly Post Processor'),
    'description': tr(
        'Post processor to calculate the number of affected elderly people'),
    'input': {
        'population': {
            'value': population_count_field,
            'type': 'field'
        },
        'elderly_ratio': {
            'value': elderly_ratio_field,
            'type': 'field'
        }
    },
    'output': {
        'elderly': {
            'value': elderly_count_field,
            'formula': 'population * elderly_ratio'
        }
    }
}
post_processor_size_rate = {
    'key': 'post_processor_size_rate',
    'name': tr('Size Rate Post Processor'),
    'description': tr(
        'Post processor to calculate the value of feature based on the size '
        'of the feature. If feature is polygon we use area in m^2. If feature '
        'is line we use length per m.'),
    'input': {
        'size': {
            'value': 'size',
            'type': 'geometry_property'
            # We can add something later, like mandatory requirement, another
            #  source of input (e.g. parameter)
        },
        'rate': {
            'value': feature_rate_field,
            'type': 'field'
        }
    },
    'output': {
        'elderly': {
            'value': feature_value_field,
            'formula': 'size * rate'
        }
    }
}

post_processors = [
    post_processor_gender,
    post_processor_youth,
    post_processor_adult,
    post_processor_elderly,
    post_processor_size_rate
]
