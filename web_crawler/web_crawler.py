import socket


def connect_to_server(IP, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP, port))
        return sock
    except:
        print(f"\nCouldn't connect to {IP}.\n")
        return -1


def parse_URL(link):
    # Check if link/URL is relative or absolute, extract domain
    # relative (just path without domain e.g. '/xyz'), absolute (whole path e.g. 'http://google.com/xyz') 
    # e.g. http://www.scretch.cu/explore/sites-list => HOST/DOMAIN=www.scretch.cu, PATH=explore/sites-list 
    beginning_host = link.find('http://', 0)
    end_host = link.find('/', 7)

    domain = link[(beginning_host+7) if beginning_host != -1 else 0 : end_host if end_host != -1 else len(link)]

    if domain.find('www.') == -1:
        domain = 'www.' + domain
    # Lastly, check if there is a path to a file in the parsed link
    path = link[end_host+1 if end_host != -1 else len(link):]
    return domain, path


def get_source(domain, path, sock):
    request = f'GET /{path} HTTP/1.1\r\nHost: {domain} \r\n\r\n'
    sock.sendall(str.encode(request, 'cp852'))
    return sock.recv(128000).decode('cp852')


def get_scraped_links(source, scraped_links):
    beginning_href = 0

    while True:
        # Find <a href=""> tag in page source
        beginning_href = source.find('href=', beginning_href)
        
        if beginning_href == -1:
            break
        
        end_href = source.find('"', beginning_href + 6)
        link = source[beginning_href + 6:end_href]
        beginning_href = end_href + 1

        if link not in scraped_links:   # and link.find('http://') != -1
            scraped_links.append(link)
 

counter_visited = 0

scraped_links = [ 'http://www.scratchpads.eu/explore/sites-list' ]
visited_links = []

for link in scraped_links:
    # Get domain and path from URL
    domain, path = parse_URL(link)
    # Connect to page
    sock = connect_to_server(domain, 80)
    # In case it can't connect to site (site no longer exists, invalid URL or something similar)
    if sock == -1: continue

    page_source = get_source(domain, path, sock)
    get_scraped_links(page_source, scraped_links)
    # URL is valid and scraped, so add it to the list of visited links
    visited_links.append(link)

    if counter_visited == 50: break
    
    counter_visited += 1

print(visited_links)


