suffix=".html"
if suffix == ".html":
    content = "text/html"
elif suffix == ".jpg":
    content = "image/jpeg"
elif suffix == ".png":
    content = "image/png"
else:
    raise RuntimeError("Unknown content type")


#if 'span' in s:
#    has_sapm = True
#else:
#    has_sapm = False

