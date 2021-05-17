# Config file for DEGARI's recommender module
# Here are specified the features of a dataset in order to generate its recommendations


# configuration for GAM dataset

# name of json description file for input
jsonDescrFile = "gam_only_lemmas.json"

# artwork identifier attribute in json description file, corresponding to a prototype file name in protPath
instanceID = "Nid"

# instance title attributes in json description file
# the first attribute is the artwork instance's title, followed by other main features
instanceTitle = ["Titolo"]

# list of instance description attributes in json description file
instanceDescr = ["Descrizione"]

# prototypes folder path
protPath = "gam_for_cocos/"


"""
# configuration for WikiArt dataset

# name of json description file for input
jsonDescrFile = "wikiart_only_lemmas.json"

# artwork identifier attribute in json description file, corresponding to a prototype file name in protPath
instanceID = "ID"

# instance title attributes in json description file
# the first attribute is the artwork instance's title, followed by other main features
instanceTitle = ["Title"]

# list of instance description attributes in json description file
instanceDescr = ["Description"]

# prototypes folder path
protPath = "wikiart_for_cocos/"
"""

"""
# configuration for ArsMeteo dataset

# name of json description file for input
jsonDescrFile = "arsmeteo_only_lemmas.json"

# artwork identifier attribute in json description file, corresponding to a prototype file name in protPath
instanceID = "titolo"

# instance title attributes in json description file
# the first attribute is the artwork instance's title, followed by other main features
instanceTitle = ["titolo"]

# list of instance description attributes in json description file
instanceDescr = ["descrizione", "testo", "titolo"]

# prototypes folder path
protPath = "arsmeteo_for_cocos/"
"""

"""
# configuration for SPICE dataset

# name of json description file for input
jsonDescrFile = "spice_only_lemmas.json"

# artwork identifier attribute in json description file, corresponding to a prototype file name in protPath
instanceID = "opera"

# instance title attributes in json description file
# the first attribute is the artwork instance's title, followed by other main features
instanceTitle = ["titolo"]

# list of instance description attributes in json description file
instanceDescr = ["evento", "storia", "titolo", "sensazione"]

# prototypes folder path
protPath = "spice_for_cocos/"
"""

"""
# configuration for RaiPlay dataset

# name of json description file for input
jsonDescrFile = "raiplay_only_lemmas.json"

# artwork identifier attribute in json description file, corresponding to a prototype file name in protPath
instanceID = "programma"

# instance title attributes in json description file
# the first attribute is the artwork instance's title (used to identify it), followed by other main features
instanceTitle = ["name", "descrProgramma"]

# list of instance description attributes in json description file
instanceDescr = ["description", "name", "descrProgramma", "programma"]

# prototypes folder path
protPath = "raiplay_for_cocos/"
"""
