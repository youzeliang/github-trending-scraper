import kagglehub

# Download latest version
path = kagglehub.dataset_download("alaotach/github-trending-repositories")

print("Path to dataset files:", path)