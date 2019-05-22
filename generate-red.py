#!/usr/bin/env python3

from ruamel.yaml import YAML

yaml = YAML(typ='safe')

with open('knime-labelfree-quantification.cwl.yml') as f:
    cwl = yaml.load(f)

red = {
    'redVersion': '7',
    'cli': cwl,
    'inputs': {
        'input_dir': {
            'class': 'Directory',
            'connector': {
                'command': 'red-connector-http-archive',
                'access': {
                    'url': 'https://s3.denbi.uni-tuebingen.de/fb-test/demo_container/cibi_user_meeting_2018/labelfree_example.tar.gz',
                    'archiveFormat': 'gztar'
                }
            }
        },
        'database_name': 's_pyo_sf370_potato_human_target_decoy_with_contaminants.fasta'
    },
    'container': {
        'engine': 'docker',
        'settings': {
            'image': {
                'url': 'docker.io/deepprojects/knime-labelfree-quantification:dev'
            }
        }
    }
}

with open('knime-labelfree-quantification.red.yml', 'w') as f:
    yaml.dump(red, f)
