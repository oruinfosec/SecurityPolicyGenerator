# -*- coding: utf-8 -*-
import jinja2
import configparser
import os

#Set jinja2 environment.
templateLoader = jinja2.FileSystemLoader(searchpath ="./templates/")
templateEnv = jinja2.Environment(loader=templateLoader)

#Importing user variables from a config .ini file
configuration_parser = configparser.ConfigParser()
configuration_parser.read('variables.ini', encoding='utf-8-sig')
variable_dictionary = configuration_parser['Company data']

list_of_directories = os.listdir('./templates/')
for TEMPLATE_FILE in list_of_directories:
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(
        variable_dictionary
    ).encode('utf-8')
    html_file = open(variable_dictionary.get('company')+'_'+TEMPLATE_FILE+'.md', 'wb')
    html_file.write(outputText)
    html_file.close()
print("Successfuly generated "+ variable_dictionary.get('company')+" security policies!")

#TODO check if variables are empty or not, give warning
#TODO create a nicer CLI
#TODO make it a bit more robust, check for bugs