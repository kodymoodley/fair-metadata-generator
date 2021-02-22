# [FAIR](https://www.go-fair.org/fair-principles/) metadata generator

## Description

A simple command line Python script to generate rich machine-readable metadata descriptions of datasets in [JSON-LD](https://json-ld.org/) using [Schema.org](https://schema.org/) vocabulary.

The script ``fairmetadatagenerator.py`` asks users to answer a set of pre-determined questions about their dataset. The answers are used to generate a metadata description of their dataset in JSON-LD format which is then meant to be published in metadata registries such as https://fairsharing.org/ or to be [embedded into any website or webpage](https://developers.google.com/search/docs/guides/intro-structured-data) describing the dataset. This is so that search engines can:

+ more effectively index your dataset or website to make it more visible and findable by those searching for similar content (**F**indability, **A**ccessibility)
+ provide rich information about your dataset to users so that they can more quickly and effectively decide whether it is relevant for their purposes (**I**nteroperability, **R**eusability)

[Google](https://www.google.com/), for example, is gradually developing support for [dataset search tools](https://datasetsearch.research.google.com/) to help researchers find and reuse relevant data. Generating structured metadata about your datasets before you publish them to the Web (using tools such as FAIR metadata generator), therefore prepares your data to be more effectively found and reused in such search tools.



