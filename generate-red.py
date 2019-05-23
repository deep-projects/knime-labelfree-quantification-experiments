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
            },
            'listing': [{
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
