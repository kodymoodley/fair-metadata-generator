#!/usr/bin/env python
import pandas as pd
df = pd.read_csv ("questions.csv", index_col=None)

title = input(df[df['question_id']==1]['question'].values[0] + " ")
description = input(df[df['question_id']==2]['question'].values[0] + " ")
creator_given_name = input(df[df['question_id']==3]['question'].values[0] + " ")
creator_family_name = input(df[df['question_id']==4]['question'].values[0] + " ")
creator_occupation = input(df[df['question_id']==5]['question'].values[0] + " ")
creator_email = input(df[df['question_id']==6]['question'].values[0] + " ")
creator_image = input(df[df['question_id']==63]['question'].values[0] + " ")
creator_affiliation_name = input(df[df['question_id']==7]['question'].values[0] + " ")
creator_affiliation_url = input(df[df['question_id']==8]['question'].values[0] + " ")
creator_affiliation_logo = input(df[df['question_id']==9]['question'].values[0] + " ")
contributors_boolean = input(df[df['question_id']==10]['question'].values[0] + " ")
contributors_count = ""
contributors = []

if (contributors_boolean.lower() == 'y'):
    contributors_count = input(df[df['question_id']==11]['question'].values[0] + " ")
    num_of_contributors = int(contributors_count)
    for i in range(1, num_of_contributors+1):
        contributor = {}
        contributor['givenName'] = input(df[df['question_id']==12]['question'].values[0] + str(i) + " ")
        contributor['familyName'] = input(df[df['question_id']==13]['question'].values[0] + str(i) + " ")
        contributor['jobTitle'] = input(df[df['question_id']==14]['question'].values[0] + str(i) + " ")
        contributor['email'] = input(df[df['question_id']==15]['question'].values[0] + str(i) + " ")
        contributor['image'] = input(df[df['question_id']==64]['question'].values[0] + str(i) + " ")
        contributor['name'] = input(df[df['question_id']==16]['question'].values[0] + str(i) + " ")
        contributor['url'] = input(df[df['question_id']==17]['question'].values[0] + str(i) + " ")
        contributor['logo'] = input(df[df['question_id']==18]['question'].values[0] + str(i) + " ")
        contributors.append(contributor)

publisher = input(df[df['question_id']==19]['question'].values[0] + " ")

if (publisher == 'p'):
    same_as_creator = input(df[df['question_id']==20]['question'].values[0] + " ")
    if (same_as_creator == 'y'):
        publisher_given_name = creator_given_name
        publisher_family_name = creator_given_name
        publisher_occupation = creator_occupation
        publisher_email = creator_email
        publisher_image = creator_image
        publisher_affiliation_name = creator_affiliation_name
        publisher_affiliation_url = creator_affiliation_url
        publisher_affiliation_logo = creator_affiliation_logo
    else:
        publisher_given_name = input(df[df['question_id']==21]['question'].values[0] + " ")
        publisher_family_name = input(df[df['question_id']==22]['question'].values[0] + " ")
        publisher_occupation = input(df[df['question_id']==23]['question'].values[0] + " ")
        publisher_image = input(df[df['question_id']==65]['question'].values[0] + " ")
        publisher_email = input(df[df['question_id']==24]['question'].values[0] + " ")
        publisher_affiliation_name = input(df[df['question_id']==25]['question'].values[0] + " ")
        publisher_affiliation_url = input(df[df['question_id']==26]['question'].values[0] + " ")
        publisher_affiliation_logo = input(df[df['question_id']==27]['question'].values[0] + " ")
    
    dataset_version = input(df[df['question_id']==28]['question'].values[0] + " ")
    license = input(df[df['question_id']==29]['question'].values[0] + " ")
    data_format = input(df[df['question_id']==30]['question'].values[0] + " ")
    date_created = input(df[df['question_id']==31]['question'].values[0] + " ")
    date_published = input(df[df['question_id']==32]['question'].values[0] + " ")
    url = input(df[df['question_id']==33]['question'].values[0] + " ")
    lang = input(df[df['question_id']==34]['question'].values[0] + " ")
    temporal = input(df[df['question_id']==35]['question'].values[0] + " ")
    temporal_coverage = input(df[df['question_id']==36]['question'].values[0] + " ")
    keywords = input(df[df['question_id']==37]['question'].values[0] + " ")
    distribution_content_url = input(df[df['question_id']==38]['question'].values[0] + " ")
    distribution_content_size = input(df[df['question_id']==39]['question'].values[0] + " ")
    distribution_content_format = input(df[df['question_id']==40]['question'].values[0] + " ")
    generated_by_software = input(df[df['question_id']==41]['question'].values[0] + " ")
    if (generated_by_software == 'y'):
        name_of_software = input(df[df['question_id']==42]['question'].values[0] + " ")
        desc_of_software = input(df[df['question_id']==45]['question'].values[0] + " ")
        version_of_software = input(df[df['question_id']==43]['question'].values[0] + " ")
        url_of_software = input(df[df['question_id']==44]['question'].values[0] + " ")
        software_type = input(df[df['question_id']==46]['question'].values[0] + " ")
        operating_system = input(df[df['question_id']==47]['question'].values[0] + " ")

    publication_associated = input(df[df['question_id']==48]['question'].values[0] + " ")
    if (publication_associated == 'y'):
        name_of_publication = input(df[df['question_id']==49]['question'].values[0] + " ")
        publication_authors = input(df[df['question_id']==50]['question'].values[0] + " ")
        date_published_pub = input(df[df['question_id']==53]['question'].values[0] + " ")
        doi_publication = input(df[df['question_id']==54]['question'].values[0] + " ")
        publisher_of_publication = input(df[df['question_id']==51]['question'].values[0] + " ")
        publisher_pub_url = input(df[df['question_id']==52]['question'].values[0] + " ")

    dataset_dependency_exists = input(df[df['question_id']==58]['question'].values[0] + " ")
    if (dataset_dependency_exists == 'y'):
        name_of_related_dataset = input(df[df['question_id']==59]['question'].values[0] + " ")
        desc_of_related_dataset = input(df[df['question_id']==60]['question'].values[0] + " ")
        version_of_related_dataset = input(df[df['question_id']==61]['question'].values[0] + " ")
        url_of_related_dataset = input(df[df['question_id']==62]['question'].values[0] + " ")

