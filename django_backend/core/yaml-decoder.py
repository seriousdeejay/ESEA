import os
import yaml

BIA = "C:\\Users\\Work\\Desktop\\Scriptie 2020\\ESEA\\django_backend\\core\\uploadedfiles\\BIA.yaml"

method = "BIA"

def open_yaml_file(file):
    with open(file, 'r') as stream:
        try:
            file = (yaml.safe_load(stream))
            process_yaml_file(file)
        except yaml.YAMLError as exc:
            print(exc)

def process_yaml_file(method_yaml):
    parent_topic_list = []

    # topic model requires
    # name
    # description
    # (parent_topic or not)
    # method
    # (questions)

    # Get the parent topic
    topics = method_yaml['topics']
    for topic in topics:
        # print(dict, loaded_yaml['topics'][dict])
        if 'topic' in topics[topic].keys():
            parent_topic = topics[topic]['topic']
            if parent_topic not in parent_topic_list:
                parent_topic_list.append(parent_topic)
                #print(parent_topic_list)
        topics[topic]['method'] = method
        #print(topic, topics[topic]) ### Hosts name, description, parenttopic and method
    
    surveys = method_yaml['surveys']
    for survey in surveys:
        survey = surveys[survey]
        print(survey['name'])
        print(survey['responserate'])
        for question in (survey['questions']):
            question = survey['questions'][question]
            print(question)

    indicators = method_yaml['indicators']
    for indicator in indicators:
        pass
        



        # for item, value in loaded_yaml[dict].items():
            
    # supertopic = loaded_yaml['topics']['C1']
    # print(supertopic)
    
    # for key, value in loaded_yaml['topics'].items():
    #     print(key, "--", value['name'])
    #     try: 
    #         print(value['description'][:10])
    #     except: pass

    #     if value['topic'] not in parent_topic_list:
    #         parent_topic_list.append(value['topic'])
    #     print(value['topic'])

    


open_yaml_file(BIA)


# try:
#     document = yaml.safe_load(BIA)
#     print(document)
# except yaml.YAMLError as exc:
#     print(exc)
#     try:
#         document = yamldict = yaml.safe_load(file)

#         for item, value in document.items():
#             print(item, ":", value)
#     except yaml.YAMLError as exc:
#             print(exc)
        