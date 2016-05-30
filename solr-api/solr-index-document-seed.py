import requests


def callIndexAPI(JSONdata):

    headers = {'content-type': 'application/json'}
    url = 'http://54.x.x.x:8080/solr/cdcr/update'
    data = JSONdata

    requests.post(url, json=data, headers=headers)


def callCommitAPI():

    headers = {'content-type': 'application/json'}
    url = 'http://54.x.x.x:8080/solr/cdcr/update?commit=true'

    requests.post(url, headers=headers)


def buildJSONData(docID):

    doc = {}
    doc.update({'uuid': str(docID)})
    doc.update({'content': "testing"})
    # Insert all doc.update for all the field in the document...

    return doc


def main():

    # Define the number of documents to be index into solr (seed)
    # Define the offset, so that the batch process can run with index tracking
    # Define json_data as array which contain multiple JSON documents to call the POST update index API of solr
    indexNo = 10000
    offset = 1
    json_data = []

    for x in range(offset, indexNo + 1):
        json_data.append(buildJSONData(x))

    for item in json_data:
        print(item)

    # callIndexAPI(json_data)

    # Commit the changes to reflect in the collection
    # callCommitAPI()

# Start the indexing
main()
