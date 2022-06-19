import os
import shutil

# Original Path to clean
# Replace "UserId" with the name of your user.
originalPath = 'C:\\Users\\UserId\\Desktop\\'
# originalPath = 'C:\\Users\\UserId\\\Downloads\\'

# Move to PATHS
picturesPath = 'C:\\Users\\UserId\\Pictures\\'
documentsPath = 'C:\\Users\\UserId\\Documents\\'
videosPath = 'C:\\Users\\UserId\\Videos\\'
musicPath = 'C:\\Users\\UserId\\Music\\'
textPath = 'C:\\Users\\UserId\\Desktop\\Texts\\'
jsonPath = 'C:\\Users\\UserId\\Desktop\\Jsons\\'
htmlPath = 'C:\\Users\\UserId\\Desktop\\Htmls\\'
yamlPath = 'C:\\Users\\UserId\\Desktop\\Yamls\\'


def checkPath(path):
    pathExist = os.path.exists(path)
    if not pathExist:
        # Create a new directory because it does not exist
        os.makedirs(path, exist_ok=True)


checkPath(textPath)
checkPath(jsonPath)
checkPath(htmlPath)
checkPath(yamlPath)

files = os.listdir(originalPath)
files.sort()

for f in files:
    if f.endswith(('.png', '.jpg', '.jpeg')):
        src = originalPath+f
        dst = picturesPath+f
        shutil.move(src, dst)
    elif f.endswith(('.pdf', '.docx', '.xlsx', '.pptx')):
        src = originalPath+f
        dst = documentsPath+f
        shutil.move(src, dst)
    elif f.endswith(('.mp4', '.flv')):
        src = originalPath+f
        dst = videosPath+f
        shutil.move(src, dst)
    elif f.endswith('.txt'):
        src = originalPath+f
        dst = textPath+f
        shutil.move(src, dst)
    elif f.endswith('.json'):
        src = originalPath+f
        dst = jsonPath+f
        shutil.move(src, dst)
    elif f.endswith('.html'):
        src = originalPath+f
        dst = htmlPath+f
        shutil.move(src, dst)
    elif f.endswith('.yaml'):
        src = originalPath+f
        dst = yamlPath+f
        shutil.move(src, dst)
