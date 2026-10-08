import urllib.request

emailId = input()

web_address = "https://www.ecs.soton.ac.uk/people/" + emailId

with urllib.request.urlopen(web_address) as response:
        html = response.read()

        html = str(html)

        h1_tag_index = html.index("<h1>")

        h1_tag_index_end = html.index("</h1>")

        print(html[h1_tag_index+4:h1_tag_index_end])
