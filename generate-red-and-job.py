#!/usr/bin/env python3

from ruamel.yaml import YAML

yaml = YAML(typ='safe')


INPUT_DIR_LISTING = [{
    'class': 'Directory',
    'basename': 'datasets',
    'listing': [{
        'class': 'File',
        'basename': 'lfq_spikein_dilution_1.mzML'
    }, {
        'class': 'File',
        'basename': 'lfq_spikein_dilution_2.mzML'
    }, {
        'class': 'File',
        'basename': 'lfq_spikein_dilution_3.mzML'
    }]
}, {
    'class': 'Directory',
    'basename': 'databases',
    'listing': [{
        'class': 'File',
        'basename': 's_pyo_sf370_potato_human_target_decoy_with_contaminants.fasta'
    }, {
        'class': 'File',
        'basename': 's_pyo_sf370_potato_human_target_decoy_with_contaminants.fasta.phr'
    }, {
        'class': 'File',
        'basename': 's_pyo_sf370_potato_human_target_decoy_with_contaminants.fasta.pin'
    }, {
        'class': 'File',
        'basename': 's_pyo_sf370_potato_human_target_decoy_with_contaminants.fasta.psq'
    }, {
        'class': 'File',
        'basename': 'uniprot-s-pyogenes-sf370-plus-potato-and-human-spike-ins.fasta'
    }, {
        'class': 'File',
        'basename': 'uniprot-s-pyogenes-sf370-plus-potato-and-human-spike-ins.fasta.phr'
    }, {
        'class': 'File',
        'basename': 'uniprot-s-pyogenes-sf370-plus-potato-and-human-spike-ins.fasta.pin'
    }, {
        'class': 'File',
        'basename': 'uniprot-s-pyogenes-sf370-plus-potato-and-human-spike-ins.fasta.psq'
    }]
}]

DATABASE_NAME = 's_pyo_sf370_potato_human_target_decoy_with_contaminants.fasta'


with open('knime-labelfree-quantification.cwl.yml') as f:
    cwl = yaml.load(f)

docker_image_url = cwl['requirements']['DockerRequirement']['dockerPull']

del cwl['requirements']


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
            },
            'listing': INPUT_DIR_LISTING
        },
        'database_name': DATABASE_NAME
    },
    'container': {
        'engine': 'docker',
        'settings': {
            'image': {
                'url': docker_image_url
            }
        }
    }
}

job = {
    'input_dir': {
        'class': 'Directory',
        'location': 'labelfree_example',
        'listing': INPUT_DIR_LISTING
    },
    'database_name': DATABASE_NAME
}

with open('knime-labelfree-quantification.red.yml', 'w') as f:
    yaml.dump(red, f)

with open('job.yml', 'w') as f:
    yaml.dump(job, f)

