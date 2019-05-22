# KNIME Labelfree Quantification Experiments

This is the [KNIME Labelfree Quantification](http://citar.eaas.uni-freiburg.de/citar-headless-client/?id=188b6194-ea68-4e59-88c2-61d652941e29#/container-landing-page) workflow. We have extended the original [Docker image](https://hub.docker.com/r/fbartusch/knime-labelfree-quantification/tags) to be compatible with [RED and Curious Containers](https://www.curious-containers.cc).

## Run Experiment

```bash
# install CC-FAICE
pip3 install --user cc-faice==7.*
faice --version

# execute RED experiment
cd knime-labelfree-quantification-experiments
faice agent red knime-labelfree-quantification.red.yml
```

## Resources

* [Docker Build Directory](https://github.com/deep-projects/appliances/tree/master/knime-labelfree-quantification/0.1)
