# Vince Purcell
# Data Mining 1 = Summer 2021

import sys
import apiclient
import config
import json
from IPython.core.display import HTML

api_key = config.gDevKey

patdevcx = '016938528964600140909:i6wj7bxhnra'  #custom search engine for patents
Gdevcx = '016938528964600140909:wupywukfgda'  #general google search engine
GSdevcx = '016938528964600140909:agrqxfwuuuq'  #google scholar
GLIdevcx = '016938528964600140909:m1qf0rkoow4'  #google linked-in
GPRdevcx = '016938528964600140909:zkjzldc4wwa'   #press releases
GVCdevcx = '016938528964600140909:zkjzldc4wwa'   #venture capital

def print_results_to_text(result, fileStr):
    file = open(fileStr, "w")
    count = 1
    for i in result['items']:
        file.write("RESULT " + str(count) + ":\n")
        toWrite = i
        toWrite.pop('pagemap')
        file.writelines(json.dumps(toWrite, indent=4))
        file.write("\n\n")
        count = count + 1

# Code below was Taken and slightly modified from Professor Breitzman's Code
def search_and_print(query, api_key, fileStr, search_engine_key=Gdevcx, number_of_desired_results=10):
    service = apiclient.discovery.build("customsearch", "v1", developerKey=api_key)
    resource = service.cse()

    number_of_results_printed = 0

    while number_of_results_printed < number_of_desired_results:

        left_to_print = number_of_desired_results - number_of_results_printed
        left_to_print = 10 if left_to_print >= 10 else left_to_print
        print_count_start = number_of_results_printed + 1

        result = resource.list(q=query, cx=search_engine_key, num=left_to_print, start=print_count_start).execute()
        
        if 'items' in result:
            print_results_to_text(result, fileStr)
        else:
            break

        number_of_results_printed += left_to_print

if __name__ == "__main__":
    output = "QueryResults.txt"
    search_and_print('how to make a million dollars in a day', api_key, output)