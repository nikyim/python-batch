import requests
import time


def callIndexAPI(JSONdata):

    headers = {'content-type': 'application/json'}
    url = 'http://54.179.153.188:8080/solr/cdcr/update?shards=cdcr_my'
    data = JSONdata

    requests.post(url, json=data, headers=headers)


def callSourceCommitAPI():

    headers = {'content-type': 'application/json'}
    url = 'http://54.179.153.188:8080/solr/cdcr/update?commit=true&shards=cdcr_my'

    requests.post(url, headers=headers)


def callTargetCommitAPI():

    headers = {'content-type': 'application/json'}
    url = 'http://52.221.238.180:8080/solr/cdcr/update?commit=true&shards=cdcr_my'

    requests.post(url, headers=headers)


def buildJSONData(docID):

    doc = {}
    doc.update({'id': 'cdcrShard1!' + str(docID)})
    doc.update({'author_s': "author_" + str(docID)})
    doc.update({'subject_s': "subject_" + str(docID)})
    doc.update({'dd_f': docID})
    doc.update({'numpages_i': str(docID)})
    doc.update({'desc_txt': ["author_" + str(docID)]})
    doc.update({'price_f': docID})
    doc.update({'title_s': "title_" + str(docID)})
    doc.update({'isbn_l': docID})
    doc.update({'yearpub_i': docID})
    doc.update({'publisher_s': "publisher_" + str(docID)})

    # Insert all doc.update for all the field in the document...

    return doc


def main():

    # Define the number of documents to be index into solr (seed)
    # Define the offset, so that the batch process can run with index tracking
    # Define json_data as array which contain multiple JSON documents to call the POST update index API of solr
    indexNo = 1000
    offset = 3001
    json_data = []

    for x in range(offset, offset + indexNo):
        json_data.append(buildJSONData(x))

    # for item in json_data:
    #     print(item)

    # Index the data in the collection
    source_index_start_time = time.time()
    callIndexAPI(json_data)
    source_index_end_time = time.time()

    # Commit the changes to reflect in the collection
    source_commit_start_time = time.time()
    callSourceCommitAPI()
    source_commit_end_time = time.time()

    # Sync the indexed data to target collection
    target_commit_start_time = time.time()
    callTargetCommitAPI()
    target_commit_end_time = time.time()

    print("--- %s seconds for source collection indexing---" % (source_index_end_time - source_index_start_time))
    print("--- %s seconds for source collection commit---" % (source_commit_end_time - source_commit_start_time))
    print("--- %s seconds for source target commit---" % (target_commit_end_time - target_commit_start_time))
    print("--- %s records indexed ---" % (indexNo + 1 - offset))


# Start the indexing
if __name__ == "__main__":
    main()

