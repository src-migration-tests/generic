def convert(path):
    a = path.split('/')
    i = 0
    while i < len(a):
        if a[i] == '.':
            del a[i]
            i -= 1
        elif a[i] == '..':
            del a[i]
            if i > 0:
                del a[i - 1]
                i -= 1
            i -= 1
        i += 1
    path = '/'.join([item for item in a if item != ''])
    return path

print(convert('/root/../mnt/proc/x/././/////./.././abc/user/../x'))
print(convert('/a/b/c/../../../../a/b/c/../a/../../../a'))