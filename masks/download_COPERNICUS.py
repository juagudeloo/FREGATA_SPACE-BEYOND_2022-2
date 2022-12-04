import gdown

# a folder

url = "https://drive.google.com/drive/folders/1S0KGczfzo2fpjjf-A_BLxQHlgsQllqsE?usp=share_link"
gdown.download_folder(url, quiet = True, use_cookies=False)
