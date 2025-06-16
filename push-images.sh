#!/bin/bash

# GitHub username (lowercase)
GITHUB_USERNAME="vinitchauhan"

#export GITHUB_PAT=your_personal_access_token

echo $GITHUB_PAT | docker login ghcr.io -u VinitChauhan --password-stdin

# Tag images for GitHub Container Registry
docker tag ai-learning:streamlit ghcr.io/$GITHUB_USERNAME/ai-learning:streamlit
docker tag ai-learning:flask ghcr.io/$GITHUB_USERNAME/ai-learning:flask
docker tag ai-learning:backend ghcr.io/$GITHUB_USERNAME/ai-learning:backend

# Push images to GitHub Container Registry
docker push ghcr.io/$GITHUB_USERNAME/ai-learning:streamlit
docker push ghcr.io/$GITHUB_USERNAME/ai-learning:flask
docker push ghcr.io/$GITHUB_USERNAME/ai-learning:backend 