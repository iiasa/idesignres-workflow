# Scenario Explorer Workflow Template

Copyright 2022-2024 IIASA

[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Overview

This is a template for project-specific scenario processing workflows.

To use this template for a project, do the following:
- Create a new repository from this template
- Update the title and overview section of this Readme
- Start adding definitions and mappings 
- If you want to use the [common-definitions](https://github.com/IAMconsortium/common-definitions)
  developed and maintained by the IAMC, rename the file `nomenclature_template.yaml`
  to `nomenclature.yaml`.

### Project nomenclature

The folder `definitions` can contain the project nomenclature, i.e., list of allowed
variables and regions, for use in the validation workflow. See the **nomenclature**
package for more information ([link](https://github.com/iamconsortium/nomenclature)).

The folder `mappings` can contain model mappings that are used to register models and
define how results should be processed upon upload to a Scenario Explorer.

### Model registration

This is the step-by-step guide to registering your model:

1. Fork this repository
2. Follow the instructions from the nomenclature documentation here: <https://nomenclature-iamc.readthedocs.io/en/stable/user_guide/model-registration.html>. 
Please make sure to follow the instructions completely, both the _Model mapping_ and the _Region definitions_ part. You'll have to end up with two files.
3. Open a pull request into this repository. Make sure that the tests run through and correct any potential issues. If the tests are failing you can view the details by clicking on the failed test run.

4. Set [@danielhuppmann](https://github.com/danielhuppmann) and [@phackstock](https://github.com/phackstock) as reviewers.
5. Once everything is in order we will merge your pull request and your model will be registered.

### Workflow

The module `workflow.py` has a function `main(df: pyam.IamDataFrame) -> pyam.IamDataFrame:`.

Per default, this function takes an **IamDataFrame** and returns it without
modifications. [Read the docs](https://pyam-iamc.readthedocs.io) for more information
about the **pyam** package for scenario analysis and data visualization.

**Important**: Do not change the name of the module `workflow.py` or the function `main`
as they are called like this by the Job Execution Service. Details can be found
[here](https://wiki.ece.iiasa.ac.at/wiki/index.php/Scenario_Explorer/Setup#Job_Execution_Service).
