import gzip

with open("../dataset/parsed.pkl", "rb") as f1:
    with gzip.open("../dataset/zipped.pkl.gz", "wb") as f2:
        f2.writelines(f1)
