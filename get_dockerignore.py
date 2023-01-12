from github import Github
import json
import time
import traceback
ACCESS_TOKEN = "your token"


g = Github(ACCESS_TOKEN)


def search_github(keyword):
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
        return
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')

    query = f'in:file extension:dockerignore'
    result = g.search_code(query, order='desc')
    max_size = 200   #100
    try:
        print(f'Found {result.totalCount} file(s)')

        if result.totalCount > max_size:
            result = result[:max_size]

        
        count = 0
        resjson = []

        for file in result:
            time.sleep(15)
            if count < 18:
                count += 1
        
                new_d = {
                    "file_url": file.download_url,
                    "file_name":file.name,
                    "repository":file.repository.full_name,
                    "file_full_name":file.path,
                    "star":file.repository.stargazers_count,
                    }

                resjson.append(new_d)
                with open("dockerignorelistdict3.json", "w") as f:
                    print("Camon!")
                    json.dump(resjson, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
                print(f'{file.download_url}')

            else:
                count = 0
                time.sleep(80)
                
    except:
        traceback.print_exc()
        print("rate fuck")
        time.sleep(80)

keywords = ""
while(1):
    search_github(keywords)
