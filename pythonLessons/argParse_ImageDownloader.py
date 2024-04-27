import argparse
import requests

def download_file(url, local_filename):
    """got this from stack over flow
    """ 
    if local_filename == None:
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename


def noAction(url, fileName):
    print("No action")
    
parser = argparse.ArgumentParser(prog="IMAGE DOWNLOADER",
                                 description="downloads image from the url given")
parser.add_argument("url")

parser.add_argument("fileName",
                    type=str)

parser.add_argument('--download',
                    dest='downloadURLcontent',
                    action='store_const',
                    const=download_file,
                    default=noAction)

args = parser.parse_args()

url = args.url
fileName = args.fileName
print(url)
print(fileName)

args.downloadURLcontent(url, fileName) #you could call download_file(url, fileName) instead of using args.downloadURLcontent(url, fileName)