if (publisher == 'o'):
    publisher_organisation_name = input(df[df['question_id']==55]['question'].values[0] + " ")
    publisher_organisation_url = input(df[df['question_id']==56]['question'].values[0] + " ")
    publisher_organisation_logo = input(df[df['question_id']==57]['question'].values[0] + " ")
    dataset_version = input(df[df['question_id']==28]['question'].values[0] + " ")
    license = input(df[df['question_id']==29]['question'].values[0] + " ")
    data_format = input(df[df['question_id']==30]['question'].values[0] + " ")
    date_created = input(df[df['question_id']==31]['question'].values[0] + " ")
    date_published = input(df[df['question_id']==32]['question'].values[0] + " ")
    url = input(df[df['question_id']==33]['question'].values[0] + " ")
    lang = input(df[df['question_id']==34]['question'].values[0] + " ")
    temporal = input(df[df['question_id']==35]['question'].values[0] + " ")
    temporal_coverage = input(df[df['question_id']==36]['question'].values[0] + " ")
    keywords = input(df[df['question_id']==37]['question'].values[0] + " ")
    distribution_content_url = input(df[df['question_id']==38]['question'].values[0] + " ")
    distribution_content_size = input(df[df['question_id']==39]['question'].values[0] + " ")
    distribution_content_format = input(df[df['question_id']==40]['question'].values[0] + " ")
    generated_by_software = input(df[df['question_id']==41]['question'].values[0] + " ")
    if (generated_by_software == 'y'):
        name_of_software = input(df[df['question_id']==42]['question'].values[0] + " ")
        desc_of_software = input(df[df['question_id']==45]['question'].values[0] + " ")
        version_of_software = input(df[df['question_id']==43]['question'].values[0] + " ")
        url_of_software = input(df[df['question_id']==44]['question'].values[0] + " ")
        software_type = input(df[df['question_id']==46]['question'].values[0] + " ")
        operating_system = input(df[df['question_id']==47]['question'].values[0] + " ")

    publication_associated = input(df[df['question_id']==48]['question'].values[0] + " ")
    if (publication_associated == 'y'):
        name_of_publication = input(df[df['question_id']==49]['question'].values[0] + " ")
        publication_authors = input(df[df['question_id']==50]['question'].values[0] + " ")
        date_published_pub = input(df[df['question_id']==53]['question'].values[0] + " ")
        doi_publication = input(df[df['question_id']==54]['question'].values[0] + " ")
        publisher_of_publication = input(df[df['question_id']==51]['question'].values[0] + " ")
        publisher_pub_url = input(df[df['question_id']==52]['question'].values[0] + " ")

    dataset_dependency_exists = input(df[df['question_id']==58]['question'].values[0] + " ")
    if (dataset_dependency_exists == 'y'):
        name_of_related_dataset = input(df[df['question_id']==59]['question'].values[0] + " ")
        desc_of_related_dataset = input(df[df['question_id']==60]['question'].values[0] + " ")
        version_of_related_dataset = input(df[df['question_id']==61]['question'].values[0] + " ")
        url_of_related_dataset = input(df[df['question_id']==62]['question'].values[0] + " ")

import json

with open('jsonldtemplate.jsonld') as json_file:
    data = json.load(json_file)

# -- Begin: key-val properties
data['name'] = title
data['description'] = description
data['version'] = dataset_version
data['license'] = license
data['encodingFormat'] = data_format
data['url'] = url
data['temporal'] = temporal
data['temporalCoverage'] = temporal_coverage

# -- Begin: simple properties
# Language
data['inLanguage'] = {
    "@type": "Language",
    "name": lang,
    "alternateName": lang
}

# Keywords
newkeywords = []
for item in keywords.split(","):
    newkeywords.append(item.strip())

data['keywords'] = newkeywords 

# Dates
data['dateCreated'] = {
    "@type": "Date",
    "@value": date_created
}

