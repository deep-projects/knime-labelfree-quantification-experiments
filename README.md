# KNIME Labelfree Quantification Experiments

This is the [KNIME Labelfree Quantification](http://citar.eaas.uni-freiburg.de/citar-headless-client/?id=188b6194-ea68-4e59-88c2-61d652941e29#/container-landing-page) workflow. We have extended the original [Docker image](https://hub.docker.com/r/fbartusch/knime-labelfree-quantification) to be compatible with [RED and Curious Containers](https://www.curious-containers.cc).

## Execute from Reproducible Experiment Description (RED)

```bash
# install CC-FAICE
pip3 install --user pipx
pipx install cc-faice==7.*


# prepare
cd knime-labelfree-quantification

# execute
faice agent red knime-labelfree-quantification.red.yml

# check outputs
ls outputs/*
```

## Alternative: Execute from Common Workflow Language (CWL)

```bash
# install CWLTool
pip3 install --user pipx
pipx install cwltool

# prepare
cd knime-labelfree-quantification
curl -fOL https://s3.denbi.uni-tuebingen.de/fb-test/demo_container/cibi_user_meeting_2018/labelfree_example.tar.gz
mkdir labelfree_example
tar -zxvf labelfree_example.tar.gz -C labelfree_example

# execute
cwltool knime-labelfree-quantification.cwl.yml job.yml

# check outputs
ls *.csv *.log
```

## Resources

* [Docker Build Directory](https://github.com/deep-projects/appliances/tree/master/knime-labelfree-quantification/0.2)
