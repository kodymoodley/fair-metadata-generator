# [FAIR](https://www.go-fair.org/fair-principles/) metadata generator

### Description

A simple command line Python script to generate rich machine-readable metadata descriptions of datasets in [JSON-LD](https://json-ld.org/) using [Schema.org](https://schema.org/) vocabulary.

The script ``fairmetadatagenerator.py`` asks users to answer a set of pre-determined questions about their dataset. The answers are used to generate a metadata description of their dataset in JSON-LD format which is then meant to be published in metadata registries such as https://fairsharing.org/ or to be [embedded into any website or webpage](https://developers.google.com/search/docs/guides/intro-structured-data) describing the dataset. This is so that search engines can:

+ more effectively index your dataset or website to make it more visible and findable by those searching for similar content (**F**indability, **A**ccessibility)
+ provide rich information about your dataset to users so that they can more quickly and effectively decide whether it is relevant for their purposes (**I**nteroperability, **R**eusability)

[Google](https://www.google.com/), for example, is gradually developing support for [dataset search tools](https://datasetsearch.research.google.com/) to help researchers find and reuse relevant data. Generating structured metadata about your datasets before you publish them to the Web (using tools such as FAIR metadata generator), therefore prepares your data to be more effectively found and reused in such search tools.

### Requirements

+ [Python 3.7+](https://www.python.org/downloads/)
+ Python libraries specified in ``requirements.txt`` in this repository

To install the required libraries in ``requirements.txt`` run: ``pip install -r requirements.txt`` in your command line environment (after installing Python).

### Usage

Run ``python fairmetadatagenerator.py`` in your command line environment after installing Python and the required libraries

### Generate an [HTML](https://html.spec.whatwg.org/) page from my JSON-LD file

Want a human-readable version of your JSON-LD metadata? Use [this script](https://github.com/kodymoodley/fair-metadata-html-page-generator) to automatically generate a static HTML page describing the information inside your JSON-LD file.

### License and contributions

The FAIR metadata generator is copyrighted by [Kody Moodley](https://sites.google.com/site/kodymoodley/) and released under the [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.txt)

Contributions and bug reports are helpful and welcome.
