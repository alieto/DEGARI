# Config file for DEGARI's prototyper module
# Here are specified the features of a dataset
#   in order to generate its artworks prototypes
#   and the lemmatized description files


# configuration for GAM dataset

# alpha-2 language tag of this dataset
language = "it"

# name of json description file for input
jsonDescrFile = "gam.json"

# name of transformer's output (lemmatized description file)
lemmatizedDescrFile = "gam_only_lemmas.json"

# instance's artwork identifier attribute in json description file
instanceID = "Nid"

# list of instance description attributes in json description file
instanceDescr = ["Titolo", "Descrizione"]

# output folder path
outPath = "gam_for_cocos/"


"""
# configuration for WikiArt dataset

# alpha-2 language tag of this dataset
language = "en"

# name of json description file for input
jsonDescrFile = "wikiart-emotions-descriptions.json"

# name of transformer's output (lemmatized description file)
lemmatizedDescrFile = "wikiart_only_lemmas.json"

# instance's artwork identifier attribute in json description file
instanceID = "ID"

# list of instance description attributes in json description file
instanceDescr = ["Description"]

# output folder path
outPath = "wikiart_for_cocos/"
"""

"""
# configuration for ArsMeteo dataset

# alpha-2 language tag of this dataset
language = "it"

# name of json description file for input
jsonDescrFile = "opera.json"

# name of transformer's output (lemmatized description file)
lemmatizedDescrFile = "arsmeteo_only_lemmas.json"

# instance's artwork identifier attribute in json description file
instanceID = "titolo"

# list of instance description attributes in json description file
instanceDescr = ["descrizione", "testo"]

# output folder path
outPath = "arsmeteo_for_cocos/"
"""

"""
# configuration for SPICE dataset

# alpha-2 language tag of this dataset
language = "it"

# name of json description file for input
jsonDescrFile = "descrizioni.json"

# name of transformer's output (lemmatized description file)
lemmatizedDescrFile = "spice_only_lemmas.json"

# instance's artwork identifier attribute in json description file
instanceID = "opera"

# list of instance description attributes in json description file
instanceDescr = ["evento", "storia", "sensazione", "oggetti"]

# output folder path
outPath = "spice_for_cocos/"
"""

"""
# configuration for RaiPlay dataset

# alpha-2 language tag of this dataset
language = "it"

# name of json description file for input
jsonDescrFile = "descrizioni_raiplay.json"

# name of transformer's output (lemmatized description file)
lemmatizedDescrFile = "raiplay_only_lemmas.json"

# instance's artwork identifier attribute in json description file
instanceID = "programma"

# list of instance description attributes in json description file
instanceDescr = ["description", "descrProgramma"]

# output folder path
outPath = "raiplay_for_cocos/"
"""