data['datePublished'] = {
    "@type": "Date",
    "@value": date_published
}
# -- End: simple properties

# -- Begin: complex properties
# Creator
data['creator'] = {
    "@type": "Person",
    "name": creator_given_name + " " + creator_family_name,
    "givenName": creator_given_name,
    "familyName": creator_family_name,
    "jobTitle": creator_occupation,
    "email": creator_email,
    "image": creator_image,
    "affiliation": {
        "@type": "Organization",
        "name": creator_affiliation_name,
        "url": {
            "@type": "URL",
            "@value": creator_affiliation_url
        },
        "logo": {
            "@type": "ImageObject",
            "contentUrl": creator_affiliation_logo
        }
    }
}

# Contributors
newcontributors = []
for item in contributors:
    current_item = {
        "@type": "Person",
        "givenName": item['givenName'],
        "familyName": item['familyName'],
        "jobTitle": item['jobTitle'],
        "email": item['email'],
        "image": item['image'],
        "affiliation": {
            "@type": "Organization",
            "name": item['name'],
            "url": {
                "@type": "URL",
                "@value": item['url']
            },
            "logo": {
                "@type": "ImageObject",
                "contentUrl": item['logo']
            }
        }
    }
    newcontributors.append(current_item)
    
data['contributor'] = newcontributors

# Publisher
if (publisher == 'p'):
    if (same_as_creator == 'y'):
        data['publisher'] = data['creator']
    else:
        data['publisher'] = {
            "@type": "Person",
            "name": publisher_given_name + " " + publisher_family_name,
            "givenName": publisher_given_name,
            "familyName": publisher_family_name,
            "jobTitle": publisher_occupation,
            "email": publisher_email,
            "image": publisher_image,
            "affiliation": {
                "@type": "Organization",
                "name": publisher_affiliation_name,
                "url": {
                    "@type": "URL",
                    "@value": publisher_affiliation_url
                }
            }
        }
else:
    data['publisher'] = {
        "@type": "Organization",
        "name": publisher_organisation_name,
        "url": {
            "@type": "URL",
            "@value": publisher_organisation_url
        },
        "logo": {
            "@type": "ImageObject",
            "contentUrl": publisher_organisation_logo
        }
    } 
    
# Download
data['distribution'] = {
    "@type": "DataDownload",
    "contentUrl": {
        "@type": "URL",
        "@value": distribution_content_url
    },
    "encodingFormat": distribution_content_format,
    "contentSize": distribution_content_size
}

# Software and / or related datasets
if ((generated_by_software == 'y') and (dataset_dependency_exists == 'y')):
    data['isBasedOn'] = [{
        "@type": "SoftwareApplication",
        "name": name_of_software,
        "description": desc_of_software,
        "applicationCategory": software_type,
        "operatingSystem": operating_system,
        "version": version_of_software,
        "url": {
            "@type": "URL",
            "@value": url_of_software
        }
    }, {
       "@type": "CreativeWork",
       "name": name_of_related_dataset,
       "description": desc_of_related_dataset,
       "version": version_of_related_dataset,
        "url": {
            "@type": "URL",
            "@value": url_of_related_dataset
        }
    }]
else:
    if (generated_by_software == 'y'):
        data['isBasedOn'] = {
            "@type": "SoftwareApplication",
            "name": name_of_software,
            "description": desc_of_software,
            "applicationCategory": software_type,
            "operatingSystem": operating_system,
            "version": version_of_software,
            "url": {
                "@type": "URL",
                "@value": url_of_software
            }
        }
    else:
        data['isBasedOn'] = {
            "@type": "CreativeWork",
            "name": name_of_related_dataset,
            "description": desc_of_related_dataset,
            "version": version_of_related_dataset,
            "url": {
                "@type": "URL",
                "@value": url_of_related_dataset
            }
        }        

# Publication
new_pub_authors = []
for item in publication_authors.split(","):
    current_item = {
        "@type": "Person",
        "name": item.strip()
    }
    new_pub_authors.append(current_item)
    
data['citation'] = {
    "@type": "CreativeWork",
    "name": name_of_publication,
    "creator": new_pub_authors,
    "publisher": {
        "@type": "Organization",
        "name": publisher_of_publication,
        "url": {
            "@type": "URL",
            "@value": publisher_pub_url
        }
    },
    "datePublished": {
        "@type": "Date",
        "@value": date_published_pub
    },
    "sameAs": {
        "@type": "URL",
        "@value": doi_publication
    }
}

# -- End: complex properties

import datetime; 
  
current_time_stamp = datetime.datetime.now()  
current_time_stamp = str(current_time_stamp).replace(" ","_")
current_time_stamp = current_time_stamp.replace("-","")
current_time_stamp = current_time_stamp.replace(":","")
current_time_stamp = current_time_stamp.replace(".","")

if ('v' not in data['version'].lower()):
    data['version'] = 'v' + data['version']
    
metadata_output_filename = data['name'].replace(" ","_") + "_" + data['version'].replace(" ","_") + "_" + current_time_stamp + ".jsonld"

with open(metadata_output_filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

