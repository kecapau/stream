import streamlit as st
from PIL import Image
img = Image.open('./Da.PNG')
st.image(img)



#git config --global user.email "newking5@naver.com"
#git config --global user.name "Kim"

#git commit -a
#git commit -m "markdown"
#git config --global push.default current



#git add main.py
#git commit -m "Update main.py"
#git push


##### Git 중 충돌났을 떄 
"""git fetch origin
git merge origin/main
git add <충돌 수정된 파일>
git commit -m "Resolve merge conflict"
git push origin main
git push origin main --force"""
