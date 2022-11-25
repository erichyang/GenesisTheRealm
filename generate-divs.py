import os
dir = 'images/Regions/Netherhub/'
filenames = [x for x in os.listdir(dir) if x[-4:] == ".jpg"]
for fn in filenames:
    print(f"""<div class="col-4"><span class="image fit"><img src="{dir}{fn}" alt=""/></span></div>""")
