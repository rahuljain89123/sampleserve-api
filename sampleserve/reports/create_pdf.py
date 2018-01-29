
import os
import time
import tempfile
import docraptor

from flask import current_app

# Setup docraptor
docraptor.configuration.username = "zGOJP6Qh4E01kK3Ty6o"
doc_api = docraptor.DocApi()


def save_file(filename, document):
    temp_dir = current_app.config['REPORTS_DIR']
    file_path = temp_dir + "/" + filename
    # Print the current path and debug relative path
    path = os.path.dirname(os.path.abspath(__file__))
    print(path)

    with open(file_path, 'wb+') as fd:
        fd.write(document)
    return dict(directory=temp_dir, filename=filename, file_path=file_path)


def create_pdf_from_document_url(document_url, filename):
    document = doc_api.create_doc({
        "test": True,                                                   # test documents are free but watermarked
        # "document_content": "<html><body>Hello World</body></html>",    # supply content directly
        "document_url": document_url,   # or use a url
        "name": filename,                                 # help you find a document later
        "document_type": "pdf",                                         # pdf or xls or xlsx
        "javascript": True,                                           # enable JavaScript processing
        "prince_options": {
            "media": "screen",                                          # use screen styles instead of print styles
            "baseurl": "http://test.sampleserve.net",                              # pretend URL when using document_content
        },
    })
    # print(document)
    pdf_details = save_file(filename, document)
    return pdf_details


def create_pdf_from_document_content(document_content, filename):
    document = doc_api.create_doc({
        "test": True,                                                   # test documents are free but watermarked
        "document_content": document_content,    # supply content directly
        # "document_url": document_url,   # or use a url
        "name": filename,                                 # help you find a document later
        "document_type": "pdf",                                         # pdf or xls or xlsx
        "javascript": True,                                           # enable JavaScript processing
        "prince_options": {
            "media": "screen",                                          # use screen styles instead of print styles
            "baseurl": "http://test.sampleserve.net",                              # pretend URL when using document_content
        },
    })
    # print(document)
    pdf_details = save_file(filename, document)
    return pdf_details
