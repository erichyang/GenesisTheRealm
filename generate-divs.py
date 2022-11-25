import os
dir = 'images/7/'
filenames = [x for x in os.listdir(dir) if x[-5:] == ".webp"]
for fn in filenames:
    print(f"""<div class="col-4"><span class="image fit"><img src="{dir}{fn}" alt=""/></span></div>""")
