# xrang迭代器

```
def xrange(min,max=0):
    o = 0
    if max == 0:
        while o < min:
            yield o
            o += 1
    else:
        if min < max:
            while min < max:
                yield min
                min += 1
        else:
            print("输入值非法")
```

