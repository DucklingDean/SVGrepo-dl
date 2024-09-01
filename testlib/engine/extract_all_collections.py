

from svgrepo_dl.engine import extract_all_collections




collections = extract_all_collections()
for c in collections:
    print(c["url"])







